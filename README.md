# UserID [Service Repository]
Tracking users across various devices, IPs, browsers, sessions and websites is a non-trivial challenge for recommender system implementations. We follow the industry standard in the use of dual browser-device fingerprinting systems. Accordingly, we will develop two rule-based microservices that validate or infer user identities. 
* Browser fingerprinting: use http metadata & cross-site cookies to validate fingerprint match with a known user. These fingerprints confidently validate user identity.
* Device fingerprinting: use time-of-day, IP address, browser type, device type and screen-size to infer user identity which must validated store-side or otherwise supported by browser fingerprinting results.

Hosted on port 8890.

Fingerprint schema:
```
fingerprint = {
    "uid": 'jae90a8dvza93',
    "unix": 1528692901,
    "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36" \
    " (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
    "ip": "34.210.113.137",
    "swidth": 300,
    "sheight": 500
}
```
