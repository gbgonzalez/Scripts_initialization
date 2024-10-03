import argparse
from DB.connect import database_connect,database_engine
from models.User import User

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=str, help="Select an script option")
    parser.add_argument("-id", "--id_user", type=int, help="Send an user ID")
    args = parser.parse_args()

    if args.option == "show_users_database_sqlalchemy":
        # python app\database_scripts.py -o show_users_database_sqlalchemy

        session = database_connect("init_scripts")

        # SELECT * FROM users
        users = session.query(User).all()

        for user in users:
            print(user)
            print(user.name)
            print(user.email)
            print("-----------")

    if args.option == "show_users_database_classic":
        # python app\database_scripts.py -o show_users_database_classic

        engine = database_engine("init_scripts")

        sql_query = "SELECT * FROM users"
        users = engine.execute(sql_query).all()

        for user in users:
            print(user)
            print(user.name)
            print(user.email)
            print("-----------")

    if args.option == "add_database":
        # python app\database_scripts.py -o add_database

        session = database_connect("init_scripts")
        new_user = User(name="test1", email="try@try.com")
        session.add(new_user)
        session.commit()

    if args.option == "remove_user":
        # python app\database_scripts.py -o remove_user -id 7

        session = database_connect("init_scripts")

        # SELECT * FROM User where id = args.id_user
        remove_user = session.query(User).filter_by(id=args.id_user).first()

        session.delete(remove_user)
        session.commit()



