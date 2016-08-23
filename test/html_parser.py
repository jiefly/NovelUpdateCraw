import re
import urllib
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def pase(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf8')
        return self._get_new_urls(page_url, soup), self._get_new_data(page_url, soup)

    def _get_new_data(self, page_url, soup):
        #  <li class="stname"><a href="/mulu_3510.html">五行天</a></li>
        #  <li><a href="/mulu_3510.html">第三百六十七章 石像</a></li>
        #  <li class="gxdate">08-22 09:59</li>
        #  <li class="gxdate">10.0</li>
        book_info = {}
        books = {}
        # 小说最新章节标题
        books_new_title = {}
        # 小说最新章节地址
        books_new_url = {}
        # 小说名字
        books_name = {}
        # 小说地址
        books_url = {}
        # 小说最近更新时间
        books_update_time = {}
        # 网站url
        web_url = "http://www.zhuizhuishu.com/"

        item = soup.find('ul', class_="xiaoshuolist").find('li', class_="stname")
        item = item.find_next_sibling('li')
        item = item.find_next_sibling('li')
        item = item.find_next_sibling('li')
        count = 0
        while (item.find_next_sibling('li') != None):
            item = item.find_next_sibling('li')
            if item is not None:
                count = count + 1
                if count == 1:
                    book_info['name_and_url'] = item
                elif count == 2:
                    book_info['title_and_url'] = item
                elif count == 3:
                    book_info['update_time'] = item
                # 每四个<li>组成一个完整的bookInfo
                if count % 4 == 0:
                    count = 0
                    book = []
                    name = book_info['name_and_url'].find('a').get_text()
                    book.append(name)
                    url = urllib.parse.urljoin(web_url, book_info['name_and_url'].find('a')['href'])
                    book.append(url)
                    title = book_info['title_and_url'].find('a').get_text()
                    book.append(title)
                    new_url = urllib.parse.urljoin(web_url,
                                                   book_info['title_and_url'].find('a')['href'])
                    book.append(new_url)
                    update_time = book_info['update_time'].get_text()
                    book.append(update_time)
                    books[name] = book

            else:
                print("处理完一个页面啦。。。")
                break
        return books

    def _get_new_urls(self, page_url, soup):
        if page_url != "http://www.zhuizhuishu.com/top.html":
            return
        new_urls = set()
        # 这是小说榜单页面
        # <a href="/top_2.html" style="margin-right:5px;">2</a>

        # links = soup.find('div', id="divPageNav").find_all('a',
        #                                                    href=re.compile(r"/top_\d+\.html"))
        # for link in links:
        #     new_url = link['href']
        #     new_full_url = urllib.parse.urljoin(page_url, new_url)
        #     new_urls.add(new_full_url)
        link = soup.find('div', id="divPageNav").find('a', text="尾页")['href']
        patt = re.compile(r"(\d+)")
        page_num = int(patt.search(link).group())
        for i in range(1,page_num+1):
            new_url = urllib.parse.urljoin(page_url,''.join(['/top_',str(i),'.html']))
            new_urls.add(new_url)
        return new_urls
