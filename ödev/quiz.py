#quiz, zaman arada çalışmamakta
import time
import logging
import threading
import random
doru=[]
yanlis=[]
sorular=["Mor renkli, dengeyi seven Marvel kötüsü?  a)Thanos b)Vision c)Thor", "2**5?  a)16 b)32 c)2", "En yüksek dağ?  a)Everest b)Ağrı c)Himalaya", "İnek sütü hangi, hayvandan çıkar  a)keçi b)elma c)inek", "En iyi öğretmen?  a)Veysel Kaya", "www açılımı?  a)world wide web b)worıld wayd web c)dünya kadar ağ", "Olimpik yüzme havuzu kaç metre uzunluğunda?  a)50m b)55m c)60m", "Kaç dil sağdan sola yazılır?  a)10 b)11 c)12", "Nobel ödülü alan ilk kadın?  a)Marie Curie b)George Washington c)Lise Meitner", "9+10?  a)19 b)91 c)21", "Windows>Linux doğru mu?  a)evet b)hayır", "Yıldırım tanrısı?  a)zeus b)posseidon c)hades", "Güneş tanrısı?  a)fa b)re c)ra", "Piramitler nasıl yapıdlı?  a)karmaşık sistemlerle b)uzaylılar c)sihir", "Dünyadaki en iyi kelime?  a)JELİBON b)kedi c)patates", "Dünyadaki ikinci en iyi kelime?  a)jelibon b)KEDİ c)patates", "Bilgi yarışması yazmak zor iş?  a)evet b)hayır", "Kahoot çok eğlenceli?  a)evet b)hayır", "Bu ödev gerektiğinden uzun sürdü?  a)evet b)hayır", "Veysel Hoca'nın bilgisayarı ne marka?  a)lenovo b)hp c)apple"]
cevaplar=["a", "b", "a", "c", "a", "a", "a", "c", "a", "c", "a", "a", "c", "b", "a", "b", "a", "a", "a","c"]
sayac=1
def hah():
    sayac+=1
while sayac<11:
    sayı=random.randint(0,19)
    print(sayac, ". soru---->", sorular[sayı])
    k_cevap=str(input("Bu sorunun cevabı? 5 saniyen var"))
    t=threading.Timer(0.1, hah)
    t.start()
    if k_cevap==cevaplar[sayı]:
        doru.append("doğru")
        t.cancel()
    else:
        yanlis.append("yanlış")
        t.cancel()
    sayac+=1
deneme_sayisi=len(doru)
tutulan_sayi=random.randint(1,300)
print(f"1 ile 300 arasındaki sayıyı bulmak için {deneme_sayisi} kadar tahmin hakkın var, bol şans!")
while deneme_sayisi!=0:
    print(f"Şimdilik kalan deneme hakkın {deneme_sayisi}")
    a=int(input("İlk sayın kaç olsun?"))
    b=int(input("Peki ya ikinci?"))
    c=int(input("üçüncüye ne dersin?"))
    if a+b+c==tutulan_sayi:
        print("Congrqats my man, bildin")
    else:
        deneme_sayisi-=1
        print(f"Üzgünüm ama bilemedin, kalan tahmin hakkın {deneme_sayisi}")
        if deneme_sayisi==0:
            print("Kalan tahmin hakkın 0, mağlesef oyun bitti")
            break






