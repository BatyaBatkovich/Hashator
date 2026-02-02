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


def hash_2_coord(
    filename,
):  #  Function that reads a file line by line, converts each hash to two decimal numbers and returns a list of tuples
    with open(filename, "r") as file:
        lines = file.readlines()

    decimal_list = []  # List of tuples to store decimal numbers
    for line in lines:
        hash_string = line.strip()  # nettoie les /n /t etc les " "
        decimalx = (
            int(hash_string[:3], 16) / 10
        )  # Convert first 3 characters of hash to decimal to get x coordinate
        decimaly = (
            int(hash_string[-3:], 16) / 10
        )  # Convert last 3 characters of hash to decimal to get y coordinate
        decimal_list.append((decimalx, decimaly))  # Creating a list of with x and y

    return decimal_list


def list_2_coord(list_data):  #  prend en parametre la liste avec les hash
    decimal_list = []  # List of tuples to store decimal numbers
    for item in list_data:
        hash_string = item
        decimalx = (
            int(hash_string[:3], 16) / 10
        )  # Convert first 3 characters of hash to decimal to get x coordinate
        decimaly = (
            int(hash_string[-3:], 16) / 10
        )  # Convert last 3 characters of hash to decimal to get y coordinate
        decimal_list.append((decimalx, decimaly))  # Creating a list of with x and y

    return decimal_list


def show_pixel(decimal_list):  # Function to show pixel superpositions
    for x, y in decimal_list:
        x, y = int(x), int(y)
        if 0 <= x < 409 and 0 <= y < 409:  # S'assurer que x et y sont dans les limites
            current_color = im.img.getpixel(
                (x, y)
            )  # Check if a pixel already exists at this position
            if current_color == (255, 255, 255):  # If it's white
                im.set_pixel(
                    x, y, (0, 255, 0)
                )  # Green dot is set in case of no collision
            elif current_color == (0, 255, 0):  # If it's white
                im.set_pixel(x, y, (255, 0, 0))  # Green dot is set if no collision
            elif current_color == (255, 0, 0):  # If it's already red
                im.set_pixel(
                    x, y, (0, 0, 255)
                )  # Change to blue dot for multiple collisions


# im = image(409, 409, "white")  # Create a blank image of size 409x409 with white background
# decimal_list = hash_2_coord("sha1rand.txt") # Get the list of decimal coordinates from the file
# show_pixel(decimal_list)  # Show pixel superpositions
# im.save(input("Enter the file name to save the image (with .png extension): "))
