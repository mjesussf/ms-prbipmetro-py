from app import create_app
# from flask_mongoalchemy import MongoAlchemy
from flask import Response, request
import simplejson as json2
from app.factories.PuntoRecargaFactory import pr_list_from_datos_gob_cl, as_pr_list_as_json
from app.models.PuntoRecarga import PuntoRecarga
from app.models.Coordinate import Coordinate
from app.web_services.DatosGobClWebService import get_prpibmetro
from pymodm import *
from pymongo.errors import *
from app.services.GeoServices import get_coordinates_on_range
import os
connect(os.environ.get('MONGODB_URI'))
application = create_app()


@application.route('/')
def hello_world():
    return 'Hello world.'


@application.route('/refresh_data')
def refresh_data():
    # user = mongo.db.test.find_one_or_404({'p': 1})
    # print(user)
    # return JSONEncoder().encode(user)
    pr_list = pr_list_from_datos_gob_cl(get_prpibmetro())
    try:
        pr_ids = PuntoRecarga.objects.bulk_create(pr_list)
        json_list = as_pr_list_as_json(pr_list)
        r = Response(response=json_list, status=200, mimetype="application/json")
        r.headers["Content-Type"] = "application/json; charset=utf-8"
        return r
    except BulkWriteError as bwe:
        return bwe.__dict__['_OperationFailure__details']['writeErrors'][0]['errmsg']


@application.route('/get_all_lat_lng')
def get_all():
    pr_list = PuntoRecarga.objects.raw({})
    pr_list = pr_list.only('longitud', 'latitud')
    json_list = as_pr_list_as_json(pr_list)
    r = Response(response=json_list, status=200, mimetype="application/json")
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


@application.route('/get_in_range')
def get_in_range():
    radius = float(request.args.get('radius'))
    given_coordinates = Coordinate()
    given_coordinates.latitud = float(request.args.get('lat'))
    given_coordinates.longitud = float(request.args.get('lng'))
    pr_list = PuntoRecarga.objects.raw({})
    nl = get_coordinates_on_range(radius, given_coordinates, pr_list)
    json_list = as_pr_list_as_json(nl)
    r = Response(response=json_list, status=200, mimetype="application/json")
    r.headers["Content-Type"] = "application/json; charset=utf-8"
    return r


def app(environ, start_response):
    port = int(os.environ.get('PORT', 9000))
    application.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    app(None, None)



