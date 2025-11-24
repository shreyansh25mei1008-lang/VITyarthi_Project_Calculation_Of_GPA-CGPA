GPA and CGPA Calculator (Relative Grading System)
Overview
This Python program implements a complex academic grading system based on relative performance (using the class Mean ($\mu$) and Standard Deviation ($\sigma$)) combined with absolute minimum pass criteria. It provides functions to:
Determine the Letter Grade for a course based on relative and absolute rules.
Calculate the Grade Point Average (GPA) for a single semester.
Calculate the Cumulative Grade Point Average (CGPA) across multiple semesters.
Prerequisites
The program requires Python 3.6 or higher. No external libraries are needed beyond standard built-in modules (typing).
Core Grading Logic Implemented
The calculate_letter_grade function incorporates the following rules based on the provided institutional criteria:
1. Relative Grading Formula (Determines S, A, B, C, D, E)
The letter grade is assigned based on where the student's total_marks fall relative to the class mean ($\mu$) and standard deviation ($\sigma$):
Grade
Criteria
S
Total Marks $\ge$ ($\mu + 1.5\sigma$)
A
($\mu + 0.5\sigma$) $\le$ Total Marks $<$ ($\mu + 1.5\sigma$)
B
($\mu - 0.5\sigma$) $\le$ Total Marks $<$ ($\mu + 0.5\sigma$)
C
($\mu - 1.0\sigma$) $\le$ Total Marks $<$ ($\mu - 0.5\sigma$)
D
($\mu - 1.5\sigma$) $\le$ Total Marks $<$ ($\mu - 1.0\sigma$)
E
Total Marks $<$ ($\mu - 1.5\sigma$) (provided absolute pass criteria are met)

2. Absolute Fail Criteria (Overrides Relative Grade to 'F')
The program checks for mandatory minimum requirements first:
For LT/LP/LTP Courses: The grade is 'F' if (TEE Marks < 40%) OR (CAT I + CAT II + TEE Total < 40%).
For PJ/P Courses: The grade is 'F' if (TEE Marks < 50%) OR (Project/Lab CAM + TEE Total < 50%).
Program Structure and Usage
The program is structured around a utility function for grading and an object-oriented approach for data management.
Class: Course
This class is used to store and manage course data necessary for GPA/CGPA calculation.
Attribute
Type
Description
name
str
Name of the course.
credits
float
Credit weightage of the course.
letter_grade
str
The final grade assigned (e.g., "S", "A", "F").

Function: calculate_letter_grade()
This is the core grading engine.
def calculate_letter_grade(
    total_marks: float, 
    tee_marks: float, 
    cat1_cat2_tee_total: float,
    mean: float, 
    std_dev: float,
    course_type: str = "LT/LP/LTP"
) -> str:
    # ... implementation details


Function: calculate_gpa()
Calculates the weighted average grade point for a list of Course objects (a single semester). Note: Courses with a 'P' (Pass-Fail) grade are excluded from the calculation.
def calculate_gpa(courses: List[Course]) -> float:
    # ... implementation details


Function: calculate_cgpa()
Calculates the cumulative weighted average across multiple semesters (a list of lists of Course objects).
def calculate_cgpa(semesters: List[List[Course]]) -> float:
    # ... implementation details


How to Run the Demonstration
The file includes an if __name__ == "__main__": block with demonstration tests that simulate various student performances (S grade, B grade, absolute F grade) and calculates sample GPA and CGPA values.
To run the program, execute the file from your terminal:
python gpa_cgpa_calculator.py


