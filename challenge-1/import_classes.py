import csv

def rows_for(file_path):
    file = open(file_path)
    reader = csv.DictReader(file)

    rows = []
    for row in reader:
        rows.append(row)

    return rows

def normalize(class_rows, enrollment_rows):
    normalized = {}

    for class_row in class_rows:
        class_id = class_row['class_id']

        class_enrollment_rows = list(filter(lambda row: row['class_id'] == class_id, enrollment_rows))
        teacher_enrollment_row = next(filter(lambda row: row['user_id'].startswith('teacher_'), class_enrollment_rows), None)
        if teacher_enrollment_row == None:
            continue

        normalized[class_id] = normalize_class(class_row, teacher_enrollment_row)

    return normalized

def normalize_class(class_row, teacher_enrollment_row):
    return {
        'school_id': class_row['school_id'],
        'source_id': class_row['class_id'],
        'class_name': class_row['class_name'],
        'teacher_id': teacher_enrollment_row['user_id'],
    }

def import_classes():
    class_rows = rows_for('../csv-files/classes.csv')
    enrollment_rows = rows_for('../csv-files/enrollments.csv')

    return normalize(class_rows, enrollment_rows)

expected_total = 42
imported_classes = import_classes()

if len(imported_classes) == expected_total:
    print("All classes created! :D")
else:
    print(f"Expected {expected_total} classes, {len(imported_classes)} were created. :(")
