
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
    status bit(2) default 2,
    foreign key (wishMoviceName) references WishMovies(moviceName)
) charset = utf8;
/*
    status = 0 inavailable
    status = 1 waiting
    status = 2 start
*/

create table MovicesDownloadUrl
(
    moviceName varchar(128) not null,
    downloadUrl varchar(512) not null,
    available bool default true,
    primary key (downloadUrl),
    foreign key (moviceName) references MovicesInformantion(moviceName)
) charset = utf8;

 

delimiter &&
create trigger setMovicesDownloadUrlAvailable
after update on MovicesDownloadUrl for each row
begin
set @count = (select count(*)  from MovicesDownloadUrl where MovicesDownloadUrl.moviceName = new.moviceName and MovicesDownloadUrl.available = true)
    
if  @count = 0 then
	update MovicesInformantion set status = 2 where moviceName = new.moviceName
else
	@count = 0
end if
end; &&


delimiter &&
create trigger setWishMovicesAvailable 
after update on WishMovies
for each row
begin

    if new.needToCrawl then
        update on MovicesInformantion set  status = 2; 
    else
        update on MovicesInformantion set status = 0;
    end if;
end; &&
