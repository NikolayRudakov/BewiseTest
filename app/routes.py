# ./app/routes.py
from flask import jsonify, request
import json

from ask import get_one_quest
from models import db, Jserv


def init_routes(app):
    @app.route("/api", methods=["POST"])
    def get_api_base_url():
        q_num_arg = request.args.get("questions_num")
        if q_num_arg is None:
            request_data = request.get_json()
            q_num = request_data["questions_num"]
            if q_num is None:
                return "Требуется обязательный целочисленный JSON questions_num.", 422
        else:
            if not q_num_arg.isnumeric():
                return (
                    "Требуется обязательный целочисленный параметр questions_num.",
                    422,
                )
            q_num = int(q_num_arg)
        if q_num < 1:
            return "Требуется количество запросов больше нуля.", 422

        if Jserv.query.first() is not None:
            # Ответом на запрос из должен быть предыдущей сохранённый вопрос для викторины.
            replay = Jserv.query.order_by(Jserv.id.desc()).first()
        else:
            #  В случае его отсутствия - пустой объект.
            replay = {}

        while q_num > 0:
            dmg = get_one_quest()[0]
            if Jserv.query.filter_by(id_ext=dmg["id"]).first() is not None:
                q_num += 1
            else:
                jserv = Jserv(
                    id_ext=dmg["id"],
                    question_text=dmg["question"],
                    answer=dmg["answer"],
                    timestamp=dmg["created_at"],
                )
                db.session.add(jserv)
                db.session.commit()
            q_num -= 1

        return json.dumps(replay.to_dict()), 201
