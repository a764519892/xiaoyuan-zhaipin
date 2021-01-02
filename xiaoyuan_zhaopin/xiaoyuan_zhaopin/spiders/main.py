import scrapy
import re
import json




class MyspiderSpider(scrapy.Spider):
    name = "xiaoyuan"

    start_urls = [
        'https://xiaoyuan.zhaopin.com/',
    ]
    def parse(self, response):
        # urls = ['https://xiaoyuan.zhaopin.com/search/jn=2&pg=%s&cts=655' % i for i in range(1, 35)]
        # for url in urls:
        #     yield scrapy.Request(url, callback=self.wenzhou_zhaopin)
        # urls1 = ['https://xiaoyuan.zhaopin.com/search/jn=2&pg=%s&cts=565' % i for i in range(1, 35)]
        # for url1 in urls1:
        #     yield scrapy.Request(url1, callback=self.shijiazhuang_zhaopin)
        # urls2 = ['https://xiaoyuan.zhaopin.com/search/jn=2&pg=%s&cts=565&dt=1' % i for i in range(1, 35)]
        # for url2 in urls2:
        #     yield scrapy.Request(url2, callback=self.shijiazhuang_zhaopin)
        # urls3 = ['https://xiaoyuan.zhaopin.com/search/jn=2&pg=%s&cts=655&dt=1' % i for i in range(1, 35)]
        # for url3 in urls3:
        #     yield scrapy.Request(url3, callback=self.wenzhou_zhaopin)
        # urls4 = ('https://xiaoyuan.zhaopin.com/search/jn=2&cts=565&pg=1')
        # yield scrapy.Request(urls4, callback=self.shijiazhuang_zhaopin_daquan)
        urls5 = ('https://xiaoyuan.zhaopin.com/search/jn=2&pg=1&cts=655')
        yield scrapy.Request(urls5, callback=self.wenzhou_zhaopin_daquan)

    def wenzhou_zhaopin_daquan(self,response):
        # 工作地点 =response.xpath('//*[@id="queryOption"]/div[2]/div[1]/p[1]/span//text()').getall()
        职位类型 = response.xpath('//*[@id="queryOption"]/div[3]/div[1]/p[1]/span//text()').getall()
        for i in 职位类型:
            zhiwei_leixing = re.findall(r".*?\(", i.strip())
            zhiwei_leixing = ''.join(zhiwei_leixing)
            zhiwei_leixing = re.sub('\(', '', zhiwei_leixing)
            zhiwei_leixing_num = re.findall(r"\(.*?\)", i.strip())
            zhiwei_leixing_num = ''.join(zhiwei_leixing_num)
            zhiwei_leixing_num = re.sub('([\(\)])', '', zhiwei_leixing_num)
            if int(zhiwei_leixing_num) % 30 != 0:
                if int(zhiwei_leixing_num) // 30 <= 34:
                    zhiwei_leixing_page = int(zhiwei_leixing_num) // 30 + 1
                else:
                    zhiwei_leixing_page = 34
            else:
                if int(zhiwei_leixing_num) // 30 + 1 <= 34:
                    zhiwei_leixing_page = int(zhiwei_leixing_num) // 30 + 1
                else:
                    zhiwei_leixing_page = 34
            # print(zhiwei_leixing + ':'+ zhiwei_leixing_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\wenzhou.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_POSITION_SMALLTYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                zhiwei_leixing_url = t[zhiwei_leixing]
                urls = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=655&pg=%s&jt={}'.format(zhiwei_leixing_url) % i
                        for i in range(1, zhiwei_leixing_page + 1)]
                for url in urls:
                    yield scrapy.Request(url, callback=self.wenzhou_zhaopin)

        行业类型 = response.xpath('//*[@id="queryOption"]/div[4]/div[1]/p[1]/span//text()').getall()
        for i in 行业类型:
            hangye_leixing = re.findall(r".*?\(", i.strip())
            hangye_leixing = ''.join(hangye_leixing)
            hangye_leixing = re.sub('\(', '', hangye_leixing)
            hangye_leixing_num = re.findall(r"\(.*?\)", i.strip())
            hangye_leixing_num = ''.join(hangye_leixing_num)
            hangye_leixing_num = re.sub('([\(\)])', '', hangye_leixing_num)
            if int(hangye_leixing_num) % 30 != 0:
                if int(hangye_leixing_num) // 30 <= 34:
                    hangye_leixing_page = int(hangye_leixing_num) // 30 + 1
                else:
                    hangye_leixing_page = 34
            else:
                if (int(hangye_leixing_num // 30) + 1) <= 34:
                    hangye_leixing_page = int(hangye_leixing_num) // 30 + 1
                else:
                    hangye_leixing_page = 34
            # print(hangye_leixing + ':' + hangye_leixing_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\wenzhou.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_INDUSTRY']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                hangye_leixing_url = t[hangye_leixing]
                urls1 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=655&pg=%s&ind={}'.format(hangye_leixing_url) % i
                         for i in range(1, hangye_leixing_page + 1)]
                for url1 in urls1:
                    yield scrapy.Request(url1, callback=self.wenzhou_zhaopin)
        公司性质 = response.xpath('//*[@id="queryOption"]/div[5]/div[1]/p[1]/span//text()').getall()
        for i in 公司性质:
            gongsi_xingzhi = re.findall(r".*?\(", i.strip())
            gongsi_xingzhi = ''.join(gongsi_xingzhi)
            gongsi_xingzhi = re.sub('\(', '', gongsi_xingzhi)
            gongsi_xingzhi_num = re.findall(r"\(.*?\)", i.strip())
            gongsi_xingzhi_num = ''.join(gongsi_xingzhi_num)
            gongsi_xingzhi_num = re.sub('([\(\)])', '', gongsi_xingzhi_num)
            if int(gongsi_xingzhi_num) % 30 != 0:
                if int(gongsi_xingzhi_num) // 30 <= 34:
                    gongsi_xingzhi_page = int(gongsi_xingzhi_num) // 30 + 1
                else:
                    gongsi_xingzhi_page = 34
            else:
                if int(gongsi_xingzhi_num) // 30 + 1 <= 34:
                    gongsi_xingzhi_page = int(gongsi_xingzhi_num) // 30 + 1
                else:
                    gongsi_xingzhi_page = 34
            # print(gongsi_xingzhi+ ':' +gongsi_xingzhi_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\wenzhou.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_COMPANY_TYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                gongsi_xingzhi_url = t[gongsi_xingzhi]
                urls2 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=655&pg=%s&cor={}'.format(gongsi_xingzhi_url) % i
                         for i in range(1, gongsi_xingzhi_page + 1)]
                for url2 in urls2:
                    yield scrapy.Request(url2, callback=self.wenzhou_zhaopin)

        职位来源 = response.xpath('//*[@id="queryOption"]/div[6]/div[1]/p[1]/span//text()').getall()
        for i in 职位来源:
            zhiwei_laiyuan = re.findall(r".*?\(", i.strip())
            zhiwei_laiyuan = ''.join(zhiwei_laiyuan)
            zhiwei_laiyuan = re.sub('\(', '', zhiwei_laiyuan)
            zhiwei_laiyuan_num = re.findall(r"\(.*?\)", i.strip())
            zhiwei_laiyuan_num = ''.join(zhiwei_laiyuan_num)
            zhiwei_laiyuan_num = re.sub('([\(\)])', '', zhiwei_laiyuan_num)
            if int(zhiwei_leixing_num) % 30 != 0:
                if int(zhiwei_laiyuan_num) // 30 <= 34:
                    zhiwei_laiyuan_page = int(zhiwei_laiyuan_num) // 30 + 1
                else:
                    zhiwei_laiyuan_page = 34
            else:
                if (int(zhiwei_laiyuan_num // 30) + 1) <= 34:
                    zhiwei_laiyuan_page = int(zhiwei_laiyuan_num) // 30 + 1
                else:
                    zhiwei_laiyuan_page = 34
            # print(zhiwei_laiyuan + ':' +zhiwei_laiyuan_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\wenzhou.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_POSITION_SOURCE_TYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                zhiwei_laiyuan_url = t[zhiwei_laiyuan]
                urls2 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=655&pg=%s&js={}'.format(zhiwei_laiyuan_url) % i
                         for i in range(1, zhiwei_laiyuan_page + 1)]
                for url2 in urls2:
                    yield scrapy.Request(url2, callback=self.wenzhou_zhaopin)


    def shijiazhuang_zhaopin_daquan(self,response):
        # 工作地点 =response.xpath('//*[@id="queryOption"]/div[2]/div[1]/p[1]/span//text()').getall()
        职位类型 =response.xpath('//*[@id="queryOption"]/div[3]/div[1]/p[1]/span//text()').getall()
        for i in 职位类型:
            zhiwei_leixing = re.findall(r".*?\(", i.strip())
            zhiwei_leixing = ''.join(zhiwei_leixing)
            zhiwei_leixing = re.sub('\(', '', zhiwei_leixing)
            zhiwei_leixing_num = re.findall(r"\(.*?\)", i.strip())
            zhiwei_leixing_num = ''.join(zhiwei_leixing_num)
            zhiwei_leixing_num = re.sub('([\(\)])', '', zhiwei_leixing_num)
            if int(zhiwei_leixing_num) % 30 !=0:
                if int(zhiwei_leixing_num)//30 <=34:
                    zhiwei_leixing_page = int(zhiwei_leixing_num)//30+1
                else:
                    zhiwei_leixing_page = 34
            else:
                if int(zhiwei_leixing_num)//30+1 <=34:
                    zhiwei_leixing_page = int(zhiwei_leixing_num)//30 + 1
                else:
                    zhiwei_leixing_page = 34
            #print(zhiwei_leixing + ':'+ zhiwei_leixing_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\shijiazhuang.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_POSITION_SMALLTYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                zhiwei_leixing_url = t[zhiwei_leixing]
                urls = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=565&pg=%s&jt={}'.format(zhiwei_leixing_url) % i for i in range(1, zhiwei_leixing_page+1)]
                for url in urls:
                    yield scrapy.Request(url, callback=self.shijiazhuang_zhaopin)

        行业类型 =response.xpath('//*[@id="queryOption"]/div[4]/div[1]/p[1]/span//text()').getall()
        for i in 行业类型:
            hangye_leixing= re.findall(r".*?\(", i.strip())
            hangye_leixing = ''.join(hangye_leixing)
            hangye_leixing= re.sub('\(', '', hangye_leixing)
            hangye_leixing_num = re.findall(r"\(.*?\)", i.strip())
            hangye_leixing_num = ''.join(hangye_leixing_num)
            hangye_leixing_num = re.sub('([\(\)])', '', hangye_leixing_num)
            if int(hangye_leixing_num) % 30 !=0:
                if int(hangye_leixing_num)//30 <=34:
                    hangye_leixing_page = int(hangye_leixing_num)//30+1
                else:
                    hangye_leixing_page = 34
            else:
                if (int(hangye_leixing_num//30)+1) <=34:
                    hangye_leixing_page = int(hangye_leixing_num)//30+1
                else:
                    hangye_leixing_page = 34
            #print(hangye_leixing + ':' + hangye_leixing_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\shijiazhuang.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_INDUSTRY']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                hangye_leixing_url = t[hangye_leixing]
                urls1 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=565&pg=%s&ind={}'.format(hangye_leixing_url) % i for i in range(1, hangye_leixing_page+1)]
                for url1 in urls1:
                    yield scrapy.Request(url1, callback=self.shijiazhuang_zhaopin)
        公司性质 =response.xpath('//*[@id="queryOption"]/div[5]/div[1]/p[1]/span//text()').getall()
        for i in 公司性质:
            gongsi_xingzhi=re.findall(r".*?\(", i.strip())
            gongsi_xingzhi = ''.join(gongsi_xingzhi)
            gongsi_xingzhi =re.sub('\(', '', gongsi_xingzhi)
            gongsi_xingzhi_num = re.findall(r"\(.*?\)", i.strip())
            gongsi_xingzhi_num = ''.join(gongsi_xingzhi_num)
            gongsi_xingzhi_num = re.sub('([\(\)])', '', gongsi_xingzhi_num)
            if int(gongsi_xingzhi_num) % 30 !=0:
                if int(gongsi_xingzhi_num)//30 <=34:
                    gongsi_xingzhi_page = int(gongsi_xingzhi_num)//30+1
                else:
                    gongsi_xingzhi_page = 34
            else:
                if int(gongsi_xingzhi_num)//30+1 <=34:
                    gongsi_xingzhi_page = int(gongsi_xingzhi_num)//30+1
                else:
                    gongsi_xingzhi_page = 34
            #print(gongsi_xingzhi+ ':' +gongsi_xingzhi_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\shijiazhuang.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_COMPANY_TYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                gongsi_xingzhi_url = t[gongsi_xingzhi]
                urls2 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=565&pg=%s&cor={}'.format(gongsi_xingzhi_url) % i for i in range(1, gongsi_xingzhi_page+1)]
                for url2 in urls2:
                    yield scrapy.Request(url2, callback=self.shijiazhuang_zhaopin)

        职位来源 =response.xpath('//*[@id="queryOption"]/div[6]/div[1]/p[1]/span//text()').getall()
        for i in  职位来源:
            zhiwei_laiyuan=re.findall(r".*?\(", i.strip())
            zhiwei_laiyuan=''.join(zhiwei_laiyuan)
            zhiwei_laiyuan =re.sub('\(', '', zhiwei_laiyuan)
            zhiwei_laiyuan_num = re.findall(r"\(.*?\)", i.strip())
            zhiwei_laiyuan_num = ''.join(zhiwei_laiyuan_num)
            zhiwei_laiyuan_num = re.sub('([\(\)])', '', zhiwei_laiyuan_num)
            if int(zhiwei_leixing_num) % 30 !=0:
                if int(zhiwei_laiyuan_num)//30 <=34:
                    zhiwei_laiyuan_page = int(zhiwei_laiyuan_num)//30+1
                else:
                    zhiwei_laiyuan_page = 34
            else:
                if (int(zhiwei_laiyuan_num//30)+1) <=34:
                    zhiwei_laiyuan_page = int(zhiwei_laiyuan_num)//30+1
                else:
                    zhiwei_laiyuan_page = 34
            #print(zhiwei_laiyuan + ':' +zhiwei_laiyuan_num)
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\shijiazhuang.json', 'r',
                      encoding='utf8')as fp:
                content = fp.read()
                a = json.loads(content)['souoption']['SOU_POSITION_SOURCE_TYPE']
                ming = []
                zhi = []
                for i in a:
                    ming.append(i['name'])
                    zhi.append(i['code'])
                t = dict(zip(ming, zhi))
                zhiwei_laiyuan_url = t[zhiwei_laiyuan]
                urls2 = ['https://xiaoyuan.zhaopin.com/search/jn=2&cts=565&pg=%s&js={}'.format(zhiwei_laiyuan_url) % i for i in range(1, zhiwei_laiyuan_page+1)]
                for url2 in urls2:
                    yield scrapy.Request(url2, callback=self.shijiazhuang_zhaopin)




    def shijiazhuang_zhaopin(self,response):
        zhiwei = []
        chengshi = []
        zhaopinrenshu = []
        fabushijian = []
        leixing = []
        gongsi = []
        # page_1 = len(response.xpath('//*[@class="fn-left position"]//text()').extract())//2+1
        for i in range(1, 31):
            gongsi1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/div[1]/div[2]//text()".format(
                    i)).get(default='')
            zhiwei1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/div[1]/div[1]//text()".format(
                    i)).get(default='')
            chengshi1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[1]//text()".format(
                    i)).get(default='')
            zhaopinrenshu1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[2]//text()".format(
                    i)).get(default='')
            fabushijian1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[3]//text()".format(
                    i)).get(default='')
            leixing1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[4]//text()".format(
                    i)).get(default='')
            zhiwei.append(zhiwei1)
            chengshi.append(chengshi1)
            zhaopinrenshu.append(zhaopinrenshu1)
            fabushijian.append(fabushijian1)
            leixing.append(leixing1)
            gongsi.append(gongsi1)
        # gongsi=response.xpath('//*[@class="fn-right company"]//text()').extract()
        for i in range(len(zhiwei)):
            yield {
                'zhiwei': zhiwei[i],
                # 'xingzhi': xingzhi[i],
                'chengshi': chengshi[i],
                'zhaopinrenshu': zhaopinrenshu[i],
                'fabushijian': fabushijian[i],
                'gongsi': gongsi[i],
                'leixing': leixing[i],
                'wenjian_mingcheng': 'xiaoyuan_zhaopin_shijiazhuang'

            }
    def wenzhou_zhaopin(self,response):
        # zhiwei =response.xpath('//*[@class="fn-left position"]//text()').extract()
        # #xingzhi=response.xpath('//*[@class="fn-left source"]//text()').extract()
        # #xingzhi_1 = response.xpath('//*[@class="fn-left source blueBg"]//text()').extract()
        # chengshi=response.xpath('//*[@class="city fn-left"]//text()').extract()
        # zhaopinrenshu=response.xpath('//*[@class="num fn-left"]//text()').extract()
        # fabushijian=response.xpath('//*[@class="time fn-left"]//text()').extract()
        zhiwei =[]
        chengshi =[]
        zhaopinrenshu=[]
        fabushijian=[]
        leixing =[]
        gongsi = []
        for i in range(1,31):
            gongsi1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/div[1]/div[2]//text()".format(i)).get(default='')
            zhiwei1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/div[1]/div[1]//text()".format(i)).get(default='')
            chengshi1 =response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[1]//text()".format(i)).get(default='')
            zhaopinrenshu1=response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[2]//text()".format(i)).get(default='')
            fabushijian1=response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[3]//text()".format(i)).get(default='')
            leixing1 = response.xpath(
                "//body/div[@id='root']/div[@id='search']/div[@id='sou-position']/div[1]/div[2]/div[1]/div[1]/div[{}]/p[1]/span[4]//text()".format(i)).get(default='')
            zhiwei.append(zhiwei1)
            chengshi.append(chengshi1)
            zhaopinrenshu.append(zhaopinrenshu1)
            fabushijian.append(fabushijian1)
            leixing.append(leixing1)
            gongsi.append(gongsi1)
        #gongsi=response.xpath('//*[@class="fn-right company"]//text()').extract()
        for i in range(len(zhiwei)):
            yield {
                'zhiwei': zhiwei[i],
                #'xingzhi': xingzhi[i],
                'chengshi': chengshi[i],
                'zhaopinrenshu': zhaopinrenshu[i],
                'fabushijian': fabushijian[i],
                'gongsi': gongsi[i],
                'leixing': leixing[i],
                'wenjian_mingcheng':'xiaoyuan_zhaopin_wenzhou'

            }


