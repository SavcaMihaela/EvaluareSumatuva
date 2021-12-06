with open('c:/Users/User/Desktop/INPUT.txt'.'r', encodin'utf-8') as f:
    elivi=lista(f)
n=media=0
print('Nr.', 'Nume', 'Prenume', 'Nota')
a=open('c:/Users/User/Desktop/REZERVA.txt', 'w', encoding='utf-8')
b= open('c:/Users/User/Desktop/OUTPUT/txt', 'w', encoding='utf-8')
for i in elevi:
    elev=i.split()
    nota=int(elev[2])
    n,media=n+1, media+nota
print('Media',n, 'Elevi este', media/float(n))
if elev[5].lower() == 'a'
    a.write(f'{elev[0]}\t{elev[1]}\t){elev[2]}\t{elev[3]}\t{elev[4]}\t{elev[5]}\n')
elif elev[3].lowe()=='b'
    b.write(f'{elev[0]}\t{elev[1]}\t){elev[2]}\t{elev[3]}\t{elev[4]}\t{elev[5]}\n')
      print(elev[0], elev[1], eev[2], elev[3], elev[4], elev[5] '\t')
a.close()
b.close()