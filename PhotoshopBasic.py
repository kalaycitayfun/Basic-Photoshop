'''
Created on 1 May 2018

@author: AsusNB
'''
import os
import sys
import time
from PIL import Image, ImageFilter, ImageEnhance

varsayılan = os.getcwd()
img_list = []  # Resim isimleri bu listede.


class psB():
    def list_add(self):
        while True:
            x = input("Resim İsmi(Örn: img.jpg): ")
            if x == 'Q':
                break
            else:
                if x in os.listdir():
                    img_list.append(x)
                    print('Resim Eklendi!\n')
                    break

                else:
                    sys.stderr.write('Bu Kökdizininde Böyle Bir Resim Yok!\n')
                    sys.stderr.flush()
                    continue

    def open_list(self):
        print("Resim Listesi:")
        if len(img_list) > 0:
            for i in img_list:
                print(i)
        else:
            sys.stderr.write('Listede Hiç Resim Yok , Resim Ekle!')
            sys.stderr.flush()

    def open_photo(self):
        print("Resim Listesi:")
        if len(img_list) > 0:
            for i in img_list:
                print(i)
            x = input('Resim Sec: ')
            if x in img_list:
                img1 = Image.open(x).show()
            else:
                sys.stderr.write('Hatalı Girdi')
                sys.stderr.flush()
        else:
            sys.stderr.write('Listede Hiç Resim Yok , Resim Ekle!')
            sys.stderr.flush()

    def dosya_konumu(self):
        global varsayılan
        print('\nŞuanki Dosya Konumu: ', varsayılan)
        while True:
            x = input('\n0-Konuma Bak\n1-Konumu Değiştir\n2-Konuma Git\n3-Klasör Oluştur\n4-Çıkış İçin:Q\nSecenek: ')
            if x == '0':
                print('\nDosya Konumu: ', varsayılan)
            elif x == '1':
                varsayılan = input("Kayıt Adresi(Örn: C:/Users/AsusNB/Desktop): ")
                print('Dosya Konumu Değiştirildi!')
            elif x == '2':
                os.startfile(varsayılan)
            elif x == '3':
                try:
                    name = input('Klasör İsmi: ')
                    dizin = input("Kayıt Adresi(Örn: C:/Users/AsusNB/Desktop): ")
                    varsayılan = dizin + '/' + name
                    os.mkdir(varsayılan)
                    print('Klasör Oluşturuldu, Yeni Kayıt Yeri Ayarlandı.')
                except:
                    sys.stderr.write('Kökdizini Adresi Eksik veya Hatalı Girildi, Tekrar Dene!\n')
                    sys.stderr.flush()
            else:
                break

    def rotate(self, r=0):
        x = input('Döndürme İşlemi Uygulanacak Resmi Secin: ')
        if x in img_list:
            img2 = Image.open(x)
            s = input("Resim Kaydedilsin mi? (E/H): ")
            if s == 'E':
                name = input('Resim Yeni İsmi: ')
                print("\nResim {} Derece Döndürüldü ve Kaydedildi!\nKayıtlı Olduğu Dizin Açılıyor.".format(r))
                time.sleep(2)
                img2.rotate(r).save(name + str(r) + ".jpg")
                os.startfile(varsayılan)
            elif s == 'H':
                print("Resim {} Derece Döndürüldü ve Resim Açılıyor".format(r))
                time.sleep(2)
                img2.rotate(r).show()
            else:
                sys.stderr.write('Hatalı Secenek')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İsmi Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def convert(self):
        x = input("\n1-Siyah-Beyaz Yap\n2-RGB Yap\nSecenek: ")
        y = input('\nFiltre İşlemi Uygulanacak Resmi Secin: ')
        if y in img_list:
            img3 = Image.open(y)
            if x == '1':
                s = input("Resim Kaydedilsin mi? (E/H): ")
                if s == 'E':
                    name = input('Resim Yeni İsmi: ')
                    print("\nSiyah-Beyaz Filtre Uygulandı ve Kaydedildi!\nKayıtlı Olduğu Dizin Açılıyor.")
                    time.sleep(2)
                    img3.convert(mode='L').save(name + ".jpg")
                    os.startfile(varsayılan)
                elif s == 'H':
                    print("\nSiyah-Beyaz Filtre Uygulandı ve Resim Açılıyor")
                    time.sleep(2)
                    img3.convert(mode='L').show()
                else:
                    sys.stderr.write('Hatalı Secenek')
                    sys.stderr.flush()
            elif x == '2':
                s = input("Resim Kaydedilsin mi? (E/H): ")
                if s == 'E':
                    name = input('Resim Yeni İsmi: ')
                    print("\nRGB Filtre Uygulandı ve Kaydedildi!\nKayıtlı Olduğu Dizin Açılıyor.")
                    time.sleep(2)
                    img3.convert(mode='RGB').save(name + ".jpg")
                    os.startfile(varsayılan)
                elif s == 'H':
                    print("\nRGB Filtre Uygulandı ve Resim Açılıyor")
                    time.sleep(2)
                    img3.convert(mode='RGB').show()
                else:
                    sys.stderr.write('Hatalı Secenek')
                    sys.stderr.flush()
            else:
                sys.stderr.write('Hatalı Secenek')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İSmi Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def blur(self, b):
        y = input('\Blur İşlemi Uygulanacak Resmi Secin: ')
        if y in img_list:
            img4 = Image.open(y)
            s = input("Kaydedilsin mi? (E/H): ")
            if s == 'E':
                name = input('Resim Yeni İsmi: ')
                print("\nResime Blur Yapıldı ve Kaydedidi!\nKayıtlı Olduğu Dizin Açılıyor.")
                time.sleep(2)
                img4.filter(ImageFilter.GaussianBlur(b)).save(name + ".jpg")
                os.startfile(varsayılan)
            elif s == 'H':
                print("Resime Blur Yapıldı ve Resim Açılıyor.")
                time.sleep(2)
                img4.filter(ImageFilter.GaussianBlur(b)).show()
            else:
                sys.stderr.write('Hatalı Secenek!')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İsmi Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def point(self, p):
        y = input('\nParlaklık  İşlemi Uygulanacak Resmi Secin: ')
        if y in img_list:
            img5 = Image.open(y)
            s = input("Kaydedilsin mi? (E/H): ")
            if s == 'E':
                name = input('Resim Yeni İsmi: ')
                print("\nResmin Parlaklığı Ayarlandı ve Kaydedidi!\nKayıtlı Olduğu Dizin Açılıyor.")
                time.sleep(2)
                img5.point(lambda i: i * p).save(name + ".jpg")
                os.startfile(varsayılan)
            elif s == 'H':
                print("Resmin Parlaklığı Ayarlandı ve Resim Açılıyor.")
                time.sleep(2)
                img5.point(lambda i: i * p).show()
            else:
                sys.stderr.write('Hatalı Secenek!')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İsm0i Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def enhance(self, e):
        y = input('\nKontrast İşlemi Uygulanacak Resmi Secin: ')
        if y in img_list:
            img6 = Image.open(y)
            img7 = ImageEnhance.Contrast(img6)
            s = input("Kaydedilsin mi? (E/H): ")
            if s == 'E':
                name = input('Resimin Yeni İsmi: ')
                print("\nResmin Kontrastı Ayarlandı ve Kaydedidi!\nKayıtlı Olduğu Dizin Açılıyor.")
                time.sleep(2)
                img7.enhance(e).save(name + ".jpg")
                os.startfile(varsayılan)
            elif s == 'H':
                print("Resmin Kontrastı Ayarlandı ve Resim Açılıyor.")
                time.sleep(2)
                img7.enhance(e).show()
            else:
                sys.stderr.write('Hatalı Secenek!')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İsmi Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def crop(self, x0, y0, x1, y1):
        y = input('\nKırpma İşlemi Uygulanacak Resmi Secin: ')
        if y in img_list:
            img8 = Image.open(y)
            s = input("Kaydedilsin mi? (E/H): ")
            if s == 'E':
                name = input('Resimin Yeni İsmi: ')
                print("\nKırpma İşlemi Yapıldı ve Kaydedidi!\nKayıtlı Olduğu Dizin Açılıyor.")
                time.sleep(2)
                img8.crop((x0, y0, x1, y1)).save(name + ".jpg")
                os.startfile(varsayılan)
            elif s == 'H':
                print("Kırpma İşlemi Yapıldı ve Resim Açılıyor.")
                time.sleep(2)
                img8.crop((x0, y0, x1, y1)).show()
            else:
                sys.stderr.write('Hatalı Secenek!')
                sys.stderr.flush()
        else:
            sys.stderr.write('Girilen Resim İsmi Listede Kayıtlı Değil!')
            sys.stderr.flush()

    def open_g(self):
        print("Dosya Konumu: ", varsayılan)
        os.startfile(varsayılan)


def hakkında():
    sys.stderr.write("""
[T]=================================[K]
|                                     |
|  Photoshop Basic Açık Kaynak Kodlu  |
|   Bir Resim Düzenleme Programıdır   |
|                                     |
|       power by: Tayfun Kalaycı      |
|=====================================|
         """)
    sys.stderr.flush()


def tablo():
    print("""
[T]========================[K]
|                            |
| Photoshop Basic Programına |
|       Hoşgeldiniz!         |
|                            |
| 0- Listeye Resim Ekle      |
| 1- Resim Listesini Aç      |
| 2- Eklenmiş Resim Aç       |
| 3- Kayıt Konum Ayarı       |
| 4- Resmi Döndür            |
| 5- Renk Ayarları           |
| 6- Blur Ayarı              |
| 7- Parlaklık Ayarı         |
| 8- Kontrast Ayarı           |
| 9- Resim Kırp              |
|                            |
| Resim Galerisi: P          |
| Hakkında: H                |
| Tabloyu Yazdır: T          |                           
| Çıkış İçin: Q              |
|                            |
|============================|
          """)


ps_basic = psB()

tablo()
time.sleep(5)

while True:
    x = input('\nLütfen Bir Secenek Secin(Exit:Q): ')
    if x == 'Q':
        sys.stderr.write("Kullandığınız için teşekkürler.\nTayfun KALAYCI")
        sys.stderr.flush()
        break
    elif x == '0':
        ps_basic.list_add()
    elif x == '1':
        ps_basic.open_list()
    elif x == '2':
        ps_basic.open_photo()
    elif x == '3':
        ps_basic.dosya_konumu()
    elif x == '4':
        derece = int(input('Kaç Derece Dönecek(Örn: 90): '))
        ps_basic.rotate(derece)
    elif x == '5':
        ps_basic.convert()
    elif x == '6':
        blur_oranı = int(input('Blur Oranı(Örn: 0,1,2...): '))
        ps_basic.blur(blur_oranı)
    elif x == '7':
        parlaklık = float(input('Parlaklık Oranı(Örn: 2.5): '))
        ps_basic.point(parlaklık)
    elif x == '8':
        kontrast = float(input('Kontrast Oranı(Örn: 2.5): '))
        ps_basic.enhance(kontrast)
    elif x == '9':
        x0 = int(input('x0: '))
        y0 = int(input('y0: '))
        x1 = int(input('x1: '))
        y1 = int(input('y2: '))
        ps_basic.crop(x0, y0, x1, y1)
    elif x == 'P':
        ps_basic.open_g()
    elif x == 'T':
        tablo()
    elif x == 'H':
        hakkında()
    else:
        sys.stderr.write('Hatalı Secenek!')
        sys.stderr.flush()
        continue
