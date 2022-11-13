from . import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.LargeBinary(100), nullable=False)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String)
    birthday = db.Column(db.String, nullable=False)
    study = db.Column(db.String, nullable=False)
    faculty = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    """
    teachers = relationship('Teacher',
                            cascade='all,delete',
                            back_populates='subjects')
    timetables = relationship('TimeTable',
                              cascade='all,delete',
                              back_populates='subjects')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    subject = Column(String, ForeignKey('subjects.name'), nullable=False)
    subjects = relationship('Subject',
                            cascade='all,delete',
                            back_populates='teachers')


class TimeTable(Base):
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)
    week = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    subject = Column(String, ForeignKey('subjects.name'), nullable=False)
    room = Column(String, nullable=True)
    start_time = Column(Integer, nullable=False)
    subjects = relationship('Subject', back_populates='timetables')

    def __str__(self):
        t = str(self.start_time)
        if len(t) < 4:
            t = f"0{t[0]}:{t[1:]}"
        else:
            t = f"{t[:2]}:{t[2:]}"
        return f"{self.subject} {self.room} {t} "


def get_schedule_for_week(week_id):
    data = session.query(
        TimeTable, Teacher.full_name).filter(TimeTable.week == week_id).join(
            TimeTable.subjects).join(Subject.teachers).order_by(
                TimeTable.day).order_by(TimeTable.start_time).all()
    answer = [[] for i in range(5)]
    for lesson, teacher_name in data:
        answer[lesson.day].append(str(lesson) + teacher_name)
    return answer


def get_schedule_for_day(week_id, day_id):
    data = session.query(TimeTable, Teacher.full_name).filter(
        TimeTable.week == week_id).filter(TimeTable.day == day_id).join(
            TimeTable.subjects).join(Subject.teachers).order_by(
                TimeTable.day).order_by(TimeTable.start_time).all()
    return [str(lesson) + teacher_name for lesson, teacher_name in data]"""
