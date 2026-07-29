from app.database.connection import Base, SessionLocal, engine
from app.database.models import (
    Department,
    Employee,
    Project,
    Customer,
    Product,
    CustomerOrder,
)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

departments = [

    Department(name="Sales"),

    Department(name="Engineering"),

    Department(name="HR"),
]

db.add_all(departments)

db.commit()

employees = [

    Employee(name="Alice", department_id=1, salary=60000),

    Employee(name="Bob", department_id=2, salary=85000),

    Employee(name="Charlie", department_id=3, salary=50000),

    Employee(name="David", department_id=2, salary=90000),
]

db.add_all(employees)

db.commit()

projects = [

    Project(name="AI Agent", department_id=2),

    Project(name="CRM Upgrade", department_id=1),

    Project(name="Hiring Portal", department_id=3),
]

db.add_all(projects)

db.commit()

customers = [

    Customer(name="John", city="New York"),

    Customer(name="Emma", city="Chicago"),

    Customer(name="Michael", city="Boston"),
]

db.add_all(customers)

db.commit()

products = [

    Product(name="Laptop", price=1200),

    Product(name="Mouse", price=30),

    Product(name="Keyboard", price=80),
]

db.add_all(products)

db.commit()

orders = [

    CustomerOrder(
        customer_id=1,
        product_id=1,
        quantity=1,
        order_date="2025-01-01",
    ),

    CustomerOrder(
        customer_id=2,
        product_id=2,
        quantity=3,
        order_date="2025-01-02",
    ),

    CustomerOrder(
        customer_id=3,
        product_id=3,
        quantity=2,
        order_date="2025-01-03",
    ),
]

db.add_all(orders)

db.commit()

print("Database initialized successfully!")

db.close()