# 👤 Employee Data Generator

This is a Python-based employee data generator that uses the [Faker](https://github.com/joke2k/faker) library to create realistic employee profiles for testing, prototyping, or demo purposes. You can export the generated data to CSV or JSON formats.

---

## ✨ Features

* Randomly generates employee records with:

  * Unique Employee ID (UUID)
  * Full Name (gender-specific)
  * Gender
  * Email and Phone Number
  * Address
  * Department and Job Title
  * Salary (based on job title range)
  * Joining Date and Experience (in years)
  * Performance Score (1.0 to 5.0)

* Exports to:

  * **CSV**
  * **JSON**
  * **Console output (pretty printed)**

* Supports **command-line arguments** for full control

---

## 🚀 Getting Started

### 📦 Prerequisites

Make sure you have Python 3 installed. Then install dependencies:

```bash
pip install faker
```

---

### ▶️ Usage

Run the script from the command line:

```bash
python employee.py
```

This generates 10 employee records and prints them to the console.

---

### 🔧 Command-Line Options

| Option    | Description                     | Example      |
| --------- | ------------------------------- | ------------ |
| `--count` | Number of employees to generate | `--count 50` |
| `--csv`   | Export data to a CSV file       | `--csv`      |
| `--json`  | Export data to a JSON file      | `--json`     |

#### 🔁 Combined Example:

```bash
python employee.py --count 100 --csv --json
```

This generates 100 employees and saves both `employee_data.csv` and `employee_data.json`.

---

## 📂 Output Files

* `employee_data.csv` — Tabular format of employee data
* `employee_data.json` — JSON format with full employee details

---

## 💡 Example Output (Console)

```json
[
  {
    "Employee ID": "ecac7843-9c98-48b6-9f9f-993f929a69f1",
    "Name": "Sarah Johnson",
    "Gender": "Female",
    "Email": "sarah.johnson@example.com",
    "Phone": "(123) 456-7890",
    "Address": "123 Main St, Springfield, IL 62704",
    "Department": "Marketing",
    "Job Title": "Marketing Specialist",
    "Salary ($)": 64320.00,
    "Join Date": "2019-03-18",
    "Experience (years)": 5.19,
    "Performance Score": 4.21
  }
]
```

---

## 🤝 Contributing

Pull requests and feedback are welcome! Feel free to fork the repo and submit improvements.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧠 Author

Developed by [HoorainMahtab]([https://github.com/khanzadi2](https://github.com/hoorain17))
