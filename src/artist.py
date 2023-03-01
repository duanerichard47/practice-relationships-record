class Artist:
    def __init__(self, name):
        self.name = name
       
      

    def get_name(self):
        return self.name
    

    def get_records(self):
         return self.records
    
    def get_first_record(self):
        return self.records[0]
    
# testing = Artist("mouse")
# print(Artist.get_records)
# print(testing.name)

'''
class Artist:
    def __init__(self, name):
        self.name = name
        self.records = []
    
    def get_name(self):
        return self.name
    
    def get_records(self):
        return self.records
    
    def get_first_record(self):
        min_record = self.records[0]
        for record in self.records:
            if record.year < min_record.year:
                min_record = record
        return min_record
'''