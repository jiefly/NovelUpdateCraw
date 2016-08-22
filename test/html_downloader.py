import urllib


class HtmlDownloader(object):


    def downloade(self, new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()
