from hashage import Hashator, lose_lose
from Create_image import image, list_2_coord, show_pixel
from passlib.hash import lmhash, mssql2000
import hashlib

# Source - https://stackoverflow.com/q/419163
if __name__ == "__main__":
    # D'abord il faut faire une strucuture de data qui stock les hash
    im = image(409, 409, "white")
    Machine_for_hash = Hashator(None)
    Machine_for_hash.from_file("fr_dict.txt")
    # print(f"SQL 2000:   {Machine_for_hash.hashtor(hashlib.sha224)}")
    # Machine_for_hash = Hashator(None)

    # print(Machine_for_hash.hashtor(hashlib.sha224))
    decimal_list = list_2_coord(Machine_for_hash.hashtor(lose_lose))
    print(decimal_list)
    show_pixel(decimal_list, im)
    im.save(input("Enter the file name to save the image (with .png extension): "))
    # Machine_for_hash.from_integer(12345666532234)  # -> on charge dans la machine
