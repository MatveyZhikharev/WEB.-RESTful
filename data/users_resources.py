from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash

from data import db_session
from data.users import User
from data.reqparse_users import parser


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


def set_password(password):
    return generate_password_hash(password)


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify(
            {
                "users": users.to_dict(
                    only=(
                        "id",
                        "surname",
                        "age",
                        "email",
                        "position",
                        "speciality",
                        "address",
                        "hashed_password",
                        "modifed_date",
                    )
                )
            }
        )

    def post(self, user_id):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        session.commit()
        return jsonify({"success": "OK"})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                "users": [
                    item.to_dict(
                        only=(
                            "id",
                            "surname",
                            "age",
                            "email",
                            "position",
                            "speciality",
                            "address",
                            "email",
                            "hashed_password",
                            "modifed_date",
                        )
                    )
                    for item in users
                ]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=args["id"],
            surname=args["surname"],
            age=args["age"],
            address=args["address"],
            email=args["email"],
            position=args["position"],
            speciality=args["speciality"],
            hashed_password=set_password(args["hashed_password"]),
        )
        session.add(users)
        session.commit()
        return jsonify({"success": "OK"})
