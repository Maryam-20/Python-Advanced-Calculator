Questions= {
    'Q1.' : 'Adrenal gland is divided into how many part?',
    'Q2.' : 'Oxytocin is secreted from which gland?',
    'Q3.' : 'Endocrine glands are also known as?',
    'Q4.' : 'What convert angiotensin i to angiotensin ii? ',
    'Q5.' : 'Hormone secreted from the pineal gland is?'
}

Answers = [
    ['a) 3', 'b) 2','c) 4'],
    ['a) adrenal gland', 'b) pineal gland', 'c) pituitary gland'],
    ['a) paracrine gland', 'b) autocrine gland', 'c) ductless gland'],
    ['a) renin', 'b) aldosterone', 'c) angiotensin converting enzyme'],
    ['a) serotonin', 'b) melatonin', 'c) histamine']
]

correct_ans = ['b', 'c', 'c', 'c', 'b']



x = int(input('How many student are taking this test: ')) + 1
print("All student should register their details correctly")
num_std = range(1, x)
student_info = {}
for student in num_std:
    print('Each student should register their details')
    print('Input Your Inormation student',student)
    name = input('FULL NAME >')
    level = input('LEVEL >')
    dept = input('DEPARTMENT >')
    details = {'name': name, 'level': level, 'dept': dept}
    student_info[name] = details


students_score = []
students_score_name = {}
for student in student_info:
    num = 0
    score = 0
    print('ATTEMPT ALL QUESTIONS STUDENT', student)
    for ques_no, ques in Questions.items():
        print(ques_no, ques)
        print(Answers[num])
        user = input("your answer ")
        if user ==  correct_ans[num]:
             score += 5
        num +=1
    students_score.append(score)
    students_score_name[student] = score
highest_score = max(students_score)
highest_score_stdName = max(students_score_name, key=students_score_name.get)
print("The winner of this quiz is " + str(highest_score_stdName) + " with the highest score of " + str(highest_score))
