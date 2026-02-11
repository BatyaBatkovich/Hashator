import hashlib
from dataclasses import dataclass  # -> j'ai vu cela en cours ))
# import json
# from streebog import streebog256, streebog512

# import pyhash
# import Crypto.Hash
import zlib
import passlib.registry

from passlib.hash import lmhash, mssql2000

# import inspect -> a tester plus tard
# import kagglehub -> une lib de merde
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any
)  # -> pour ne pas faire les remarque sur le type utiliser ( IDE,LINTER)

### EXEMPLE TROUVER SUR HABR.RU ###

# example_string = "Hello, World!"

# md5_hash = hashlib.md5(example_string.encode()).hexdigest()
# print(f"MD5: {md5_hash}")

# SHA-1
# sha1_hash = hashlib.sha1(example_string.encode()).hexdigest()
# print(f"SHA-1: {sha1_hash}")

# SHA-256
# sha256_hash = hashlib.sha256(example_string.encode()).hexdigest()
# print(f"SHA-256: {sha256_hash}")

### MEOW MEOW MEOW ####


# "mp4" "mp3"   "jpg"   10100101010 1a3f2b


# encode -> "01020200101"  bin = 010101010010


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
            #print(f"Hashing element: {element} -> Raw output: {raw_output}")
            if isinstance(raw_output, int):
                result_list.append(hex(raw_output))
            elif hasattr(raw_output, "hexdigest"):
                result_list.append(raw_output.hexdigest())
            else:
                result_list.append(str(raw_output))
        return result_list

        # dataset_of_string = ...


# source : https://stackoverflow.com/questions/36238076/what-is-the-equivalent-c-c-loselose-algorithm-in-python
def lose_lose(data: bytes) -> int:
    hsh = 0
    for bytes in data:
        hsh += bytes
    return hsh


def get_available_algos() -> list[str]:
    algos: list[str] = []
    try:
        algos.extend(sorted(passlib.registry.list_crypt_handlers()))
    except Exception:
        pass

    try:
        algos.extend(sorted(hashlib.algorithms_guaranteed))
    except Exception:
        pass

    algos.append("lose_lose")

    seen: set[str] = set()
    unique_algos: list[str] = []
    for algo in algos:
        if algo in seen:
            continue
        seen.add(algo)
        unique_algos.append(algo)
    return unique_algos


def resolve_hash_algo(name: str) -> Callable[[bytes | Any], Any] | None:
    if name == "lose_lose":
        return lose_lose

    try:
        if name in hashlib.algorithms_available:
            return lambda data, algo=name: hashlib.new(algo, data)
    except Exception:
        pass

    try:
        handler = passlib.registry.get_crypt_handler(name)
        if handler is not None:
            return handler.hash
    except Exception:
        pass

    return None


# dataset_of_list = ...
# dataset_of_string = ...
# dataset_of_int    = ...
# dataset_file = ...

# def md5_hash(self):  # la premiere algo
#    result_of_hash = hashlib.md5(self.array_to_hash.encode()).hexdigest()
#    return result_of_hash

# def _hash(self): ...

# def _hash(self): ...

# def _hash(self): ...

# def custom_hash(self):  # la derniere


# path = kagglehub.dataset_download("boiniabhiram/wine-quality-dataset")

# print("Path to dataset files:", path)

# Machine_for_hash = Hashator(None)  # fait lui manger ta chaine :wa hasher

# Machine_for_hash2 = Hashator(None)
# Machine_for_hash.from_integer(12345666532234)  # -> on charge dans la machine
# Machine_for_hash.from_list([11223, 54445, 45423])
# print(Machine_for_hash.hashtor(hashlib.sha224))
# Machine_for_hash.from_file("fr_dict.txt")

# print(dir(hashlib))
# print(Machine_for_hash.hashtor(hash))
# print(Machine_for_hash.hashtor(zlib.adler32))
# print(Machine_for_hash.hashtor(zlib.crc32))
# print(f"GOST-256: {Machine_for_hash.hashtor(streebog256)}")
# print(f"GOST-512: {Machine_for_hash.hashtor(streebog512)}")
# print(f"Win95 LM:   {Machine_for_hash.hashtor(lmhash.hash)}")
# print(f"Unix DES:   {Machine_for_hash.hashtor(des_crypt.hash)}")
# print(f"SQL 2000:   {Machine_for_hash.hashtor(mssql2000.hash)}")
# print(help(hashlib))
