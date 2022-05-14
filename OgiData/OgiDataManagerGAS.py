
import json
import requests


class OgiDataManagerGAS:
    def __init__(self, gas_url):
        self.gas_url = gas_url
        return

    def insertData(self, table, data):
        url = self.gas_url
        params = {
            'table': table,
            'data': json.dumps([data])
        }
        response = requests.post(url, params)
        ret = response.json()
        return ret

    def insertDatas(self, table, datas):
        url = self.gas_url
        params = {
            'table': table,
            'data': json.dumps(datas)
        }
        response = requests.post(url, params)
        ret = response.json()
        return ret

    def getData(self, table, start_index=None, limit=None, asc=None):
        url = self.gas_url
        params = {
            'table': table
        }
        if start_index != None:
            params['start_index'] = start_index
        if limit != None:
            params['limit'] = limit
        if asc != None:
            if asc:
                params['asc'] = "YES"
            else:
                params['asc'] = "NO"
        response = requests.get(url, params)
        ret = response.json()
        return ret
