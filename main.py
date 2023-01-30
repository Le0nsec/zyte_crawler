# zyte-autoextract library required (Python 3.6+ required). Install it by executing:
#    pip install zyte-autoextract

from autoextract.sync import request_raw
import json

API_KEY = '**********'

# xz.aliyun.com : 9807 - 12073   // 2021.07.06 - 2023.01.28
# tttang.com : 1 - 1876          // 2019-02-11 - 2023.01.28
# paper.seebug.org : 9 - 2040    // 2016-08-04 - 2023.01.28

def tttang():
    url = 'https://tttang.com/archive/{}/'
    NOT_FOUND_PAGE = [3, 5, 6, 7, 8, 10, 633, 1273, 1274, 1275, 1277, 1278, 1283, 1284, 1285, 1286, 1287, 1289, 1295, 1296, 1298, 1299, 1300, 1302, 1305, 1306, 1309, 1310, 1311, 1316, 1317, 1318, 1319, 1320, 1321, 1324, 1325, 1326, 1328, 1329, 1330, 1333, 1335, 1336, 1340, 1341, 1343, 1346, 1349, 1351, 1356, 1358, 1359, 1360, 1363, 1364, 1366, 1367, 1370, 1371, 1372, 1373, 1374, 1376, 1383, 1385, 1401, 1404, 1407, 1410, 1413, 1417, 1421, 1424, 1431, 1438, 1442, 1449, 1452, 1453, 1455, 1456, 1460, 1461, 1467, 1469, 1470, 1471, 1473, 1475, 1477, 1478, 1479, 1481, 1482, 1486, 1490, 1493, 1494, 1495, 1496, 1498, 1499, 1500, 1502, 1503, 1505, 1506, 1507, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1527, 1528, 1529, 1531, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1543, 1544, 1549, 1551, 1552, 1554, 1556, 1561, 1562, 1563, 1564, 1566, 1567, 1571, 1575, 1576, 1578, 1580, 1586, 1594, 1596, 1598, 1599, 1600, 1602, 1604, 1608, 1610, 1615, 1619, 1621, 1623, 1625, 1630, 1632, 1633, 1635, 1636, 1638, 1642, 1644, 1646, 1649, 1651, 1652, 1654, 1655, 1656, 1657, 1658, 1659, 1663, 1666, 1667, 1668, 1669, 1671, 1674, 1676, 1677, 1679, 1680, 1681, 1684, 1685, 1688, 1689, 1690, 1691, 1694, 1700, 1702, 1705, 1708, 1711, 1713, 1717, 1721, 1722, 1723, 1724, 1725, 1731, 1733, 1735, 1737, 1738, 1741, 1746, 1748, 1750, 1752, 1754, 1756, 1757, 1759, 1760, 1761, 1763, 1764, 1765, 1770, 1773, 1774, 1776, 1778, 1780, 1783, 1784, 1787, 1788, 1790, 1792, 1794, 1795, 1797, 1799, 1802, 1807, 1809, 1811, 1812, 1814, 1816, 1817, 1818, 1820, 1821, 1822, 1823, 1825, 1826, 1827, 1828, 1829, 1834, 1835, 1836, 1838, 1839, 1841, 1842, 1843, 1844, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1866, 1867, 1868, 1870, 1872]
    for i in range(1, 1877):
        if i in NOT_FOUND_PAGE:
            continue
        page = url.format(i)
        result = crawl(page)
        if result:
            write_json(result, './tttang.com/{}.json'.format(i))

def xianzhi():
    url = 'https://xz.aliyun.com/t/{}'
    for i in range(9807, 12074):
        page = url.format(i)
        result = crawl(page)
        if result:
            write_json(result, './xz.aliyun.com/{}.json'.format(i))

def seebug():
    url = 'https://paper.seebug.org/{}/'
    for i in range(9, 2041):
        page = url.format(i)
        result = crawl(page)
        if result:
            write_json(result, './paper.seebug.org/{}.json'.format(i))

def crawl(page):
    query = [{
        'url': page,
        'pageType': 'article',
        'articleBodyRaw': False,
    }]

    try:
        resp = request_raw(query, api_key=API_KEY)
        article = resp[0]['article']
        print('[+] %s ok' % page)
    except Exception as e:
        print('[!] %s error: %s' % (page, e))
        return None
    return article

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    # tttang()
    # xianzhi()
    seebug()