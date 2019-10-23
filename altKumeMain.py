

import altKume,altKumeFonksiyonlar

print("Değer eklemek için '+' yı, listeyi bitirmek için herhangi bir tuşa basın.")



kume=altKume.Kume()
while(True):
    islem = input("İşlem seçiniz:")

    if (islem == "+"):

        try:
         deger = int(input("Sayı giriniz:"))
         kume.liste.append(deger)

        except ValueError:
            print("Rakam olmayan bir ifade girdiniz.")

    else:
        print("Liste eleman ekleme işlemi tamamlandı.")
        break


print("Liste elemanları:",kume.durum())




altKumeFonksiyonlar.altKumeler(kume.liste,len(kume.liste))


print("Alt kümeler  Toplamları")
altKumeFonksiyonlar.fonksiyon()

if(len(altKumeFonksiyonlar.en_buyuk_liste)==1):
  altKumeFonksiyonlar.en_buyuk_liste=altKumeFonksiyonlar.en_buyuk_liste[0]



print("Toplamı en büyük liste",altKumeFonksiyonlar.en_buyuk_liste)
print("Toplamı",altKumeFonksiyonlar.en_buyuk_toplam)




