import os
import xmlrpc.client
import base64

confPath = r"D:/aria2/aria2.conf";
appPath = r"D:/aria2/aria2c.exe";

staticClient = None;
staticIsStart = False;

class Aria2:
    def start():
        global staticIsStart;
        global staticClient;
        os.popen(appPath + " --conf-path=" + confPath);
        #需要检查
        if True:
            staticClient = xmlrpc.client.ServerProxy("http://localhost:6800/rpc");
            print(staticIsStart);
            staticIsStart = True;

    def addUri(uris, opts = {}):
        global staticClient;
        global staticIsStart;
        if staticIsStart:
            gid = staticClient.aria2.addUri(uris, opts);
            return gid;
        else:
            print("please start aria2c, running the start before!");
            return 0;

    def addTorrent(path, ops = {}):
        global staticClient;
        global staticIsStart;

        if staticIsStart:
            torrent = base64.b64encode(open(path).read());
            return staticClient.aria2.addTorrent(torrent, ops);
        else:
            print("please start aria2c, running the start before!");
            return 0;

    def addMetalink(path, ops):
        global staticClient;
        global staticIsStart;

        if staticIsStart:
            torrent = base64.b64encode(open(path).read());
            return staticClient.aria2.addMetalink(torrent, ops);
        else:
            print("please start aria2c, running the start before!");
            return 0;

    

    def remove(gid):
        global staticClient;
        global staticIsStart;

        if staticIsStart:
            return staticClient.aria2.remove(gid);
        else:
            print("please start aria2c, running the start before!");
            return 0;
 
    def forceRemove(gid):
        global staticClient;
        global staticIsStart;

        if staticIsStart:
            return staticClient.aria2.forceremove(gid);
        else:
            print("please start aria2c, running the start before!");
            return 0;

    


if __name__ == "__main__":
    Aria2.start();
    Aria2.addUri(["https://www.python.org/ftp/python/3.6.3/python-3.6.3-macosx10.6.pkg"]);
    while True:
        pass;