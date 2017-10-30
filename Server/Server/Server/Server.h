#ifndef SERVER_H_
#define SERVER_H_

#include <QObject>

#include <qtcpsocket.h>
#include <qtcpserver.h>


class Server : public QObject
{
	Q_OBJECT

public:
	Server(QObject *parent = nullptr);



	void hh() { ; }
private slots:
	void newConnection();
	void receiveData();


private:
	QTcpServer *_tcpServer;
	QTcpSocket *_tcpSocket;


};

#endif

