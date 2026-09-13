# 💰 Expense Tracker (Python)

A progressively built, industry-style **Expense Tracker** — starting from core Python fundamentals and evolving into a full-fledged, database-backed, portfolio-ready application. This project is structured as a series of versions (V1 → V6), each one adding real-world software development concepts on top of the last.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Project Roadmap](#-project-roadmap)
- [Current Status](#-current-status)
- [Features by Version](#-features-by-version)
- [Concepts Learned](#-concepts-learned)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure (Target — V6)](#-project-structure-target--v6)
- [Roadmap / What's Left](#-roadmap--whats-left)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 About the Project

This Expense Tracker isn't just a single script — it's a **learning-driven build** designed to simulate how real software matures over time: from a simple in-memory script to a menu-driven CLI app, to a validated and analyzed data tool, to a persistent, database-backed, portfolio-quality application.

Each version (`V1` to `V6`) is a checkpoint that adds new functionality and reinforces a new set of Python/software engineering concepts.

---

## 🗺️ Project Roadmap

```
V1 → Basic Logic & Data Structures
V2 → Menu-Based Application
V3 → Validation & Analysis
V4 → Data Persistence (JSON/CSV)
V5 → Database Version (SQLite)
V6 → Portfolio / Professional Version
```

---

## ✅ Current Status

| Version | Status | Description |
|--------|--------|--------------|
| **V1** | ✅ Complete | Basic expense logic using lists & dictionaries |
| **V2** | ✅ Complete | Menu-driven CLI application |
| **V3** | 🔄 In Progress | Validation, decimals, categories, and category-wise analysis done; search, edit, delete pending |
| **V4** | ⏳ Planned | Persist data using JSON/CSV files |
| **V5** | ⏳ Planned | Migrate to SQLite database with full CRUD |
| **V6** | ⏳ Planned | Polished UI, statistics, charts, clean project structure |

---

## 🧩 Features by Version

### V1 — Basic Expense Tracker ✅
- Add an expense
- Store expense details (amount, description, category)
- Store multiple expenses
- View all expenses
- Calculate total spending
- Categorize expenses
- Exit the program

**Core data structure:**
```python
expense = [
    {
        "amount": 200,
        "description": "Lunch",
        "category": "food"
    },
    {
        "amount": 500,
        "description": "Bus",
        "category": "travel"
    }
]
```

---

### V2 — Menu-Based Application ✅
Turned the script into an actual interactive application.

```
========================
     EXPENSE TRACKER
========================

1. Add Expense
2. View Expenses
3. Total Spending
4. Exit
```

- Main menu with user-driven choices
- Add multiple expenses in a session
- View all expenses
- Calculate total spending
- Exit option
- Invalid menu choice handling

---

### V3 — Validation & Analysis 🔄

**Completed:**
1. **Amount validation** — accepts `200`, `500.50`, `75.25`; rejects `abc`, `50.5.2`
2. **Decimal amount support** — e.g. `₹200.00`, `₹150.50`, `₹99.75`
3. **Description validation** — rejects empty (`""`) or whitespace-only (`"   "`) input
4. **Category validation** — restricted, case-insensitive categories: `food`, `travel`, `shopping`, `education`, `other`
5. **Category-wise spending breakdown:**
   ```
   Food:      ₹500.00
   Travel:    ₹300.00
   Shopping:  ₹0.00
   Education: ₹0.00
   Other:     ₹0.00
   ```

**Current menu:**
```
1. Add Expense
2. View Expenses
3. Total Spending
4. Category-wise Spending
5. Exit
```

**Still to complete:**
- [ ] Search/filter expenses
- [ ] Delete an expense
- [ ] Edit an expense

---

### V4 — Data Persistence ⏳
**Goal:** Make expenses survive after the program closes.

```
Program → Save expenses → JSON/CSV file → Close program
                                              ↓
                          Open program again → Load previous expenses
```

**Planned features:**
- Save expenses to file
- Load expenses on startup
- Persistent data across sessions
- JSON/CSV read & write handling
- Update saved data after add/edit/delete

---

### V5 — Database Version ⏳
**Goal:** Upgrade from file-based storage to a proper SQLite database.

**Planned schema:**
```
expenses
--------------------------------
id | amount | description | category
--------------------------------
1  | 200.00 | Lunch        | food
2  | 500.00 | Bus          | travel
3  | 100.00 | Book         | education
```

**Planned features:**
- Add expense to database
- View expenses
- Search expenses
- Filter by category
- Edit expense
- Delete expense
- Calculate totals & category-wise totals

---

### V6 — Portfolio / Professional Version ⏳
**Goal:** Make the project genuinely resume/GitHub-worthy.

**Planned features:**
- **Cleaner UI** — e.g. `1. ₹200.00 | Lunch | Food` instead of raw key:value dumps
- **Search** by category or description
- **Delete** expenses by selection
- **Edit** existing expenses (amount, description, category)
- **Statistics** — total spending + category-wise breakdown
- **Charts** — visual bar-style breakdown by category using a Python charting library
- **Modular project structure:**
  ```
  expense-tracker/
  │
  ├── main.py
  ├── database.py
  ├── expense.py
  ├── statistics.py
  ├── requirements.txt
  └── README.md
  ```

---

## 🧠 Concepts Learned

This project intentionally covers a full learning arc:

`Python basics` → `data structures (lists/dicts)` → `control flow (if/elif/else, loops)` → `input validation` → `searching` → `CRUD operations` → `file handling` → `JSON serialization` → `SQLite & SQL` → `statistics` → `data visualization` → `project structuring` → `GitHub portfolio presentation`

Specific concepts by version:
- **V1:** Lists, dictionaries, `input()`, `if/elif/else`, `while`/`for` loops, nested loops, dictionary access, accumulating totals, `.lower()`
- **V2:** Menu-driven design, infinite `while` loops, `break`, program flow control, user interaction
- **V3:** Input validation, type casting, string handling, case-insensitive comparisons, category-wise aggregation
- **V4 (planned):** File I/O, JSON serialization/deserialization, data persistence
- **V5 (planned):** SQL, SQLite, tables, primary keys, `INSERT`/`SELECT`/`UPDATE`/`DELETE`
- **V6 (planned):** Data visualization, modular architecture, clean code practices, documentation

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.10+](https://www.python.org/downloads/)

### Installation

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

*(No external dependencies required for V1–V3 — pure Python standard library.)*

### Running the Application

```bash
python main.py
```

---

## 💡 Usage

Run the script and use the on-screen menu to interact with the tracker:

```
========================
     EXPENSE TRACKER
========================

1. Add Expense
2. View Expenses
3. Total Spending
4. Category-wise Spending
5. Exit

Enter your choice: 1

Enter amount: 200
Enter description: Lunch
Enter category (food/travel/shopping/education/other): food

✅ Expense added successfully!
```

---

## 📂 Project Structure (Target — V6)

```
expense-tracker/
├── main.py             # Entry point / menu loop
├── database.py         # SQLite database operations (V5+)
├── expense.py          # Expense data model & core logic
├── statistics.py        # Totals, category-wise analysis, charts
├── requirements.txt
└── README.md
```

> Note: Up to V3, the project runs as a single script. It will be refactored into this modular structure starting V6, once the core logic across all versions is solid.

---

## 🗺️ Roadmap / What's Left

- [ ] Finish V3: search, edit, delete expenses
- [ ] Build V4: JSON/CSV-based persistence
- [ ] Build V5: SQLite database with full CRUD
- [ ] Build V6: polished UI, statistics, charts, modular structure
- [ ] Add unit tests
- [ ] Add screenshots/demo GIF
- [ ] Publish as a portfolio project on GitHub

---

## 🤝 Contributing

This is primarily a personal learning project, but suggestions and improvements are welcome:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

⭐ Following this project from V1 to V6? Star the repo to track the journey!
