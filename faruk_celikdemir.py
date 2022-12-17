import datetime

print("— İstinye Banka Hoşgeldiniz (v.0.1) —")

kullanicilar = {
    "Ahmet": {"sifre": "1234", "bakiye": 100},
    "Zeynep": {"sifre": "4321", "bakiye": 0},
}

services = [
    "Para Yatırma",
    "Para Çekme",
    "Para Transferi",
    "Hesap Bilgilerim",
    "Oturumu Kapat"
]

girisyapildi = True
while girisyapildi:

    print("1. Giriş")
    print("2. Çıkış")

    choice = input(">>> ")

    if choice == "1":

        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")

        while username not in kullanicilar or kullanicilar[username]["sifre"] != password:
            print("Kullanıcı Adı Veya Şifre Yanlış!")

            username = input("Kullanıcı Adı: ")
            password = input("Şifre: ")

        print(f"Hoşgeldiniz {username}!")
        while True:
            girisyapildi = False

            for i, service in enumerate(services, start=1):
                print(f"{i}. {service}")

            service_choice = input("Lütfen Yapmak istediğiniz işlemi tuşlayın: ")

            if service_choice == "1":

                bakiyeekle = input("Yatırmak istediğiniz tutarı girin : ")
                if 0 < int(bakiyeekle):
                    kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] + \
                                                       int(bakiyeekle)
                    print(username, "Talebiniz alınmıştır",
                          kullanicilar[username]["bakiye"], " bakiye tutarı hesabınıza eklenmiştir")
                else:
                    tekrar = True
                    while tekrar:

                        print(
                            "Böyle Bir İşlem Gerçekleştirilemez")
                        print("1. Tekrar deneme")
                        print("2. Ana menüye dön")
                        tdene = input("Yapmak istediğiniz işlemi girin : ")
                        if tdene == "1":
                            bakiyeekle = input("Yatırmak istediğiniz tutarı girin : ")
                            if 0 < int(bakiyeekle):
                                kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] + \
                                                                   int(bakiyeekle)
                                print(username, "Talebiniz alınmıştır",
                                      kullanicilar[username]["bakiye"], " bakiye tutarı hesabınıza eklenmiştir")
                                tekrar = False
                        if tdene == "2":
                            tekrar = False

            if service_choice == "2":

                bakiyeekle1 = input("ÇEKMEK istediğiniz tutarı girin : ")
                if kullanicilar[username]["bakiye"] >= int(bakiyeekle1) > 0:
                    kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] - \
                                                       int(bakiyeekle1)
                    print(username, "Talebiniz alınmıştır",
                          kullanicilar[username]["bakiye"], " hesabınızda bakiye kalmışır")

                else:
                    tekrar = True
                    while tekrar:

                        print(
                            "BAKİYENİZ 0 TL veya düşük olduğu için çekim yapamazsınız")
                        print("1. Tekrar deneme")
                        print("2. Ana menüye dön")
                        tdene = input("Yapmak istediğiniz işlemi girin : ")
                        if tdene == "1":
                            bakiyeekle1 = input(
                                "ÇEKMEK istediğiniz tutarı girin : ")
                            if kullanicilar[username]["bakiye"] >= int(bakiyeekle1)>0:
                                kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] - int(
                                    bakiyeekle1)
                                print(username, "Talebiniz alınmıştır",
                                      kullanicilar[username]["bakiye"], " hesabınızda bakiye kalmışır")
                                tekrar = False
                        if tdene == "2":
                            tekrar = False

            if service_choice == "3":

                tekrar = True

                tkullanici = input(
                    "Transfer etmek istediğiniz kişinin adını girin : ")
                tutar = input("Transfer etmek istediğiniz miktarı girin : ")

                if tkullanici in kullanicilar and kullanicilar[username]["bakiye"] >= int(
                        tutar) and tkullanici != username:

                    kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] - \
                                                       int(tutar)
                    kullanicilar[tkullanici]["bakiye"] = kullanicilar[tkullanici]["bakiye"] + int(
                        tutar)
                    print("Bakiyenizden", tutar, "tl eksiltilerek",
                          tkullanici, "İsimli kişiye aktarılmıştır")

                    print(kullanicilar[username]["bakiye"],
                          "TL BAKİYENİZ KALMIŞTIR")

                else:

                    while tekrar:

                        print(
                            "transfer sağlamak istediğiniz bilgiler hatalıdır bakiyenizi veya transfer sağlamak istediğiniz kullanıcı adını kontrol ediniz")
                        print("1. Tekrar deneme")
                        print("2. Ana menüye dön")
                        tdene = input("Yapmak istediğiniz işlemi girin : ")

                        if tdene == "1":
                            tkullanici = input(
                                "Transfer etmek istediğiniz kişinin adını girin : ")
                            tutar = input(
                                "Transfer etmek istediğiniz miktarı girin : ")
                            if tkullanici in kullanicilar and kullanicilar[username]["bakiye"] >= int(tutar):
                                kullanicilar[username]["bakiye"] = kullanicilar[username]["bakiye"] - \
                                                                   int(tutar)
                                kullanicilar[tkullanici]["bakiye"] = kullanicilar[tkullanici]["bakiye"] + int(
                                    tutar)
                                print("Bakiyenizden", tutar, "tl eksiltilerek",
                                      tkullanici, "İsimli kişiye aktarılmıştır")

                                print(kullanicilar[username]["bakiye"],
                                      "TL BAKİYENİZ KALMIŞTIR")

                                tekrar = False
                        if tdene == "2":
                            tekrar = False

            if service_choice == "4":

                zaman = datetime.datetime.now()
                print("İSTİNYEBANK")
                print(zaman.strftime("%d-%m-%Y %H:%M"))
                print("İSİM ", username)
                print("ŞİFRENİZ : ", kullanicilar[username]["sifre"])
                print("BAKİYENİZ : ", kullanicilar[username]["bakiye"])
                secim = input(
                    "Herhangi bir tuşa basarak ana menüye dönebilirsiniz : ")
                if secim == 2:
                    continue

                girisyapildi = False

            if service_choice == "5":
                print("...")
                girisyapildi = True
                break

            print(f"Seçtiğiniz işlem: {services[int(service_choice) - 1]}")


    elif choice == "2":

        print("Çıkış...")
        break