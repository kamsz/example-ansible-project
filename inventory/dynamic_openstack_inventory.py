import simplejson as json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--list", action="store_true")
parser.add_argument("--host", action="store")
args = parser.parse_args()

# TODO: Retrieve inventory data from external source
inventory = {
    "_meta": {
        "hostvars": {
            "172.16.1.1": {
                "rack": "D1"
            }
        }
    },
    "web_servers": {
        "hosts": ["172.16.1.1", "172.16.1.2"],
        "vars": {
            "apache_version": "2.4.18"
        }
    }
}
if args.host:
        host = args.host
        print inventory['meta']['hostvars'][host]
        return json.dumps(inventory['meta']['hostvars'][host], ensure_ascii=False)
    elif args.list:
        print inventory
        return json.dumps(inventory, ensure_ascii=False)
    else:
        return {'_meta': {'hostvars': {}}}
