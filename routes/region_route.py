from flask import Blueprint, request
from Config import db, Region, CarTaxParam, AreaTaxParam

region = Blueprint('region', __name__)


@region.route('/v1/add/region', methods=['POST'])
def add_region():
    data = request.get_json()
    id = request.json['id']
    name = request.json['name']
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if id in regions:
        return {'ERROR': 'Such region exists'}, 400
    else:
        new_region = Region(id, name)
        db.session.add(new_region)
        db.session.commit()
    return {'message': 'OK'}, 200


@region.route('/v1/region/update', methods=['POST'])
def region_udate():
    data_1 = request.get_json()
    id = request.json['id']
    name = request.json['name']
    region = list(map(lambda x: x.get_id(), Region.query.all()))
    if id in region:
        new_data = Region.query.filter_by(id=id).update({'name': name})
        db.session.commit()
        return {'message': 'Region updated'}, 200
    else:
        return {'ERROR': 'No region with such id'}, 400


@region.route('/v1/region/delete', methods=['POST'])
def region_delete():
    data_2 = request.get_json()
    id = request.json['id']
    region = list(map(lambda x: x.get_id(), Region.query.all()))
    if id in region:
        new_data = Region.query.filter_by(id=id).delete()
        new_data = CarTaxParam.query.filter_by(city_id=id).delete()
        new_data = AreaTaxParam.query.filter_by(city_id=id).delete()
        db.session.commit()
        return {'message': 'Data sucsessfully deleted'}, 200
    else:
        return {'ERROR': 'No region with such id'}, 400


@region.route('/v1/region/get/<id>')
def fetch_region(id):
    data_3 = request.get_json()
    id = request.json['id']
    region = list(map(lambda x: x.get_id(), Region.query.all()))
    if id in region:
        region = list(map(lambda x: x.__repr__(), Region.query.filter_by(id=id).all()))
        return region, 200
    else:
        return {'ERROR': 'No region with such id'}, 400



@region.route('/v1/region/get/all')
def fetch_all():
    if id is None:
        return {'reason': 'Не корректные данные'}, 400
    region = list(map(lambda x: x.__repr__(), Region.query.all()))
    return region, 200
