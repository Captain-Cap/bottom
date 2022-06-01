import json
from flask import Flask, request


app = Flask(__name__)


baloons = {
    1: {'id': 1, 'Firm': 'Maker Street', 'paint_code': 'ms400-504', 'color': 'grey-blue', 'volume': 400, 'starting_weight': 300},
    2: {'id': 2, 'Firm': 'Maker Street', 'paint_code': 'ms400-101', 'color': 'yellow', 'volume': 400, 'starting_weight': 300},
}
        

@app.get('/api/v1/baloons/')
def get_baloons():
    return json.dumps(baloons)


@app.get('/api/v1/baloons/<int:id>')
def get_baloon_by_id(id):
    baloon = baloons.get(id)
    if not baloon:
        raise IndexError("id does not exist")
    return baloon


@app.post('/api/v1/baloons/')
def add_baloons():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if baloon:
        raise ValueError('such id already exists')
    baloons[id_payload] = payload


@app.delete('/api/v1/baloons/<int:id>')
def del_baloon(id):
    baloon = baloons.get(id)
    if baloon:
        del baloons[id]
    else:
        raise IndexError("id does not exist")


@app.put('/api/v1/baloons/')
def changed_balloon():
    payload = request.json
    id_payload = payload['id']
    baloon = baloons.get(id_payload)
    if baloon:
        baloons[id_payload] = payload
    else:
        raise IndexError('id does not exist')


if __name__ == "__main__":
    app.run(debug=True)