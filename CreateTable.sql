create table Downloads
(
	gid int(64) not null primary key,
	moviceName varchar(128) not null,
    savePath varchar(256) default null,
    status bit(3) default 3,
    speed int(10),
    useTime int(10) default 0
) charset = utf8;
                

create table User
(
	name varchar(64) not null primary key,
    password binary(128) not null,
    email varchar(128) default 'ex-ac@outlook.com'
) charset = utf8;


create table WishMovies
(
	moviceName varchar(128) not null,
    userName varchar(64) not null,
    createTime datetime,
    sendEmail bool default false,
	savePath varchar(256) default null,
    foreign key (userName) references User(name),
    primary key (moviceName, userName)
) charset = utf8;


create table MovicesInformantion
(
    
	mvoviceName varchar(128) not null primary key,
    wishMoviceName varchar(128) not null,
    url varchar(1024) not null,
    source varchar(64) not null,
    createTime datetime,
    foreign key (wishMoviceName) references WishMovies(moviceName)
) charset = utf8;

create table MoviesDownloadUrl
(
    moviceName varchar(128) not null,
    downloadUrl varchar(512) not null,
    createTime datetime,
    available bool default true,
    primary key (moviceName, downloadUrl)
) charset = utf8;