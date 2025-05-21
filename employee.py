import csv
import json
import uuid
import argparse
from faker import Faker
from random import choice, randint, uniform
from datetime import datetime, timedelta

fake = Faker()

# Job roles and average salaries (for simulation)
job_roles = {
    'Software Engineer': (80000, 120000),
    'Data Scientist': (85000, 130000),
    'Product Manager': (90000, 140000),
    'HR Manager': (60000, 90000),
    'Marketing Specialist': (55000, 85000),
    'Sales Executive': (50000, 80000)
}

departments = ['IT', 'HR', 'Sales', 'Marketing', 'Finance', 'Operations']

def generate_employee():
    gender = choice(['male', 'female'])
    name = fake.name_male() if gender == 'male' else fake.name_female()
    job, (min_sal, max_sal) = choice(list(job_roles.items()))
    join_date = fake.date_between(start_date='-10y', end_date='-1d')
    experience_years = round((datetime.today().date() - join_date).days / 365, 2)


    return {
        'Employee ID': str(uuid.uuid4()),
        'Name': name,
        'Gender': gender.title(),
        'Email': fake.email(),
        'Phone': fake.phone_number(),
        'Address': fake.address().replace('\n', ', '),
        'Department': choice(departments),
        'Job Title': job,
        'Salary ($)': round(uniform(min_sal, max_sal), 2),
        'Join Date': join_date.strftime('%Y-%m-%d'),
        'Experience (years)': experience_years,
        'Performance Score': round(uniform(1.0, 5.0), 2)
    }

def generate_employees(num):
    return [generate_employee() for _ in range(num)]

def save_to_csv(employees, filename='employee_data.csv'):
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)

def save_to_json(employees, filename='employee_data.json'):
    with open(filename, mode='w') as f:
        json.dump(employees, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate random employee data.")
    parser.add_argument('--count', type=int, default=10, help='Number of employees to generate')
    parser.add_argument('--csv', action='store_true', help='Export to CSV')
    parser.add_argument('--json', action='store_true', help='Export to JSON')

    args = parser.parse_args()
    employees = generate_employees(args.count)

    if args.csv:
        save_to_csv(employees)
        print(f"Saved {args.count} employees to employee_data.csv")
    if args.json:
        save_to_json(employees)
        print(f"Saved {args.count} employees to employee_data.json")
    
    if not args.csv and not args.json:
        print(json.dumps(employees, indent=2))
