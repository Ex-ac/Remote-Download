#ifndef CLIENT_H_
#define CLIENT_H_

#include <qlabel.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include <qlayout.h>

#include <qtcpsocket.h>

#include <QtWidgets/QMainWindow>


class Client : public QMainWindow
{
	Q_OBJECT

public:
	Client(QWidget *parent = nullptr);

	private slots:

	void on_sendPushButton_clicked();
	void on_disOrConnectPushButton_clicked();
	void connected();
	void readyRead();

private:
	QLabel *_label;
	QLineEdit *_lineEdit;
	QPushButton *_disOrConnectPushButton;
	QPushButton *_sendPushButton;
	QLabel *_messageLabel;
	
	QTcpSocket *_tcpSocket;
	bool _hasConnected = false;
};

#endif