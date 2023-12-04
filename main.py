from routes.region_route import region
from routes.car_route import car
from routes.area_route import area
from Config import app
import argparse

parser = argparse.ArgumentParser

# регистрируем приложения
app.register_blueprint(region)
app.register_blueprint(car)
app.register_blueprint(area)

if __name__ == '__main__':
    # parser.add_argument('-c', '--create', action='create_database')
    app.run(debug=True, host='0.0.0.0', port='4567')
