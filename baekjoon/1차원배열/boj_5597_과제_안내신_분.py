# import sys

# student_ids = [i + 1 for i in range(30)]

# submitted_students = [int(sys.stdin.readline()) for _ in range(28)]

# for student in student_ids:
#     if student not in submitted_students:
#         print(student)

import sys
submitted_students = [int(sys.stdin.readline()) for _ in range(28)]
missing = sorted(set(range(1, 31)) - set(submitted_students))
for student in missing:
    print(student)

