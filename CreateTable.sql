
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
    sendEmail bool default false,
	savePath varchar(256) default null,
    needToCrawl bool default true,
    foreign key (userName) references User(name),
    primary key (moviceName, userName)
) charset = utf8;


create table MovicesInformantion
(
	moviceName varchar(128) not null primary key,
    wishMoviceName varchar(128) not null,
    url varchar(1024) not null,
    source varchar(64) not null,
    createTime datetime,
    status bit(2) default 3,
    foreign key (wishMoviceName) references WishMovies(moviceName)
) charset = utf8;

create table MovicesDownloadUrl
(
    moviceName varchar(128) not null,
    downloadUrl varchar(512) not null,
    available bool default true,
    primary key (downloadUrl),
    foreign key (moviceName) references MovicesInformantion(moviceName)
) charset = utf8;


create trigger MovicesInformantionSelect
before select on MovicesInformantion
for each row
begin
    update MovicesInformantion set status = 3 where datediff(now(), createTime) > 10
end

 

delimiter &&
create trigger setMovicesDownloadUrlAvailable
after update on MovicesDownloadUrl for each row
begin
set @count = (select count(*)  from MovicesDownloadUrl where MovicesDownloadUrl.moviceName = new.moviceName and MovicesDownloadUrl.available = true)
    
if  @count = 0 then
	update MovicesInformantion set status = 3 where moviceName = new.moviceName
else
	@count = 0
end if
end; &&
