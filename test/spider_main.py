# -*-coding:utf-8-*-
from test import html_downloader
from test import html_outputer
from test import html_parser
from test import url_manager
import pickle

from test import work_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.manager = work_manager.WorkManager()

    def save_craw_info(self, old_urls, new_urls, books_data):
        output_old_urls = open('old_urls.pkl', 'wb')
        output_new_urls = open('new_urls.pkl', 'wb')
        output_books_data = open('books_data.pkl', 'wb')
        # 保存已经爬过的url
        pickle.dump(old_urls, output_old_urls)
        # 保存爬到的数据
        pickle.dump(books_data, output_books_data)
        # 保存还没有爬过的url
        pickle.dump(new_urls, output_new_urls)
        output_old_urls.close()
        output_books_data.close()
        output_new_urls.close()

    def init_craw_data(self):
        global root_url
        try:
            books_old_url_file = open('old_urls.pkl', 'rb')
            books_new_url_file = open('new_urls.pkl', 'rb')
            books_data_file = open('books_data.pkl', 'rb')
            old_urls = pickle.load(books_old_url_file)
            new_urls = pickle.load(books_new_url_file)
            books_data = pickle.load(books_data_file)
            self.outputer.init_data(books_data)
            self.urls.add_old_urls(old_urls)
            self.urls.add_new_urls(new_urls)
            for url in new_urls:
                root_url = url
                break
            obj_spider.craw(root_url)
            return
        except:
            root_url = "http://www.zhuizhuishu.com/top.html"
            obj_spider.craw(root_url)
            return

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while (self.urls.has_new_url()):
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s ' % (count, new_url))
                html_content = self.downloader.downloade(new_url)
                new_urls, new_data = self.parser.pase(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count >= 100:
                    break
                count = count + 1
            except:
                print("craw failed")
        obj_spider.save_craw_info(self.urls.get_old_urls(), self.urls.get_new_urls(),
                                  self.outputer.datas)
        self.outputer.output_html()


if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.init_craw_data()
