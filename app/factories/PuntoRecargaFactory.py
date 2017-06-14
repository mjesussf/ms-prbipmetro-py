from app.models.PuntoRecarga import PuntoRecarga
import simplejson as json2

dgc_mapping = {
    '_id': '_id',
    'CODIGO': 'codigo',
    'ENTIDAD': 'entidad',
    'NOMBRE FANTASIA': 'nombre_fantasia',
    'DIRECCION': 'direccion',
    'COMUNA': 'comuna',
    'HORARIO REFERENCIAL': 'horario_referencial',
    'ESTE': 'este',
    'NORTE': 'norte',
    'LONGITUD': 'longitud',
    'LATITUD': 'latitud',
}


def from_datos_gob_cl(_dict):
    pr = PuntoRecarga()
    for key, value in _dict.items():
        pr.doSth(name=dgc_mapping[key], value=value)
    return pr


def pr_list_from_datos_gob_cl(_records):
    prs = []
    for pr_dgc in _records:
        pr = from_datos_gob_cl(pr_dgc)
        if pr._id is not None:
            prs.append(pr)
    return prs


def as_pr_list_as_json(_list):
    return json2.dumps([p.__dict__['_data'] for p in _list])
