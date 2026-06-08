import json

version_json = '''
{
 "date": "2026-04-30T15:56:56+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "5085ce96b7cceeaed5e4ac9f44f2a2e1a57fa1df",
 "version": "0.9.3"
}
'''


def get_versions():
    return json.loads(version_json)
