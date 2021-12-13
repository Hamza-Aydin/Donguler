#Armstrong sayısı bulma(Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.)
while True:
    sayı = int(input("lütfen bir sayı giriniz:"))
    basamak_sayısı = int(input("lütfen basamak sayısı giriniz:"))

    for a in sayı:
        b = 0
        b=b+a**basamak_sayısı
        if b == sayı:
            print("Bu sayı Armstrong sayısıdır:", sayı)
        else:
            print("Bu sayı Armstrong sayısı değildir!!")
















