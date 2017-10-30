#include "Server.h"

#include <qhostaddress.h>
#include <iostream>
#include <qbytearray.h>
#include <qdatastream.h>

Server::Server(QObject *parent)
	: QObject(parent)
{
	_tcpSocket = nullptr;
	_tcpServer = new QTcpServer();
	_tcpServer->listen(QHostAddress::Any, 8805);
	connect(_tcpServer, SIGNAL(newConnection()), this, SLOT(newConnection()));
}	

void Server::newConnection()
{
	if (_tcpServer->hasPendingConnections())
	{
		_tcpSocket = _tcpServer->nextPendingConnection();
		std::cout << "has new connect!";
		connect(_tcpSocket, SIGNAL(readyRead()), this, SLOT(receiveData()));
	}
}


void Server::receiveData()
{
	QByteArray byteArray1 = _tcpSocket->readAll();
	QDataStream dataStream(&byteArray1, QIODevice::ReadOnly);
	QString str;
	do
	{
		dataStream >> str;
		qDebug() << str << "\n";
	} while (!dataStream.atEnd());

	QByteArray byteArray;
	QDataStream outDataStream(&byteArray, QIODevice::ReadWrite);
	outDataStream << QString("get massage!");
	_tcpSocket->write(byteArray);

}
