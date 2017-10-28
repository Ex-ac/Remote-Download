from mysql import *
from getMovices import *

if __name__ == "__main__":
    db = Aria2cMySQL();
    if db.connect():
        wishMoviceList = db.moviceNeedGetUrl();

        for each in wishMoviceList:
            movicesInformantionList = [];
            movicesInformantionList.append(getMovicesInformationFrom80s(each));
            movicesInformantionList.append(getMOvicesInformationFromPiaoHua(each));
            temp = db.addMovicesInformantion(each, movicesInformantionList);
            if temp[-1] != True:
                #错误处理
                pass;
        
        movicesInformantionList = [];

        movicesInformantionList = db.MovicesInformantionNeedUpdate();

        movicesDownloadUrlList = [];

        for each in movicesInformantionList:
            temp = [];
            if each["source"] == "piaohua":
                temp = getMovicesDownloadUrlFromPiaohua(each["url"]);
            elif each["source"] == "80s":
                temp = getMovicesDownloadUrlFrom80s(each["url"]);
            else:
                pass;

            d
