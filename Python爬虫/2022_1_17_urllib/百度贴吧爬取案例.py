'''
    实现步骤:
        1. 查看所抓内容在响应内容中是否存在
            右键-查看网页源码-搜索数据关键字
        2. 查找并分析url地址规律
            第一页:https://tieba.baidu.com/f?kw=??&ie=utf-8&pn=0
            第二页:https://tieba.baidu.com/f?kw=??&ie=utf-8&pn=50
            第三页:https://tieba.baidu.com/f?kw=??&ie=utf-8&pn=100
            页数:pn = (n-1) * 50
        3. 发请求获取响应内容

        4. 保存到本地文件
'''

from urllib import request, parse


class BaiduTieBaSpider:

    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

    def get_html(self, url):
        """获取响应内容函数"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    def parse_html(self, word):
        """解析提取数据函数"""
        result = parse.quote(word)
        return result

    def save_html(self, filename, html):
        """数据处理函数"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html)

    def run(self):
        """程序入口函数"""
        # 输入查询贴吧关键字
        word = input('请输入您要查询贴吧的关键字:')
        # 数据编码
        result = self.parse_html(word)
        # 查询起始页
        start = int(input('请输入查询起始页:')) - 1
        # 终止页
        end = int(input('请输入终止页数:'))
        for i in range(start, end):
            url = self.url.format(result, i * 50)
            html = self.get_html(url)
            filename = './test/{}_{}.html'.format(word, i + 1)
            self.save_html(filename, html)
            print('{}_{}页数据爬取完毕'.format(word, i + 1))

if __name__ == '__main__':
    spider = BaiduTieBaSpider()
    spider.run()