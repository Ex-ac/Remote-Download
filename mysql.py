import pymysql.cursors
import hashlib

StaticConfig = {
    "host": "extryi.top",
    "port": 3306,
    "user": "user",
    "password": "7866",
    "db": "study",
    "charset": "utf8",
}


class Aria2cMySQL:

    def __init__(self):
        self._connection = None;
        self.cursor = None;

    def connect(self, config = {}):

        global StaticConfig;
        temp = StaticConfig;
        temp.update(config);

        try:
            self._connection = pymysql.connect(**temp);
            self._cursor = self._connection.cursor();
            return True;
        except Exception as identifier:
            print(identifier);
            return False;

    def cretaeUser(self, userName, password, email = None):
        temp = hashlib.md5();
        temp.update(password.encode("utf-8"));
        password = temp.hexdigest();
        
        sql = "insert into User (name, password, email) values (%s, %s, %s)";
        try:
            self._cursor.execute(sql, (userName, password, email));
            self._connection.commit();
            return True;
        except Exception as e:
            if e.args[0] == 1062:
                print("该用户已经注册！！");
            return False;
    
    def changePassword(self, userName, password):
        temp = hashlib.md5();
        temp.update(password.encode("utf-8"));
        password = temp.hexdigest();

        sql = "update User set password = %s where name = %s";
        try:
            self._cursor.execute(sql, (password, userName));
            self._connection.commit();
            return True;
        except Exception as e:
            print(e);
            return False;


    def changeEmail(self, userName, email):
        sql = "update User set email = %s where name = %s";
        try:
            self._cursor.execute(sql, (email, userName));
            self._connection.commit();
            return True;
        except Exception as e:
            print(e);
            return False;

    def getUserAll(self, userName):
        sql = "select name, password, email from User where name = %s";

        try:
            self._cursor.execute(sql, userName);
            return self._cursor.fetchone();
        except Exception as e:
            print(e);
            return None;

    def getPassword(self, userName):
        sql = "select password from User where name = %s";
        try:
            self._cursor.execute(sql, userName);
            return self._cursor.fetchone()[0];
        except Exception as e:
            print(e);
            return None;

    def getEmail(self, userName):
        sql = "select email from User where name = %s";
        try:
            self._cursor.execute(sql, userName);
            return self._cursor.fetchone()[0];
        except Exception as e:
            print(e);
            return None;

    def userLoginUp(self, userName, password):
       
        result = self.getPassword(userName);

        temp = hashlib.md5();
        temp.update(password.encode("utf-8"));
        temp = temp.hexdigest();

        if temp == result:
            return True;
        else:
            return False;


    def addWishMovice():
        







if __name__ == "__main__":


    db = Aria2cMySQL();
    db.connect();

    db.userLoginUp("ex", "7866");
    db.getEmail("ex");
    db.getPassword("ex");
    db.getUserAll("ex");


    