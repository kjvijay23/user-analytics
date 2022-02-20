import os
from user_analytics import app, connectivity, dao, utils
import unittest
import tempfile
import json
from mock import patch, MagicMock, Mock
from google.cloud import bigquery
import pandas as pd


class bq_stub():
    def result(query):
        return bq_stub()

    def to_dataframe(query):
        return pd.DataFrame([1])


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch('user_analytics.connectivity.connections.connect_bq')
    def test_heartbeat(self, bq_mock):
        rv = self.app.get('/heartbeat')
        self.assertEqual(bq_mock.call_count, 1)
        assert 'If not click the link' in str(rv.data)

    def test_heart_beat(self):
        rv = self.app.get('/heartbeat')
        with self.assertRaises(AssertionError):
            assert '.json was not found' in str(rv.data)

    @patch('user_analytics.connectivity.connections.connect_bq')
    def test_orderStatus(self, bq_mock):
        rv = self.app.get('/orderStatus/')
        response = json.loads(rv.data)
        expected = {'error': 'Bad request - Required fullvisitorid'}
        self.assertDictEqual(response, expected)

    @patch('user_analytics.connectivity.connections.connect_bq')
    def test_orderResponse(self, bq_mock):
        rv = self.app.get('/orderStatus/123')
        expected = 'b\'"No data found for the visitor_id 123"\\n\''
        self.assertEqual(str(rv.data), expected)

    def test_utils(self):
        rv = utils.get_uuid()
        self.assertIsInstance(rv, str)
        self.assertFalse((utils.str_to_bool('F')))
        self.assertTrue(utils.notify)

    @patch('google.cloud.bigquery.Client', autospec=True)
    def test_dao(self, mock_bigquery):
        mock_bigquery.query.return_value = bq_stub()
        rv = dao.get_order_status(mock_bigquery, 123)
        self.assertIsInstance(rv, dict)


if __name__ == '__main__':
    unittest.main()
