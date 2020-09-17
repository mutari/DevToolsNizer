class Functions:

    def __init__(self, db):
        self.db = db

    def get_all(self, table_name, args):
        data = self.db.get_all_data(table_name)
        if(self.has_args(args)):
            for i in args:
                if(i == "-j"):
                    data = self.db.json(data)
        print(data)

    def has_args(slef, args):
        if(len(args) > 0):
            return True
        return False