from copy import copy
from collections import defaultdict
import yaml


def load_config():
  def __filter_factory(t, f):
    t = copy(t)
    f = copy(f)
    print("T: ", t)
    print("F: ", f)
    def func(matches):
      for key in t:
        if not matches[key]:
          return False
      for key in f:
        if matches[key]:
          return False
      return True
    return func

  config = defaultdict(list, **yaml.load(open('./config.yml')))
  filters = {}
  for option in ["confident", "probable", "plausible", "improbable"]:
    filter_options = []
    for filter_ in config[option]:
      filter_ = defaultdict(list, filter_)
      filter_ = __filter_factory(filter_[True], filter_[False])
      filter_options.append(filter_)
    filters[option] = filter_options

  return filters

from ua_parser import user_agent_parser
from copy import copy

def featurize(fingerprint, target):
  fingerprint = copy(fingerprint)
  target = copy(target)
  
  parsed = user_agent_parser.Parse(fingerprint["ua"])
  fingerprint["os"] = parsed["os"]
  fingerprint["browser"] = parsed["user_agent"]
  
  parsed = user_agent_parser.Parse(target["ua"])
  target["os"] = parsed["os"]
  target["browser"] = parsed["user_agent"]
  
  print(fingerprint)
  print(target)
  matches = {}
  matches["uid"] = fingerprint["uid"] == target["uid"]
  matches["os_family"] = fingerprint["os"]["family"] == target["os"]["family"]
  matches["os_major"] = (fingerprint["os"]["major"] == target["os"]["major"]) and matches["os_family"]
  matches["os_minor"] = (fingerprint["os"]["minor"] == target["os"]["minor"]) and matches["os_major"]
  matches["os_exact"] = (fingerprint["os"]["patch"] == target["os"]["patch"]) and matches["os_minor"]
  matches["browser_family"] = fingerprint["browser"]["family"] == target["browser"]["family"]
  matches["browser_major"] = (fingerprint["browser"]["major"] == target["browser"]["major"]) and matches["browser_family"]
  matches["browser_minor"] = (fingerprint["browser"]["minor"] == target["browser"]["minor"]) and matches["browser_major"]
  matches["browser_exact"] = (fingerprint["browser"]["patch"] == target["browser"]["patch"]) and matches["browser_minor"]
  parse_ip = lambda ip, n: ".".join(ip.split(".")[:n])
  matches["ip_exact"] = fingerprint["ip"] == target["ip"]
  matches["ip_3"] = parse_ip(fingerprint["ip"], 3) == parse_ip(target["ip"], 3)
  matches["ip_2"] = parse_ip(fingerprint["ip"], 2) == parse_ip(target["ip"], 2)
  matches["screen"] = (fingerprint["swidth"] == target["swidth"]) and (fingerprint["sheight"] == target["sheight"])
  
  feature_vector = [1 if x else 0 for x in matches.values()]
  return matches, feature_vector
