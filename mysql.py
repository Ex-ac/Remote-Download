import pymysql
import hashlib
import datetime
import os

from enum import Enum

StaticConfig = {
    "host": "extryi.top",
    "port": 3306,
    "user": "user",
    "password": "7866",
    "db": "study",
    "charset": "utf8",
}


class DownloadStatus(Enum):
    Inavalibel = 0
    Delete = 1
    Running = 2
    Pause = 3


class Aria2cMySQL:

    def __init__(self):
        self._connection = None
        self.cursor = None

    def connect(self, config={}):

        global StaticConfig
        temp = StaticConfig
        temp.update(config)

        try:
            self._connection = pymysql.connect(**temp)
            self._cursor = self._connection.cursor()
            return True
        except Exception as identifier:
            print(identifier)
            return False

    def moviceNeedToGetUrl(self):
        sql = "select moviceName from WishMovies where needToCrawl = true group by moviceName";

        try:
            self._cursor.execute(sql);
            return self._cursor.fetchall();
        
        except Exception as e:
            
            print(e);
            return None;

    

    def movicesInformantionNeedUpdate(self):
        sql = "select moviceName, url, source from MovicesInformantion where status = 2";
        try:
            self._cursor.execute(sql);
            return self._cursor.fetchall();
        except Exception as e:
            print(e);
            return None;

    def addMovicesInformantion(self, wishName, movicesInformantionList):
        sql = "insert into MovicesInformantion (wishMoviceName, moviceName, url, source) values (%s, %s, %s, %s)";
        
        errorMsg = [];
        for each in movicesInformantionList:
            try:
                self._cursor.execute(sql, (wishName, each["name"], each["url"], each["source"]));
            except Exception as e:
                if e.args[0] == 1062:
                    sqlt = "update MovicesInformate set createTime = %s, downloadUrl = %s where moviceName = %s";
                    try:
                        self._cursor.execute(sqlt, (datetime.datetime.now(), each["url"], each["name"]));
                    except Exception as e:
                        print(e);
                        errorMsg.append(e);
                else:
                    print(e);
                    errorMsg.append(e);
        try:
            self._connection.commit();
            errorMsg.append(True);
        except Exception as e:
           
            #主键约束则更新时间
            errorMsg.append(e);
            print(e);

        return errorMsg;
       




    def addMoviceDownloadUrl(self, moviceName, downloadUrlList):
        sql = "insert into MovicesDownloadUrl (moviceName, downloadUrl) valuse (%s, %s)";

        try:
            self._cursor.execute(sql, (moviceName, downloadUrl, datetime.datetime.now()));
            self._connection.commit();
            return True;
        except Exception as e:
            print(e);
            return False;


'''
    def createUser(self, userName, password, email=None):
        temp = hashlib.md5()
        temp.update(password.encode("utf-8"))
        password = temp.hexdigest()

        sql = "insert into User (name, password, email) values (%s, %s, %s)"
        try:
            self._cursor.execute(sql, (userName, password, email))
            self._connection.commit()
            return True
        except Exception as e:
            if e.args[0] == 1062:
                print("该用户已经注册！！")
            return False

    def changePassword(self, userName, password):
        temp = hashlib.md5()
        temp.update(password.encode("utf-8"))
        password = temp.hexdigest()

        sql = "update User set password = %s where name = %s"
        try:
            self._cursor.execute(sql, (password, userName))
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def changeEmail(self, userName, email):
        sql = "update User set email = %s where name = %s"
        try:
            self._cursor.execute(sql, (email, userName))
            self._connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def getUserAll(self, userName):
        sql = "select name, password, email from User where name = %s"

        try:
            self._cursor.execute(sql, userName)
            return self._cursor.fetchone()
        except Exception as e:
            print(e)
            return None

    def getPassword(self, userName):
        sql = "select password from User where name = %s"
        try:
            self._cursor.execute(sql, userName)
            return self._cursor.fetchone()[0]
        except Exception as e:
            print(e)
            return None

    def getEmail(self, userName):
        sql = "select email from User where name = %s"
        try:
            self._cursor.execute(sql, userName)
            return self._cursor.fetchone()[0]
        except Exception as e:
            print(e)
            return None

    def userLoginUp(self, userName, password):

        result = self.getPassword(userName)

        temp = hashlib.md5()
        temp.update(password.encode("utf-8"))
        temp = temp.hexdigest()

        if temp == result:
            return True
        else:
            return False

    def addWishMovice(self, moviceName, userName, sendEmial=False, savePath=None):
        sql = "insert into WishMovies (moviceName, userName, createTime, sendEmail, savePath) values (%s, %s, %s, %s, %s)"
        if savePath and not os.path.isdir(savePath):
            print("path is inavaliable!")
            savePath = None
        try:
            self._cursor.execute(
                sql, (moviceName, userName, datetime.datetime.now(), sendEmial, savePath))
            self._connection.commit()
            return True
        except Exception as e:
            # userName inavalibel
            if e.args[0] == 1062:
                print("该用户已添加该部电影")
            elif e.args[0] == 1452:
                print("无效的用户")
            print(e)
            return False

    def whosNeedSendEmail(self, movice):
        sql = "select name, email from WishMovies inner join User where moviceName = %s and sendEmail = true group by name"
        try:
            self._cursor.execute(sql, movice)
            return self._cursor.fetchall()
        except Exception as e:
            print(e)
            return None;
'''

    
    

'''
    def setMoviceDownloadUrlInavailable(self, downloadUrl):
        sql = "update  MovicesDownloadUrl set available = false where downloadUrl = %s";

        try:
            self._cursor.execute(sql, downloadUrl);
            self._connection.commit();
            return True;
        except Exception as e:
            print(e);
            return False;

    def downloadInfo(self, gid = None):
        if gid :
            sql = "select * from Downloads where gid = %s" % gid;
        else:
            sql = "select * from Downloads";
        try:
            self._cursor.execute(sql);
            return self._cursor.fetchall();
        except Exception as e:
            print(e);
            return None;

    def updateDownLoadInfo(self, gid, speed, useTime = 2, size = 0):
        sql = "update Downloads set speed = %s, useTime +=%s, size = %s wher gid = %s";
        try:
            self._cursor.execute(sql, (speed, useTime, size, gid));
            self._connection.commit();
            return True;
        except Exception as e:
            print(e);
            return False;
'''


print("using Mysql.py");

if __name__ == "__main__":

    db = Aria2cMySQL()
    db.connect()


