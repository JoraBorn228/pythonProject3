import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Music(SqlAlchemyBase):
    __tablename__ = 'music'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    playlist = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    number_of_files = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    executor = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user = orm.relation('User')

    def __repr__(self):
        return f'<Плейлист> {self.playlist}'
