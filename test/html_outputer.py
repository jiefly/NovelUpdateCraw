class HtmlOutputer(object):
    def __init__(self):
        self.datas = {}
    def collect_data(self, data):
        if data is None:
            return
        self.datas = dict(data,**self.datas)

    def init_data(self, books_data):
        self.datas = books_data

    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')

        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"></head>")
        fout.write("<body>")
        fout.write("<ul>")

        for k,data in self.datas.items():
            fout.write("<li>")
            fout.write("<ul>%s" % k)
            fout.write("<li>book_name:%s</li>" % data[0])
            fout.write("<li>book_url:%s</li>" % data[1])
            fout.write("<li>book_title:%s</li>" % data[2])
            fout.write("<li>book_title_url:%s</li>" % data[3])
            fout.write("<li>book_update_time:%s</li>" % data[4])
            fout.write("</ul>")
            fout.write("</li>")

        fout.write("</ul>")
        fout.write("</body>")
        fout.write("</html>")


