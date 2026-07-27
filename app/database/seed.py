from app.database.connection import Base, SessionLocal, engine
from app.database.models import Employee

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(Employee).count() == 0:

    employees = [
        Employee(name="Alice", department="Sales", salary=60000),
        Employee(name="Bob", department="Engineering", salary=85000),
        Employee(name="Charlie", department="HR", salary=50000),
        Employee(name="David", department="Engineering", salary=90000),
    ]

    db.add_all(employees)
    db.commit()

print("Database initialized successfully!")

db.close()