from islemler import islemler

islem = islemler()
dongu = True
while dongu:
    secilen = islem.islemler()
    match secilen:
        case "1":
            islem.gorevEkle()
        case "2":
            islem.gorevGor()
        case "3":
            islem.gorevDuzenle()
        case "4":
            islem.gorevSil()
        case "5":
            print("Çıkış yapıldı")
            dongu = False
        case _:
            print("Geçersiz değer")
