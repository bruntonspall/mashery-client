import hashlib, time, json

class Api(object):
    def __init__(self, key='', secret='', path='', host="api.mashery.com"):
        self.key = key
        self.secret = secret
        self._path = path
        self.host = host
       
    def get_signature(self):
        return hashlib.md5("%s%s%s" % (self.key,self.secret,str(int(time.time())))).hexdigest()

    signature = property(get_signature)

    def get_path(self):
        return "%s?apikey=%s&sig=%s" % (self._path, self.key, self.signature)

    path = property(get_path)
        
    def postdata(self, method, *params):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        })

def call_api_httplib(api, method, *params):
    import httplib
    params = api.postdata(method, *params)
    conn = httplib.HTTPConnection(api.host)
    headers = {"Content-type": "application/json", "Accept": "text/plain", "Content-length": repr(len(params))}
    conn.request("POST", api.path, params, headers)
    response = conn.getresponse()
    return response.read()
