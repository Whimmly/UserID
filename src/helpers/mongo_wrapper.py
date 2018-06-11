import os
import logging
from pymongo import MongoClient

host = '35.174.77.181'
port = 27016
client = MongoClient(host, port)
user_db = client['user']
fingerprints_col = user_db["fingerprints"]


def get_fingerprints():
  '''
  Args:
    - features (list, str): desired feature values to add to
                the returned result dictionary.
  '''
  for fingerprint_ in fingerprints_col.find_all():
    fingerprint = {}
    for key in ["uid", "unix", "ua", "ip", "swidth", "sheight"]:
      fingerprint[key] = fingerprint_.get(key)
    yield fingerprint
