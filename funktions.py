class Functions:

    def __init__(self, db):
        self.db = db

    def get_all(self, table_name, args):
        data = self.convertToDir(self.db.get_all_data(table_name))

        if self.has_args(args):
            for i in args:
                if i == "-j":
                    data = self.db.json(data)
        print(data)

    def clear_all(self, table_name, args): 
        result = self.db.clear_all_data(table_name)
        
        if self.has_args(args):
            for i in args:
                if i == "-p":
                    print(result)
    
    def get_by(self, table_name, args):
        name = "_id"
        value = "0"

        if self.has_args(args):
            for i, arg in enumerate(args):
                if arg == "-n":
                    name = args[i+1]
                elif arg == "-v":
                    value = args[i+1]
        print(name, value)
        print(self.convertToDir(self.db.get_by(table_name, name, value)))
        return self.convertToDir(self.db.get_by(table_name, name, value))

                

    def alert_comfirm(self):
        if input('Write "YES" to comfirm:') == "YES":
            return True
        return False
        

    def has_args(slef, args):
        if(len(args) > 0):
            return True
        return False

    def convertToDir(self, data):
        out = []
        for item in data:
            out.append(item)
        return out