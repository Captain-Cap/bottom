from flask import request, abort, Blueprint
from cap.storage import BalloonsStorage


routes = Blueprint("balloons", __name__)
storage = BalloonsStorage()


@routes.get('/')
def get_balloons():
    return storage.get_all()


@routes.get('/<int:id>')
def get_balloon_by_id(id):
    try:
        return storage.get_balloon_by_id(id)
    except ValueError:
        abort(404, "balloon not found")


@routes.post('/')
def add_balloon():
    try:
        storage.add(request.json)
        return request.json
    except ValueError:
        abort(409, "such id already exists")


@routes.delete('/<int:id>')
def del_balloon(id):
    try:
        storage.delete(id)
        return {}, 204
    except KeyError:
        abort(404, "balloon not found")


@routes.put('/')
def change_balloon():
    try:
        storage.update(request.json)
        return request.json
    except ValueError:
        abort(404, "id does not exist")