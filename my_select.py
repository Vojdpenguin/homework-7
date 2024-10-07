from sqlalchemy import func, desc
from models import Student, Grade, Group, Subject, Teacher  # імпортуємо класи з файлу моделей
from db_config import Session
# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1(session):
    return session.query(
        Student.student_name, func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(session, subject_id):
    return session.query(
        Student.student_name, func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).first()

# 3. Знайти середній бал у групах з певного предмета
def select_3(session, subject_id):
    return session.query(
        Group.group_name, func.avg(Grade.grade).label('avg_grade')
    ).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()

# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4(session):
    return session.query(func.avg(Grade.grade)).scalar()

# 5. Знайти які курси читає певний викладач
def select_5(session, teacher_id):
    return session.query(Subject.subject_name).filter(Subject.teacher_id == teacher_id).all()

# 6. Знайти список студентів у певній групі
def select_6(session, group_id):
    return session.query(Student.student_name).filter(Student.group_id == group_id).all()

# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(session, group_id, subject_id):
    return session.query(
        Student.student_name, Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(session, teacher_id):
    return session.query(
        func.avg(Grade.grade).label('avg_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).all()

# 9. Знайти список курсів, які відвідує певний студент
def select_9(session, student_id):
    return session.query(Subject.subject_name).join(Grade).filter(Grade.student_id == student_id).all()

# 10. Список курсів, які певному студенту читає певний викладач
def select_10(session, student_id, teacher_id):
    return session.query(
        Subject.subject_name
    ).join(Grade).join(Subject).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()
