import hashlib
from dataclasses import dataclass  # -> j'ai vu cela en cours ))
import zlib
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any,
)


@dataclass
class Hashator:
    array_to_hash: list[bytes] | None  # le massiv de data qu'on souhaite hasher
    # result_of_hash: None  # le result de hash

    def from_list(self, data):  # need to be bytes after this method
        self.array_to_hash = [str(i).encode() for i in data]

    def from_integer(self, data):
        self.array_to_hash = [str(data).encode()]
        return self.array_to_hash

    def from_str(self, data):
        self.array_to_hash = [data.encode()]
        return self.array_to_hash

    def from_file(self, filename):
        with open(filename, "r", errors="ignore") as file:
            self.array_to_hash = [line.strip().encode() for line in file]
        return self.array_to_hash

    def hashtor(
        self, func_hashage: Callable[[bytes | Any], Any]
    ) -> list:  # FINALEMENT UNE STRING C LA MERDE - A REFAIRE TOUT ICI POUR RECEVOIR UNE LISTE DES HASH
        if not self.array_to_hash:
            return []

        result_list = []
        for element in self.array_to_hash:
            raw_output = func_hashage(element)
            # print(f"Hashing element: {element} -> Raw output: {raw_output}")
            if isinstance(raw_output, int):
                result_list.append(hex(raw_output))
            elif hasattr(raw_output, "hexdigest"):
                result_list.append(raw_output.hexdigest())
            else:
                result_list.append(str(raw_output))
        return result_list


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
    }

    if name in custom_hashes:
        return custom_hashes[name]

    try:
        if name in hashlib.algorithms_available:
            return lambda data, algo=name: hashlib.new(algo, data)
    except Exception:
        pass

    return None
