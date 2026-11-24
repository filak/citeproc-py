import json

version_json = '''
{
 "date": "2026-11-24T12:00:01+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "55e52e0ab020251fb05c1f20e95254c01d331f4a",
 "version": "0.12.3"
}
'''


def get_versions():
    return json.loads(version_json)
