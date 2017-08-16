import re
import bs4 as bs
import urllib.request


soup = urllib.request.urlopen('https://tabs.ultimate-guitar.com/e/emmure/10_signs_you_should_leave_tab.htm').read()
soup = bs.BeautifulSoup(soup, 'lxml')
contents = soup.find("pre", {"class": "js-tab-content js-copy-content js-tab-controls-item"})
tabs = str(contents)
digits = re.findall(r'(?<=-)(\d+)', tabs)


def separate_zeros(string):
    return list(string)

test = [separate_zeros(number) if len(number) >= 2 and number[0] == '0' and number[1] == '0'
        else number for number in digits]

flattened = []
for element in test:
    if type(element) == list:
        for inside in element:
            flattened.append(inside)
    if type(element) != list:
        flattened.append(element)


convert_int = [int(x) for x in flattened]
converted = [format(x, 'b') if x > 1 else str(x) for x in convert_int]
total = ''.join(converted)
length = 8

binaryTabs = [total[i:i+length] for i in range(0, len(total), length)]
print(binaryTabs)

