# lab2_Umutoni-Rita
Individual Python Coding Lab

This project has two parts. A Python program reads a student's grades from a CSV file and works out their final grade, GPA, and whether they PASSED or FAILED. It also shows which formative assignment(s) they can resubmit. A shell script then archives the grades file so the folder is ready for the next batch of grades.

## Files
- `grade-evaluator.py` - the Python program that checks the grades and gives the final result
- `organizer.sh` - the shell script that archives `grades.csv` and keeps a log
- `grades.csv` - the student's grades (assignment, group, score, weight)
- `README.md` - this file

## How to run

### 1. Grade evaluator
To check the student's standing, run:

```
python3 grade-evaluator.py
```

You will be asked which CSV file to use (for example, `grades.csv`). The program then:

1. Checks that every score is between 0 and 100.
2. Checks that the weights are correct: Formative adds up to 60, Summative adds up to 40, and the total is 100.
3. Calculates the weighted score for each assignment, the final grade, and the GPA using `GPA = (Final Grade / 100) * 5.0`.
4. Decides if the student PASSED or FAILED. To pass, the student needs at least 50% in Formative **and** at least 50% in Summative.
5. Finds the failed formative assignments (score below 50) and shows the one with the highest weight for resubmission. If more than one has the same highest weight, it shows all of them.

If something is wrong with the file (it's missing, empty, has a bad score or the weights don't add up), the program prints an error explaining what went wrong.

### 2. Organizer
The organizer needs a Linux terminal. Run:

```
bash organizer.sh
```

The script:

1. Creates an `archive` folder if it doesn't exist yet.
2. Moves `grades.csv` into `archive/` and renames it with a timestamp, for example `grades_20251105-170000.csv`.
3. Creates a new, empty `grades.csv` so it's ready for the next grades.
4. Adds a line to `organizer.log` with the timestamp, the original file name and the archived file name. The log keeps every run.

## Testing
With the provided `grades.csv`, the program should show:
- Final Grade: 60.00%
- GPA: 3.00
- Formative: 56.67%, Summative: 65.00%
- Final decision: PASSED
- Resubmission: Group Exercise **and** Functions and Debugging Lab (both failed with the same weight of 20, so both are shown)
