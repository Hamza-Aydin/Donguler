print("""
*****************************
Kullanıcı Kayıt Etme Programı
*****************************
""")

kullanıcı_adı="hhamza"
parola="das4679"
giriş_hakkı=3

while True:
    kullanıcı_adı1=input("Kullanıcı adınızı giriniz:")
    parola1=input("parolanızı giriniz:")
    if kullanıcı_adı1 != kullanıcı_adı and parola1==parola:
        print("kullanıcı adı hatalı")
        giriş_hakkı-=1
    elif kullanıcı_adı1==kullanıcı_adı and parola1!=parola:
        print("parola hatalı")
        giriş_hakkı-=1
    elif kullanıcı_adı1!=kullanıcı_adı and parola1!=parola:
        print("kullanıcı adı ve parola hatalı")
        giriş_hakkı-=1
    else:
        print("sisteme giriliyor...")
        break
    if giriş_hakkı==0:
        print("giriş hakkınız bitti!")
        break