from hashage import Hashator
from Create_image import image, hash_2_coord, show_pixel


# Source - https://stackoverflow.com/q/419163
if __name__ == "__main__":
    # D'abord il faut faire une strucuture de data qui stock les hash

    im = image(409, 409, "white")

    Machine_for_hash = Hashator(None)  # fait lui manger ta chaine :wa hasher
    Machine_for_hash.from_integer(12345666532234)  # -> on charge dans la machine
