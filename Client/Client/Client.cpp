#include "Client.h"
#include <qbytearray.h>
#include <qdatastream.h>

Client::Client(QWidget *parent)
	: QMainWindow(parent)
{
	_label = new QLabel(tr("Send:"));
	_lineEdit = new QLineEdit;
	_disOrConnectPushButton = new QPushButton(tr("Connect"));
	_sendPushButton = new QPushButton(tr("Send"));
	_sendPushButton->setEnabled(false);
	_messageLabel = new QLabel();

	QGridLayout *mainLayout = new QGridLayout;
	mainLayout->addWidget(_label, 0, 0);
	mainLayout->addWidget(_lineEdit, 0, 1);
	mainLayout->addWidget(_disOrConnectPushButton, 1, 0);
	mainLayout->addWidget(_sendPushButton, 1, 1);
	mainLayout->addWidget(_messageLabel, 2, 0);

	QWidget *widget = new QWidget;
	widget->setLayout(mainLayout);

	setCentralWidget(widget);
	_tcpSocket = new QTcpSocket();
	connect(_disOrConnectPushButton, SIGNAL(clicked()), this, SLOT(on_disOrConnectPushButton_clicked()));
}

void Client::on_disOrConnectPushButton_clicked()
{
	if (!_hasConnected)
	{
		_tcpSocket->connectToHost("127.0.0.1", 8805, QTcpSocket::ReadWrite);
		connect(_tcpSocket, SIGNAL(connected()), this, SLOT(connected()));
	}
	else
	{
		_tcpSocket->close();
		_disOrConnectPushButton->setText(tr("Connect"));
		_hasConnected = false;
	}
}

void Client::connected()
{
	_disOrConnectPushButton->setText(tr("Disconnect"));
	_sendPushButton->setEnabled(true);
	_hasConnected = true;
	connect(_tcpSocket, SIGNAL(readyRead()), this, SLOT(readyRead()));
	connect(_sendPushButton, SIGNAL(clicked()), this, SLOT(on_sendPushButton_clicked()));
}

void Client::on_sendPushButton_clicked()
{
	QByteArray byteArray;
	QDataStream outDataStream(&byteArray, QIODevice::ReadWrite);
	outDataStream << _lineEdit->text();
	_tcpSocket->write(byteArray);
}

void Client::readyRead()
{
	QByteArray byteArray = _tcpSocket->readAll();
	QDataStream inDataStream(&byteArray, QIODevice::ReadOnly);
	QString str;

	inDataStream >> str;
	_messageLabel->setText(str);

}