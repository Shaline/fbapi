import json
import requests


class FbBatchRequests:
    def __init__(self):
        self.requests = []

    def add(self, method, url, body=None):
        r = {
            'method': method, 
            'relative_url': url
        }

        if body:
            r['body'] = body

        self.requests.append(r)

    def execute(self, access_token):
        GRAPH_URL = 'https://graph.facebook.com'
        resp = requests.post(GRAPH_URL, {
            'access_token': access_token,
            'batch': json.dumps(self.requests)
        })

        #TODO: validate response

        return None
