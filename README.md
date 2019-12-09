

# Section 1
2019-12-08 19:28:32,674 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2019-12-08 19:28:32,674 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,674 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2019-12-08 19:28:32,674 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,674 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("customers")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("customers")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("items")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("items")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("orders")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("orders")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("order_lines")
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,675 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("order_lines")
2019-12-08 19:28:32,676 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,676 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE customers (
	id INTEGER NOT NULL, 
	first_name VARCHAR(100) NOT NULL, 
	last_name VARCHAR(100) NOT NULL, 
	username VARCHAR(50) NOT NULL, 
	email VARCHAR(200) NOT NULL, 
	address VARCHAR(200) NOT NULL, 
	town VARCHAR(200) NOT NULL, 
	created_on DATETIME, 
	updated_on DATETIME, 
	PRIMARY KEY (id)
)


2019-12-08 19:28:32,676 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,679 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,679 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE items (
	id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	cost_price NUMERIC(10, 2) NOT NULL, 
	selling_price NUMERIC(10, 2) NOT NULL, 
	quantity INTEGER NOT NULL, 
	PRIMARY KEY (id)
)


2019-12-08 19:28:32,679 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,682 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,682 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE orders (
	id INTEGER NOT NULL, 
	customer_id INTEGER, 
	date_placed DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(customer_id) REFERENCES customers (id)
)


2019-12-08 19:28:32,682 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,684 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,685 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE order_lines (
	id INTEGER NOT NULL, 
	order_id INTEGER, 
	item_id INTEGER, 
	quantity SMALLINT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES orders (id), 
	FOREIGN KEY(item_id) REFERENCES items (id)
)


2019-12-08 19:28:32,685 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,687 INFO sqlalchemy.engine.base.Engine COMMIT
None
None
2019-12-08 19:28:32,691 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,692 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,692 INFO sqlalchemy.engine.base.Engine ('Toby', 'Miller', 'tmiller', 'tmiller@example.com', '1662 Kinney Street', 'Wolfden', '2019-12-08 19:28:32.692378', '2019-12-08 19:28:32.692389')
2019-12-08 19:28:32,692 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,692 INFO sqlalchemy.engine.base.Engine ('Scott', 'Harvey', 'scottharvey', 'scottharvey@example.com', '424 Patterson Street', 'Beckinsdale', '2019-12-08 19:28:32.692787', '2019-12-08 19:28:32.692790')
2019-12-08 19:28:32,693 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,696 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,697 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id = ?
2019-12-08 19:28:32,697 INFO sqlalchemy.engine.base.Engine (1,)
1
2019-12-08 19:28:32,697 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id = ?
2019-12-08 19:28:32,697 INFO sqlalchemy.engine.base.Engine (2,)
2
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine ('John', 'Lara', 'johnlara', 'johnlara@mail.com', '3073 Derek Drive', 'Norfolk', '2019-12-08 19:28:32.698349', '2019-12-08 19:28:32.698353')
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine ('Sarah', 'Tomlin', 'sarahtomlin', 'sarahtomlin@mail.com', '3572 Poplar Avenue', 'Norfolk', '2019-12-08 19:28:32.698591', '2019-12-08 19:28:32.698595')
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine ('Toby', 'Miller', 'tmiller', 'tmiller@example.com', '1662 Kinney Street', 'Wolfden', '2019-12-08 19:28:32.698758', '2019-12-08 19:28:32.698761')
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine INSERT INTO customers (first_name, last_name, username, email, address, town, created_on, updated_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
2019-12-08 19:28:32,698 INFO sqlalchemy.engine.base.Engine ('Scott', 'Harvey', 'scottharvey', 'scottharvey@example.com', '424 Patterson Street', 'Beckinsdale', '2019-12-08 19:28:32.698903', '2019-12-08 19:28:32.698906')
2019-12-08 19:28:32,699 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,701 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,701 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,701 INFO sqlalchemy.engine.base.Engine ('Chair', 9.21, 10.81, 5)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Pen', 3.45, 4.51, 3)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Headphone', 15.52, 16.81, 50)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Travel Bag', 20.1, 24.21, 50)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Keyboard', 20.1, 22.11, 50)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Monitor', 200.14, 212.89, 50)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Watch', 100.58, 104.41, 50)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine INSERT INTO items (name, cost_price, selling_price, quantity) VALUES (?, ?, ?, ?)
2019-12-08 19:28:32,702 INFO sqlalchemy.engine.base.Engine ('Water Bottle', 20.89, 25.0, 50)
2019-12-08 19:28:32,703 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,706 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,706 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id = ?
2019-12-08 19:28:32,706 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,707 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,707 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,708 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,708 INFO sqlalchemy.engine.base.Engine (2,)
/home/hao/anaconda3/envs/py37/lib/python3.7/site-packages/sqlalchemy/sql/sqltypes.py:666: SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively, and SQLAlchemy must convert from floating point - rounding errors and other issues may occur. Please consider storing Decimal numbers as strings or integers on this platform for lossless storage.
  "storage." % (dialect.name, dialect.driver)
2019-12-08 19:28:32,709 INFO sqlalchemy.engine.base.Engine INSERT INTO orders (customer_id, date_placed) VALUES (?, ?)
2019-12-08 19:28:32,709 INFO sqlalchemy.engine.base.Engine (1, '2019-12-08 19:28:32.709336')
2019-12-08 19:28:32,709 INFO sqlalchemy.engine.base.Engine INSERT INTO orders (customer_id, date_placed) VALUES (?, ?)
2019-12-08 19:28:32,709 INFO sqlalchemy.engine.base.Engine (1, '2019-12-08 19:28:32.709581')
2019-12-08 19:28:32,709 INFO sqlalchemy.engine.base.Engine COMMIT
--------------------------------------------------------------------------

# Section 2
2019-12-08 19:28:32,711 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,712 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id = ?
2019-12-08 19:28:32,712 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,712 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,712 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,713 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,713 INFO sqlalchemy.engine.base.Engine (2,)
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine INSERT INTO orders (customer_id, date_placed) VALUES (?, ?)
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine (1, '2019-12-08 19:28:32.714024')
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine INSERT INTO order_lines (order_id, item_id, quantity) VALUES (?, ?, ?)
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine (3, 1, 5)
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine INSERT INTO order_lines (order_id, item_id, quantity) VALUES (?, ?, ?)
2019-12-08 19:28:32,714 INFO sqlalchemy.engine.base.Engine (3, 2, 10)
2019-12-08 19:28:32,715 INFO sqlalchemy.engine.base.Engine COMMIT
customer1.orders
2019-12-08 19:28:32,718 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,719 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id = ?
2019-12-08 19:28:32,719 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,720 INFO sqlalchemy.engine.base.Engine SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders 
WHERE ? = orders.customer_id
2019-12-08 19:28:32,720 INFO sqlalchemy.engine.base.Engine (1,)
[<__main__.Order object at 0x7f152cb09910>, <__main__.Order object at 0x7f152cbb0d50>, <__main__.Order object at 0x7f152cb11f10>]

order1.customer
<__main__.Customer object at 0x7f152cba2a90>

customer1.orders(3).order_lines
2019-12-08 19:28:32,721 INFO sqlalchemy.engine.base.Engine SELECT order_lines.id AS order_lines_id, order_lines.order_id AS order_lines_order_id, order_lines.item_id AS order_lines_item_id, order_lines.quantity AS order_lines_quantity 
FROM order_lines 
WHERE ? = order_lines.order_id
2019-12-08 19:28:32,721 INFO sqlalchemy.engine.base.Engine (3,)
[<__main__.OrderLine object at 0x7f152cb11950>, <__main__.OrderLine object at 0x7f152cb11a10>]

details of customer1.orders(3).order_lines
ol id:
1

ol.item_id:
1

ol.quantity:
5

ol id:
2

ol.item_id:
2

ol.quantity:
10

--------------------------------------------------------------------------

# Section 3
2019-12-08 19:28:32,721 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
2019-12-08 19:28:32,721 INFO sqlalchemy.engine.base.Engine ()
2019-12-08 19:28:32,722 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
2019-12-08 19:28:32,722 INFO sqlalchemy.engine.base.Engine ()
1 Toby
2 Scott
3 John
4 Sarah
5 Toby
6 Scott

2019-12-08 19:28:32,722 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name 
FROM customers
2019-12-08 19:28:32,722 INFO sqlalchemy.engine.base.Engine ()
[(1, 'Toby'), (2, 'Scott'), (3, 'John'), (4, 'Sarah'), (5, 'Toby'), (6, 'Scott')]
2019-12-08 19:28:32,724 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1 
FROM (SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers) AS anon_1
2019-12-08 19:28:32,724 INFO sqlalchemy.engine.base.Engine ()
6
2019-12-08 19:28:32,725 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1 
FROM (SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items) AS anon_1
2019-12-08 19:28:32,725 INFO sqlalchemy.engine.base.Engine ()
8
2019-12-08 19:28:32,726 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1 
FROM (SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders) AS anon_1
2019-12-08 19:28:32,726 INFO sqlalchemy.engine.base.Engine ()
3
2019-12-08 19:28:32,727 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,727 INFO sqlalchemy.engine.base.Engine (1, 0)
<__main__.Customer object at 0x7f152cba2a90>
2019-12-08 19:28:32,728 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,728 INFO sqlalchemy.engine.base.Engine (1, 0)
<__main__.Item object at 0x7f152cb09790>
2019-12-08 19:28:32,728 INFO sqlalchemy.engine.base.Engine SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,728 INFO sqlalchemy.engine.base.Engine (1, 0)
<__main__.Order object at 0x7f152cb09910>
<__main__.Customer object at 0x7f152cba2a90>
<__main__.Item object at 0x7f152cb09790>
2019-12-08 19:28:32,729 INFO sqlalchemy.engine.base.Engine SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders 
WHERE orders.id = ?
2019-12-08 19:28:32,729 INFO sqlalchemy.engine.base.Engine (100,)
None
2019-12-08 19:28:32,730 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name = ?
2019-12-08 19:28:32,730 INFO sqlalchemy.engine.base.Engine ('John',)
[<__main__.Customer object at 0x7f152cd12110>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name = ?
2019-12-08 19:28:32,731 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id <= ? AND customers.town = ?
2019-12-08 19:28:32,731 INFO sqlalchemy.engine.base.Engine (5, 'Norfolk')
[<__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cd12150>]
2019-12-08 19:28:32,731 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.town = ? OR customers.town = ?
2019-12-08 19:28:32,731 INFO sqlalchemy.engine.base.Engine ('Peterbrugh', 'Norfolk')
[<__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cd12150>]
2019-12-08 19:28:32,732 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name = ? AND customers.town = ?
2019-12-08 19:28:32,732 INFO sqlalchemy.engine.base.Engine ('John', 'Norfolk')
[<__main__.Customer object at 0x7f152cd12110>]
2019-12-08 19:28:32,733 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name = ? AND customers.town != ?
2019-12-08 19:28:32,733 INFO sqlalchemy.engine.base.Engine ('John', 'Peterbrugh')
[<__main__.Customer object at 0x7f152cd12110>]
2019-12-08 19:28:32,734 INFO sqlalchemy.engine.base.Engine SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders 
WHERE orders.date_placed IS NULL
2019-12-08 19:28:32,734 INFO sqlalchemy.engine.base.Engine ()
[]
2019-12-08 19:28:32,734 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name IN (?, ?)
2019-12-08 19:28:32,734 INFO sqlalchemy.engine.base.Engine ('Toby', 'Sarah')
[<__main__.Customer object at 0x7f152cba2a90>, <__main__.Customer object at 0x7f152cd12150>, <__main__.Customer object at 0x7f152cd120d0>]
2019-12-08 19:28:32,735 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name NOT IN (?, ?)
2019-12-08 19:28:32,735 INFO sqlalchemy.engine.base.Engine ('Toby', 'Sarah')
[<__main__.Customer object at 0x7f152cba2a50>, <__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cb53550>]
2019-12-08 19:28:32,736 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.cost_price BETWEEN ? AND ?
2019-12-08 19:28:32,736 INFO sqlalchemy.engine.base.Engine (10, 50)
[<__main__.Item object at 0x7f152cb099d0>, <__main__.Item object at 0x7f152cb53290>, <__main__.Item object at 0x7f152cb530d0>, <__main__.Item object at 0x7f152cb11f50>]
2019-12-08 19:28:32,736 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.cost_price NOT BETWEEN ? AND ?
2019-12-08 19:28:32,736 INFO sqlalchemy.engine.base.Engine (10, 50)
[<__main__.Item object at 0x7f152cb09790>, <__main__.Item object at 0x7f152cb09350>, <__main__.Item object at 0x7f152cb53810>, <__main__.Item object at 0x7f152cb53cd0>]
2019-12-08 19:28:32,737 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.name LIKE ?
2019-12-08 19:28:32,737 INFO sqlalchemy.engine.base.Engine ('%r',)
[<__main__.Item object at 0x7f152cb09790>, <__main__.Item object at 0x7f152cb53810>]
2019-12-08 19:28:32,738 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,738 INFO sqlalchemy.engine.base.Engine ('w%',)
[<__main__.Item object at 0x7f152cb53cd0>, <__main__.Item object at 0x7f152cb11f50>]
2019-12-08 19:28:32,738 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.name NOT LIKE ?
2019-12-08 19:28:32,738 INFO sqlalchemy.engine.base.Engine ('W%',)
[<__main__.Item object at 0x7f152cb09790>, <__main__.Item object at 0x7f152cb09350>, <__main__.Item object at 0x7f152cb099d0>, <__main__.Item object at 0x7f152cb53290>, <__main__.Item object at 0x7f152cb530d0>, <__main__.Item object at 0x7f152cb53810>]
2019-12-08 19:28:32,739 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,739 INFO sqlalchemy.engine.base.Engine (2, 0)
[<__main__.Customer object at 0x7f152cba2a90>, <__main__.Customer object at 0x7f152cba2a50>]
2019-12-08 19:28:32,740 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE lower(customers.address) LIKE lower(?)
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,740 INFO sqlalchemy.engine.base.Engine ('%avenue', 2, 0)
[<__main__.Customer object at 0x7f152cd12150>]
2019-12-08 19:28:32,741 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,741 INFO sqlalchemy.engine.base.Engine (2, 2)
[<__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cd12150>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
2019-12-08 19:28:32,742 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,742 INFO sqlalchemy.engine.base.Engine ('wa%',)
[<__main__.Item object at 0x7f152cb53cd0>, <__main__.Item object at 0x7f152cb11f50>]
2019-12-08 19:28:32,743 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE lower(items.name) LIKE lower(?) ORDER BY items.cost_price
2019-12-08 19:28:32,743 INFO sqlalchemy.engine.base.Engine ('wa%',)
[<__main__.Item object at 0x7f152cb11f50>, <__main__.Item object at 0x7f152cb53cd0>]
2019-12-08 19:28:32,744 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE lower(items.name) LIKE lower(?) ORDER BY items.cost_price DESC
2019-12-08 19:28:32,744 INFO sqlalchemy.engine.base.Engine ('wa%',)
[<__main__.Item object at 0x7f152cb53cd0>, <__main__.Item object at 0x7f152cb11f50>]
2019-12-08 19:28:32,745 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers JOIN orders ON customers.id = orders.customer_id
2019-12-08 19:28:32,745 INFO sqlalchemy.engine.base.Engine ()
[<__main__.Customer object at 0x7f152cba2a90>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers JOIN orders ON customers.id = orders.customer_id
2019-12-08 19:28:32,746 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.username AS customers_username, orders.id AS orders_id 
FROM customers JOIN orders ON customers.id = orders.customer_id
2019-12-08 19:28:32,746 INFO sqlalchemy.engine.base.Engine ()
[(1, 'tmiller', 1), (1, 'tmiller', 2), (1, 'tmiller', 3)]
2019-12-08 19:28:32,748 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers JOIN orders ON customers.id = orders.customer_id JOIN order_lines ON orders.id = order_lines.order_id JOIN items ON items.id = order_lines.item_id
2019-12-08 19:28:32,748 INFO sqlalchemy.engine.base.Engine ()
[<__main__.Customer object at 0x7f152cba2a90>]

2019-12-08 19:28:32,748 INFO sqlalchemy.engine.base.Engine SELECT customers.first_name AS customers_first_name, orders.id AS orders_id 
FROM customers LEFT OUTER JOIN orders ON customers.id = orders.customer_id
2019-12-08 19:28:32,748 INFO sqlalchemy.engine.base.Engine ()
[('Toby', 1), ('Toby', 2), ('Toby', 3), ('Scott', None), ('John', None), ('Sarah', None), ('Toby', None), ('Scott', None)]
2019-12-08 19:28:32,749 INFO sqlalchemy.engine.base.Engine SELECT count(customers.id) AS count_1 
FROM customers JOIN orders ON customers.id = orders.customer_id 
WHERE customers.first_name = ? AND customers.last_name = ? GROUP BY customers.id
2019-12-08 19:28:32,749 INFO sqlalchemy.engine.base.Engine ('John', 'Green')
None
2019-12-08 19:28:32,750 INFO sqlalchemy.engine.base.Engine SELECT count(?) AS town_count, customers.town AS customers_town 
FROM customers GROUP BY customers.town 
HAVING count(?) > ?
2019-12-08 19:28:32,750 INFO sqlalchemy.engine.base.Engine ('*', '*', 2)
[]
----------------------------------------------------------------

# Section 4
2019-12-08 19:28:32,750 INFO sqlalchemy.engine.base.Engine SELECT customers.town AS customers_town 
FROM customers 
WHERE customers.id < ?
2019-12-08 19:28:32,750 INFO sqlalchemy.engine.base.Engine (10,)
[('Wolfden',), ('Beckinsdale',), ('Norfolk',), ('Norfolk',), ('Wolfden',), ('Beckinsdale',)]
2019-12-08 19:28:32,751 INFO sqlalchemy.engine.base.Engine SELECT DISTINCT customers.town AS customers_town 
FROM customers 
WHERE customers.id < ?
2019-12-08 19:28:32,751 INFO sqlalchemy.engine.base.Engine (10,)
[('Wolfden',), ('Beckinsdale',), ('Norfolk',)]
2019-12-08 19:28:32,751 INFO sqlalchemy.engine.base.Engine SELECT count(DISTINCT customers.town) AS count_1, count(customers.town) AS count_2 
FROM customers
2019-12-08 19:28:32,751 INFO sqlalchemy.engine.base.Engine ()
[(3, 6)]
----------------------------------------------------------------

# Section 5
2019-12-08 19:28:32,752 INFO sqlalchemy.engine.base.Engine SELECT CAST(? AS INTEGER) AS anon_1, CAST(? AS NUMERIC(10, 2)) AS anon_2
2019-12-08 19:28:32,752 INFO sqlalchemy.engine.base.Engine (3, 3.14)
[(3, Decimal('3.14'))]
----------------------------------------------------------------

# Section 6
SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ?
SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ?
2019-12-08 19:28:32,754 INFO sqlalchemy.engine.base.Engine SELECT anon_1.items_id AS anon_1_items_id, anon_1.items_name AS anon_1_items_name 
FROM (SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ? UNION SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ?) AS anon_1
2019-12-08 19:28:32,754 INFO sqlalchemy.engine.base.Engine ('Wa%', '%e%')
[(2, 'Pen'), (3, 'Headphone'), (4, 'Travel Bag'), (5, 'Keyboard'), (7, 'Watch'), (8, 'Water Bottle')]
2019-12-08 19:28:32,755 INFO sqlalchemy.engine.base.Engine SELECT anon_1.items_id AS anon_1_items_id, anon_1.items_name AS anon_1_items_name 
FROM (SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ? UNION ALL SELECT items.id AS items_id, items.name AS items_name 
FROM items 
WHERE items.name LIKE ?) AS anon_1
2019-12-08 19:28:32,755 INFO sqlalchemy.engine.base.Engine ('Wa%', '%e%')
[(7, 'Watch'), (8, 'Water Bottle'), (2, 'Pen'), (3, 'Headphone'), (4, 'Travel Bag'), (5, 'Keyboard'), (8, 'Water Bottle')]
----------------------------------------------------------------

# Section 7
None
2019-12-08 19:28:32,756 INFO sqlalchemy.engine.base.Engine UPDATE items SET selling_price=? WHERE items.id = ?
2019-12-08 19:28:32,756 INFO sqlalchemy.engine.base.Engine (25.91, 8)
2019-12-08 19:28:32,756 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,759 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,759 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id 
FROM items 
WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,759 INFO sqlalchemy.engine.base.Engine ('W%',)
2019-12-08 19:28:32,760 INFO sqlalchemy.engine.base.Engine UPDATE items SET quantity=? WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,760 INFO sqlalchemy.engine.base.Engine (60, 'W%')
2
2019-12-08 19:28:32,760 INFO sqlalchemy.engine.base.Engine COMMIT
----------------------------------------------------------------

# Section 8
2019-12-08 19:28:32,762 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,762 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.name = ?
2019-12-08 19:28:32,762 INFO sqlalchemy.engine.base.Engine ('Monitor',)
[<__main__.Item object at 0x7f152cb53810>]
2019-12-08 19:28:32,763 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,763 INFO sqlalchemy.engine.base.Engine (7,)
2019-12-08 19:28:32,764 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,764 INFO sqlalchemy.engine.base.Engine (8,)
2019-12-08 19:28:32,764 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,764 INFO sqlalchemy.engine.base.Engine (2,)
2019-12-08 19:28:32,764 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,765 INFO sqlalchemy.engine.base.Engine (1,)
2019-12-08 19:28:32,765 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,765 INFO sqlalchemy.engine.base.Engine (4,)
2019-12-08 19:28:32,765 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,765 INFO sqlalchemy.engine.base.Engine (3,)
2019-12-08 19:28:32,766 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id, items.name AS items_name, items.cost_price AS items_cost_price, items.selling_price AS items_selling_price, items.quantity AS items_quantity 
FROM items 
WHERE items.id = ?
2019-12-08 19:28:32,766 INFO sqlalchemy.engine.base.Engine (5,)
2019-12-08 19:28:32,766 INFO sqlalchemy.engine.base.Engine DELETE FROM items WHERE items.name = ?
2019-12-08 19:28:32,766 INFO sqlalchemy.engine.base.Engine ('Monitor',)
1
2019-12-08 19:28:32,766 INFO sqlalchemy.engine.base.Engine COMMIT
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine SELECT items.id AS items_id 
FROM items 
WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine ('W%',)
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine DELETE FROM items WHERE lower(items.name) LIKE lower(?)
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine ('W%',)
2
2019-12-08 19:28:32,769 INFO sqlalchemy.engine.base.Engine COMMIT
----------------------------------------------------------------

# Section 9
2019-12-08 19:28:32,772 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-12-08 19:28:32,772 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE first_name = 'John'
2019-12-08 19:28:32,772 INFO sqlalchemy.engine.base.Engine ()
[<__main__.Customer object at 0x7f152cd12110>]
2019-12-08 19:28:32,773 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE town like 'Nor%'
2019-12-08 19:28:32,773 INFO sqlalchemy.engine.base.Engine ()
[<__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cd12150>]
2019-12-08 19:28:32,773 INFO sqlalchemy.engine.base.Engine SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE town like 'Nor%' ORDER BY first_name, id desc
2019-12-08 19:28:32,773 INFO sqlalchemy.engine.base.Engine ()
[<__main__.Customer object at 0x7f152cd12110>, <__main__.Customer object at 0x7f152cd12150>]
----------------------------------------------------------------

# Section 10
2019-12-08 19:28:32,774 INFO sqlalchemy.engine.base.Engine SELECT orders.id AS orders_id, orders.customer_id AS orders_customer_id, orders.date_placed AS orders_date_placed 
FROM orders 
WHERE orders.id = ?
2019-12-08 19:28:32,774 INFO sqlalchemy.engine.base.Engine (1,)
Order already shipped.

Process finished with exit code 0
