from flask import Blueprint, request
from Config import db, Region, CarTaxParam, AreaTaxParam

area = Blueprint('area', __name__)


#  endpoint для внесения данных по земельному налогу
@area.route('/v1/area/tax-param/add', methods=['POST'])
def add():
    data_11 = request.get_json
    id = request.json['id']
    city_id = request.json['city_id']
    rate = request.json['rate']
    areas = list(map(lambda x: x.get_id(), AreaTaxParam.query.all()))
    if id in areas:
        return {'ERROR': 'Area tax id exists'}, 400
    else:
        new_data = AreaTaxParam(id, city_id, rate)
        db.session.add(new_data)
        db.session.commit()
        return {'message': 'Tax added'}, 200


#  endpoint для обновления данных по земельному налогу
@area.route('/v1/area/tax-param/update', methods=['POST'])
def update():
    data_12 = request.get_json
    id = request.json['id']
    city_id = request.json['city_id']
    rate = request.json['rate']
    areas = list(map(lambda x: x.get_id(), AreaTaxParam.query.all()))

    if id in areas:

        new_data = AreaTaxParam.query.filter_by(id=id).update({'city_id': city_id, 'rate': rate})
        db.session.commit()
        return {'message': 'Updated'}, 200
    else:
        return {'ERROR': 'No such id'}, 400


#  endpoint для удаления данных по земельному налогу
@area.route('/v1/area/tax-param/delete', methods=['POST'])
def delete():
    data_13 = request.get_json
    id = request.json['id']
    areas = list(map(lambda x: x.get_id(), AreaTaxParam.query.all()))
    if id in areas:
        new_data1 = AreaTaxParam.query.filter_by(id=id).delete()
        db.session.commit()
        return {'message': 'Deleted'}, 200
    else:
        return {'ERROR': 'Земельный налог с таким id не существует'}, 400


#  endpoint для выведения данных по земельному налогу
@area.route('/v1/area/tax-param/get/<id>')
def fetch(id):
    data_14 = request.get_json
    id = request.json['id']
    if id is None:
        return {'ERROR': 'Incorrect data'}, 400

    tax = list(map(lambda x: x.__repr__(), AreaTaxParam.query.filter_by(id=id).all()))
    return tax, 200


@area.route('/v1/area/tax-param/get/all')
def fetch_all():
    data_15 = request.get_json
    tax = list(map(lambda x: x.__repr__(), AreaTaxParam.query.all()))
    return tax, 200


#  endpoint для подсчёта налога
@area.route('/v1/area/tax/calc/<id>/<price>')
def calc(id, price):
    data_16 = request.get_json
    id = request.json['id']
    price = request.json['price']
    if id is None or price is None:
        return {'ERROR': 'Incorrect data'}, 400

    rate = list(map(lambda x: x.get_data_for_rate(), AreaTaxParam.query.filter_by(id=id).all()))

    if rate is None:
        return {'ERROR': 'No tax'}, 400
    else:
        rate = int(rate[0])
        res = int(rate) * int(price)
        message = {'result': res}
        return message, 200
