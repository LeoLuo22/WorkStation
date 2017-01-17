import requests
from bs4 import BeautifulSoup
import lxml
import random
import time
import threading

HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

threadLock = threading.Lock()

class BookSpider(threading.Thread):
    def __init__(self, payload):
        threading.Thread.__init__(self)
        self.unusedUrls = []
        self.payload = payload
        with open('unusedUrls.txt', 'r') as fh:
            for line in fh:
                line = line.replace('\n', '')
                self.unusedUrls.append(line)

    def get_urls(self, payload=None):
        """Discover more urls
        @param payload: dict, {'marc_no': 'id'}
        @return
        """
        if payload == None:
            payload = self.payload
        threadLock.acquire()
        ajax_url = 'http://wiscom.chd.edu.cn:8080/opac/ajax_likehood_book.php'
        try:
            response = requests.get(ajax_url, params=payload, headers=HEAD)
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            return self.get_urls({'marc_no': self.unusedUrls[random.randint(0, len(self.unusedUrls)-1)]})
        soup = BeautifulSoup(response.text, 'lxml')
        hrefs = soup.find_all('a', attrs={'target': '_blank'})
        for href in hrefs:
            marc_no = href.get('href').split('=')[1]
            if marc_no not in self.unusedUrls:
                print(marc_no)
                with open('unusedUrls.txt', 'a') as f:
                    f.write(marc_no+'\n')
                self.unusedUrls.append(marc_no)
        self.get_urls({'marc_no': self.unusedUrls[random.randint(0, len(self.unusedUrls)-1)]})
        threadLock.release()

    def run(self):
        threadLock.acquire()
        self.get_urls()
        threadLock.release()

def main():

    threads = []
    book1 = BookSpider({'marc_no': '0000378068'})
    book2 = BookSpider({'marc_no': '0000190486'})
    book3 = BookSpider({'marc_no': '0000353887'})
    book4 = BookSpider({'marc_no': '0000196987'})

    book1.start()
    book2.start()
    book3.start()
    book4.start()

    threads.append(book1)
    threads.append(book2)
    threads.append(book3)
    threads.append(book4)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()

