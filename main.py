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

        movicesInformantionList = db.
