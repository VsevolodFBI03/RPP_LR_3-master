from flask import Blueprint, request
from Config import db, Region, CarTaxParam

car = Blueprint('car', __name__)


#  endpoint для внесения данных по налогу
@car.route('/v1/car/tax-param/add', methods=['POST'])
def add():
    data_5 = request.get_json()
    id = request.json['id']
    city_id = request.json['city_id']
    from_hp_car = request.json['from_hp_car']
    to_hp_car = request.json['to_hp_car']
    from_production_year_car = request.json['from_production_year_car']
    to_production_year_car = request.json['to_production_year_car']
    rate = request.json['rate']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if city_id not in regions:
        return {'reason': 'No such id or rate...'}, 400
    else:
        new_data = CarTaxParam(id, city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car,
                               rate)
        db.session.add(new_data)
        db.session.commit()
        return {'reason': 'Tax added'}, 200


#  endpoint для обновления данных по автоналогу
@car.route('/v1/car/tax-param/update', methods=['POST'])
def update():
    data_6 = request.get_json()
    id = request.json['id']
    city_id = request.json['city_id']
    from_hp_car = request.json['from_hp_car']
    to_hp_car = request.json['to_hp_car']
    from_production_year_car = request.json['from_production_year_car']
    to_production_year_car = request.json['to_production_year_car']
    rate = request.json['rate']
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if city_id not in regions:
        return {'reason': 'No such id or rate...'}, 400
    else:
        new_data = CarTaxParam.query.filter_by(id=id).update(
            {'city_id': city_id, 'from_hp_car': from_hp_car, 'to_hp_car': to_hp_car,
             'from_production_year_car': from_production_year_car, 'to_production_year_car': to_production_year_car,
             'rate': rate})
        db.session.commit()
        return {'message': 'Updated'}, 200


#  endpoint для удаления данных по автоналогу
@car.route('/v1/car/delete', methods=['POST'])
def delete():
    data_7 = request.get_json()
    id = request.json['id']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))

    if id in car:

        new_data1 = CarTaxParam.query.filter_by(id=id).delete()
        db.session.commit()
        return {'message': 'Tax deleted'}, 200
    else:
        return {'ERROR': 'No such id'}, 400


#  endpoint для получения данных по автоналогу
@car.route('/v1/car/tax-param/get/<id>')
def fetch(id):
    data_8 = request.get_json()
    id = request.json['id']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))
    if id in car:
        car_tax = list(map(lambda x: x.__repr__(), CarTaxParam.query.filter_by(id=id, ).all()))
        return car_tax, 200
    else:
        return {'reason': 'Incorrect data'}, 400


@car.route('/v1/car/tax-param/get/all')
def fetch_all():
    if id is None:
        return {'ERROR': 'Incorrect data'}, 400
    tax_auto = list(map(lambda x: x.__repr__(), CarTaxParam.query.all()))
    return tax_auto, 200


#  endpoint для подсчёта налога
@car.route('/v1/car/tax/calc/<id>/<year>/<hp>')
def calc(id, year, hp):
    data_10 = request.get_json
    id = request.json['id']
    hp = request.json['hp']
    year = request.json['year']
    rate = list(map(lambda x: x.get_data_for_rate(), CarTaxParam.query.filter_by(id=id).all()))

    if rate is None:
        return {'ERROR': 'No tax'}, 400
    else:
        for i in rate:
            if int(i[2]) < int(hp) <= int(i[3]) and int(i[4]) < int(year) <= int(i[5]):
                res = int(i[6]) * int(hp)
                message = {'result': res}
                return message, 200
            else:
                return {'ERROR': 'No tax'}, 400
