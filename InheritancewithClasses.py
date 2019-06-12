#Parent Class
class Organism:
    name="Unknown"
    species="Unknown"
    legs=None
    arms=None
    dna="Sequence A"
    origin="Unknown"
    carbon_based=True
    
    def information(self):
        msg="\n Name: {} \n Species: {} \n Legs: {}\n Arms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
#child class instance
class Human(Organism):
    name="Mandeep"
    species="homosapien"
    legs=2
    arms=2
    origin='Earth'
    
    def ingenuity(self):
        msg="\nCreates a deadly weapon using only a paper clip, chewing gum, roll a duct tape!"
        return msg
#Another child class
class Dog(Organism):
    name="Spot"
    species="Canise"
    legs=4
    arms=0
    dna="Squence 2"
    origin="Earth"
    
    def bit(self):
        msg="\n Emits a loud, menacing growl and bites down ferociously on it's target"
        return msg
#Another child class instance
class Bacterium(Organism):
    name='X'
    species='Bacteria'
    legs=0
    arms=0
    dna="Squence C"
    origin="Mars"
    
    def replication(self):
        msg="\n the cells begin to divide and multiply into two seperate organisms"
        return msg    
    






if __name__=="__main__":
    human=Human()
    print(human.information())
    print(human.ingenuity())
    
    dog= Dog()
    print(dog.information())
    print(dog.bit())
    
    bacteria= Bacterium()
    print(bacteria.information())
    print(bacteria.replication())