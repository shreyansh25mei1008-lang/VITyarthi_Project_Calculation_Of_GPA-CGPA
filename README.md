📘 Relative Grading System + GPA/CGPA Calculator

A Python program that simulates relative grade assignment and calculates GPA and CGPA based on course grades.

This project includes:

A dynamic relative grading algorithm using mean & standard deviation

Minimum pass criteria for different course types

GPA & CGPA computation using weighted grade points

A sample demonstration (Part 1 & Part 2) showing how the system works

✨ Features
🎯 1. Relative Grade Assignment

Grades are assigned based on the student’s total marks relative to the mean and standard deviation:

Condition	Grade
total ≥ mean + 1.5σ	S
total ≥ mean + 0.5σ	A
total ≥ mean − 0.5σ	B
total ≥ mean − 1.0σ	C
total ≥ mean − 1.5σ	D
otherwise	E
🔐 2. Pass/Fail Rules
For LT / LP / LTP courses:

TEE < 40% → F

Overall (CAT1 + CAT2 + TEE) < 40% → F

For P / PJ courses:

TEE < 50% → F

Overall < 50% → F

➗ 3. GPA Calculation

Letter grades map to grade points:

S:10 | A:9 | B:8 | C:7 | D:6 | E:5 | F:0 | N:0 | P:-1


Courses with P grade are excluded from GPA (ignored due to grade point -1).

GPA formula:

GPA = Σ(grade_point × credits) / Σ(credits)

📊 4. CGPA Calculation

CGPA is computed by flattening all semesters and applying the same GPA formula across all courses.

📁 Project Structure
.
├── main.py      # Program source code
└── README.md    # Documentation

▶️ Running the Program

Make sure you have Python 3.7+ installed.

Run:

python main.py


You will see:

Relative grading simulation

Semester 1 GPA

Semester 2 GPA

Total attempted credits

Final CGPA

🧪 Example Output
--- PART 1: Relative Grade Assignment Simulation ---
Marks: 81.00 (TEE Pass) -> Grade: S
Marks: 65.00 (TEE Pass) -> Grade: B
Marks: 49.00 (TEE Pass) -> Grade: E
Marks: 50.00 (TEE: 18.0 - TEE Fail) -> Grade: F

--- PART 2: GPA and CGPA Calculation ---
Semester 1 GPA: 8.89
Semester 2 GPA: 5.46

Total Credits Attempted (non-P): 18.5
Cumulative Grade Point Average (CGPA): 6.87

🧩 Code Components
calculate_letter_grade()

Implements pass criteria + relative grade cutoff logic.

Course class

Stores course name, credits, and letter grade.

calculate_gpa()

Computes GPA for a list of Course objects.

calculate_cgpa()

Computes CGPA across semesters.

🔧 Requirements

Python 3.7+

No external libraries required
