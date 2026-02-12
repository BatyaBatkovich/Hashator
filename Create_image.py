from PIL import Image
from Class import image

def list_2_coord(list_data, width, height):  #  prend en parametre la liste avec les hash
    decimal_list = []  # List of tuples to store decimal numbers
    for item in list_data:
        hash_string = item
        if hash_string.startswith("0x"):
            hash_string = hash_string[2:]
        if len(hash_string) < 6:
            hash_string = hash_string.zfill(6)
        hash_string = int(hash_string, 16)
        x = hash_string % width
        y = (hash_string // width) % height
        decimal_list.append((x, y))
    return decimal_list

def show_pixel(decimal_list, im, width, height):  # Function to show pixel superpositions
    collision_count = 0
    for x, y in decimal_list:
        x, y = int(x), int(y)
        if (0 <= x < width and 0 <= y < height):  # S'assurer que x et y sont dans les limites
            current_color = im.img.getpixel((x, y))  # Check if a pixel already exists at this position
            if current_color == (255, 255, 255):  # If it's white
                im.set_pixel(x, y, (255, 255, 120))  # Yellow dot is set in case of no collision
            elif current_color == (255, 255, 120):  # If it's yellow
                collision_count += 1
                im.set_pixel(x, y, (255, 165, 0))  # orange dot is set if collision
            elif current_color == (255, 165, 0):  # If it's already orange
                collision_count += 1
                im.set_pixel(x, y, (255, 30, 30))  # Change to red dot for multiple collisions
            elif current_color == (255, 30, 30):  # If it's already red
                collision_count += 1
    return collision_count
