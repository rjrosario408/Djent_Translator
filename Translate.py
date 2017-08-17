import re
import bs4 as bs
import urllib.request


def binary_tabs(link):
    soup = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(soup, 'lxml')
    contents = soup.find("pre", {"class": "js-tab-content js-copy-content js-tab-controls-item"})
    tabs = str(contents)
    digits = re.findall(r'(?<=-)(\d+)', tabs)

    test = [list(number) if len(number) >= 2 and number[0] == '0' and number[1] == '0'
            else number for number in digits]

    flattened = []
    for element in test:
        if type(element) == list:
            for inside in element:
                flattened.append(int(inside))
        if type(element) != list:
            flattened.append(int(element))

    total = ''.join([format(x, 'b') if x > 1 else str(x) for x in flattened])
    length = 8

    return [total[i:i + length] for i in range(0, len(total), length)]

binary_tabs('https://tabs.ultimate-guitar.com/e/emmure/10_signs_you_should_leave_tab.htm')
