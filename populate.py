import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','simplesocial.settings')

import django
django.setup()

from feedbacks import models

# DEPARTMENTS
csedept = models.Department.objects.get(department_id='CSE')
ecedept = models.Department.objects.get(department_id='ECE')
icedept = models.Department.objects.get(department_id='ICE')
itdept = models.Department.objects.get(department_id='IT')
eeedept = models.Department.objects.get(department_id='EEE')

# SEMESTERS
sem1 = models.Semester.objects.get(semester_number=1)
sem2 = models.Semester.objects.get(semester_number=2)
sem3 = models.Semester.objects.get(semester_number=3)
sem4 = models.Semester.objects.get(semester_number=4)
sem5 = models.Semester.objects.get(semester_number=5)
sem6 = models.Semester.objects.get(semester_number=6)
sem7 = models.Semester.objects.get(semester_number=7)
sem8 = models.Semester.objects.get(semester_number=8)


# IT
subject_name_3_IT = ['Applied Mathematics – III', 'Foundation of Computer Science',
              'Switching Theory and Logic Design', 'Circuits and Systems', 'Data Structure', 'Computer Graphics and Multimedia']
subject_name_5_IT = ['Algorithms Design and Analysis', 'Software Engineering',
              'Java Programming', 'Industrial Management', 'Communication Systems', 'Communication Skills for Professionals']
subject_name_7_IT = ['Advanced Computer Networks', 'Cryptography and Network Security',
              'Wireless Communication', 'Software Testing', 'Advanced Database Administration']

subject_code_3_IT = ['AMIII', 'FCS', 'STLD', 'CnS', 'DS', 'CGMM']
subject_code_5_IT = ['ADA', 'SE', 'JAVA', 'IM', 'CS', 'CSP']
subject_code_7_IT = ['ACN', 'CNS', 'WC', 'ST', 'ADBA']

teacher_name_IT = ['Sarita Yadav', 'Rajeev Nehra', 'Gopal Chaudhary', 'Bharat Singh', 'Kusum Tharani', 'Neeraj Kumar', 'Arvind Rehalia',
                    'Surinder Kaur', 'Parul Yadav', 'Arun Dubey', 'Alka Leekha', 'Puneet Singh Lamba', 'Neha Gupta', 'Shikha Rastogi',
                    'Shafali Dhall', 'Achin Jain', 'Taranpreet Kaur', 'Rachna Tewani', 'Deepak', 'Rubeena', 'Ashish Joshi', 'Pooja Saxena']

teacher_id_IT = ['SY', 'RN', 'GC', 'BS', 'KT', 'NK', 'AR', 'SK', 'PY', 'AD', 'AL', 'PSL', 'NG', 'SR', 'SD', 'ACJ',
                'TK', 'RT', 'DG', 'RB', 'ASJ', 'PS']


# POPULATE IT
def populate():
# ADD IT TEACHERS
    for i in range(len(teacher_name_IT)):
        teacher = models.Teacher.objects.get_or_create(teacher_id = teacher_id_IT[i],
                                          teacher_name = teacher_name_IT[i])[0]
        teacher.department.add(itdept)

# ADD 3rd SEMESTER IT SUBJECTS
    for i in range(len(subject_name_3_IT)):
        subject = models.Subject.objects.get_or_create(subject_code = subject_code_3_IT[i],
                                          subject_name = subject_name_3_IT[i])[0]
        subject.semester.add(sem3)
        subject.department.add(itdept)

# ADD 5th SEMESTER IT SUBJECTS
    for i in range(len(subject_name_5_IT)):
        subject = models.Subject.objects.get_or_create(subject_code = subject_code_5_IT[i],
                                          subject_name = subject_name_5_IT[i])[0]
        subject.semester.add(sem5)
        subject.department.add(itdept)

# ADD 7th SEMESTER IT SUBJECTS
    for i in range(len(subject_name_7_IT)):
        subject = models.Subject.objects.get_or_create(subject_code = subject_code_7_IT[i],
                                          subject_name = subject_name_7_IT[i])[0]
        subject.semester.add(sem7)
        subject.department.add(itdept)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')
