import random
def game():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("Masukan angka: "))
        if(b>a):
            print("Terlalu besar, coba lagi")
        elif(b<a):
            print("Terlalu kecil, coba lagi")
        else:
            print("Benar")
            break
game()
