import mathplotlib.pyplot as plt

fichier_1 = open(input("entrer nom fichier pour axe x"),"r")
fichier_2 = open(input("entrer nom fichier pour axe y"),"r")
tailles_fenetre = int(input("entrer la taille de la fenetre"))

ligne_x = fichier_1.readline()
stockage_x = ""
while ligne_x !="":
    stockage_x += ligne_x[:len(ligne_x)-1]
    ligne_x = fichier_1.readline()

ligne_y = fichier_2.readline()
stockage_y = ""
while ligne_y !="":
    stockage_y += ligne_y[:len(ligne_y)-1]
    ligne_y = fichier_2.readline()

fichier_1.close(),fichier_2.close()


plt.title("Dot Plot") # titre du graphique
plt.xlabel("Axe X") # label/nom de l'axe des abscisses
plt.ylabel("Axe Y") # label/nom de l'axe des des ordonnees
plt.xlim(0, len(stockage_x)) # taille/longueur de l'axe des "x"
plt.ylim(0, len(stockage_y)) # taille/longueur de l'axe des "y"
point_x = 0
point_y = 0
while point_x < len(stockage_x)-1:
    while point_y < len(stockage_y)-1:
        if stockage_x[point_x:(point_x+tailles_fenetre)-1] == stockage_y[point_y:(point_y+tailles_fenetre)-1]:
            plt.scatter(point_x,point_y, c="red", s=15)
        point_y += 1
    point_y = 0
    point_x += 1
plt.savefig("TD7.png")
plt.show()   
