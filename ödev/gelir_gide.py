#gelir gider kodları
gelirler=[]
giderler=[]
sayi=int(input("kaç adet veri girmek istersiniz?"))
for i in range(sayi):
    gelir_gider=int(input("Eğer gelir eklemek istiyorsan 5'i, gider eklemek istiyorsan 6'yı tuşla"))
    if gelir_gider==5:
        a=input("eklemek istediğin gelirin miktarı ve ismi nedir? LÜTFEN ÖNCE MİKTARI GİRİNİZ")
        gelirler.insert(0, a)
    elif gelir_gider==6:
        b=input("eklemek istediğin giderin miktarı ve ismi nedir? LÜTFEN ÖNCE MİKTARI GİRİNİZ")
        giderler.insert(0, b)
    else:
        print("Birdahakine geçerli bir veri girdiğinden emin ol")
        break
gelirler.sort()
giderler.sort()
c=int(input(f"Ailenin gelirleri --{gelirler}-- giderleri ise --{giderler}--'dir. Gelirlerden bir veri görmek istersen 2'i, giderlerden bir veri görmek istersen 3'yı tuşla"))
if c==2:
    d=int(input("Kaçıncı geliri çağırmak istersiniz?"))
    e=d-1
    print("Bu geliri çağırdınız", "__"gelirler[e]"__")
elif c==3:
    d=int(input("Kaçıncı geliri çağırmak istersiniz?"))
    e=d-1
    print("Bu gideri çağırdınız", "__"gelirler[e]"__")
else:
    print("BURAYA KADAR GELİP YANLIŞ BASMIŞ OLMASLISIN!!! BİRDAHAKİNE DAHA DİKKATLİ OL!!!")