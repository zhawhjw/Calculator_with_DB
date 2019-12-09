from datetime import datetime, date

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, ForeignKey, SmallInteger, or_, and_, \
    not_
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("postgresql://postgres:pass@localhost:54320/mydb")
# engine = create_engine("postgresql://postgres:pass@db:5432/mydb")

engine = create_engine('sqlite:///foo.db?check_same_thread=False', echo=True)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')

    # def __repr__(self):
    #    return "<Customer(first_name='%s', last_name='%s', username='%s', email='%s', address='%s', town='%s')>" % (
    #        self.first_name, self.last_name, self.username, self.email, self.address, self.town)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)
    # orders = relationship("Order", backref='customer')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    order_lines = relationship("OrderLine", backref='orders')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    # item = relationship("Item")


Base.metadata.create_all(engine)

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

print(c1.id)
print(c2.id)

session.add_all([c1, c2])

# session.new

session.commit()

print(c1.id)
print(c2.id)

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer_id=c1.id)
o2 = Order(customer_id=c1.id)

line_item1 = OrderLine(order_id=o1.id, item_id=i1.id, quantity=3)
line_item2 = OrderLine(order_id=o1.id, item_id=i2.id, quantity=2)
line_item3 = OrderLine(order_id=o2.id, item_id=i1.id, quantity=1)
line_item4 = OrderLine(order_id=o2.id, item_id=i2.id, quantity=4)

session.add_all([o1, o2])

# session.new
session.commit()

o3 = Order(customer_id=c1.id)
orderline1 = OrderLine(item_id=i1.id, quantity=5)
orderline2 = OrderLine(item_id=i2.id, quantity=10)

o3.order_lines.append(orderline1)
o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

print("customer1.orders")
print(c1.orders)
print()

print("order1.customer")
print(o1.customer)
print()

print("customer1.orders(3).order_lines")
print(c1.orders[2].order_lines)
print()

print("details of customer1.orders(3).order_lines")
for ol in c1.orders[2].order_lines:
    print("ol id:")
    print(ol.id)
    print()
    print("ol.item_id:")
    print(ol.item_id)
    print()
    print("ol.quantity:")
    print(ol.quantity)
    print()

print('--------------------------------------------------------------------------')
print()

print("Section 3")

session.query(Customer).all()

session.query(Customer)

q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

print()

print(session.query(Customer.id, Customer.first_name).all())

print (session.query(Customer).count())  # get the total number of records in the customers table
print(session.query(Item).count())  # get the total number of records in the items table
print(session.query(Order).count())  # get the total number of records in the orders table

print(session.query(Customer).first())
print(session.query(Item).first())
print(session.query(Order).first())

print(session.query(Customer).get(1))
print(session.query(Item).get(1))
print(session.query(Order).get(100))

print(session.query(Customer).filter(Customer.first_name == 'John').all())

print(session.query(Customer).filter(Customer.first_name == 'John'))

print(session.query(Customer).filter(Customer.id <= 5, Customer.town == "Norfolk").all())

print(session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all())

# find all customers whose first name is John and live in Norfolk

print(session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all())

# find all johns who don't live in Peterbrugh

print(session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all())

print(session.query(Order).filter(Order.date_placed == None).all())

print(session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all())

print(session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all())

print(session.query(Item).filter(Item.cost_price.between(10, 50)).all())

print(session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all())

print(session.query(Item).filter(Item.name.like("%r")).all())

print(session.query(Item).filter(Item.name.ilike("w%")).all())

print(session.query(Item).filter(not_(Item.name.like("W%"))).all())

print(session.query(Customer).limit(2).all())
print(session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all())

print(session.query(Customer).limit(2).offset(2).all())

print(session.query(Customer).limit(2).offset(2))

print(session.query(Item).filter(Item.name.ilike("wa%")).all())
print(session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all())

from sqlalchemy import desc

print(session.query(Item).filter(Item.name.ilike("wa%")).order_by(desc(Item.cost_price)).all())

print(session.query(Customer).join(Order).all())

print(session.query(Customer).join(Order))

print(session.query(Customer.id, Customer.username, Order.id).join(Order).all())

print(session.query(Customer).join(Order).join(OrderLine).join(Item).all())

print()
'''
session.query(
    Customer.first_name,
    Item.name,
    Item.selling_price,
    OrderLine.quantity
).join(Order).join(OrderLine).join(Item).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
    Order.id == 1,
).all()
'''
print(session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()
)


#print(session.query(
#    Customer.first_name,
#    Order.id,
#).outerjoin(Order, full=True).all()
#)

from sqlalchemy import func

print(session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar()
)

# find the number of customers lives in each town

print(session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") > 2).all())

print("----------------------------------------------------------------")
print()
print("Section 4")

from sqlalchemy import distinct

print(session.query(Customer.town).filter(Customer.id < 10).all())
print(session.query(Customer.town).filter(Customer.id < 10).distinct().all())

print(session.query(
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all())

print("----------------------------------------------------------------")
print()
print("Section 5")

from sqlalchemy import cast, Date, distinct, union

print(session.query(
    cast(3, Integer),
    cast(3.14, Numeric(10, 2)),
    #date('now'),
    #cast(datetime.now(), Date),
).all())

print("----------------------------------------------------------------")
print()
print("Section 6")

s1 = session.query(Item.id, Item.name).filter(Item.name.like("Wa%"))
s2 = session.query(Item.id, Item.name).filter(Item.name.like("%e%"))
print(s1)
print(s2)
print(s1.union(s2).all())

print(s1.union_all(s2).all())

print("----------------------------------------------------------------")
print()
print("Section 7")

i = session.query(Item).get(8)
i.selling_price = 25.91
print(session.add(i))
session.commit()

print(session.query(Item).filter(
    Item.name.ilike("W%")
).update({"quantity": 60}, synchronize_session='fetch'))
session.commit()

print("----------------------------------------------------------------")
print()
print("Section 8")

print(session.query(Item).filter(Item.name == 'Monitor').all())
print(session.query(Item).filter(Item.name == 'Monitor').delete())

session.commit()

print(session.query(Item).filter(
    Item.name.ilike("W%")
).delete(synchronize_session='fetch'))
session.commit()

print("----------------------------------------------------------------")
print()
print("Section 9")

from sqlalchemy import text

print(session.query(Customer).filter(text("first_name = 'John'")).all())

print(session.query(Customer).filter(text("town like 'Nor%'")).all())

print(session.query(Customer).filter(text("town like 'Nor%'")).order_by(text("first_name, id desc")).all())

print("----------------------------------------------------------------")
print()
print("Section 10")

from sqlalchemy.exc import IntegrityError
from datetime import datetime


def dispatch_order(order_id):
    # check whether order_id is valid or not
    order = session.query(Order).get(order_id)

    if not order:
        raise ValueError("Invalid order id: {}.".format(order_id))

    if order.date_placed:
        print("Order already shipped.")
        return

    try:
        for i in order.order_lines:
            i.item.quantity = i.item.quantity - i.quantity

        order.date_placed = datetime.now()
        session.commit()
        print("Transaction completed.")

    except IntegrityError as e:
        print(e)
        print("Rolling back ...")
        session.rollback()
        print("Transaction failed.")


dispatch_order(1)
