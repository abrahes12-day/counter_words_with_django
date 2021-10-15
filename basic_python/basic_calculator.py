a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = input("Enter operator: ")

if c == '+':
    print("Hasil penjumlahan: ", a+b)
elif c == '-':
    print("Hasil pengurangan: ", a-b)
elif c == '*':
    print("Hasil perkalian: ", a*b)
elif c == '/':
    print("Hasil pembagian: ", abs(a/b))