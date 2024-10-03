from pathlib import Path
import argparse
from export import user_to_csv, user_to_pickle_dict


if __name__ == "__main__":
    path = Path.cwd()
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--option", type=str, help="Select an script option")

    args = parser.parse_args()

    if args.option == "database_to_csv":
        # python app\export_scripts.py -o database_to_csv

        export_route = f"{path}/files/users.csv"
        user_to_csv(export_route)

    if args.option == "database_to_pickle":
        # python app\export_scripts.py -o database_to_pickle

        export_route = f"{path}/files/users.pkl"
        user_to_pickle_dict(export_route)

