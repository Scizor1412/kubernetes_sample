# write a python program which takes students and their enrolled subjects in JSON and produce an output which is a list of tuple pairs of students who have enrolled in the same course
 
input = {
    'paulo': ['maths', 'chemistry', 'biology'],
    'nurdin': ['maths', 'history'],
    'victor': ['chemistry', 'physics'],
    'skyler': ['chemistry', 'history']
}

[('paulo', 'nurdin'), ('paulo', 'victor'), ('paulo', 'skyler'),
                  ('victor', 'skyler'), ('skyler', 'nurdin')]


subject_list = {}

for student, subjects in input.items():
    for subject in subjects:
        if subject not in subject_list:
            subject_list[subject] = []
        subject_list[subject].append(student)

print(subject_list)

for subject in subject_list:
    if len(subject_list[subject]) > 1:
        for i in range(len(subject_list[subject])):
            for j in range(i + 1, len(subject_list[subject])):
                print((subject_list[subject][i], subject_list[subject][j]))