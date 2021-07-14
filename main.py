from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
if sys.version_info.major == 3:
    unicode = str

def get_tables(htmldoc):
    soup = BeautifulSoup(htmldoc)
    return soup.findAll('table')

def makelist(table):
    result = []
    allrows = table.findAll('<tr>')
    for row in allrows:
        result.append([])
        allcols = row.findAll('<td>')
        for col in allcols:
            # thestrings = [unicode(s) for s in col.find_all(text=True)]
            # thetext = ''.join(thestrings)
            # result[-1].append(thetext)
    return result

url = "http://www.nationalmovemgmt.com:8011/mrcjava/servlet/MRCMPOWER.I00140s"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")
tables = get_tables(html)
print(len(makelist(tables)))

"""
table_index = html.find("<tbody class=\"stripe\" id=\"mrc_main_table\">")

start_index = table_index + len("<tbody class=\"stripe\" id=\"mrc_main_table\">")

end_index = html.find("<!-- End data table -->")


table = html[start_index:end_index]


print(table)

"""