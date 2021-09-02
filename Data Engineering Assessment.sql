
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


/*1.	Using the tables above, write a query that returns, for each order, the order_id, the product name, the difference in days between the product go live date and the ordered at date, and the marketing ad network and source. This result should be five rows. Also include the output of the query. */
select o.id, p.name, datediff(p.go_live_date, o.ordered_at), m.ad_network, m.source
from orders o
join product p on o.product_id = p.id
join marketing_orders mo on o.id = mo.order_id
join marketing m on mo.marketing_id = m.id
order by o.id;

/*2.	Using the tables above, write a query that returns the best performing marketing ad network and source, a count of how many orders it had, and the best selling product for that ad network and source. Also include the output of the query.
Hint: The best selling product will have to be retrieved through seeing which orders are associated with the best performing marketing ad network and source. In this case, best performing means “Has the largest number of records in the DB associated with it”. This result will be a single row.
*/
select m.ad_network, m.source, count(o.id), p.name
from orders o
join marketing_orders mo on o.id = mo.order_id
join marketing m on mo.marketing_id = m.id
join product p on o.product_id = p.id
group by m.ad_network, m.source
order by count(o.id) desc;

/*3.	Write a query that determines the best selling product for each month of orders. Also include the output of the query.*/
select p.name, count(o.id)
from orders o
join product p on o.product_id = p.id
group by p.name
order by count(o.id) desc;






