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
    
    resultList = [];
    result = html.xpath('//a[@target="_blank"]');

    for each in result:
        temp = {
            "url" : "",
            "name" : "",
            "source" : "80s"
        };
        try:

            temp["url"] = urllib.parse.urljoin(url, each.xpath("./@href")[0]);
            tempStr = "".join(each.xpath("./text()")[1]);

            tempStr = tempStr.replace(" ", "");
            tempStr = tempStr.replace("\n", "");
            temp["name"] = tempStr;
            resultList.append(temp);
    
        except Exception as e:
            print(e);
    return resultList;

def getMovicesDownloadUrlFrom80s(moviceInformationPage):
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Host" : "www.80s.tw",
        "Referer" : "http://www.80s.tw/",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    };
    #moviceInformationPage += "?charset=utf-8";

    request = urllib.request.Request(moviceInformationPage, headers = headers);

    html = etree.HTML(urllib.request.urlopen(request).read().decode("utf8"));


    result = html.xpath('//input[@name]/@value');
    resultList = [];
    for each in result:
       resultList.append("".join(each));


    
    return resultList;

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

    resultList = [];
    for each in result:
        temp = {
            'url' : "",
            "name" : "",
            "source" : "piaohua"
        };

        try:

            temp["url"] = "".join(each.xpath("./a/@href"));
            temp["name"] = "".join(each.xpath(".//font/text()"));
            resultList.append(temp);
        except Exception as e:
            print(e);
    return resultList;


def getMovicesDownloadUrlFromPiaohua(moviceInformationPage):
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Host" : "vod.cnzol.com",
        "Referer" : "http://vod.cnzol.com/",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    };
    moviceInformationPage = moviceInformationPage + "?charset=utf-8";

    request = urllib.request.Request(moviceInformationPage, headers = headers);
    html = urllib.request.urlopen(request).read().decode("utf8");

    html = etree.HTML(html);

    result = html.xpath("//table//button/@data-clipboard-text");

    resultList = [];
    
    for each in result:
        resultList.append("".join(each));

    return resultList;
        



if __name__ == "__main__":
    getMovicesDownloadUrlFrom80s("http://www.80s.tw/ju/21533");