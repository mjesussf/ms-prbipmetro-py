from pymodm import MongoModel, fields


class PuntoRecarga(MongoModel):
    _id = fields.IntegerField(primary_key=True)
    codigo = fields.CharField()
    entidad = fields.CharField()
    nombre_fantasia = fields.CharField()
    direccion = fields.CharField()
    comuna = fields.CharField()
    horario_referencial = fields.CharField()
    este = fields.FloatField()
    norte = fields.FloatField()
    longitud = fields.FloatField()
    latitud = fields.FloatField()

    def doSth(self, name, value):
        setattr(self, name, value)

    def __str__(self):
        return '<' +PuntoRecarga.__name__ +'>:'+ str(self._id)




