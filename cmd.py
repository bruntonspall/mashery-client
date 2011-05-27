import mashery
import json

def int_if(v):
  try:
    return int(v)
  except ValueError:
    return v

if __name__ == "__main__":
    config = json.load(file('config.json'))
    # I could of sworn that mashery.Api(**v) should work here...
    apis = dict([(k, mashery.Api(key = v['key'], secret=v['secret'], path=v['path'], host=v['host'])) for k,v in config.iteritems()])
    live = apis['live']
    import sys
    method = sys.argv[1]
    args = [int_if(v) for v in sys.argv[2:]]
    print(json.dumps(json.loads(mashery.call_api_httplib(live, method, args)), indent=2))
