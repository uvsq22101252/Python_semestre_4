import matplotlib.pyplot as plt

def dotplot(seq1,seq2,fenetre,identité):
    fichier_1 = open(seq1,"r")
    fichier_2 = open(seq2,"r")
    tailles_fenetre = int(fenetre)

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
    
    for x in range(0,len(stockage_x)-1):
        for y in range(0,len(stockage_y)-1):
            print((y+tailles_fenetre)-1)
            if stockage_x[x:(x+tailles_fenetre)-1]== stockage_y[y:(y+tailles_fenetre)-1]:
                plt.scatter(x,y, c="red", s=15)
    
    plt.savefig("TD7.png")
    plt.show()



def pidentité(x,y):
    id= 0
    for i in range(0,len(x)-1):
        if x[i]==y[i]:
            id+=1
    pourcentage_id = (id // len(x))* 100
    return pourcentage_id

dotplot("seqx.txt","seqy.txt",2,0)

# and pidentité(stockage_x[point_x:(point_x+tailles_fenetre)-1],stockage_y[point_y:(point_y+tailles_fenetre)-1])> identité

