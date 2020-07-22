class Person:
    def __init__(self, number, name):  # constructor
        # default public
        self.number = number
        self.name = name
    def hi(self):
        print(f'I m {self.name}')
        print(f'number {self.number}')
    
    def modifymyname(self,name):
        self.name = name
        
    

if __name__ == "__main__":
    Ann = Person(28,"Ann")
    print(Ann)
    Ann.hi()
    
    Ann.modifymyname("Debo")
    Ann.hi()
    
    Ann.name = "HowHow"
    Ann.hi()