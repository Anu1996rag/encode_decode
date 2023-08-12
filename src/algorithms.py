""" Configuration of Encoding and Decoding Algorithms"""

from base64 import (
    a85decode,
    a85encode,

    b16decode,
    b16encode,

    b32decode,
    b32encode,

    b32hexdecode,
    b32hexencode,

    b64decode,
    b64encode,

    b85decode,
    b85encode
)

from binascii import hexlify, unhexlify

from hashlib import (
    blake2b,
    blake2s,
    md5,
    sha1,
    sha224,
    sha256,
    sha384,
    sha3_224,
    sha3_256,
    sha3_384,
    sha3_512,
    sha512,
)

ENCODING_ALGORITHMS = {
    "a85encode": a85encode,
    "b16encode": b16encode,
    "b32encode": b32encode,
    "b32hexencode": b32hexencode,
    "b64encode": b64encode,
    "b85encode": b85encode,
    "hexlify": hexlify,
}

DECODING_ALGORITHMS = {
    "a85decode": a85decode,
    "b16decode": b16decode,
    "b32decode": b32decode,
    "b32hexdecode": b32hexdecode,
    "b64decode": b64decode,
    "b85decode": b85decode,
    "unhexlify": unhexlify,
}

HASHING_ALGORITHMS = {
    "blake2b": blake2b,
    "blake2s": blake2s,
    "md5": md5,
    "sha1": sha1,
    "sha224": sha224,
    "sha256": sha256,
    "sha384": sha384,
    "sha3_224": sha3_224,
    "sha3_256": sha3_256,
    "sha3_384": sha3_384,
    "sha3_512": sha3_512,
    "sha512": sha512,
}
