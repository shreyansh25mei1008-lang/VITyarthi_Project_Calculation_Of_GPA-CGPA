from typing import Dict, List, Optional, Union

GRADE_POINTS: Dict[str, int] = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0,
    "N": 0,
    "P": -1
}


def calculate_letter_grade(
        total_marks: float,
        tee_marks: float,
        cat1_cat2_tee_total: float,
        mean: float,
        std_dev: float,
        course_type: str = "LT/LP/LTP"
) -> str:
    if course_type in ["LT/LP/LTP"] and (tee_marks < 0.4 * 100 or cat1_cat2_tee_total < 0.4 * 100):
        return "F"

    if course_type in ["PJ/P"] and (tee_marks < 0.5 * 100 or cat1_cat2_tee_total < 0.5 * 100):
        return "F"

    if total_marks >= (mean + 1.5 * std_dev):
        return "S"

    if total_marks >= (mean + 0.5 * std_dev):
        return "A"

    if total_marks >= (mean - 0.5 * std_dev):
        return "B"

    if total_marks >= (mean - 1.0 * std_dev):
        return "C"

    if total_marks >= (mean - 1.5 * std_dev):
        return "D"

    return "E"


class Course:
    def __init__(self, name: str, credits: float, letter_grade: str):
        self.name = name
        self.credits = credits
        self.letter_grade = letter_grade.upper()

    def get_grade_point(self) -> Optional[int]:
        return GRADE_POINTS.get(self.letter_grade)


def calculate_gpa(courses: List[Course]) -> float:
    total_grade_points = 0.0
    total_credits = 0.0

    for course in courses:
        grade_point = course.get_grade_point()

        if grade_point is not None and grade_point != -1:
            total_grade_points += grade_point * course.credits
            total_credits += course.credits

    if total_credits == 0:
        return 0.0

    return total_grade_points / total_credits


def calculate_cgpa(semesters: List[List[Course]]) -> float:
    all_courses = [course for semester in semesters for course in semester]
    return calculate_gpa(all_courses)


if __name__ == "__main__":
    MEAN = 65.0
    STD_DEV = 10.0

    MAX_TEE = 60
    MAX_CAT_TEE = 100

    print("--- PART 1: Relative Grade Assignment Simulation ---")
    print(f"Course Statistics: Mean={MEAN:.2f}, Std Dev={STD_DEV:.2f}")

    s_grade_marks = MEAN + 1.5 * STD_DEV + 1
    grade_s = calculate_letter_grade(s_grade_marks, 0.7 * MAX_TEE, 0.75 * MAX_CAT_TEE, MEAN, STD_DEV)
    print(f"Marks: {s_grade_marks:.2f} (TEE Pass) -> Grade: {grade_s} (Points: {GRADE_POINTS[grade_s]})")

    b_grade_marks = MEAN
    grade_b = calculate_letter_grade(b_grade_marks, 0.6 * MAX_TEE, 0.65 * MAX_CAT_TEE, MEAN, STD_DEV)
    print(f"Marks: {b_grade_marks:.2f} (TEE Pass) -> Grade: {grade_b} (Points: {GRADE_POINTS[grade_b]})")

    e_grade_marks = MEAN - 1.5 * STD_DEV - 1
    grade_e = calculate_letter_grade(e_grade_marks, 0.5 * MAX_TEE, 0.5 * MAX_CAT_TEE, MEAN, STD_DEV)
    print(f"Marks: {e_grade_marks:.2f} (TEE Pass) -> Grade: {grade_e} (Points: {GRADE_POINTS[grade_e]})")

    f_grade_marks = 50.0
    f_tee_marks = 0.3 * MAX_TEE
    grade_f = calculate_letter_grade(f_grade_marks, f_tee_marks, 0.6 * MAX_CAT_TEE, MEAN, STD_DEV)
    print(
        f"Marks: {f_grade_marks:.2f} (TEE: {f_tee_marks:.1f} - TEE Fail) -> Grade: {grade_f} (Points: {GRADE_POINTS[grade_f]})")

    print("\n--- PART 2: GPA and CGPA Calculation ---")

    sem1_courses = [
        Course("Calculus", 4.0, "A"),
        Course("Physics", 3.0, "S"),
        Course("Lab 1", 1.5, "B"),
        Course("Pass/Fail", 1.0, "P")
    ]
    sem1_gpa = calculate_gpa(sem1_courses)
    print(f"Semester 1 GPA: {sem1_gpa:.2f}")

    sem2_courses = [
        Course("Data Structures", 4.0, "A"),
        Course("Digital Logic", 3.0, "C"),
        Course("Ethics", 2.0, "D"),
        Course("Microprocessors", 4.0, "E"),
        Course("Failed Course", 3.0, "F")
    ]
    sem2_gpa = calculate_gpa(sem2_courses)
    print(f"Semester 2 GPA: {sem2_gpa:.2f}")

    all_semesters = [sem1_courses, sem2_courses]
    cgpa = calculate_cgpa(all_semesters)

    all_courses = [course for semester in all_semesters for course in semester]
    print(f"\nTotal Credits Attempted (non-P): {sum(c.credits for c in all_courses if c.letter_grade != 'P'):.1f}")
    print(f"Cumulative Grade Point Average (CGPA): {cgpa:.2f}")