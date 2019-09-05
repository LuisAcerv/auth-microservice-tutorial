import sqlalchemy as db

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    engine = db.create_engine('postgresql://user:password@localhost/authdb')
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")