import pymysql.cursors



class MySQL:
    config = {
        "host" : "192.168.1.103",
        "port" : 3306,
        "user" : "user",
        "passwpord" : "7866",
        "db" : "study",
        "charset" : "utf8",
    }
    _connection = [];
    def connect(self, config = config):
        pass;


if __name__ == "__main__":
    db = pymysql.connect("localhost", "user", "7866", "study");
    cursor = db.cursor();
    cursor.execute("show tables");
    print(cursor.fetchall());