import random

while True:
    x=int(input("Bir sayı giriniz:"))
    c=random.randint(0,100)
    if c==x:
        print("Şanslı şooopar!")
        break
    print(f"{x} girildi {c} üretildi. Soooooryy!")