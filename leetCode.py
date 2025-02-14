# menghilangkan blangan a yang ada di b
a = list(map(int, input("Bilangan a :").split()))
b = list(map(int, input("Bilangan b :").split()))
hasil = hasil = [i for i in a if i not in b] 
print(hasil)