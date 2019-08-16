#!/usr/bin/env python3
#! -*- coding:utf8 -*-

__model__ = "config"
__version__ = "0.0.3"
__log__ = """
0.0.3 2018年3月22日 添加dapentiChecker
"""


# 需要注意，撰写子类时应该在此进行导入，否则lambda函数无法正常工作。

import bilibiliChecker
import zimuzuChecker
import expressChecker
import weatherChecker
import dapentiChecker
"""这是项目的配置文件，包括slack通知Webhook地址以及数据库用户名和密码，在上传Github和服务器前请确认此处信息。"""

data = {
    "model":{
        "bilibili":{
            "type":"bilibili",
            "slack_url":"https://hooks.slack.com/services/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",
            "func": lambda meta:getattr(bilibiliChecker.BiliChecker(metadata={}),"checkData")(meta)
            },
        "zimuzu":{
            "type":"zimuzu",
            "slack_url":"https://hooks.slack.com/services/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",
            "func": lambda meta:getattr(zimuzuChecker.ZMZChecker(metadata={}),"checkData")(meta)
            },
        "express":{
            "type":"express",
            "slack_url":"https://hooks.slack.com/services/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",
            "func": lambda meta:getattr(expressChecker.ExpressChecker(metadata={}),"checkData")(meta)
            },
        "weather":{
            "type":"weather",
            "slack_url":"https://hooks.slack.com/services/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",
            "func": lambda meta:weatherChecker.checkWeather(meta),
            "appcode":"bc5cf43ec23e40ccbf7424ec8774252c"
            },
        "dapenti":{
            "type":"dapenti",
            "slack_url":"https://hooks.slack.com/services/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",
            "func": lambda meta:dapentiChecker.checkTugua(meta)
            },
        "test":{
            "type":"test",
            "slack_url":"https://hooks.slack.com/services/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"
            },
        },
    "database":{
        "retry":3,
        "address":"file.mazhangjing.com",
        "port":27017,
        "name":["alidb","notice"],
        "auth":["corkine","mi960032"],
        },
}


	# OLD EXAMPLE
    # NUBANI = "[努巴尼守望先锋更新推送]","https://space.bilibili.com/ajax/member/getSubmitVideos?mid=20990353&pagesize=30&tid=0&page=1&keyword=&order=pubdate","https://space.bilibili.com/20990353/#/video"
    # ABU = "[阿布垃圾手册更新推送]","https://space.bilibili.com/ajax/member/getSubmitVideos?mid=13127303&pagesize=30&tid=0&page=1&keyword=&order=pubdate","https://space.bilibili.com/13127303/#/"
    # SKYTI = "[FROM SKYTI]","https://space.bilibili.com/ajax/member/getSubmitVideos?mid=14527421&pagesize=30&tid=0&page=1&keyword=&order=pubdate","https://space.bilibili.com/14527421/#/"
    # AIFOU = "[爱否科技更新推送]","https://space.bilibili.com/ajax/member/getSubmitVideos?mid=7458285&pagesize=30&tid=0&page=1&keyword=&order=pubdate","https://space.bilibili.com/7458285/#/"
    # KJMX = "[科技美学更新推送]","https://space.bilibili.com/ajax/member/getSubmitVideos?mid=3766866&pagesize=30&tid=0&page=1&keyword=&order=pubdate","https://space.bilibili.com/3766866?from=search&seid=7562537744771981035#/video"

    # SHIELD = "[神盾局特工更新]","http://diaodiaode.me/rss/feed/30675","http://www.zimuzu.tv/resource/30675"
    # DESCOVERY = "[星际迷航更新]","http://diaodiaode.me/rss/feed/35640","http://www.zimuzu.tv/resource/35640"
    # MIND = "[犯罪心理更新]","http://diaodiaode.me/rss/feed/11003","http://www.zimuzu.tv/resource/11003"
    # #TIANFU = "[天赋异禀更新]","http://diaodiaode.me/rss/feed/35668","http://www.zimuzu.tv/resource/35668"
    # XDYZ = "[相对宇宙更新]","http://diaodiaode.me/rss/feed/35840","http://www.zimuzu.tv/resource/35840"
    # #CARBON = "[副本更新]","http://diaodiaode.me/rss/feed/35833","http://www.zimuzu.tv/resource/35833"
    # HL = "[国土安全更新]","http://diaodiaode.me/rss/feed/11088","http://www.zimuzu.tv/resource/11088"
	
	# # NEW EXAMPLE
    # EXAMPLE = 
    # [{
    # "name":"孔夫子书籍",
    # "id":24323435431111,
    # "status":1,
    # "rate":20,
    # "type":"express",
    # "info":"50832418805076",
    # "data":[]
    # },{
    # "name":"神盾局特工更新",
    # "id":24323435431112,
    # "status":1,
    # "rate":25,
    # "type":"zimuzu",
    # "info":"[神盾局特工更新] http://diaodiaode.me/rss/feed/30675 http://www.zimuzu.tv/resource/30675",
    # "data":[]
    # },{
    # "name":"星际迷航更新",
    # "id":24323435431113,
    # "status":1,
    # "rate":25,
    # "type":"zimuzu",
    # "info":"[星际迷航更新] http://diaodiaode.me/rss/feed/35640 http://www.zimuzu.tv/resource/35640",
    # "data":[]
    # },{
    # "name":"犯罪心理更新",
    # "id":24323435431114,
    # "status":1,
    # "rate":25,
    # "type":"zimuzu",
    # "info":"[犯罪心理更新] http://diaodiaode.me/rss/feed/11003 http://www.zimuzu.tv/resource/11003",
    # "data":[]
    # },{
    # "name":"相对宇宙更新",
    # "id":24323435431115,
    # "status":1,
    # "rate":25,
    # "type":"zimuzu",
    # "info":"[相对宇宙更新] http://diaodiaode.me/rss/feed/35840 http://www.zimuzu.tv/resource/35840",
    # "data":[]
    # },{
    # "name":"科技美学更新推送",
    # "id":24323435431126,
    # "status":1,
    # "rate":30,
    # "type":"bilibili",
    # "info":"[科技美学更新推送] https://space.bilibili.com/ajax/member/getSubmitVideos?mid=3766866&pagesize=30&tid=0&page=1&keyword=&order=pubdate https://space.bilibili.com/3766866?from=search&seid=7562537744771981035#/video",
    # "data":[]
    # }]

