# Introduction to joining data sets

mysql> create table spark.orders(order_id int(11),order_date datetime,order_customer_id int(11), order_status varchar(25), primary key(order_id));
Query OK, 0 rows affected (0.04 sec)

mysql> create table spark.order_items(order_item_id int(11),order_item_order_id int(11),order_item_product_id int(11),order_item_quantity int(11),order_item_subtotal float, order_item_product_price float,primary key(order_item_id));
Query OK, 0 rows affected (0.07 sec)

mysql> insert into spark.orders values(1, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.orders values(2, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.orders values(3, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.orders values(4, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.orders values(5, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.orders values(6, '1994-10-10',11,'123s');
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.order_items values(1,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.01 sec)
mysql> insert into spark.order_items values(2,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.order_items values(3,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.order_items values(4,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.order_items values(5,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.00 sec)
mysql> insert into spark.order_items values(6,2,3,1,2.4,5.6);
Query OK, 1 row affected (0.00 sec)
mysql> commit;
Query OK, 0 rows affected (0.00 sec)

###  get the revenue and number of orders from order_items on daily basis.

Read the data from orders and order_items
Extract the key from orders and order_items (using map)
Join the orders and order_items
Get revenue per order item per day
Get order count per date from order_items (aggregation). As there are orders which do not have corresponding records in order_items, we cannot get count using order table. We need to join order_items with orders to get total number of orders per day.
Get revenue per day from joined data



