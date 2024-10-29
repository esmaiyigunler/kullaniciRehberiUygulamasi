print("Kullanıcı Rehberi Uygulaması")
print("1. Bilgi Ekle")
print("2. Bilgi Güncelle")
print("3. Bilgi Görüntüle")
print("4. Çıkış")
rehber = []

while True:
    secim = input("Lütfen bir seçim yapınız: ")

    if secim == "1":
        isim = input("Eklemek istediğiniz ismi giriniz: ")
        yas = int(input("Eklemek istediğiniz kişinin yaşını giriniz: "))
        eposta = input("Eklemek istediğiniz kişinin eposta adresini giriniz: ")
        rehber.append({"isim": isim, "yas": yas, "eposta": eposta})
        print(f"{isim} bilgileri eklendi.")
    
    elif secim == "2":
        guncellenecekIsim = input("Güncellemek istediğiniz ismi giriniz: ")
        for kisi in rehber:
            if kisi["isim"] == guncellenecekIsim:
                yeniIsim = input("Yeni ismi giriniz (değiştirmeyecekseniz aynı ismi girin): ")
                yeniYas = int(input("Yeni yaşı giriniz: "))
                yeniEposta = input("Yeni eposta adresini giriniz: ")
                
               
                kisi["isim"] = yeniIsim
                kisi["yas"] = yeniYas
                kisi["eposta"] = yeniEposta
                print(f"{guncellenecekIsim} bilgileri güncellendi.")
                break
        else:
            print("Kişi bulunamadı.")
    
    elif secim == "3":
        for kisi in rehber:
            print(f"İsim: {kisi['isim']}, Yaş: {kisi['yas']}, E-posta: {kisi['eposta']}")
    
    elif secim == "4":
        print("Çıkış yapılıyor.")
        break
    
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
