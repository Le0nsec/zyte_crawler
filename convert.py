from markdownify import markdownify as md
import json
from os import listdir, path
import re

XZ_JSON_PATH = "./xz.aliyun.com/"
XZ_MD_PATH = "./xz.aliyun.com.md/"

TTTANG_JSON_PATH = "./tttang.com/"
TTTANG_MD_PATH = "./tttang.com.md/"

SEEBUG_JSON_PATH = "./paper.seebug.org/"
SEEBUG_MD_PATH = "./paper.seebug.org.md/"

def convert(json_path, md_path):
	file_list = listdir(json_path)
	for file_name in file_list:
		data = parse_json(json_path + file_name)
		if data:
			# convert html to markdown
			md_text = md(data["articleBodyHtml"], heading_style="ATX")
			md_name = path.splitext(file_name)[0] + "-" + data["headline"] + ".md"
			data["md_text"] = md_text
			write_md(md_path + clean_file_name(md_name), data)

def clean_file_name(filename):
    invalid_chars='[\\\/:*?"<>|]'
    replace_char=''
    return re.sub(invalid_chars,replace_char,filename)

def parse_json(file_name):	
	try:
		with open(file_name, "r") as f:
			data = json.load(f)
		url = data["url"]
		datePublishedRaw = data["datePublishedRaw"]
		headline = data["headline"]
		articleBodyHtml = data["articleBodyHtml"]

	except Exception as e:
		print('%s error: %s' %(file_name, e))
		return None
	
	return {
		"url": url,
		"datePublishedRaw": datePublishedRaw,
		"headline": headline,
		"articleBodyHtml": articleBodyHtml
	}

def write_md(md_name, data):
	markdown = """---
title: %s
date: %s
url: %s
---

%s""" %(data["headline"], data["datePublishedRaw"], data["url"], data["md_text"])
	try:
		with open(md_name, "w") as f:
			f.write(markdown)
	except Exception as e:
		print('%s error: %s' %(md_name, e))
		return None


if __name__ == "__main__":
	# convert(XZ_JSON_PATH, XZ_MD_PATH)
	# convert(TTTANG_JSON_PATH, TTTANG_MD_PATH)
	convert(SEEBUG_JSON_PATH, SEEBUG_MD_PATH)