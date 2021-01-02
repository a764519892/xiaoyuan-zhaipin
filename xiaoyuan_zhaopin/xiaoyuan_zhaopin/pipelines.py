# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class XiaoyuanZhaopinPipeline:
    def process_item(self, item, spider):
        if item['zhiwei'] != '':
            print('---------write------------------')
            with open(r'D:\Study\pythonProject\scrapy\paqu_xiaoyuan_zhaopin\xiaoyuan_zhaopin\{}.csv'.format(item['wenjian_mingcheng']), 'a+', encoding='utf-8_sig') as f:
                # fieldnames = ['公司', '类型', '职位', '城市', '招聘人数','发布时间']  # 这是标题栏的内容
                # writer = csv.DictWriter(f, fieldnames=fieldnames)  # 把标题栏加入到csv文件中
                # writer.writeheader()  # 这一行是写入第一行的标题栏，放在for循环的外面，不然就会出现很多个标题栏
                # f.write(item['gongsi'] + '*' + item['leixing']+ '*'+ item['zhiwei']+  '*' + item['chengshi'] + '*'
                #         + item['zhaopinrenshu'] + '*' + item['fabushijian']  +'\n')  # 用逗号隔开
                csv_writer = csv.writer(f)
                csv_writer.writerow([item['gongsi'],item['leixing'], item['zhiwei'],item['chengshi'],
                        item['zhaopinrenshu'],item['fabushijian']])
                # writer.writerow(
                #     {'公司': item['gongsi'], '类型': item['leixing'], '职位': item['zhiwei'], '城市': item['chengshi'],
                #      '招聘人数': item['zhaopinrenshu'],'发布时间':item['fabushijian']})
            return item
        else:
            return item

