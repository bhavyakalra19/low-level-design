#"A class should have one and only one reason to change, meaning that a class should have only one job"

# Below example shows that one class journal is used to save 
# journal and count apeend it to array other class PersistenceManager 
# is used to load the journal data in a temp file. This shows 
# that a class should have on responsibilty.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
        
    def add_entry(self,text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        
    def remove_entry(self,pos):
        del self.entries[pos]
        
    def __str__(self):
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
        
    # def load(self, filename):
    #     pass
    
    # def low_from_web(self, uri):
    #     pass
    

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry("I'm bhavya")
j.add_entry("I'm learning solid principles")

# print(f"journnal entries : \n{j}")

file = r"check.txt"
PersistenceManager.save_to_file(j,file)

with open(file) as fh:
    print(fh.read())