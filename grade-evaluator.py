import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                # Convert numeric fields to floats for calculations
                    assignments.append({
                        'assignment': row['assignment'],
                        'group': row['group'],
                        'score': float(row['score']),
                        'weight': float(row['weight'])
                    })
                except (ValueError, TypeError, KeyError):
                    print(f"Error: Invalid row in CSV: {row}")
                    sys.exit(1)
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # If CSV is empty (After archival)
    if len(data) == 0:
        print("Error: The file has no assignment records. Add grades before running.")
        sys.exit(1)

    formative = 0
    summative = 0
    total_weight = 0
    for assignment in data:
    # a) Check if all scores are percentage based (0-100)
        score = assignment['score']
        if score < 0 or score > 100:
            print(f"Error: Score for assignment '{assignment['assignment']}' is out of range (0-100).")
            sys.exit(1)
            
    # b) Validate total weights (Total=100, Summative=40, Formative=60)
        if assignment['group'] == "Formative":
            formative += assignment['weight']
        elif assignment['group'] == "Summative":
            summative += assignment['weight']
        total_weight += assignment['weight']
    if formative != 60 or summative != 40:
        print(f"Error: Total weights are incorrect. Formative: {formative}, Summative: {summative}. Expected: Formative=60, Summative=40.")
        sys.exit(1)
    if total_weight != 100:
        print(f"Error: Total weight of all assignments is {total_weight}, but it should be 100.")
        sys.exit(1)
        
    # c) Calculate the Final Grade and GPA
    final_grade = 0
    for assignment in data:
        name = assignment['assignment']
        score = assignment['score']
        weight = assignment['weight']
        final_weight = (score / 100) * weight
        final_grade += final_weight
        print(f"{name} final weight: {final_weight:.2f}")
    print(f"Final Grade: {final_grade:.2f}%")
    gpa = (final_grade / 100) * 5
    print(f"GPA: {gpa:.2f}")
    
    # d) Determine Pass/Fail status (>= 50% in BOTH categories)
    formative_score = 0
    summative_score = 0
    final_decision = ""
    for assignment in data:
        if assignment['group'] == "Formative":
            formative_score += (assignment['score'] / 100) * assignment['weight']
        elif assignment['group'] == "Summative":
            summative_score += (assignment['score'] / 100) * assignment['weight']
            
    formative_percent = (formative_score / formative) * 100
    summative_percent = (summative_score / summative) * 100
    print(f"Formative: {formative_percent:.2f}%  Summative: {summative_percent:.2f}%")

    if formative_percent >= 50 and summative_percent >= 50:
        final_decision = "PASSED"
    else:
        final_decision = "FAILED"

    # e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    failed_formative = []

    for assignment in data:
        if assignment['group'] == "Formative" and assignment['score'] < 50:
            failed_formative.append(assignment)

    resubmission_options = []

    if failed_formative:
        highest_weight = failed_formative[0]['weight']

        for assignment in failed_formative:
            if assignment['weight'] > highest_weight:
                highest_weight = assignment['weight']

        for assignment in failed_formative:
            if assignment['weight'] == highest_weight:
                resubmission_options.append(assignment)
                
    # f) Print the final decision (PASSED / FAILED) and resubmission options
    print(f"Final decision: You {final_decision}")
    print("Resubmission options:")
    for assignment in resubmission_options:
        print(f" - {assignment['assignment']}")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)