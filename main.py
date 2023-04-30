from flask import Flask
from data import db_session, users_resources
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/mars_explorer.sqlite")

    # для списка объектов
    api.add_resource(users_resources.UsersListResource, "/api/v2/users")

    # для одного объекта
    api.add_resource(users_resources.UsersResource, "/api/v2/users/<int:user_id>")

    app.run()


if __name__ == "__main__":
    main()
