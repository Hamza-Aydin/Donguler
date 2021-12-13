print("""***********************
Faktoriyel Bulma Programı
Çıkmak için 'q' ya basınız.
************************""")

while True:
    sayı=input("Lütfen Sayı Giriniz:")

    if sayı=="q":
        print("Çıkış Yapılıyor...")
        break
    else:
        sayı=int(sayı)
        faktoriyel=1
        for i in range(1,sayı+1):
            faktoriyel*=i
        print("Faktoriyeli:",faktoriyel)
