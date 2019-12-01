from sgqlc.operation import Operation
from sbrschema import sbrschema as schema
from sgqlc.endpoint.http import HTTPEndpoint
import time
import json

sitid = 4
domid = 0

def json_pretty_print(d, file=None):
    args = {'sort_keys': True, 'indent': 2, 'separators': (',', ': ')}
    if file:
        return json.dump(d, file, **args)
    return json.dumps(d, **args)



def query_sbr(query, variables=None):
    url = 'https://www.sportsbookreview.com/ms-odds-v2/odds-v2-service'
    endpoint = HTTPEndpoint(url)
    return endpoint(query, variables)


op = Operation(schema.Query)

class SBRQuery(object):

    def __init__(self):
        self.op = Operation(schema.Query)

    @staticmethod
    def query(query, variables=None):
        url = 'https://www.sportsbookreview.com/ms-odds-v2/odds-v2-service'
        endpoint = HTTPEndpoint(url)
        return endpoint(query, variables)

    @staticmethod
    def json_pretty_print(d, file=None):
        args = {'sort_keys': True, 'indent': 2, 'separators': (',', ': ')}
        if file:
            return json.dump(d, file, **args)
        return json.dumps(d, **args)

    




