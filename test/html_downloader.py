import urllib


class HtmlDownloader(object):


    def downloade(self, new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)

        if response.getcode() != 200:
            return None
        html = response.read()
        new_html = html[2:len(html)]
        new_html = str(new_html,'utf-8','ignore')
        response.close()
        return new_html