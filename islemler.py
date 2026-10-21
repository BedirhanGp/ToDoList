class islemler:
    def __init__(self):
        self.liste = []

    def islemler(self):
        secilen = input("""Yapmak istediğiniz işlemi seçiniz : 
1-Görev ekle
2-Görevleri gör
3-Görevleri Düzenle
4-Görev sil 
5-Çıkış\n""")
        return secilen

    def gorevEkle(self):
        while True:
            gorev = input("Yapılacak görev giriniz : ")
            if gorev.strip() == "":
                print("Hata! Görev boş olamaz!")
            else:
                self.liste.append(gorev)
                break

    def gorevGor(self):
        if not self.liste:
            print("Listelenecek görev yok.")
            return
        for i in range(len(self.liste)):
            print(f"{i + 1}. {self.liste[i]}")

    def gorevDuzenle(self):
        if not self.liste:
            print("Liste boş, düzenlenecek görev yok.")
            return
        donguDuzenle = True
        while donguDuzenle:
            duzenle = input("Düzenlemek istediğiniz görevin sırasını seçiniz : ")
            if not duzenle.isdigit():
                print("Hata! Lütfen sayı giriniz")
            elif int(duzenle) > len(self.liste) or int(duzenle) < 1:
                print("Hata! Tekrar deneyiniz")
            else:
                print("Düzenlenecek görev", duzenle, ":", self.liste[int(duzenle) - 1])
                while True:
                    duzenlenen = input("Düzenlenmiş görevi giriniz : ")
                    if duzenlenen.strip() == "":
                        print("Hata! Görev boş olamaz")
                    else:
                        break
                while True:
                    emin = input("Düzenlemek istediğinize emin misiniz? e/h \n")
                    if emin == "e":
                        self.liste[int(duzenle) - 1] = duzenlenen
                        print("Düzenleme işlemi tamamlandı")
                        donguDuzenle = False
                        break
                    elif emin == "h":
                        print("Düzenleme işlemi iptal edildi!")
                        donguDuzenle = False
                        break
                    else:
                        print("Hata! Tekrar deneyiniz")

    def gorevSil(self):
        if not self.liste:
            print("Liste boş, silinecek görev yok.")
            return
        donguSil = True
        while donguSil:
            silinecek = input("Silmek istediğiniz görevin sırasını seçiniz : ")
            if not silinecek.isdigit():
                print("Hata! Lütfen sayı giriniz")
            elif int(silinecek) > len(self.liste) or int(silinecek) < 1:
                print("Hata! Tekrar deneyiniz")
            else:
                print("Silinecek görev", silinecek, ":", self.liste[int(silinecek) - 1])
                while True:
                    emin = input("Silmek istediğinize emin misiniz? e/h \n")
                    if emin == "e":
                        self.liste.pop(int(silinecek) - 1)
                        print("Silinme işlemi tamamlandı")
                        donguSil = False
                        break
                    elif emin == "h":
                        print("Silme işlemi iptal edildi!")
                        donguSil = False
                        break
                    else:
                        print("Hata! Tekrar deneyiniz")
