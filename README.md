# 💰 Expense Tracker (Python)

A progressively built, industry-style **Expense Tracker** — evolving from core Python fundamentals into a full-fledged, database-backed, portfolio-ready application. Built as a series of versions (V1 → V6), each one layering on real-world software development concepts, culminating in a polished CLI application with persistence, a database backend, search/edit/delete, statistics, and charts.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Project Journey (V1 → V6)](#-project-journey-v1--v6)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Concepts Learned](#-concepts-learned)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📌 About the Project

This Expense Tracker is a **learning-driven, fully completed build** that simulates how real software matures over time — from a simple in-memory script to a menu-driven CLI app, to a validated and analyzed data tool, to a persistent, database-backed, portfolio-quality application.

All six planned versions (`V1` through `V6`) have been completed, taking the project from basic Python scripting to a modular, database-powered application with search, edit, delete, statistics, and data visualization.

---

## 🗺️ Project Journey (V1 → V6)

| Version | Status | Description |
|--------|--------|--------------|
| **V1** — Basic Expense Tracker | ✅ Complete | Core logic using lists & dictionaries |
| **V2** — Menu-Based Application | ✅ Complete | Interactive, menu-driven CLI |
| **V3** — Validation & Analysis | ✅ Complete | Input validation, decimals, categories, search, edit, delete |
| **V4** — Data Persistence | ✅ Complete | JSON/CSV-based save & load |
| **V5** — Database Version | ✅ Complete | Migrated to SQLite with full CRUD |
| **V6** — Portfolio / Professional Version | ✅ Complete | Clean UI, statistics, charts, modular structure |

```
V1 → V2 → V3 → V4 → V5 → V6
Basic   Menu   Validated   Persistent   Database   Portfolio-Ready
Logic   Driven  & Analyzed    (JSON)     (SQLite)     Application
```

---

## ✨ Features

- ➕ **Add expenses** with amount, description, and category
- ✅ **Input validation** — rejects invalid amounts, empty descriptions, and invalid categories
- 💵 **Decimal amount support** (e.g. ₹200.00, ₹150.50)
- 🏷️ **Category system** — `food`, `travel`, `shopping`, `education`, `other` (case-insensitive)
- 📋 **View all expenses** in a clean, readable format
- 🔍 **Search expenses** by category or description
- ✏️ **Edit existing expenses** (amount, description, category)
- 🗑️ **Delete expenses**
- 📊 **Total spending calculation**
- 📈 **Category-wise spending breakdown**
- 📉 **Charts** — visual breakdown of spending by category
- 💾 **Persistent storage** — expenses saved and loaded via SQLite database
- 🧱 **Modular, clean project structure** — separated into logical files/modules
- ⚠️ **Robust error handling** for invalid inputs and edge cases throughout

---

## 🛠️ Tech Stack

| Category         | Technology                          |
|-------------------|--------------------------------------|
| Language          | Python 3.10+                        |
| Database          | SQLite                              |
| Data Persistence  | SQLite (evolved from JSON/CSV in V4) |
| Visualization     | Python charting library (e.g. Matplotlib) |
| Interface         | Command-Line Interface (CLI)        |
| Version Control   | Git & GitHub                        |

---

## 🧠 Concepts Learned

This project covers a complete learning arc, one version at a time:

`Python basics` → `data structures (lists/dicts)` → `control flow` → `input validation` → `searching` → `CRUD operations` → `file handling` → `JSON serialization` → `SQLite & SQL` → `statistics` → `data visualization` → `modular project structuring` → `GitHub portfolio presentation`

**By version:**
- **V1:** Lists, dictionaries, `input()`, `if/elif/else`, `while`/`for` loops, nested loops, dictionary access, accumulating totals, `.lower()`
- **V2:** Menu-driven design, infinite `while` loops, `break`, program flow control, user interaction
- **V3:** Input validation, type casting, string handling, case-insensitive comparisons, search logic, update/delete operations
- **V4:** File I/O, JSON/CSV serialization & deserialization, persisting data across sessions
- **V5:** SQL fundamentals, SQLite integration, tables, primary keys, `INSERT` / `SELECT` / `UPDATE` / `DELETE` queries
- **V6:** Data visualization, modular architecture, clean code practices, project documentation

---

## 📂 Project Structure

```
expense-tracker/
├── main.py             # Entry point / menu loop
├── database.py         # SQLite database connection & queries
├── expense.py          # Expense data model & core logic
├── statistics.py        # Totals, category-wise analysis, charts
├── requirements.txt     # Project dependencies
├── data/
│   └── expenses.db      # SQLite database file
├── LICENSE
└── README.md
```

> ⚠️ *Update file names above if your actual module names differ.*

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.10+](https://www.python.org/downloads/)
- pip

### Installation

```bash
git clone https://github.com/abhinavspillai7-web/expense-tracker.git
cd expense-tracker
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

---

## 💡 Usage

```
========================
     EXPENSE TRACKER
========================

1. Add Expense
2. View Expenses
3. Search Expense
4. Edit Expense
5. Delete Expense
6. Total Spending
7. Category-wise Spending
8. View Charts
9. Exit

Enter your choice: 1

Enter amount: 200
Enter description: Lunch
Enter category (food/travel/shopping/education/other): food

✅ Expense added successfully!
```

---

## 📊 Sample Output

**Expense list:**
```
1. ₹200.00 | Lunch | Food
2. ₹500.00 | Bus   | Travel
3. ₹150.00 | Book  | Education
```

**Category-wise spending:**
```
Food:       ₹200.00
Travel:     ₹500.00
Shopping:   ₹0.00
Education:  ₹150.00
Other:      ₹0.00

Total Spending: ₹850.00
```

**Chart (category breakdown):**
```
Food       ████████
Travel     ████████████████████
Shopping
Education  ██████
Other
```

---

## 🔮 Future Enhancements

While all planned versions (V1–V6) are complete, potential next steps include:

- [ ] Add a graphical interface (Tkinter / Streamlit / Flask web app)
- [ ] Multi-user support with authentication
- [ ] Export reports to PDF/Excel
- [ ] Monthly/yearly trend analysis
- [ ] Budget limits and alerts
- [ ] Unit test coverage with `pytest`
- [ ] Multi-currency support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Abhinav S Pillai**
📧 abhinavspillai7@gmail.com
🔗 [GitHub](https://github.com/abhinavspillai7-web)

---

⭐ If you found this project useful, consider giving it a star on GitHub — it took a full journey from V1 to V6 to get here!
