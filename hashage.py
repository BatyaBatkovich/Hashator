import hashlib
from dataclasses import dataclass  # -> j'ai vu cela en cours ))

# import kagglehub
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any,
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

    # def from_list(self): #need to be bytes after this method

    def from_integer(self, data):
        self.array_to_hash = [str(data).encode()]
        return self.array_to_hash

    def from_str(self, data):
        self.array_to_hash = [data.encode()]
        return self.array_to_hash

    def from_file(self): ...

    def hashtor(self, func_hashage: Callable[[bytes], Any]) -> str:
        if not self.array_to_hash:
            return "Hashator need data XD"
        result = b"".join(self.array_to_hash)
        return func_hashage(result).hexdigest()


# dataset_of_string = ...
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
# Machine_for_hash2.from_integer(12345666532234)  # -> on charge dans la machine
Machine_for_hash.from_str("swededededed")
print(Machine_for_hash.hashtor(hashlib.md5))
