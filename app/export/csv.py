import csv
import pickle
from DB.connect import database_connect
from models.User import User

def user_to_csv(export_route):

    session = database_connect("init_scripts")
    users = session.query(User).all()

    with open(export_route, 'w', encoding="UTF8", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter="\t")
        writer.writerow([ "ID", "Name", "Email" ])
        for user in users:
            writer.writerow([ user.id, user.name, user.email ])


def user_to_pickle_dict(export_route):

    users_dict = {}
    session = database_connect("init_scripts")
    users = session.query(User).all()

    for user in users:
        users_dict[user.id] = {"name": user.name, "email": user.email}

    pickle.dump(users_dict, open(export_route, 'wb'))




