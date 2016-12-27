from .sql import Sql
from TestScrapy.items import TestscrapyItem

class TestScrapyPipeline(object):

    def process_item(self,item,spider):
        if isinstance(item,TestscrapyItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                Sql.insert_dd_name(xs_name,xs_author,category,name_id)
                print('开始存小说标题')