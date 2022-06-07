class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self,name,age,healthLevel,happinessLevel):
        self.name = name
        self.age = age
        self.healthLevel = healthLevel
        self.happinessLevel = happinessLevel

    def display_info(self):
        print("this Animal name is :",self.name,"health Level:",self.healthLevel,"happiness Level",self.happinessLevel)
    
    def feed(healthLevel,happinessLevel):
        self.healthLevel+=10
        self.happinessLevel+10


class Lion(Animal):
     def __init__(self, name, age=2, healthLevel: int = 3, happinessLevel: int = 3):
            super().__init__(name,age,healthLevel,happinessLevel)

class Tiger(Animal):
    def __init__(self, name, age=3, healthLevel: int = 4, happinessLevel: int = 5, female: bool = True):
        super().__init__(name,age,healthLevel,happinessLevel)
        self.female = female

class Bear(Animal):
    def __init__(self, name, age=6, healthLevel: int = 2, happinessLevel: int = 10, color: str="green"):
        super().__init__(name,age,healthLevel,happinessLevel)
        self.color = color

zoo1 = Zoo("Shahad's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
