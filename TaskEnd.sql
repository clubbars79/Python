drop database if exists vk;
create database vk;
use vk;

drop table if exists `users`;
create table `users` (
	id int(11) auto_increment primary key,
    firstname varchar(50),
    lastname varchar(50) COMMENT 'Фамиль', -- COMMENT на случай, если имя неочевидное
    email varchar(120) UNIQUE,
	
    index users_firstname_lastname_idx(firstname, lastname)
) COMMENT 'юзеры';

INSERT INTO users
VALUES 
(1,'Иван','Иванов','mail.ru'),
(2,'Семен','Семенов','gmail.com'),
(3,'Петр','Петров','yandex.ru'),
(4,'Сергей','Сергеев','postfix.com');


SELECT 
	id,
	firstname, 
	lastname,
	email 
FROM vk.users;

drop table if exists `messages`;
create table `messages` (
	id int(11) auto_increment primary key,
    user_id int(11) not null,
    message varchar(250) not null,
	foreign key (user_id) references users(id) on delete cascade-- пока рано, т.к. таблицы media еще нет
);

drop table if exists `likes`;
create table `likes` (
	id int(11) auto_increment primary key,
	user_id int(11) not null,
    message_id int(11) not null,
    foreign key (user_id) references users(id) on delete cascade,
    foreign key (message_id) references messages(id) on delete cascade
);

drop table if exists `media`;
create table `media` (
	id int(11) auto_increment primary key,
	user_id int(11) not null,
    url varchar(250) not null,
	foreign key (user_id) references users(id) on delete cascade
);
 

delimiter //
create procedure delete_user(in user_id int(11))
begin
	start transaction;
	delete from `messages` where user_id = user_id;
	delete from `likes` where user_id = user_id;
	delete from `media` where user_id = user_id;
	delete from `users` where id = user_id;
	commit;
	select user_id;
end //
delimiter ;

call delete_user(3);

SELECT 
	id,
	firstname, 
	lastname,
	email 
FROM vk.users;
