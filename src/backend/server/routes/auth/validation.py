# -*- coding=utf-8 -*-
r"""

"""
import hashlib
import os


def generate_hash(password: str) -> bytes:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100_000
    )
    return salt + key


def validate_password(hashed: bytes, password: str) -> bool:
    salt = hashed[:32]
    hash_key = hashed[32:]
    check_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100_000
    )
    return hash_key == check_key
