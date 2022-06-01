import json
from flask import Flask, request, abort
from flask import Blueprint
from cap.storage import BaloonsStorage


routes = Blueprint("balloons", __name__)
storage = BaloonsStorage()


@routes.get('/')
def get_baloons():
    storage.get_all()


@routes.get('/<int:id>')
def get_baloon_by_id(id):
    try:
        return storage.get_balloon_by_id(id)
    except ValueError:
        abort(404, "balloon not found")


@routes.post('/')
def add_baloons():
    try:
        return storage.add(request.json)
    except ValueError:
        abort(409, "such id already exists")


@routes.delete('/<int:id>')
def del_baloon(id):
    try:
        return storage.delete(id), 204
    except KeyError:
        abort(404, "balloon not found")


@routes.put('/')
def change_balloon():
    try:
        return storage.update(request.json)
    except ValueError:
        abort(404, "id does not exist")
