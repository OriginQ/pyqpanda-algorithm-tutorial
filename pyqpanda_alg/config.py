import platform
import configparser
import os
import json
import requests
import subprocess
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
import time


class RSAMethod:
    def __init__(self):
        pass

    def encrypt(self, text, pubkey):
        pass

    def decrypt(self, text, privkey):
        pass


class SerialNumberUtil:
    def __init__(self):
        pass

    def get_all_sn(self):
        pass

class AuthSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Authorization(metaclass=AuthSingleton):
    def __init__(self):
        pass

    def check(self):
        pass

