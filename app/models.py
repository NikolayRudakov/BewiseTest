# ./app/models.py
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Jserv(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_ext = db.Column(db.Integer, nullable=False, unique=True, index=True)
    question_text = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, index=True)

    def to_dict(self):
        return dict(
            id=self.id,
            id_ext=self.id_ext,
            question_tex=self.question_text,
            answer=self.answer,
            timestamp=self.timestamp.strftime("%d.%m.%Y %H:%M:%S"),
        )
