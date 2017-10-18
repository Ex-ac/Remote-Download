import  smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "492093401@qq.com";
receiver = "qq492093401@163.com";
smtpserver = "smtp.qq.com";
username = "492093401@qq.com";
password = "ravpwedvlialbjjj";
port = 465;





if __name__ == "__main__":

    msg = MIMEText("fff", "text", "utf-8");
    msg["Subject"] = Header("dfkghj", "utf-8");

    smtp = smtplib.SMTP_SSL(smtpserver, 465);
    print("ok");

    smtp.login(username, password);
    print("gsf");
    smtp.sendmail(sender, receiver, msg.as_string());
    print("adhfjklad");
    smtp.quit();

