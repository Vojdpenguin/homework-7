from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date

# Base class for declarative class definitions
Base = declarative_base()

# Таблиця студентів
class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete='SET NULL', onupdate='CASCADE'),
                                          nullable=True)

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

# Таблиця груп
class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_name: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)

    students = relationship("Student", back_populates="group")

# Таблиця викладачів
class Teacher(Base):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    subjects = relationship("Subject", back_populates="teacher")

# Таблиця предметів
class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id', ondelete='SET NULL', onupdate='CASCADE'),
                                            nullable=True)

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

# Таблиця оцінок студентів
class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'),
                                            nullable=False)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'),
                                            nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    date_of: Mapped[Date] = mapped_column(Date, nullable=False)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

# Таблиця версій бази даних для Alembic
class AlembicVersion(Base):
    __tablename__ = 'alembic_version'
    version_num = mapped_column(String(32), primary_key=True)
