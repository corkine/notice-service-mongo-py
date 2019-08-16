#!/usr/bin/env python3
"""此模块用来进行各项目的检查。但不涉及具体检查方式和API调用，而是直接运行子模块获得一个返回值。
"""

__model__ = "checker"
__version__ = "0.1.0"
__log__ = """
0.0.0 START AT 2018-03-03
0.0.1 2018-03-04 服务器测试部署本
0.0.2 2018-03-05 添加了config文件，用以保存数据库密码、数据结构类型以及函数调用方法，这样的话，本模块就无需再进行更改。
顺便删除了在每个项目中进行频率判定的代码，现在在metalist即进行判断。删除了在每个项目中判断status==1的代码，
因为在数据库获取信息时即可过滤status!=1的项目。
0.0.3 2018-03-05 更改了日志记录策略，如果没有更新或者没有错误消息则不记录日志。如果在数据库发现一条新记录(状态为-1)，则不会默认推送
前三条消息，而是推送一条“将会继续保持更新的消息”,然后将此条目标记为开始。
0.0.4 2018-03-05 修正了一个bug，现在新添加的项目会立即收到测试推送的通知，而不是等到rate到达的时候
0.0.5 2018-03-07 服务器自动化更新版本，上线测试
0.1.0 2018-03-15 修正了rate字段类型判断的问题。同时由于新版本发布，将此版本移动至偶数版本号进行维护，代号Marvin I"""

from connect import Connection
import config

class Checker:
    """Checker用于定时根据数据库信息查询网站/API是否有更新。
    查询项目的源信息作为字典meta传入。
    - 根据此字典的type字段进行不同模块Checker调用
    - 根据此字典的rate字段进行不同间隔分钟数的Checker调用
    - 根据此字典的info/data字段传入各自子模块Checker参数并返回：其一为数据库保存列，其二为推送列，其三为是否终止查询
    
    Checker不涉及数据库连接、数据导入、信息推送和数据库写入"""

    def __init__(self,meta):
        """初始化查询，传入信息必须包含类型、频率、状态、id、信息和数据"""
        self.meta = meta
        for item in ["rate","type","status","id","info","data"]:
            if not item in self.meta:
                raise ValueError("From goCheck(): Data is not completion")
    
    def rateNow(self,rate=None,now=None):
        """根据查询项的查询频率判断当前时间是否要进行项目的查询"""
        if not rate:
            raise ValueError("From isNow function: You must intro a rate.")
        
        if not (isinstance(rate,float) or isinstance(rate,int)) or str(rate).startswith("@"):
            return False
        if not now:
            import time
            hm = time.strptime(time.ctime())[3:5]
            if len(str(hm[0])) == 1:
                hour = "0" + str(hm[0])
            else:
                hour = str(hm[0])
            if len(str(hm[1])) == 1:
                mint = "0" + str(hm[1])
            else:
                mint = str(hm[1])
            now = hour + mint
            # print(now)
        hour = []
        for x in range(24):
            x = str(x)
            if len(x) == 1:
                x = "0" + x
            hour.append(x)
        minute = []
        for x in range(60):
            x = str(x)
            if len(x) == 1:
                x = "0" + x
            minute.append(x)
        times = []
        for x in hour:
            for y in minute:
                times_sum = x + y
                times.append(times_sum)
        count = 0
        for x in times:
            if count % int(rate) == 0:
                # print(x,count)
                if x == now:
                    return True
            count += 1
        return False

    def goCheck(self,meta={}):
        """将查询分布到不同的子模块查询类中进行查询，返回数据库保存列表、推送列表和是否终止查询参数
        如果需要新建子模块，只需返回两个文本字段列表和是否终止参数,将此函数保存在config.data字典中"""
        if meta == {}:
            meta = self.meta
        func = config.data["model"][meta["type"]]["func"]
        return func(meta)

class Updater:
    """接受WebAPI地址和数据信息，将数据推送到互联网接口，比如Slack、邮件等"""

    def __init__(self,url=""):
        self.url = url
        pass
    
    def toSlack(self, url = "" , text = ""):
        '''将文本打包为json格式，使用Webhook的方式POST到Slack的Webhook，返回状态码'''
        import json, requests
        if url == "":
            url = self.url
        payload = {'text':text}
        data = json.dumps(payload)
        response = requests.post(url, data=data)
        return response.text

class TransDB(Connection):
    """用于alidb/notice数据库的连接、查询和写入以及修改，继承自Connection类"""
    
    def __init__(self,address,username,passwd,retry):
        super().__init__(address=address,username=username,passwd=passwd,retry=0)
        # print(self.getStatus())
        self.notice = self.db.notice


    def queryInfo(self):
        result = self.notice.find({"status":{"$in":[1,-1]}})
        result = list(result)
        return result

    def writeData(self,meta={},data=[]):
        if meta == {} or data == []:
            return 0
        r = self.notice.update_many({"id":meta["id"]},{"$push":{"data":{"$each":data}}})
        if r.modified_count == 1:return 1
        else: return 0

    def endItem(self,meta={}):
        if meta == {}:
            return 0
        r = self.notice.update_one({"id":meta["id"]},{"$set":{"status":0}})
        if r.modified_count == 1: return 1
        else: return 0

    def startItem(self,meta={}):
        if meta == {}:
            return 0
        r = self.notice.update_one({"id":meta["id"]},{"$set":{"status":1}})
        if r.modified_count == 1: return 1
        else: 
            return 0
 

def mainCheck(meta,db=TransDB):
    import traceback, pymongo
    log = ""
    """接受项目元信息、数据库句柄以进行面向过程的更新查询、数据库写入、推送通知以及项目终止和日志记录类"""
    trans = db
    log += "\n====================正在处理：%s/%s/%s====================\n"%(meta["name"],meta["type"],meta["rate"])
    log += "\n基本信息：\n%s\n"%meta["info"]
    #进行数据检查
    # 由于数据库获取信息已经考虑到所有status为1的情况，这里不需要重新判断。
    result = Checker(meta).goCheck()
    if meta["type"] in config.data["model"]:
        url = config.data["model"][str(meta["type"])]["slack_url"]
    else:
        url = config.data["model"]["test"]["slack_url"]
    #如果是新建对象，则直接保存，只推送一条消息
    if meta["status"] == -1:
        a,b,c = result
        newitem = "[%s] 已保存设置，Slack将会推送其更新消息。"%(meta["name"])
        result = a,[newitem],c
    #进行数据推送
    pushlog = ""
    pushcode = 0
    try:
        if isinstance(result[1],list):
            #如果为空集合，则不会进行下一步
            for x in result[1]:
                for y in range(3):
                    r = Updater(url).toSlack(text=x)
                    if r == "ok": 
                        pushlog += "\n推送消息成功。\n"
                        break
        elif isinstance(result[1],str):
            for y in range(3):
                r = Updater(url).toSlack(text=result[1])
                if r == "ok": 
                    pushlog += "\n推送消息成功。\n"
                    break
    except:
        pushlog += "\n[在推送时发生错误]，错误详情如下：\n"
        pushlog += "\n%s\n"%traceback.format_exc()
    finally:
        if "推送消息成功" in pushlog:
            pushcode = 1
        else:
            pushcode = 0
        # pushlog += "\n推送流程处理完毕。\n"
        log += pushlog
    # 进行数据库保存
    savelog = ""
    savecode = 0
    if pushcode == 1:
        try:
            code = trans.writeData(meta,result[0])
            if code != 1:raise pymongo.errors.InvalidOperation("pymongo无法保存此项目，可能是没有新数据或者网络连接失败")
            savelog += "\n保存到数据库成功。\n"
        except:
            savelog += "\n[在保存时发生错误]，错误详情如下：\n"
            savelog += "\n%s\n"%traceback.format_exc()
        finally:
            if "保存到数据库成功" in savelog:
                savecode = 1
            else:
                savecode = 0
            # savelog += "\n保存到数据库流程处理完毕。\n"
            log += savelog
    # 这里有时候需要更改以终止计划
    endlog = ""
    if result[2] == 0:
        try:
            code = trans.endItem(meta=meta)
            if code !=1:raise pymongo.errors.InvalidOperation("pymongo无法终止此项目")
            endlog += "\n已终止此项目。\n"
        except:
            endlog += "\n[在终止时发生错误]，错误详情如下：\n"
            endlog += "\n%s\n"%traceback.format_exc()
        finally:
            log += endlog
    # 有时候需要开始处理计划
    startlog = ""
    if meta["status"] == -1:
        try:
            code = trans.startItem(meta=meta)
            if code != 1 : raise pymongo.errors.InvalidOperation("pymongo无法开始此项目")
            startlog += "\n已开始此项目。\n"
        except:
            startlog += "\n[在开始时发生错误]，错误详情如下：\n"
            startlog += "\n%s\n"%traceback.format_exc()
        finally:
            log += startlog
    log += "\n整体流程处理完毕。\n"
    if endlog == "" and startlog == "" and pushcode == 0:
        log = "" #如果没有任何更新则不返回数据
    return log

def main(log="check.log"):
    import time,traceback,sys
    tmp_out = sys.stdout
    tmp_err = sys.stderr
    if log == "":
        raise ValueError("LOG文件无法打开，请检查程序所在文件夹写权限")

    try:
        file = open(log,"r",encoding="utf_8",errors="ignore")
        checklen = file.read()
        if len(checklen) > 20000:
            sys.stdout = open(log,'w',encoding="utf_8",errors="ignore")
            sys.stderr = open(log,'w',encoding="utf_8",errors="ignore")
            print("之前的历史记录已清空。\n")
        else:
            sys.stdout = open(log,'a',encoding="utf_8",errors="ignore")
            sys.stderr = open(log,'a',encoding="utf_8",errors="ignore")
        file.close()
    except:
        sys.stdout = open(log,'a',encoding="utf_8",errors="ignore")
        sys.stderr = open(log,'a',encoding="utf_8",errors="ignore")
        print("你创建了日志文件。\n")
    
    metalist = []
    try:
        address, user, passwd, retry = config.data["database"]["address"],config.data["database"]["auth"][0], \
        config.data["database"]["auth"][1],config.data["database"]["retry"]
        check = TransDB(address, user, passwd, retry)
        metalist = check.queryInfo()
    except:
        print("\n\n++++++++++++++++++%s++++++++++++++++++\n\n"%str(time.ctime()))
        print("【主进程】在连接数据库并获取元数据时出错，错误如下：\n")
        print(str(traceback.format_exc()))
        return 0
        
    try:
        sublog = ""
        subhead = ""
        if metalist != []:
            subhead += "\n\n++++++++++++++++++%s++++++++++++++++++\n\n"%str(time.ctime())
            subhead += "【主进程】项目进程准备就绪————————————>\n"
            for meta in metalist:
                try:
                    # 由于数据库获取信息已经考虑到所有status为1的情况，这里不需要重新判断。
                    # #测试用
                    # log = mainCheck(meta,check)
                    # sublog += str(log)
                    # 如果是即刚添加的话，最好在下一分钟就产生通知。
                    if "status" in meta and meta["status"] == -1:
                        log = mainCheck(meta,check)
                        sublog += str(log)
                    else:
                        if Checker(meta).rateNow(rate=meta["rate"]): 
                            log = mainCheck(meta,check)
                            sublog += str(log)
                        else : 
                            continue

                except:
                    print("【子进程】在检索和更新本项目数据时出错，错误如下：\n")
                    print(str(traceback.format_exc()))
            # 如果子项目没有更新则不返回数据
            if sublog == "":pass
            else: print(subhead,sublog) 
    except:
        print("\n\n++++++++++++++++++%s++++++++++++++++++\n\n"%str(time.ctime()))
        print("【主进程】在检索和更新数据时出错，错误如下：\n")
        print(str(traceback.format_exc()))
    finally:
        pass
        
    
    sys.stdout.close()
    sys.stderr.close()
    sys.stdout = tmp_out
    sys.stderr = tmp_err
    return 0
if __name__ == "__main__":  

    main()
