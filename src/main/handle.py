from ..helpers import get_fingerprints
from .logic import featurize, load_config


def test_fingerprint(target, model, threshold):
  probable = {}
  plausible = {}
  filters = load_config()

  for fingerprint in get_fingerprints():
    matches, feature_vector = featurize(fingerprint, target)
    for filter_ in filters["confident"]:
      if filter_(matches):
        return confident[fingerprint["uid"]]
    for filter_ in filters["probable"]:
      if filter_(matches):
        probable[fingerprint["uid"]] = feature_vector
        break
    for filter_ in filters["plausible"]:
      if filter_(matches):
        probable[fingerprint["uid"]] = feature_vector
        break
  if len(probable) is not 0:
    for uid, feature in probable:
      probable[uid] = model.score(feature)
    best_uid = sort(probable.items(), key=lambda x: x[1])[0]
    return best_uid
  if len(plausible) is not 0:
    best_uid, best_score = sort(probable.items(), key=lambda x: x[1])
    return best_uid if best_score > threshold else None
  return None


def validate_uid(fingerprint):
  pass
