% Facts
student(1, 'Alice').
student(2, 'Bob').
student(3, 'Carol').

teacher(1, 'Dr. Smith').
teacher(2, 'Prof. Johnson').

subject('CS101', 'Intro to CS').
subject('MATH202', 'Calculus II').
subject('HIST303', 'World History').

enrollment(1, 'CS101', 1).
enrollment(2, 'MATH202', 2).
enrollment(3, 'HIST303', 1).
enrollment(1, 'MATH202', 2).

% Find subjects for a student
find_subjects_for_student(StudentName, SubjectName) :-
    student(StudentID, StudentName),
    enrollment(StudentID, SubjectCode, _),
    subject(SubjectCode, SubjectName).

% Find teacher for a subject
find_teacher_for_subject(SubjectName, TeacherName) :-
    subject(SubjectCode, SubjectName),
    enrollment(_, SubjectCode, TeacherID),
    teacher(TeacherID, TeacherName).

% Find students for a subject
find_students_for_subject(SubjectName, StudentName) :-
    subject(SubjectCode, SubjectName),
    enrollment(StudentID, SubjectCode, _),
    student(StudentID, StudentName).

% Find subjects taught by a teacher
find_subjects_for_teacher(TeacherName, SubjectName) :-
    teacher(TeacherID, TeacherName),
    enrollment(_, SubjectCode, TeacherID),
    subject(SubjectCode, SubjectName).
