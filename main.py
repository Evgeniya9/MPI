
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

def main():
    print(f"Текущая дата: {date.today()}")
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()