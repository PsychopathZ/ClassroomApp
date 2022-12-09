import random

while True:
    print("""

    
[1] Öğrenci seç
[2] Seçilenler listesini temizle
[3] Çıkış Yap
    
    """)

    secim = input('> ')

    if secim == '1':
        try:
            secilenler = open('secilenler.txt', 'r', encoding='utf-8').read().splitlines()
            ogrenciler = ['OMER', 'IREM', 'AHMET', 'ZUMRA', 'BURAK', 'NEHIR', 'CEREN', 'OYKU', 'BEYZA', 'AZRA', 'GUL', 'SONER', 'BEYTULLAH', 'RESUL', 'BEGUM', 'MUHAMMED', 'ZEYNEP',  'EFE', 'FATIN', 'AYSENAZ', 'ZEYNEP Y', 'DENIZALI', 'EGE', 'ZEHRA', 'CANER', 'ASLI', 'SEVIL', 'ECRIN', 'MEDINE', 'SILA', 'AZRA P', 'TALHA', 'ENES', 'IREM M', 'SANEM']

            while True:
                ogrenci = random.choice(ogrenciler)
                if ogrenci in secilenler:
                    ogrenciler.remove(ogrenci)
                else:
                    break

            ogrenciler.remove(ogrenci)

            print("Seçilen öğrenci > " + ogrenci)

            with open('secilenler.txt', 'a', encoding='utf-8') as f:
                f.write(f"{ogrenci}\n")
        except IndexError:
            print('Seçilecek başka öğrenci kalmadı!')
    elif secim == '2':
        secilenler = open('secilenler.txt', 'w', encoding='utf-8')
        secilenler.write('')
        print('Başarıyla seçilenler dosyası temizlendi.')
    elif secim == '3':
        exit()
    else:
        print('Lütfen geçerli bir değer giriniz.')