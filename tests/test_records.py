import json
from pathlib import Path
import unittest


class RecordsTest(unittest.TestCase):
    def test_known_input_contract(self):
        source = Path(__file__).resolve().parents[1] / "data" / "records.json"
        payload = json.loads(source.read_text(encoding="utf-8"))
        registrations = {item['registry'] for item in payload['estimates']}
        for item in payload['estimates']:
            assert 0 <= item['yes'] <= item['observed'] <= item['assigned']
        assert all({item['first'], item['second']} <= registrations and item['min_shared'] <= item['max_shared'] for item in payload['overlap'])
        assert {'对照', '邀请'} == {item['arm'] for item in payload['estimates']}
        assert any(item['signed'] for item in payload['decisions'])
