
import altKumeMain,altKumeFonksiyonlar


def fonksiyon():
    for i in range(0, len(altKumeFonksiyonlar.liste2)):
        for j in range(0, len(altKumeFonksiyonlar.liste2[i])):
            altKumeMain.toplam += int(altKumeFonksiyonlar.liste2[i][j])
        print(altKumeFonksiyonlar.liste2[i], ":", altKumeMain.toplam)
        altKumeFonksiyonlar.karsilastir(altKumeFonksiyonlar.liste2[i], altKumeMain.toplam)
        altKumeMain.toplam = 0