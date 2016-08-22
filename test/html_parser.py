import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def pase(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_data(self, page_url, soup):
        #  <li class="stname"><a href="/mulu_3510.html">五行天</a></li>
        #  <li><a href="/mulu_3510.html">第三百六十七章 石像</a></li>
        #  <li class="gxdate">08-22 09:59</li>
        #  <li class="gxdate">10.0</li>
        book_info = {}
        books = {}
        # 小说最新章节标题
        books_new_title = set
        # 小说最新章节地址
        books_new_url = set
        # 小说名字
        books_name = set
        # 小说地址
        books_url = set
        # 小说最近更新时间
        books_update_time = set

        item = soup.find('ul', class_="xiaoshuolist").find('li', class_="stname")
        count = 0
        while ():
            item = item.find_next_sibling('li')
            if item is not None:
                count = count + 1
                book_info['count'] = item
                #每四个<li>组成一个完整的bookInfo
                if count % 4 == 0:
                    count = 0
                    books_name.add(book_info['1'].find('a').get_text())
                    books_url.add(urlparse(page_url,book_info['1'].find('a')['href']))
                    books_new_title.add(book_info['2'].find('a').get_text())
                    books_new_url.add(urlparse(page_url,book_info['2'].find('a')['href']))
                    books_update_time.add(book_info['3'].get_text())
            else:
                print("处理完一个页面啦。。。")
                break
        books['name'] = books_name
        books['url'] = books_url
        books['new_url'] = books_new_url
        books['new_title'] = books_new_title
        books['update_time'] = books_update_time
        return books



    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 这是小说榜单页面
        # <a href="/top_2.html" style="margin-right:5px;">2</a>
        links = soup.find('div', div="divPageNav").find_all('a',
                                                            href=re.compile(r"/top_\d+\.html"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
