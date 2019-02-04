import os

# Creer une classe Labyrinth qui dans son constructeur 
# ouvre le fichier texte et stocke chaque ligne dans une liste


class Labyrinth:
    def __init__(self, data_file):
        self.file = data_file
        self.store_lines = []

        with open(self.file) as files:
            lines = files.readlines()
            for y in lines:
                x = [i for i in y.strip()]
                self.store_lines.append(x)

    
    def __str__(self):
        list_labyrinth = self.store_lines
        str1 = '\n'.join(str(''.join(e)) for e in list_labyrinth)

        return str1

laby = Labyrinth('labyrinth.txt')

