from mysql import *
from getMovices import *
import time
if __name__ == "__main__":
    db = Aria2cMySQL();
    if db.connect():
        wishMoviceList = db.moviceNeedGetUrl();

        for each in wishMoviceList:
            movicesInformantionList = [];
            movicesInformantionList += getMovicesInformationFrom80s(each["moviceName"]);
            movicesInformantionList += getMovicesInformationFromPiaoHua(each["moviceName"]);
            temp = db.addMovicesInformantion(each["moviceName"], movicesInformantionList);
            time.sleep(2);
            if temp[0] != True:
                #错误处理
                print(temp);
        
        movicesInformantionList = [];

        movicesInformantionList = db.movicesInformantionNeedUpdate();


        for each in movicesInformantionList:
            print(each);
            temp = [];
            if each["source"] == "piaohua":
                pass;
                temp = getMovicesDownloadUrlFromPiaohua(each["url"]);
            elif each["source"] == "80s":
                temp = getMovicesDownloadUrlFrom80s(each["url"]);
            else:
                pass;
            time.sleep(2);
            temp = db.addMoviceDownloadUrl(each["moviceName"], temp);
            if temp[0] != True:
                #错误处理
                print(temp);

    
