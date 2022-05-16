#burası şifre yazma ve kaydetme
import secrets
sifreler_kumesi=[]
sifre_sayisi=int(input("Kaç tane şifre oluşturmak istersin?"))
for i in range(sifre_sayisi):
    sifreler=(secrets.token_urlsafe(16))
    sifreler_kumesi.insert(0, sifreler)
sifreler_kumesi.sort()
sifre=open("olusturulan_sifreler.txt", "w", encoding="utf-8")
for i in sifreler_kumesi:
    sifre.write(i+"\n")
sifre.close()
