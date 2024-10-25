x = int(input("Tabla inmultirii cu nr:"))
nr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(" 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n","-----------------------------")
      #,"1|", "2|", "3|", "4|", "5|", "6|", "7|", "8|", "9|", "10", sep="\n")

inmultit =[x* nr for nr in range(1,11)]
print(inmultit)


