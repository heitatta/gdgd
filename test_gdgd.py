import gdgd
import unittest
import json

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        gdgd.app.testing = True
        self.app = gdgd.app.test_client()

    def tearDown(self):
        # do nothing
        print('done')

    def test_empty_launch(self):
        res = self.app.post('/', data=launch_json)
        data = json.loads(res.data.decode('unicode_escape'))
        assert 'response' in data
        assert 'outputSpeech' in data['response']
        assert 'text' in data['response']['outputSpeech']
        assert data['response']['outputSpeech']['text'] == \
            'カフェ&バー ぐだぐだへようこそ'

    def test_intent_request(self):
        res = self.app.post('/', data=intent_json)
        data = json.loads(res.data.decode('unicode_escape'))
        assert 'response' in data
        assert 'outputSpeech' in data['response']
        assert 'text' in data['response']['outputSpeech']
        text = data['response']['outputSpeech']['text']
        assert text.find('朝には') == 0
        
        
launch_json = """{
  "session": {
    "new": true,
    "sessionId": "SessionId.some",
    "application": {
      "applicationId": "amzn1.ask.skill.app_id"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.hoge"
    }
  },
  "request": {
    "type": "LaunchRequest",
    "requestId": "EdwRequestId.req",
    "locale": "ja-JP",
    "timestamp": "2017-09-01T02:22:34Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.app_id"
      },
      "user": {
        "userId": "amzn1.ask.account.hoge"
      },
      "device": {
        "supportedInterfaces": {}
      }
    }
  },
  "version": "1.0"
}"""

intent_json = """{
    "session": {
        "new": true,
        "sessionId": "SessionId.some",
        "application": {
            "applicationId": "amzn1.ask.skill.app_id"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.hoge"
        }
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.4364d09f-e86f-47e2-be1c-bfd0444396d4",
        "intent": {
            "name": "DishIntent",
            "slots": {
                "dish": {
                    "name": "dish",
                    "value": "朝"
                }
            }
        }
    },
    "context": {
        "AudioPlayer": {
            "playerActivity": "IDLE"
        },
        "System": {
            "application": {
                "applicationId": "amzn1.ask.skill.app_id"
            },
            "user": {
                "userId": "amzn1.ask.account.hoge"
            },
            "device": {
                "supportedInterfaces": {}
            }
        }
    },
    "version": "1.0"
}"""
