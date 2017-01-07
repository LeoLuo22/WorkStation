
class BookSpider():
    def __init__(self):
        self.unusedUrls = []

    def get_urls(self, payload):
        """Discover more urls
        @param payload: dict, {'marc_no': 'id'}
        @return
        """
        ajax_url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_likehood_book.php'
        response = requests.get(ajax_url, params=payload, headers=HEAD)
        soup = BeautifulSoup(response.text, 'lxml')
        hrefs = soup.find_all('a', attrs={'target': '_blank'})
        for href in hrefs:
            marc_no = href.get('href').split('=')[1]
            if marc_no not in self.unusedUrls:
                print(marc_no)
                with open('unusedUrls.txt', 'a') as f:
                    f.write(marc_no+'\n')
                self.unusedUrls.append(marc_no)
        print(len(self.unusedUrls))
        #self.get_urls({'marc_no': self.unusedUrls[random.randint(0, len(self.unusedUrls)-1)]})
