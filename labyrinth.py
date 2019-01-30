import os

# Creer une classe Labyrinth qui dans son constructeur 
# ouvre le fichier texte et stocke chaque ligne dans une liste

class Labyrinth:
    file = ""

    def __init__(self, data_file):
        self.file = data_file

    def launch_labyrinth(self):
        x = []
        with open(self.file) as files:
            lines = files.readlines()
        for line in lines:
            print(line)
            y = [i for i in line.strip()]
            x.append(y)

        return(x)
    
    def __str__(self):
        return str(self.launch_labyrinth())
    

laby = Labyrinth('labyrinth.txt')

