import hashlib
from dataclasses import dataclass  # -> j'ai vu cela en cours ))
import zlib
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any,
)
from Class import Hashator

REGISTRY = {}


def register(cls):
    REGISTRY[cls.__name__] = cls
    return cls


@register
class sha1:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha1(data).hexdigest(), 16)


@register
class md5:
    def hash(self, data: bytes) -> int:
        return int(hashlib.md5(data).hexdigest(), 16)


@register
class blake2b:
    def hash(self, data: bytes) -> int:
        return int(hashlib.blake2b(data).hexdigest(), 16)


@register
class blake2s:
    def hash(self, data: bytes) -> int:
        return int(hashlib.blake2s(data).hexdigest(), 16)


@register
class sha224:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha224(data).hexdigest(), 16)


@register
class sha256:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha256(data).hexdigest(), 16)


@register
class sha384:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha384(data).hexdigest(), 16)


@register
class sha3_224:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha3_224(data).hexdigest(), 16)


@register
class sha3_256:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha3_256(data).hexdigest(), 16)


@register
class sha3_384:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha3_384(data).hexdigest(), 16)


@register
class sha3_512:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha3_512(data).hexdigest(), 16)


@register
class sha512:
    def hash(self, data: bytes) -> int:
        return int(hashlib.sha512(data).hexdigest(), 16)


# source : https://stackoverflow.com/questions/36238076/what-is-the-equivalent-c-c-loselose-algorithm-in-python
@register
class lose_lose:
    def hash(self, data: bytes) -> int:
        hsh = 0
        for byte in data:
            hsh += byte
        return hsh


# Source : http://www.cse.yorku.ca/~oz/hash.html
@register
class sdbm:
    def hash(self, data: bytes) -> int:
        hsh = 0
        for byte in data:
            hsh = byte + (hsh << 6) + (hsh << 16) - hsh
        return hsh & 0xFFFFFFFF


@register
class crc32:
    def hash(self, data: bytes) -> int:
        return zlib.crc32(data)


@register
class djb2:
    def hash(self, data: bytes) -> int:
        hsh = 5381
        for byte in data:
            hsh = ((hsh << 5) + hsh) + byte  # hsh * 33 + byte
        return hsh & 0xFFFFFFFF


@register
class fletcher16:
    def hash(self, data: bytes) -> int:
        sum1 = 0
        sum2 = 0
        for byte in data:
            sum1 = (sum1 + byte) % 255
            sum2 = (sum2 + sum1) % 255
        return (sum2 << 8) | sum1


@register
class custom_hashage:
    def hash(self, data: bytes) -> int:
        hsh = 0
        for byte in data:
            hsh = hsh + byte
            hsh = hsh ^ 0x55AA
            hsh = byte + (hsh << 6) + (hsh << 16) - hsh
        return hsh


def get_available_algos() -> list[str]:
    return REGISTRY.keys()


def resolve_hash_algo(name: str) -> Callable[[bytes | Any], Any] | None:
    name_lower = name.lower()
    if name_lower in REGISTRY:
        algo_class = REGISTRY[name_lower]
        instance = algo_class()
        return instance.hash

    try:
        if name in hashlib.algorithms_available:
            return lambda data: int(hashlib.new(name, data).hexdigest(), 16)
    except Exception:
        pass

    return None
    # custom_hashes = {
    # "lose_lose": lose_lose,
    # "djb2": djb2,
    # "sdbm": sdbm,
    # "crc32": crc32,
    # "fletcher16": fletcher16,
    # "custom_hashage": custom_hashage,
    # }

    # if name in custom_hashes:
    # return custom_hashes[name]

    # try:
    # if name in hashlib.algorithms_available:
    # return lambda data, algo=name: hashlib.new(algo, data)
    # except Exception:
    # pass

    return None
