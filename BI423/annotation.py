debut = 0
while seq.find(motif,debut)!=-1:
    position = seq.find(motif,debut)
    print(position)
    debut = position + 1