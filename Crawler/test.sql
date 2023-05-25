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





select * from post where service="instargam";
drop table hashtag;


delete from post;

select  from hashtag;


ALTER TABLE navernews ADD date VARCHAR(100) NOT NULL;



ALTER TABLE hashtag ADD postid int(11) NOT NULL;

select * from navernews;

INSERT into hashtag2 values(null,'twitter','유똥',
(select IFNULL(max(id),0)+1 from post));
select IFNULL(max(id),0)+1 from post;

select * from post where content like "%송태섭이 안 당한 교통사고 분량이 내 마음에 처박힌 듯%";

select * from usepost 
where
content like "%코로나%";



and (select tag from hashtag2) in '방귀';


DELETE  from post;

select id from post where content=;



select * from post where content like '%코로나%';

ALTER TABLE post ADD hashtags VARCHAR(1000) NOT NULL;


SELECT min(id) from post;


select min(id) as min, max(id) as max from post;

insert into hashtag2(id,snsName,tag) 
values( (select IFNULL(max(id),0)+1  from post),"twitrer","tag");

select IFNULL(max(id),0)+1 from post;

select * from post where id=14;


update table hashtag(id) set id=%s where id=%s;


update hashtag set postid='6' where id='2';



insert into hashtag(id,snsName,tag,postid) 
        values( (select IF(max>9000 , max+1 , 9000) from (select max(id) as max from hashtag)as h),
        "tt","tag",33);


delete from hashtag where id>1000;

#### 테이블 변경
### 추가 바람 


#1 hashtag 테이블 삭제
drop table hashtag;
#2 hashtag 테이블 생성


select title,content,link from navernews  
where title like  CONCAT('%','교통','%') or content like  concat('%','교통','%');



use crawlerdb;




insert into admin(date,today,total)  VALUES("2023-05-15",0,0);
insert into admin(date,today,total)  VALUES("2023-05-16",0,0);

insert into admin(date,today,total)  VALUES("2023-05-17",0,0);

insert into admin(date,today,total)  VALUES("2023-05-18",0,0);

insert into admin(date,today,total)  VALUES("2023-05-19",0,0);

insert into admin(date,today,total)  VALUES("2023-05-20",0,0);

insert into admin(date,today,total)  VALUES("2023-05-21",0,0);

insert into admin(date,today,total)  VALUES("2023-05-22",0,0);

insert into admin(date,today,total)  VALUES("2023-05-23",0,0);

insert into admin(date,today,total)  VALUES("2023-05-24",0,0);

insert into admin(date,today,total)  VALUES("2023-05-25",0,0);

insert into admin(date,today,total)  VALUES("2023-05-26",0,0);

insert into admin(date,today,total)  VALUES("2023-05-27",0,0);


select * from hashtag;

alter table hashtag drop primary key;


SELECT id,service,content,sns,keyword,date,link FROM post where id >= 900;

delete from post;
delete from usepost;

delete from hashtag;
delete from navernews;
select IFNULL(max(id),0) from post;

ALTER TABLE Post MODIFY COLUMN username VARCHAR(50) DEFAULT NULL;
ALTER TABLE usePost MODIFY COLUMN username VARCHAR(50) DEFAULT NULL;

select count(*) from post where service='instagram';


---------- 0423 추가 ----

ALTER Table hashtag ADD keyword varchar(10) NOT NULL;


select * from usepost;



delete from post where service='naverblogcafe';


SELECT id FROM post WHERE keyword='태풍' AND service='naverBlogCafe' LIMIT 1;


select * from hashtag where tag like '%18년%';

SELECT tag FROM hashtag where seq >= '8420';


INSERT into hashtag(id,snsName,tag,postid,keyword) 
values
(1234,"twitter","이태원",NULL,"압사"),
(1234,"naverBlogCafe","이태원",NULL,"압사"),
(1234,"instagram","이태원",NULL,"압사");



select * from hashtag WHERE tag like'%우마%';

select keyword,count(keyword)as count from hashtag where postid IS NULL group by keyword order by count desc limit 6;



insert into navernews(keyword,title,content,link,date)
values
("압사","이태원, 누군가의 마지막 장소가 된 밤 압사","temp_content","http://templocal.com","2022-10-29");



insert into navernews(keyword,title,content,link,date) values("압사","이태원", "압사","temp_content","http://templocal.com","2022-10-29")