Project Statement: Relative GPA/CGPA Calculation Engine

1. Introduction and Problem Definition

This project, implemented in gpa_cgpa_calculator.py, addresses the challenge of accurately calculating student academic performance (GPA/CGPA) within an institutional framework that employs a dual-criteria grading system: Relative Grading blended with Absolute Fail Conditions.

The core problem is to ensure that the grading algorithm correctly handles the precedence of these two rule sets:

Absolute Failure: Mandatory checks for minimum required marks in key components (e.g., TEE, CAT aggregates) must result in a failure grade ('F'), regardless of the class's overall performance.

Relative Performance: If absolute criteria are met, the final grade must be assigned based on the student's deviation from the class average (Mean, $\mu$) using the Standard Deviation ($\sigma$).

2. Mathematical and Algorithmic Core

The logic for determining the Letter Grade is the central pillar of the application. It relies entirely on the prescribed statistical thresholds:

Relative Grading Model ($\mu$ and $\sigma$ Thresholds)

The calculate_letter_grade function uses cascading if/elif statements to map the student's total_marks to the standard grade slabs:

Grade

Formula

Grade Point

S (Superior)

Total Marks $\ge$ ($\mu + 1.5\sigma$)

10

A (Excellent)

($\mu + 0.5\sigma$) $\le$ Total Marks $<$ ($\mu + 1.5\sigma$)

9

B (Good)

($\mu - 0.5\sigma$) $\le$ Total Marks $<$ ($\mu + 0.5\sigma$)

8

C (Average)

($\mu - 1.0\sigma$) $\le$ Total Marks $<$ ($\mu - 0.5\sigma$)

7

D (Pass)

($\mu - 1.5\sigma$) $\le$ Total Marks $<$ ($\mu - 1.0\sigma$)

6

E (Marginal Pass)

Total Marks $<$ ($\mu - 1.5\sigma$)

5

Absolute Fail Check Precedence

Crucially, the grading function executes the absolute minimum checks first. For instance, in LT/LP/LTP courses, an 'F' is immediately returned if the TEE component is below 40% or the core aggregate (CAT I + CAT II + TEE) is below 40%, effectively overriding any potential high grade assigned by the relative performance curve.

3. Technical Implementation Highlights

The program is built using Python 3 and emphasizes modularity and readability.

Object-Oriented Data Modeling

The Course class acts as the primary data model, encapsulating the necessary input for GPA calculation:

class Course:
    def __init__(self, name: str, credits: float, letter_grade: str):
        # ... stores course details


Weighted Average Calculation

The calculate_gpa and calculate_cgpa functions use the standard weighted average formula:
$$ \text{GPA} = \frac{\sum (\text{Grade Point} \times \text{Credits})}{\sum \text{Credits}} $$

This implementation ensures that courses with a 'P' (Pass/Fail) grade, which carry a Grade Point of -1, are correctly filtered out of the GPA/CGPA credit total, adhering to common academic policy.

4. Conclusion

The gpa_cgpa_calculator.py successfully translates a detailed, multi-layered institutional grading policy into a verifiable and reusable Python utility. It provides a robust engine for academic record computation, reconciling statistical models with necessary administrative minimums, and offers clear modularity for future integration into larger student information systems.
