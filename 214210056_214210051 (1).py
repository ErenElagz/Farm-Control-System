import random
from abc import ABC, abstractmethod


#Sınıflar
#Hayvan Ve Bitkilerim Tutuldugu Yerdir Tutulduğu Ana Sınıf
class Ciftlik(ABC):
    def __init__(self,isim,para):
        self._isim  = isim
        self._para  = para
        self._deger = 0

    #Toplam hayvan sayısını donduren fonksiyon
    @classmethod
    def Toplam_Hayvan_Sayisi(cls):
        return (inek._adet + koyun._adet + tavuk._adet)

    #Toplam mahsül sayısını donduren fonksiyon
    @classmethod
    def Toplam_Mahsül_Sayisi(cls):
        return (inek._adet + koyun._adet + tavuk._adet)

    #Ciftlik Hakkında İStatistikleri tutan fonksiyon
    @staticmethod    
    def Print():
        print("\nGenel Bilgiler")
        print("ciftlik degeri:",ciftlik._deger)
        print("güncel paranız:",ciftlik._para)
        for i in hayvan_listesi:
            print("\n> Hayvan           :",i._isim)
            print("> Adet             :",i._adet)
            print("> Hayvan Fiyatı    :",i._fiyat)
        
        for i in mahsul_listesi:
            print("\n> Mahsül           :",i._isim)
            print("> Adet             :",i._adet)
            print("> Mahsül Fiyatı    :",i._fiyat)

        for i in urun_listesi:
            print("\n> Hayvan           :",i._isim)
            print("> Adet             :",i._adet)
            print("> Ürün Fiyatı      :",i._fiyat)

    #Haftalık Hayvan Giderleri
    @staticmethod
    def Hayvan_Giderleri(inek_tuketim,koyun_tuketim,inek_olum,koyun_olum):
        if saman._adet >= 0:
            saman._adet = saman._adet - (inek._adet * inek_tuketim)
            saman._adet = saman._adet - (koyun._adet * koyun_tuketim)
            print("Saman Tüketimi:",((inek._adet * inek_tuketim)+(koyun._adet * koyun_tuketim)))
            print("Kaç Günlük Samanınız Kaldı?",str(int(saman._adet/((inek._adet * inek_tuketim)+(koyun._adet * koyun_tuketim)))),"Hafta")
        else:
            print("yeterli Samanınız Yok. Eğer Buğday Almazsanız Hayvanlarınız Ölmeye Başlayacak. ")
            print("Telef Olan İnek  Sayısı:",inek_olum)
            print("Telef Olan Koyun Sayısı:",koyun_olum)
            inek._adet  = inek._adet - inek_olum
            koyun._adet = koyun._adet - koyun_olum

            if inek._adet <=0:
                inek._adet = 0
                print("Hiç İneğiniz Kalmadı!")

            if koyun._adet <= 0:
                koyun._adet = 0
                print("Hiç Koyununuz Kalmadı!")

#Urunler hakkında bilgilerin tutldugu yerdir
class Envanter(ABC):
    def __init__(self,isim) -> None:
        self.isim = isim

    #Toplam urun sayısını donduren fonksiyon
    @abstractmethod
    def Toplam_Urun_Sayisi():
        return (süt._adet + yün._adet + yumurta._adet + un._adet + kumas._adet + yag._adet)

#Hayvan Objelerinin Özelliklerinin Olduğu Sınıf
class Hayvan(Ciftlik):
    def __init__(self,isim,adet,urun,uretim_kat_sayisi,fiyat):
        self._isim              = isim
        self._adet              = adet
        self._uretim_kat_sayisi = uretim_kat_sayisi
        self._fiyat             = fiyat
        self._onceki_fiyat      = 0
        self._urun              = urun
        self._haftalik_uretim   = 0

    #Hayvan Obje Bilgilerini Gosteren Fonksıyon
    def Yazdır(self):
        print("> Hayvan           :",self._isim)
        print("> Adet             :",self._adet)
        print("> Hayvan Fiyatı    :",self._fiyat)
        print("> Haftalık Üretimi :",self._uretim_kat_sayisi*self._adet,self._urun)

    #Alım Fonksiyonu
    def Alim(self):
        if ciftlik._para > 0:
            print("- - - - - - - - - - - - - - - - - - -")
            print("> Güncel",self._isim,"fiyatları:",self._fiyat)
            print("> Toplam",self._isim,"sayısı   :",self._adet)
            print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
            print("> Toplam Paranız              :",ciftlik._para,"₺")
            print("> En Fazla ALınabilecek Sayı  :",round((ciftlik._para/self._fiyat),0))

            alim_adeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik._para = ciftlik._para - (self._fiyat * alim_adeti)
            self._adet = self._adet + alim_adeti

        else:
            print("\n> Paranız Yetersiz!\n")

    #Satım Fonksiyonu
    def Satim(self):
        print("- - - - - - - - - - - - - - - - - - -")
        print("> Güncel",self._isim,"fiyatları:",self._fiyat)
        print("> Toplam",self._isim,"sayısı   :",self._adet)
        print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
        print("> Toplam Paranız              :",ciftlik._para,"₺")
        print("> En Fazla Satılabilecek Sayı :",self._adet)

        satim_adeti = int(input("Kaç Tane Satmak İstersiniz? "))

        if satim_adeti <= self._adet:
            ciftlik._para = ciftlik._para + (self._fiyat * satim_adeti)
            self._adet = self._adet - satim_adeti
        else:
            print("\n> Hata, O kadar Hayvanınız Yok.")     

#Tarla Objelerinin Özelliklerinin Olduğu Sınıf
class Tarla(Ciftlik):
    def __init__(self,isim,adet,urun,uretim_kat_sayisi,fiyat):
        self._isim              = isim
        self._adet              = adet
        self._uretim_kat_sayisi = uretim_kat_sayisi
        self._fiyat             = fiyat
        self._onceki_fiyat      = 0
        self._urun              = urun
        self._haftalik_uretim   = 0

    #Tarla Obje Bilgilerini Gosteren Fonksıyon
    def Yazdır(self):
        print("> Mahsül           :",self._isim)
        print("> Adet             :",self._adet)
        print("> Mahsül Fiyatı    :",self._fiyat)
        print("> Haftalık Üretimi :",self._uretim_kat_sayisi*self._adet,self._urun)

    #Alım Fonksiyonu
    def Alim(self):
        if ciftlik._para > 0:
            print("- - - - - - - - - - - - - - - - - - -")
            print("> Güncel",self._isim,"fiyatları:",self._fiyat)
            print("> Toplam",self._isim,"sayısı   :",self._adet)
            print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
            print("> Toplam Paranız              :",ciftlik._para,"₺")
            print("> En Fazla ALınabilecek Sayı  :",round((ciftlik._para/self._fiyat),0))

            alim_adeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik._para = ciftlik._para - (self._fiyat * alim_adeti)
            self._adet = self._adet + alim_adeti

        else:
            print("\n> Paranız Yetersiz!\n")

    #Satım Fonksiyonu
    def Satim(self):
        print("- - - - - - - - - - - - - - - - - - -")
        print("> Güncel",self._isim,"fiyatları:",self._fiyat)
        print("> Toplam",self._isim,"sayısı   :",self._adet)
        print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
        print("> Toplam Paranız              :",ciftlik._para,"₺")
        print("> En Fazla Satılabilecek Sayı :",self._adet)

        satim_adeti = int(input("Kaç Tane Satmak İstersiniz? "))

        if satim_adeti <= self._adet:
            ciftlik._para = ciftlik._para + (self._fiyat * satim_adeti)
            self._adet = self._adet - satim_adeti
        else:
            print("\n> Hata, O kadar Hayvanınız Yok.")

#Urun Objelerinin Özelliklerinin Olduğu Sınıf
class Urun(Envanter):
    def __init__(self,isim,adet,fiyat):
        self._isim              = isim
        self._adet              = adet
        self._fiyat             = fiyat
        self._onceki_fiyat      = 0

    #Urun Obje Bilgilerini Gosteren Fonksıyon
    def Yazdır(self):
        print("> Ürün   :",self._isim)
        print("> Adet   :",self._adet)
        print("> Fiyat  :",self._fiyat)

    #Alım Fonksiyonu
    def Alim(self):
        if ciftlik._para > 0:
            print("- - - - - - - - - - - - - - - - - - -")
            print("> Güncel",self._isim,"fiyatları:",self._fiyat)
            print("> Toplam",self._isim,"sayısı   :",self._adet)
            print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
            print("> Toplam Paranız              :",ciftlik._para,"₺")
            print("> En Fazla ALınabilecek Sayı  :",round((ciftlik._para/self._fiyat),0))

            alim_adeti = int(input("Kaç Tane Almak İstersiniz? "))
            ciftlik._para = ciftlik._para - (self._fiyat * alim_adeti)
            self._adet = self._adet + alim_adeti

        else:
            print("\n> Paranız Yetersiz!\n")

    #Satım Fonksiyonu
    def Satim(self):
        print("- - - - - - - - - - - - - - - - - - -")
        print("> Güncel",self._isim,"fiyatları:",self._fiyat)
        print("> Toplam",self._isim,"sayısı   :",self._adet)
        print("> Geçen Haftaki Fiyat         :",self._onceki_fiyat,"₺")
        print("> Toplam Paranız              :",ciftlik._para,"₺")
        print("> En Fazla Satılabilecek Sayı :",self._adet)

        satim_adeti = int(input("Kaç Tane Satmak İstersiniz? "))

        if satim_adeti <= self._adet:
            ciftlik._para = ciftlik._para + (self._fiyat * satim_adeti)
            self._adet = self._adet - satim_adeti
        else:
            print("\n> Hata, O kadar Hayvanınız Yok.")

    @classmethod
    def Toplam_Urun_Sayisi(cls):
        return (süt._adet + yün._adet + yumurta._adet + un._adet + kumas._adet + yag._adet)


#Fonksiyonlar
#Haftalık Fiyat Değişimini Oluşturan Fonksiyon
def Fiyatlandirma():
    for i in hayvan_listesi:
        i._onceki_fiyat = i._fiyat
        i._fiyat = round(i._fiyat * (random.uniform(0.9,1.1)),2)

    for i in mahsul_listesi:
        i._onceki_fiyat = i._fiyat
        i._fiyat = round(i._fiyat * (random.uniform(0.8,1.2)),2)

    for i in urun_listesi:
        i._onceki_fiyat = i._fiyat
        i._fiyat = round(i._fiyat * (random.uniform(0.7,1.3)),2)

#Haftalık Olarak Ürün Üretimini Sağlayan Fonksiyon
def Uretim():
    süt._adet = süt._adet + (inek._adet*inek._uretim_kat_sayisi)
    yün._adet = yün._adet + (koyun._adet*koyun._uretim_kat_sayisi)
    yumurta._adet = yumurta._adet + (tavuk._adet*tavuk._uretim_kat_sayisi)
    kumas._adet = kumas._adet + (pamuk._adet*pamuk._uretim_kat_sayisi)
    un._adet = un._adet + (bugday._adet*bugday._uretim_kat_sayisi)
    yag._adet = yag._adet + (aycicegi._adet*aycicegi._uretim_kat_sayisi)

#Tüm Hayvan Mahsül ve Ürünlerin  O Haftaki Fiyattan Toplam Değerini Oluşturan Fonksiyon
def Toplam_Ciftlik_Degeri():
    for x in hayvan_listesi,mahsul_listesi,urun_listesi:
        for y in x:
            ciftlik._deger += ( y._adet * y._fiyat )
            ciftlik_degerleme = ciftlik._deger
    return ciftlik_degerleme

#Değişkenler
hafta = 1

#Nesneler
ciftlik = Ciftlik("Ciftlik",5000)
#
inek     = Hayvan("İnek",3,"Süt",2,500)
koyun    = Hayvan("Koyun",5,"Yün",1,250)
tavuk    = Hayvan("Tavuk",7,"Yumurta",5,50)
#
pamuk    = Tarla("Pamuk",3,"Kumaş",1,100)
bugday   = Tarla("Buğday",5,"Un",5,500)
aycicegi = Tarla("Ayçiçeği",7,"Yağ",3,45)
#
süt      = Urun("Süt",0,5)
yün      = Urun("Yün",0,30)
yumurta  = Urun("Yumurta",0,2)
kumas    = Urun("Kumaş",0,60)
un       = Urun("Bugday",0,25)
yag      = Urun("Yağ",0,150)
saman    = Urun("Saman",100,5)
#
hayvan_listesi = [inek,koyun,tavuk]
mahsul_listesi = [pamuk,bugday,aycicegi]
urun_listesi   = [süt,yün,yumurta,kumas,un,yag,saman]


#Ana Döngü
while True:
    print("\n------------------------------------------------")
    print("Çiftlik Kontrol ve Otomasyon Sistemi")
    print("------------------------------------------------")
    print("> 1: Çiftliğim")
    print("> 2: Pazar Yeri")
    print("> 3: Güncel Ürün Fiyatları")
    print("> 4: Bir Sonraki Hafta",hafta,". hafta")
    print("> 5: Nasıl Oynanır?")
    print("> 0: Çıkış\n")
    anasayfa_sayfa = int(input("Sayfa Numarası Giriniz: "))

    #Çıkış
    if   anasayfa_sayfa == 0:
        break
    
    #Çiftliğim
    elif anasayfa_sayfa == 1:
        while True:
            print("\nÇiftliğim")
            print("-------------------------------")
            print("> 1: Ahır")
            print("> 2: Tarla")
            print("> 3: Envanter")
            print("> 4: İstatistikler")
            print("> 0: Geri\n")
            ciftligim_sayfa = int(input("Sayfa Numarası Giriniz: "))

            #Çıkış
            if  ciftligim_sayfa == 0:
                break

            #Ahır
            elif ciftligim_sayfa == 1:
                print("\n-------------------------------")
                print("Ahır\n")
                for i in hayvan_listesi:
                    i.Yazdır()
                    print("-------------------------------")

            #Tarla
            elif ciftligim_sayfa == 2:
                print("\n-------------------------------")
                print("Tarla\n")
                for i in mahsul_listesi:
                    i.Yazdır()
                    print("-------------------------------")

            #Envanter
            elif ciftligim_sayfa == 3:
                print("\n-------------------------------")
                print("Envanter\n")
                for i in urun_listesi:
                    i.Yazdır()
                    print("-------------------------------")

            #İstatistikler
            elif ciftligim_sayfa == 4:
                print("\n-------------------------------")
                print("Toplam Para",ciftlik._para)
                print("Toplam Ciftlik.Degeri:",Toplam_Ciftlik_Degeri())
                print("-------------------------------")
                print("Toplam Hayvan Sayısı:",Ciftlik.Toplam_Hayvan_Sayisi())
                print("Toplam Mahsül Sayısı:",Ciftlik.Toplam_Mahsül_Sayisi())
                print("Toplam Ürün Sayısı  :",Envanter.Toplam_Urun_Sayisi())
                print("-------------------------------\n")
                ciftlik.Print()

            #Hata
            else:
                print("\n> Geçerli Bir Değer Giriniz!\n")        

    #Pazar Yeri
    elif anasayfa_sayfa == 2:
        while True:
            print("\nPazar Yeri")
            print("-------------------------------")
            print("> 1: Alım ")
            print("> 2: Satım")
            print("> 0: Geri\n")
            pazar_yeri_sayfa = int(input("Sayfa Numarası Giriniz: "))

            #Geri
            if  pazar_yeri_sayfa == 0:
                break

            #Alim
            elif pazar_yeri_sayfa == 1:
                alim = 1
                print("- - - - - - - - - - - -")
                print("Hayvan Pazarı")
                for i in hayvan_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                print("- - - - - - - - - - - -")
                print("Meyve Sebze Hali")
                for i in mahsul_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                print("- - - - - - - - - - - -")
                print("Organik Dükkanı")
                for i in urun_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                alim_secimi = int(input("Sayfa Numarası Giriniz: "))

                if alim_secimi == 1:
                    inek.Alim()

                elif alim_secimi == 2:
                    koyun.Alim()

                elif alim_secimi == 3:
                    tavuk.Alim()

                elif alim_secimi == 4:
                    pamuk.Alim()

                elif alim_secimi == 5:
                    bugday.Alim()

                elif alim_secimi == 6:
                    aycicegi.Alim()

                elif alim_secimi == 7:
                    süt.Alim()

                elif alim_secimi == 8:
                    yün.Alim()

                elif alim_secimi == 9:
                    yumurta.Alim()

                elif alim_secimi == 10:
                    kumas.Alim()

                elif alim_secimi == 11:
                    un.Alim()

                elif alim_secimi == 12:
                    yag.Alim()

                elif alim_secimi == 13:
                    saman.Alim()

                else:
                    print("\n> Geçerli Bir Değer Giriniz!\n")
                
            #Satım
            elif pazar_yeri_sayfa == 2:
                alim = 1
                print("- - - - - - - - - - - -")
                print("Hayvan Pazarı")
                for i in hayvan_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                print("- - - - - - - - - - - -")
                print("Meyve Sebze Hali")
                for i in mahsul_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                print("- - - - - - - - - - - -")
                print("Organik Dükkanı")
                for i in urun_listesi:
                    print(">",alim,":",i._isim)
                    alim = alim + 1
                print("- - - - - - - - - - - -")

                alim_secimi = int(input("Sayfa Numarası Giriniz: "))

                if alim_secimi == 1:
                    inek.Satim()

                elif alim_secimi == 2:
                    koyun.Satim()

                elif alim_secimi == 3:
                    tavuk.Satim()

                elif alim_secimi == 4:
                    pamuk.Satim()

                elif alim_secimi == 5:
                    bugday.Satim()

                elif alim_secimi == 6:
                    aycicegi.Satim()

                elif alim_secimi == 7:
                    süt.Satim()

                elif alim_secimi == 8:
                    yün.Satim()

                elif alim_secimi == 9:
                    yumurta.Satim()

                elif alim_secimi == 10:
                    kumas.Satim()

                elif alim_secimi == 11:
                    un.Satim()

                elif alim_secimi == 12:
                    yag.Satim()

                elif alim_secimi == 13:
                    saman.Satim()

                else:
                    print("\n> Geçerli Bir Değer Giriniz!\n")                

    #Güncel Ürün Fiyatları
    elif anasayfa_sayfa == 3:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("> Hayvan      Adet      Fiyat        Önceki Fiyat")
        print("- - - - - - - - - - - - - - - - - - - - - - -")
        for i in hayvan_listesi:
            print(">",i._isim,"     ",i._adet,"      ",i._fiyat,"        ",i._onceki_fiyat)
        print("- - - - - - - - - - - - - - - - - - - - - - -")

        print("- - - - - - - - - - - - - - - - - - - - - - -")
        print("> Mahsül      Adet      Fiyat        Önceki Fiyat")
        print("- - - - - - - - - - - - - - - - - - - - - - -")
        for i in mahsul_listesi:
            print(">",i._isim,"     ",i._adet,"      ",i._fiyat,"        ",i._onceki_fiyat)
        print("- - - - - - - - - - - - - - - - - - - - - - -")

        print("- - - - - - - - - - - - - - - - - - - - - - -")
        print("> Urun        Adet      Fiyat         Önceki Fiyat")
        print("- - - - - - - - - - - - - - - - - - - - - - -")
        for i in urun_listesi:
            print(">",i._isim,"     ",i._adet,"       ",i._fiyat,"         ",i._onceki_fiyat)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    #Bir Sonraki Hafta
    elif anasayfa_sayfa == 4:
        Fiyatlandirma()
        Uretim()
        ciftlik.Hayvan_Giderleri(2,1,1,2)
        hafta = hafta + 1 

    #Nasıl Oynanır?
    elif anasayfa_sayfa == 5:
        print("\n\nYapımcılar: Eren Elagöz,Alper Diler")
        print("Ciftlik Oyunu ,bir ahır birde tarlanızın  olduğu küçük bir çiftlikte başlar.\nVe oyuna birkac hayvan birkac tarla ve 5000₺ ile başlarsınız.")
        print("Amacınız Her Hafta Üretim yapıp ve elde ettiginiz ürünleri pazar yerinde sattiğınız ve elde ettiğiniz parayla yatırım yaptığınız bir oyun")
        print("Fakat Herşey bu kadar basit değil! Her hafta fiyatlar değişiyor bazen fiyatlar çakılıyor bazende uçabiliyor")
        print("Peki ya şimdi sıra sizde elindekileri satacak mısın? bekleyecek misin? \n\n")

    #Hata
    else:
        print("\n> Geçerli Bir Değer Giriniz!\n")
