CREATE TABLE TB_USERS (
    "user_id" SERIAL PRIMARY KEY,
    "login" VARCHAR(50),
    "password" VARCHAR(50)
);



CREATE TABLE TB_MAIL (
    "mail_id" SERIAL PRIMARY KEY,
    "user_id" int,
    "login"  VARCHAR(50),
    "mail_content" TEXT NOT null,
    "to_login" VARCHAR(50),
    "spam" int
);

ALTER TABLE TB_USERS ADD UNIQUE (login);


WHERE m.login = u.login;


ALTER TABLE TB_MAIL ADD CONSTRAINT user_id FOREIGN KEY ("login") REFERENCES TB_USERS("login");


select * from TB_MAIL;

select * from TB_USERS;
commit;


SELECT * FROM TB_MAIL WHERE to_login = 'venkat@gmail.com';

UPDATE TB_MAIL SET spam = 0 WHERE to_login = 'venkat@gmail.com'and mail_id =3;

