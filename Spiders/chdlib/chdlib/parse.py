import lxml
import requests
from bs4 import BeautifulSoup

response = requests.get('http://wiscom.chd.edu.cn:8080/opac/item.php?marc_no=0000198282')

def parse():
    book = {}
    base = response.content.decode('utf-8')
    soup = BeautifulSoup(base, 'lxml')
    ID = soup.find('a', attrs={'title': '点击查看详细'}).get('href').split('=')[1]
    book['ID'] = ID
    item_detail_soup = soup.find_all('dl', attrs={'class': 'booklist'})
    for detail in item_detail_soup:
        if detail.dt.string:
            book[detail.dt.string.replace(':', '')] = detail.dd.get_text()
    book.pop('豆瓣简介：')
    isbn = get_isbn(item_detail_soup)
    book['isbn'] = isbn
    book['douban'] = get_douban_info(isbn)
    #print(book)
    lib = []
    i = []
    lib_info_soup = soup.find('div', attrs={'id': 'tabs2'})
    infos = lib_info_soup.find_all('tr', attrs={'align': 'left', 'class': 'whitetext'})
    for info in infos:
        msgs = info.find_all('td')
        for msg in msgs:
            msg = msg.get_text().replace('\xa0', '').replace('\r', '').replace('\t', '').replace('\n', '')
            i.append(msg.replace(' ',''))
        lib.append(i)
        i = []
    book['lib'] = lib

    return book



def get_isbn(soup):
    isbn_raw = soup[2].dd.string
    try:
        isbn = isbn_raw.split('/')[0]
    except AttributeError:
        return 0
    while '-' in isbn:
        isbn = isbn.replace('-', '')
    return isbn

def get_douban_info(isbn):
    """Get book's info from douban
    @param isbn
        Book's isbn
    @return
        A dict that contains douban info
    """
    info_dict = {}
    url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_douban.php'
    payload = {'isbn': isbn}
    try:
        response = requests.get(url, params=payload)
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        return self.__get_douban_info(isbn)
    infos = eval(response.text) #eval function can convert str object to dict object
    for key, value in infos.items():
        while '\\' in value:
            value = value.replace('\\', '')
            infos[key] = value
    return infos

def get_next_url(ID):
    ajax_url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_likehood_book.php?marc_no={0}'.format(ID)
    #print(ajax_url)
    response = requests.get(ajax_url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    hrefs = soup.find_all('a', attrs={'target': '_blank'})
    for href in hrefs:
        marc_no = href.get('href').split('=')[1]
        print(marc_no)

def main():
    #get_next_url('0000386626')
    print(parse())

if __name__ == '__main__':
    main()
