import hashlib
from dataclasses import dataclass  # -> j'ai vu cela en cours ))
import zlib
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any,
)
from Class import Hashator

# source : https://stackoverflow.com/questions/36238076/what-is-the-equivalent-c-c-loselose-algorithm-in-python
def lose_lose(data: bytes) -> int:
    hsh = 0
    for bytes in data:
        hsh += bytes
    return hsh


# Source : http://www.cse.yorku.ca/~oz/hash.html
def sdbm(data: bytes) -> int:
    hsh = 0
    for byte in data:
        hsh = byte + (hsh << 6) + (hsh << 16) - hsh
    return hsh & 0xFFFFFFFF


def crc32(data: bytes) -> int:
    """CRC32 checksum via zlib"""
    return zlib.crc32(data)


def djb2(data: bytes) -> int:
    """DJB2 hash by Dan Bernstein"""
    hsh = 5381
    for byte in data:
        hsh = ((hsh << 5) + hsh) + byte  # hsh * 33 + byte
    return hsh & 0xFFFFFFFF


def fletcher16(data: bytes) -> int:
    sum1 = 0
    sum2 = 0
    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1


def custom_hashage(data: bytes) -> int:
    hsh = 0
    for byte in data:
        hsh = hsh + byte
        hsh = hsh ^ 0x55AA
        hsh = byte + (hsh << 6) + (hsh << 16) - hsh
    return hsh


def get_available_algos() -> list[str]:
    algos: list[str] = []

    try:
        algos.extend(sorted(hashlib.algorithms_guaranteed))
    except Exception:
        pass

    algos.append("lose_lose")
    algos.append("sdbm")
    algos.append("djb2")
    algos.append("crc32")
    algos.append("fletcher16")
    algos.append("custom_hashage")

    seen: set[str] = set()
    unique_algos: list[str] = []
    for algo in algos:
        if algo in seen:
            continue
        seen.add(algo)
        unique_algos.append(algo)
    return unique_algos


def resolve_hash_algo(name: str) -> Callable[[bytes | Any], Any] | None:
    custom_hashes = {
        "lose_lose": lose_lose,
        "djb2": djb2,
        "sdbm": sdbm,
        "crc32": crc32,
        "fletcher16": fletcher16,
        "custom_hashage": custom_hashage,
    }

    if name in custom_hashes:
        return custom_hashes[name]

    try:
        if name in hashlib.algorithms_available:
            return lambda data, algo=name: hashlib.new(algo, data)
    except Exception:
        pass

    return None
