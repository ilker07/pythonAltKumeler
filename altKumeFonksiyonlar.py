
import math


en_buyuk_liste=[]
liste2=[]
en_buyuk_toplam=0
def dogruMu(sayi):
    d = bin(sayi)
    d = d.lstrip("0b")

    for index in range(0,len(d)-1):
        if(index!=len(d) and len(d)!=1):
          if(int(d[index])==1 and int(d[index+1])==1):
             return False

    return True

def altKumeler(arr, n):
    liste = []
    boyut = math.pow(2, n)

    for sayici in range(1, (int)(boyut)):
        for j in range(0, n):


            if (sayici & (1 << j) and dogruMu(sayici)):

                liste.append(arr[j])
        if(len(liste) !=0 and len(liste) !=1):
            liste2.append(liste)


        liste=[]

def karsilastir(gelen_liste,gelen_toplam):
    global en_buyuk_toplam
    global en_buyuk_liste


    if(gelen_toplam > en_buyuk_toplam):

        en_buyuk_toplam = gelen_toplam
        en_buyuk_liste=[]
        en_buyuk_liste.append(gelen_liste)

    elif (gelen_toplam == en_buyuk_toplam):

        en_buyuk_liste.append(gelen_liste)


def fonksiyon():
    toplam=0
    for i in range(0, len(liste2)):
        for j in range(0, len(liste2[i])):
            toplam += int(liste2[i][j])
        print(liste2[i], ":",toplam)
        karsilastir(liste2[i],toplam)
        toplam = 0

