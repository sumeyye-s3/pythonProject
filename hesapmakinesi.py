print("hesap makinesine hoşgeldiniz.")

birincisayi = int(input("bir sayı giriniz "))
ikincisayi = int(input("bir sayı giriniz "))

print("""
toplama işlemi yapmak için + 
çıkartma işlemi yapmak için -
çarpma işlemi yapmak  için *
bölme işlemi yapmak için /
""")
yapilmakistenenislem = input("yapamk istediğiniz işlem işaretini giriniz")

if(yapilmakistenenislem == "+"):
    print(birincisayi + ikincisayi)
elif(yapilmakistenenislem == "-"):
    print(birincisayi - ikincisayi)
if(yapilmakistenenislem == "*"):
    print(birincisayi * ikincisayi)
elif(yapilmakistenenislem == "/"):
    print(birincisayi / ikincisayi)
