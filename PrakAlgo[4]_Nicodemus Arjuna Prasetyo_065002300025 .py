# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @')

def angka_ke_biner(angka):
    return bin(angka)

def biner_ke_angka(biner):
    return int(biner, 2)

while True:
    print('-----PRGORAM KONVERSI BILANGAN-----')
    print("     Pilih tipe konversi:")
    print("     1. angka ke Biner")
    print("     2. Biner ke angka")
    print("     3. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        angka = int(input("Masukkan bilangan angka: "))
        biner = angka_ke_biner(angka)
        print(f"Biner: {biner}")
    elif pilihan == '2':
        biner = input("Masukkan bilangan biner: ")
        angka = biner_ke_angka(biner)
        print(f"angka: {angka}")
    elif pilihan == '3':
        print('---terima kasih---')
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
3

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @')
def cek_angka_genap(lst):
    for angka in lst:
        if angka % 2 == 0:
            return True
    return False

input_str = input("Masukkan list angka (integer)-> ")
angka_list = [int(x) for x in input_str.split()]

hasil = cek_angka_genap(angka_list)

if hasil:
    print("List memiliki angka genap.")
else:
    print("List tidak memiliki angka genap.")

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @')
def cek_angka_genap(lst):
    for angka in lst:
        if angka % 2 == 0:
            return True
    return False

input_str = input("Masukkan list angka (integer)-> ")
angka_list = [int(x) for x in input_str.split()]

hasil = cek_angka_genap(angka_list)

if hasil:
    print("List memiliki angka genap.")
else:
    print("List tidak memiliki angka genap.")