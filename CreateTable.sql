create table Downloads
(
	gid int(64) not null primary key,
	moviceName varchar(128) not null,
    savePath varchar(256) default 'default save path',
    status bit(3) default 0,
    speed int(10),
    useTime int(10) default 0
) charset = utf8;



create table User
(
	name varchar(64) not null primary key,
    password bit(128) not null,
    email varchar(128) default 'ex-ac@outlook.com'
) charset = utf8;


create table WishMovies
(
	moviceName varchar(128) not null,
    userName varchar(64) not null,
    createTime datetime,
    sendEmail bool default false,
	savePath varchar(256) default 'default path',
    foreign key (userName) references User(name),
    primary key (moviceName, userName)
) charset = utf8;


