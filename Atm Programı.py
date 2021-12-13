print("""**************************************
ATM'ye Hoşgeldiniz
İşlemler:
1=Bakiye Sorgulama
2=Para Çekme
3=Para Yatırma
Programdan çıkmak için 'q' ya basın.
**************************************""")
bakiye=1000
while True:
    işlem=input("işlem numarası giriniz:")
    if işlem=="q":
        print("çıkış yapılıyor...")
        break
    elif işlem=="1":
        print(bakiye)
    elif işlem=="2":
        miktar=int(input("lütfen miktar giriniz:"))
        if miktar> bakiye:
            print("bakiye yetersiz bu işlem yapılamaz")
            continue
        bakiye-=miktar
    elif işlem=="3":
        miktar = int(input("lütfen miktar giriniz:"))
        bakiye+=miktar
    else:
        print("geçersiz işlem numarası girdiniz!")


