class Functions:

    def __init__(self, db):
        self.db = db

    def get_all(self, table_name, args):
        out = []
        for item in self.db.get_all_data(table_name):
            out.append(item)
        data = out

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

    def alert_comfirm(self):
        if input('Write "YES" to comfirm:') == "YES":
            return True
        return False
        

    def has_args(slef, args):
        if(len(args) > 0):
            return True
        return False