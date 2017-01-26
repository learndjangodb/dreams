from django.core import signing
from django.core.signing import Signer, TimestampSigner
from datetime import timedelta

signer = Signer()
value = signer.sign('My string')  # 'My string:Z4q-qV6qotodFYH60E6Ws1YZJTY'

orig = signer.unsign(value)  # 'My string'

# BadSignature exception

value += 'm'

try:
    original = signer.unsign(value)
except signing.BadSignature:
    print("Tampering Detected")

signer2 = TimestampSigner()
va2 = signer2.sign('hello')

