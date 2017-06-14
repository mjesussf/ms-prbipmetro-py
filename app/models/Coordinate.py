from pymodm import MongoModel, fields


class Coordinate(MongoModel):
    longitud = fields.FloatField()
    latitud = fields.FloatField()

