#Mükemmel Sayı Bulma(kendi hariç bölenlerinin toplamı kendisine eşit olan sayılar)
while True:
    sayı=int(input("Lütfen sayı giriniz:"))
    bölen1=int(input("lütfen sayının bir tam bölenini giriniz:(sayıdan büyük olamaz ve daha fazla yoksa sıfır giriniz)"))
    bölen2= int(input("lütfen sayının bir tam bölenini giriniz:(sayıdan büyük olamaz ve daha fazla yoksa sıfır giriniz)"))
    bölen3= int(input("lütfen sayının bir tam bölenini giriniz:(sayıdan büyük olamaz ve daha fazla yoksa sıfır giriniz)"))

    if bölen1>sayı or bölen2>sayı or bölen3>sayı:
        print("bu bölen girilemez!!")
        continue
    elif sayı % bölen1==0 and sayı%bölen2==0 and sayı%bölen3==0 and bölen1+bölen2+bölen3==sayı:
            print("bu sayı muhteşem sayıdır:",sayı)
    else:
        print("Bu sayı muhteşem sayı değildir!!!")



