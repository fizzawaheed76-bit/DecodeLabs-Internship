# 💻 Computer Career Advisor

## 📌 Project Description

**Computer Career Advisor** is a Python-based project designed to help users explore different computer and technology career fields.

The program allows the user to select a career and view:

* 📚 Career Path
* 💼 Possible Careers
* 🛠 Recommended Skills

The project contains information for **21 computer career fields**.

## 🚀 Features

* Select from 21 computer career fields
* View the career path for a selected field
* View possible career opportunities
* View recommended skills
* Return to the career selection menu
* Handle invalid career selections
* Handle invalid menu options
* Exit the application when required

## 📚 Available Career Fields

1. Artificial Intelligence
2. Data Science
3. Data Analytics
4. Machine Learning
5. Deep Learning
6. Python Development
7. Web Development
8. App Development
9. Cybersecurity
10. Cloud Computing
11. Networking
12. DevOps
13. Database
14. Software Engineering
15. Game Development
16. Robotics
17. Computer Vision
18. NLP
19. Blockchain
20. System Administration
21. QA & Testing

## 🛠 Technologies Used

* Python
* Dictionaries
* Loops
* `while` loop
* `for` loop
* `if / elif / else`
* User input
* Conditional logic
* Data structures

## ⚙️ How the Program Works

### 1. Select a Career

The program displays the available computer career fields.

The user selects a career using its number.

Example:

```text
1. Artificial Intelligence
2. Data Science
3. Data Analytics
4. Machine Learning
...
21. QA & Testing
0. Exit
```

### 2. Select Information

After selecting a career, the user gets four main choices:

```text
1. Career Path
2. Possible Careers
3. Recommended Skills
4. Back to Career Selection
5. Exit
```

### 3. Career Path

The program displays the learning path for the selected career.

Example:

```text
Python → NumPy/Pandas → Mathematics
→ Machine Learning → Deep Learning
→ AI Projects → Deployment
```

### 4. Possible Careers

The program displays possible job roles related to the selected field.

Example:

```text
AI Engineer
AI Developer
Machine Learning Engineer
```

### 5. Recommended Skills

The program displays the skills that can be learned for the selected career.

Example:

```text
Python
NumPy
Pandas
Machine Learning
Deep Learning
Data Visualization
```

## 🔄 Program Flow

```text
Start
  ↓
Display Computer Careers
  ↓
Select Career
  ↓
Is Career Valid?
  ├── No → Show Error → Select Again
  │
  └── Yes
       ↓
   Information Menu
       ↓
   ┌───────────────┐
   │ Career Path   │
   │ Possible Jobs │
   │ Skills        │
   │ Back          │
   │ Exit          │
   └───────────────┘
```

## 📂 Project Structure

```text
Computer-Career-Advisor/
│
├── career_advisor.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code and run:

```bash
python career_advisor.py
```

Or click the **Run Python File** button in VS Code.

## 🎯 Project Objective

The main objective of this project is to provide beginners with a simple way to explore computer-related career fields and understand the learning path, possible career opportunities, and recommended skills for each field.

## 🔮 Future Improvements

Possible future improvements include:

* Convert the project into a Gradio web application
* Add a graphical user interface
* Add career search
* Add career filtering
* Add detailed descriptions for each career
* Add learning resources
* Add links to courses and documentation
* Deploy the application online

## 👩‍💻 Author

**Fizza Waheed**

Bachelor of Science in Artificial Intelligence (BSAI)

Interested in Artificial Intelligence, Machine Learning, Deep Learning, Python, and Data Analytics.
