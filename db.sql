use crawlerdb;

create DATABASE crawlerdb;
use crawlerdb;

-- db 설계--------------------------------------------------------
CREATE TABLE Post (
    id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    service varchar(100) not null,
    keyword VARCHAR(20) NOT NULL,
    username VARCHAR(50)  NULL,
    content VARCHAR(6000) NOT NULL,
    sns VARCHAR(6000) NOT NULL,
    link VARCHAR(300) NOT NULL,
    date VARCHAR(300) NOT NULL
)  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


CREATE TABLE navernews(
    id iNT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(50) not null,
    title VARCHAR(300) NOT NULL,
    content VARCHAR(5000) NOT NULL,
    link VARCHAR(200) NOT NULL,
    date VARCHAR(100) NOT NULL
);


CREATE TABLE UsePost (
    id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    service varchar(100) not null,
    keyword VARCHAR(20) NOT NULL,
    username VARCHAR(50) NOT NULL,
    content VARCHAR(6000) NOT NULL,
    sns VARCHAR(6000) NOT NULL,
    link VARCHAR(300) NOT NULL,
    date VARCHAR(300) NOT NULL
)  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

create table hashtag(
    seq int(11)UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id iNT(11) UNSIGNED NOT NULL ,
    snsName VARCHAR(50) not null,
    tag VARCHAR(100) not null,
    postid int(11) 
   keyword varchar(10) NOT NULL
);


create table admin(
    date datetime not null,
    today decimal(11) not null,
    total decimal(11) not null
);
----------------------------------------------------------------------

insert into admin(date,today,total)  VALUES("2023-05-06",0,0);
insert into admin(date,today,total)  VALUES("2023-05-07",0,0);
insert into admin(date,today,total)  VALUES("2023-05-08",0,0);
insert into admin(date,today,total)  VALUES("2023-05-09",0,0);
insert into admin(date,today,total)  VALUES("2023-05-10",0,0);
insert into admin(date,today,total)  VALUES("2023-05-11",0,0);
insert into admin(date,today,total)  VALUES("2023-05-12",0,0);
insert into admin(date,today,total)  VALUES("2023-05-13",0,0);
insert into admin(date,today,total)  VALUES("2023-05-14",0,0);
