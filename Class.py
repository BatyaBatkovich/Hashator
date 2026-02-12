from dataclasses import dataclass
from collections.abc import Callable  # PEP 585 -> a relire
from typing import (
    Any,
)
from PIL import Image

class image:
    def __init__(
        self, width, height, color="white"
    ):  # Create a blank image with given width, height and background color
        self.img = Image.new("RGB", (width, height), color=color)

    def set_pixel(self, x, y, color):  # Create a pixel at (x,y) with color
        self.img.putpixel((x, y), color)

    def save(self, filename):  # Save the image to a file
        self.img.save(filename)
    
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