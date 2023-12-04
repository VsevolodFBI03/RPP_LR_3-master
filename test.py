import requests

# тест для region_route
data = {
    'id': 54,
    'name': 'Novosibirsk'
}

url = 'http://localhost:4567/v1/add/region'
response = requests.post(url, json=data)
print(response.status_code)

print(response.content)

data_1 = {
    'id': 54,
    'name': 'MSK'
}

url_1 = 'http://localhost:4567/v1/region/update'
response = requests.post(url_1, json=data_1)
print(response.status_code)

print(response.content)

data_2 = {
    'id': 54
}

#url_2 = 'http://localhost:4567/v1/region/delete'
#response = requests.post(url_2, json=data_2)
#print(response.status_code)

#print(response.content)

#data_3 = {
   #'id': 54
#}

url_3 = 'http://localhost:4567/v1/region/get/<id>'
response = requests.get(url_3, json=data_2)
print(response.status_code)

print(response.content)

url_4 = 'http://localhost:4567/v1/region/get/all'
response = requests.get(url_4)
print(response.status_code)

print(response.content)

# тест для car_route

data_5 = {
    'id': 11,
    'city_id': 54,
    'from_hp_car': 120,
    'to_hp_car': 500,
    'from_production_year_car': 2000,
    'to_production_year_car': 2023,
    'rate': 5000

}

url_5 = 'http://localhost:4567/v1/car/tax-param/add'
response = requests.post(url_5, json=data_5)
print(response.status_code)

print(response.content)

data_6 = {
    'id': 11,
    'city_id': 54,
    'from_hp_car': 70,
    'to_hp_car': 600,
    'from_production_year_car': 2002,
    'to_production_year_car': 2023,
    'rate': 5000

}

url_6 = 'http://localhost:4567/v1/car/tax-param/update'
response = requests.post(url_6, json=data_6)
print(response.status_code)

print(response.content)

data_7 = {
    'id': 11
}

# url_7 = 'http://localhost:4567/v1/car/delete'
# response = requests.post(url_7, json=data_7)
# print(response.status_code)
#
# print(response.content)

data_8 = {
    'id': 11
}

url_8 = 'http://localhost:4567/v1/car/tax-param/get/<id>'
response = requests.get(url_8, json=data_8)
print(response.status_code)

print(response.content)

url_9 = 'http://localhost:4567/v1/car/tax-param/get/all'
response = requests.get(url_9)
print(response.status_code)

print(response.content)

data_10 = {
    'id': 11,
    'hp': 200,
    'year': 2007
}

url_10 = 'http://localhost:4567/v1/car/tax/calc/<id>/<year>/<hp>'
response = requests.get(url_10, json=data_10)
print(response.status_code)

print(response.content)

# тест для area_route

data_11 = {
    'id': 11,
    'city_id': 54,
    'rate': 20
}

url_11 = 'http://localhost:4567/v1/area/tax-param/add'
response = requests.post(url_11, json=data_11)
print(response.status_code)

print(response.content)

data_12 = {
    'id': 11,
    'city_id': 57,
    'rate': 200
}

url_12 = 'http://localhost:4567/v1/area/tax-param/update'
response = requests.post(url_12, json=data_12)
print(response.status_code)

print(response.content)

data_13 = {
    'id': 11

}

url_13 = 'http://localhost:4567/v1/area/tax-param/delete'
response = requests.post(url_13, json=data_13)
print(response.status_code)

print(response.content)

data_14 = {
    'id': 11
}

url_14 = 'http://localhost:4567/v1/area/tax-param/get/<id>'
response = requests.get(url_14, json=data_14)
print(response.status_code)

print(response.content)

url_15 = 'http://localhost:4567/v1/area/tax-param/get/all'
response = requests.get(url_15)
print(response.status_code)

print(response.content)

data_16 = {
    'id': 11,
    'price': 1000
}

url_16 = 'http://localhost:4567//v1/area/tax/calc/<id>/<price>'
response = requests.get(url_16, json=data_16)
print(response.status_code)

print(response.content)