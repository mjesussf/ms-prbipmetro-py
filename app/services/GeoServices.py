from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r


def is_on_range(radius, position1, position2):
    a = haversine(position1.longitud, position1.latitud, position2.longitud, position2.latitud)
    return a <= radius


def get_coordinates_on_range(radius, given_coordinates, coordinates):
    on_range = []
    for coordinate in coordinates:
        if is_on_range(radius, given_coordinates, coordinate):
            on_range.append(coordinate)
    return on_range
