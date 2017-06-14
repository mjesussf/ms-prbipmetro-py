import requests
import json
import os
service_endpoint = os.environ.get('WS_ENDPOINT')
service_start = os.environ.get('WS_START')


def request_prpibmetro_data(url):
    data = requests.get(url)
    return json.loads(data.content)


def get_prpibmetro():
    requested_data = []
    d = request_prpibmetro_data(service_endpoint + service_start)
    total_to_request = d['result']['total']
    while len(requested_data) < total_to_request:
        if d['success'] is False:
            break
        requested_data.extend(d['result']['records'])
        service_next = d['result']['_links']['next']
        d = request_prpibmetro_data(service_endpoint + service_next)
    return requested_data

