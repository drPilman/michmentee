create table users
(
	id serial,
	password_hash bytea not null,
	email varchar not null,
    surname varchar not null,
    name varchar not null,
    patronymic varchar not null,
    birthday varchar not null,
    study varchar not null,
    faculty varchar not null,
    number varchar not null

);

create unique index users_id_uindex
	on users (id);

create unique index users_login_uindex
	on users (email);

alter table users
	add constraint users_pk
		primary key (id);

