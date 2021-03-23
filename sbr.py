from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sbr_july_2020 import sbr_july_2020 as schema
from aenum import Enum, NamedTuple, Constant
from typing import List, Set, Dict, Tuple, Optional
from sbrodds_service import sbrodds_service as sbrodds_service_schema


class League(object):

    def __init__(self, lid, nam, spid):
        self.lid = lid
        self.nam = nam
        self.spid = spid

    def __repr__(self):
        return {"lid": self.lid, "nam": self.nam, "spid": self.spid}

    def __str__(self):
        return self.nam


class SBRClient(object):

    def __init__(self, endpoint="https://www.sportsbookreview.com/ms-odds-v2/odds-v2-service"):
        """
        Alternative endpoint access:
        https://www.oddstrader.com/odds-v2/odds-v2-service
        https://www.oddsmarket.com/oddsv2-ombmr/odds-v2-service
        :param endpoint:
        :type endpoint:
        """
        self.op = Operation(schema.Query)
        self.sitid = 4
        self.did = 0
        self.endpoint = HTTPEndpoint(endpoint)




