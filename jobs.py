import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = orm.relation('User', back_populates='job')
    start_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DATE, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)