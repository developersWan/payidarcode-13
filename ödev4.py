import json
puan = 0
devam = ("hayir")
# JSON dosyasını okuma ve yazdırma
kullanici = input("kullanıcı adınızı giriniz:")
with open("veri1.json", "r", encoding="utf-8") as f:
    oku = f.read()
veri = json.loads(oku)
if kullanici in veri:
    print("Kullanıcı sisteme zaten kayıtlı")
    islem = ("1")
else:
    islem = ("0")
# İ Ş L E M L E R
    cevap1 = input("1.Soru:")
    if cevap1 == ("1"):
        puan = puan + 10
        devam = ("evet")
    else:
        print("doğru cevap '1' idi")
        devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap2 = input("2.Soru:")
        if cevap2 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap3 = input("3.Soru:")
        if cevap3 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap4 = input("4.Soru:")
        if cevap4 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap5 = input("5.Soru:")
        if cevap5 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap6 = input("6.Soru:")
        if cevap6 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap7 = input("7.Soru:")
        if cevap7 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap8 = input("8.Soru:")
        if cevap8 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap9 = input("9.Soru:")
        if cevap9 == ("1"):
            puan = puan + 10
            devam = ("evet")
        else:
            print("doğru cevap '1' idi")
            devam = input("devam etmek için 'evet' yazınız: ")
    if devam == ("evet"):
        cevap10 = input("10.Soru:")
        if cevap10 == ("1"):
            puan = puan + 10
            print("toplam puanınız:", puan,"/ 100")
        else:
            print("doğru cevap '1' idi")
            print("toplam puanınız:", puan,"/ 100")
    if devam != ("evet"):
        print("toplam puanınız:", puan,"/100")
    veri[kullanici] = {
            "kullanici": kullanici,
            "puan": puan
        }
    d = json.dumps(veri, indent=4, ensure_ascii=False)
    with open("veri1.json", "w", encoding="utf-8") as f:
        f.write(d)
#######################