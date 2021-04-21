from flask import Blueprint


books_blueprint= Blueprint("tasks", __name__)


@books_blueprint.route('/book')
def book():
    pass

