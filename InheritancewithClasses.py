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
        msg="\n Name: {}, \n Species: {}, \n Legs: {},\n Arms: {},\nDNA: {},\nOrigin: {},\nCarbon Based: {}".format(self.name,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
    
    






if __name__=="__main__":
    