from app.database.connection import SessionLocal
from app.database.models import Employee

db = SessionLocal()

employees = db.query(Employee).all()

for employee in employees:
    print(
        employee.id,
        employee.name,
        employee.department,
        employee.salary,
    )

db.close()