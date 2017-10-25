# -*- coding:utf-8 -*-  
import urllib.robotparser
import urllib.request
import urllib.parse
from lxml import etree
import codecs
import string



def getMovicesInformationFrom80s(moviceName):

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        "Cache-Control": "max-age=0:",
        "Connection": "keep-alive",
        "Content-Length": "44",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "www.80s.tw",
        "Origin": "http://www.80s.tw",
        "Referer": "http://www.80s.tw/search",
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    };

    parameters = {
        "keyword" : moviceName
    };
    url = "http://www.80s.tw/search"

    data = urllib.parse.urlencode(parameters).encode("ascii");

    request = urllib.request.Request(url, data, headers);

    html = etree.HTML(urllib.request.urlopen(request).read().decode("utf8"));
    

    result = html.xpath('//a[@target="_blank"]');

    for each in result:
        temp = {
            "url" : "",
            "name" : ""
        };
        #print(urllib.parse.urljoin(url, each.xpath("./@href")));
        try:

            temp["url"] = urllib.parse.urljoin(url, each.xpath("./@href")[0]);
            tempStr = "".join(each.xpath("./text()")[1]);

            tempStr = tempStr.replace(" ", "");
            tempStr = tempStr.replace("\n", "");
            temp["name"] = tempStr;
            print(temp);
        except Exception as e:
            print(e);


def getMOvicesDownloadUrlFrom80s(moviceInformationPage):
    headers = {
        
    };


def getMovicesInformationFromPiaoHua(moviceName):
    
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    };

    parameters = {
        "searchword" : moviceName
    };

    data = urllib.parse.urlencode(parameters);

    searchUrl = "http://vod.cnzol.com/search.php?chid=201&charset=utf-8&%s" % data;



    html = etree.HTML(urllib.request.urlopen(searchUrl).read().decode("utf8"));

    result = html.xpath('//div[@id="list"]//strong');
    print(result);

    for each in result:
        temp = {
            'url' : "",
            "name" : ""
        };

        try:

            temp["url"] = "".join(each.xpath("./a/@href"));
            temp["name"] = "".join(each.xpath(".//font/text()"));
            print(temp);
        except Exception as e:
            print(e);







if __name__ == "__main__":

    getMovicesInformationFrom80s("变形金刚");






