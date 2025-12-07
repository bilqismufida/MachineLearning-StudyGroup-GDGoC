with open("data.txt") as file:
    for n in file:
        n = int(n)
        
        if n % 2 == 0:
            print(f"{n} adalah genap")
        else:
            print(f"{n} adalah ganjil")