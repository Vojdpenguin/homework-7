import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import Session
from models import Student, Teacher, Subject, Group, Grade, AlembicVersion

fake = Faker()

def seed_data(session: Session):
    # Додаємо групи
    group_names = [121, 122, 123]  # Це список груп

    # Створюємо об'єкти Group для кожної групи
    groups = [Group(group_name=name) for name in group_names]

    # Додаємо всі групи в сесію
    session.add_all(groups)

    # Коміт для збереження змін
    session.commit()

    # Додаємо викладачів
    teachers = [Teacher(teacher_name=fake.name()) for _ in range(3)]
    session.add_all(teachers)
    session.commit()

    # Додаємо предмети (українською)
    subjects = [
        Subject(subject_name="Математика", teacher_id=random.choice(teachers).id),
        Subject(subject_name="Фізика", teacher_id=random.choice(teachers).id),
        Subject(subject_name="Хімія", teacher_id=random.choice(teachers).id),
        Subject(subject_name="Біологія", teacher_id=random.choice(teachers).id),
        Subject(subject_name="Історія", teacher_id=random.choice(teachers).id)
    ]
    session.add_all(subjects)
    session.commit()

    # Додаємо студентів
    students = [
        Student(student_name=fake.name(), group_id=random.choice(groups).id) for _ in range(30)
    ]
    session.add_all(students)
    session.commit()

    # Додаємо оцінки
    for student in students:
        for subject in subjects:
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=random.randint(1, 12),  # Оцінка від 1 до 12
                date_of=datetime.now() - timedelta(days=random.randint(1, 30))  # Випадкова дата
            )
            session.add(grade)
    session.commit()

    # Додаємо версію Alembic
    alembic_version = AlembicVersion(version_num='1234567890abcdef')  # Замініть на вашу версію
    session.add(alembic_version)
    session.commit()
