class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_old_urls(self):
        if self.old_urls is not None:
            return self.old_urls
        else:
            return

    def add_old_urls(self, old_urls):
        for url in old_urls:
            self.old_urls.add(url)

    def get_new_urls(self):
        if self.new_urls is not None:
            return self.new_urls
        else:
            return
