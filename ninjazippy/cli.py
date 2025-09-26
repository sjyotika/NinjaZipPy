import argparse
from .core import zip_to_7z, unzip_from_7z

def main():
    parser = argparse.ArgumentParser(prog="ninjazippy", description="Zip/Unzip .7z archives")
    subparsers = parser.add_subparsers(dest="command")

    # zip
    zip_parser = subparsers.add_parser("zip", help="Zip files/folders into .7z")
    zip_parser.add_argument("source", help="Source file/folder")
    zip_parser.add_argument("dest", help="Destination .7z file")

    # unzip
    unzip_parser = subparsers.add_parser("unzip", help="Unzip .7z archive")
    unzip_parser.add_argument("archive", help="Archive file to unzip")
    unzip_parser.add_argument("dest", help="Destination folder")

    args = parser.parse_args()

    if args.command == "zip":
        zip_to_7z(args.source, args.dest)
        print(f"Zipped {args.source} → {args.dest}")
    elif args.command == "unzip":
        unzip_from_7z(args.archive, args.dest)
        print(f"Unzipped {args.archive} → {args.dest}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
