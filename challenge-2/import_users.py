import csv

def rows_for(file_path):
    file = open(file_path)
    reader = csv.DictReader(file)

    rows = []
    for row in reader:
        rows.append(row)

    return rows

def normalize_teachers(rows):
    teachers = {}
    for row in rows:
        teacher = {
            'source_id': row['teacher_id'],
            'first_name': row['teacher_first_name'],
            'last_name': row['teacher_last_name'],
            'email': row['teacher_email'],
            'phone_number': row['teacher_mobile_phone'],
        }
        teachers[teacher['email']] = teacher
    return teachers

def normalize_students(rows):
    students = {}
    for row in rows:
        student = {
            'source_id': row['student_id'],
            'first_name': row['student_first_name'],
            'last_name': row['student_last_name'],
            'dob': row['dob'],
            'grade': row['grade'],
            'email': row['student_email'],
            'phone_number': row['student_phone'],
        }
        students[student['email']] = student
    return students

def normalize_parents(rows):
    parents = {}
    for row in rows:
        parent = {
            'source_id': f"parent_{row['student_id']}_{row['guardian_first_name']}",
            'first_name': row['guardian_first_name'],
            'last_name': row['guardian_last_name'],
            'email': row['guardian_email'],
            'phone_number': row['guardian_phone'],
        }
        parents[parent['email']] = parent
    return parents

def import_users():
    users = {}

    teacher_rows = rows_for('../csv-files/teachers.csv')
    users.update(normalize_teachers(teacher_rows))

    student_rows = rows_for('../csv-files/students.csv')
    users.update(normalize_students(student_rows))

    parent_rows = rows_for('../csv-files/students.csv')
    users.update(normalize_parents(parent_rows))

    return users

expected_total = 1056
imported_users = import_users()

if len(imported_users) == expected_total:
    print("All users created! :D")
else:
    print(f"Expected {expected_total} users, {len(imported_users)} were created. :(")
