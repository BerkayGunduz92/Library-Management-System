class library:
    def __init__(self, dosya_adı='books.txt' ) -> str:
        self.dosya_adı = dosya_adı
        self.dosya = open (self.dosya_adı, 'a+', encoding='utf-8')
        print('Dosya başarılı bir şekilde açıldı')
        
        
    def kitap_ekle(self):
        """ 'txt' Dosyasına Kitap Ekleme Fonksiyonu.
        
        Kullanıcıdan kitap ismi,yazar ismi,sayfa sayısı ve yayın tarihini istiyoruz.
        Kitap ve yazar ismimlerini baş harfleri büyük olacak şekilde değişkene atama yapıyoruz.
        'writeline' komutu ile açık olan 'txt' dosyasına liste şekilde bir değişken yazıyoruz.
        """
        self.kitap_adi = input('Kitap adını giriniz: ').title()
        self.yazar = input('Yazarını giriniz: ').title()
        self.sayfa_sayisi = input('Sayfa sayısını giriniz: ')
        self.yayin_tarihi = input('Yayın yılını giriniz: ')
        self.dosya.writelines(['Kitap Adı: ', self.kitap_adi, ',', ' Yazar: ', self.yazar, ',', 
                               ' Sayfa Sayısı: ', self.sayfa_sayisi, ',', ' Yayın Tarihi: ', self.yayin_tarihi, '\n'])
        
        
    def listele(self):
        """Kitap Listeleme Foksiyonu.
        
        Bu foksiyonda açk olan 'txt' dosyasından bütün kitapları okuyup,bir değişkene atıyoruz.
        Dosyadaki kitapların sadece kitap ve yazar adı olacak şekilde ekrana basıyoruz.
        Eğer dosyada kayıtlı kitap yok ise 'Kütüphanede gösterilecek bir kitap bulunmamaktadır.' şeklinde bir yazı basılıyor.
        
        """
        self.dosya.seek(0)
        liste = self.dosya.read()
        t = liste.splitlines()
        if len(t) == 0:
            print('Kütüphanede gösterilecek bir kitap bulunmamaktadır.')
        else:
            for i in t:
                k = i.split(',')
                print(k[0], ',', k[1])

    def kitap_sil(self):
        """ 'txt' Dosyasından Kitap Silme.
        
        Silinecek kitap ismini kullanıcıdan alarak baş harfleri büyük olacak şekilde değişkene atama yapılıyor.
        Girilen kitap ismi ve indek numarası döngü sayesinde listeye kaydediliyor.
        Eğer girilen kitap ismiyle eşleşen bir kitap yok ise !kitap bulunmadı' yazısı ekrana bastırılıyor.
        Eğer eşleşen bir tane kitap varsa listeden kaldırılıp dosya temizlenmip yeni liste dosyaya yazılıyor.
        Eğer aynı isme sahip birden fazla kitap varsa bu kitaplar ekrana bastırılıp, silinecek kitap seçtiriliyor.
        Seçim sucuna göre kitap silme işlemi yapılıyor.
        
        """
        eleman_indeksi = []
        silinecek_kitap = []
        silinen_kitap = []
        self.kitap_adi = input('Silmek istediğiniz kitabın adını yazınız: ').title()
        self.dosya.seek(0)
        liste = self.dosya.read()
        t = liste.splitlines()
        for indeks,alt_liste in enumerate(t):
            if alt_liste.startswith(f'Kitap Adı: {self.kitap_adi}'):
                eleman_indeksi.append(indeks)
                silinecek_kitap.append(alt_liste)
        if len(eleman_indeksi) == 0:
            print(f'{self.kitap_adi} adlı kitap bulunamadı')
        elif len(eleman_indeksi) == 1:
            silinen_kitap = t.pop(eleman_indeksi[0])
            print(f'{silinen_kitap} listeden başarılı bir şekilde silindi.')
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines('\n'.join(t))
            self.dosya.write('\n')
        else:
            secilecek_kitaplar = [f"{i + 1}-){eleman.split(',')[0]} , {eleman.split(',')[1]}" for i, eleman in enumerate(silinecek_kitap)]
            tek_yazi = '\n'.join(secilecek_kitaplar)
            print('\n')
            print(tek_yazi,'\n')
            while True:
                try:   
                    x =int( input("""Aynı isme sahip birden fazla kitap bulundu.
Lütfen silmek istediğiniz kitabın solundaki numarayı giriniz: """))
                    if x > 0 and x <= len(silinecek_kitap):
                        break
                    else:
                        print('\n*******************************')
                        print('Lüffen doğru aralıkta sayı giriniz.')
                        print(' *******************************')
                except:
                    print('\n**************************************************')
                    print('Doğru bir kodlama yapmadınız.lütfen tekrar deneyiniz.')
                    print(' **************************************************')
                print('\n')
                print(tek_yazi)
                print('\n')
            silinen_kitap = t.pop(eleman_indeksi[x-1])
            print(f'{silinen_kitap} listeden başarılı bir şekilde silindi.')
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines('\n'.join(t))
            self.dosya.write('\n')    
        
    def __del__(self):
        if self.dosya:
            self.dosya.close()
            print(f"{self.dosya_adı} closed successfully.")
    
        
lib = library()
while True:
    print('\n')
    print("""***Seçim Menüsü***
1-) Kitapları Listele
2-) Kitap Ekle
3-) Kitap Çıkar
q-) Menüden Çık""")
    giriş = input('Yapmak istedğiniz işlemi seçiniz: ')
    print('\n')
    if giriş == '1':
        lib.listele()
    elif giriş == '2':
        while True:
            seçim_onaylama = input('Kitap ekleme işlemine devam etmek için 1\'i ana menüye dönmek için 9\'u tuşlayınız: ')
            if seçim_onaylama == '1':
                lib.kitap_ekle()
                break
            elif seçim_onaylama == '9':
                break
            else:
                print('\nHatalı tuşlama yaptınız.Lüften yapmak istediğiniz işlemi yeniden giriniz.\n')
    elif giriş == '3':
        while True:
            seçim_onaylama = input('Kitap silme işlemine devam etmek için 1\'i ana menüye dönmek için 9\'u tuşlayınız: ')
            if seçim_onaylama == '1':
                lib.kitap_sil()
                break
            elif seçim_onaylama == '9':
                break
            else:
                print('\nHatalı tuşlama yaptınız.Lüften yapmak istediğiniz işlemi yeniden giriniz.\n')
    elif giriş == 'q' or giriş == 'Q':
        break
    else:
        print('Yanlış tuşlama yaptınız!!!Lütfen seçiminizi tekrarlayınız!!!')
    