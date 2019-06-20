def chickens_dogs(number_of_heads,number_of_legs):
    #n=number[number_of_heads,number_of_legs]
    for numchicks in range(number_of_heads+1):
        #number_of_chickens,number_of_dogs
        total_animal=number_of_dogs+number_of_chickens
        if 2*number_of_chickens+4*number_of_dogs==Totalegs:
            return [number_of_chickens,number_of_dogs]
        return None
        
        Totalanimal=2*number_of_chickens+2*number_of_dogs
        number_of_dogs=(Totalegs-total_animal)
        number_of_chickens=total_animal-number_of_dogs
        return[number_of_chickens,number_of_dogs]
#dogs,chicks=chickens_dogs(heads,legs)
print(chickens_dogs(5,12))
def solve(numheads,numlegs):
    for number_of_chickens in range(numheads+1):
        number_of_dogs=numheads-number_of_chickens
        if 2*number_of_chickens+4* number_of_dogs==numlegs:
            return [number_of_chickens,number_of_dogs]
    return None
#print(solve(5,12))
        