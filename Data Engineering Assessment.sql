
.headers on 
.mode columns
/* Creating tables*/
CREATE TABLE orders( id int primary key, product_id int, ordered_at date, product_quantity varchar, created_at date, updated_at date);
CREATE TABLE product( id int primary key, name varchar, description varchar, go_live_date date, created_at date, updated_at date);
CREATE TABLE marketing( id int primary key, ad_network varchar, source varchar, created_at date, updated_at date);
CREATE TABLE marketing_orders( order_id int primary key, marketing_id int);

/* Insert some data into the table */
INSERT INTO orders values(1,3,'2021-01-01 00:00:00',1,'2021-01-01 00:00:01','2021-01-01 00:01:03');
INSERT INTO orders values(2,1,'2021-01-03 05:00:07',4,'2021-01-03 05:00:08','2021-01-03 05:02:12');
INSERT INTO orders values(3,5,'2021-01-05 12:05:00',3,'2021-01-05 12:05:01','2021-01-06 01:05:00');
INSERT INTO orders values(4,1,'2021-02-01 03:00:00',2,'2021-02-01 03:00:01','2021-02-01 03:00:01');
INSERT INTO orders values(5,1,'2021-02-05 00:00:00',3,'2021-02-05 00:00:01','2021-02-05 00:00:01');

INSERT INTO product values(1,'Mattress','A Mattress','2021-01-01','2020-12-01 00:00:00','2020-12-01 00:00:00');
INSERT INTO product values(3,'Pillow','A Pillow','2021-01-01','2020-12-01 00:00:00','2020-12-01 00:00:00');
INSERT INTO product values(5,'Comforter','A Comforter','2021-01-01','2020-12-01 00:00:00','2020-12-01 00:00:00');

INSERT INTO marketing values(1,"facebook","ads",'2020-12-01 00:00:00','2020-12-01 00:00:00');
INSERT INTO marketing values(2,"facebook","remarketing",'2020-12-01 00:00:00','2020-12-01 00:00:00');

INSERT INTO marketing_orders values(1,1);
INSERT INTO marketing_orders values(2,1);
INSERT INTO marketing_orders values(3,2);
INSERT INTO marketing_orders values(4,1);
INSERT INTO marketing_orders values(5,1);



