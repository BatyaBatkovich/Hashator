import hashlib
from Create_image import image, list_2_coord, show_pixel
from hashage import Hashator, get_available_algos, resolve_hash_algo
from hashator_cli import ASCII_BANNER, build_parser, format_list


# Source - https://stackoverflow.com/q/419163
if __name__ == "__main__":
    print(ASCII_BANNER)
    parser = build_parser()
    args = parser.parse_args()

    if args.list_algos:
        print("Algorithmes disponibles:")
        print(format_list(get_available_algos()))
    else:
        if not args.dest or not args.hash_algo:
            parser.print_help()
        else:
            hash_func = resolve_hash_algo(args.hash_algo)
            if not hash_func:
                print(f"Algo inconnu: {args.hash_algo}")
                print("Algorithmes disponibles:")
                print(format_list(get_available_algos()))
                raise SystemExit(2)

            # D'abord il faut faire une strucuture de data qui stock les hash
            im = image(512, 512, "white")
            Machine_for_hash = Hashator(None)
            Machine_for_hash.from_file(args.file)
            # print(f"SQL 2000:   {Machine_for_hash.hashtor(hashlib.sha224)}")
            # Machine_for_hash = Hashator(None)

            # print(Machine_for_hash.hashtor(hashlib.sha224))
            decimal_list = list_2_coord(Machine_for_hash.hashtor(hash_func))
            # print(decimal_list)
            show_pixel(decimal_list, im)
            im.save(args.dest)
            print(
                f"Image of hash generated and saved as '{args.dest}' with algorithm '{args.hash_algo}' on file '{args.file}'."
            )
            # Machine_for_hash.from_integer(12345666532234)  # -> on charge dans la machine
