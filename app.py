
number = int(input("Number: "))
n2 = []
n_SU = 0 
a = 0


while a == 0:
    n_SU = number % 2
    number = number // 2
    n2.append(n_SU)
    if number <= 0:
        n2.reverse()
        binary = ''.join(str(x) for x in n2)
        print(binary)

        number = int(input("Číslo: "))
        n2 = []
        n_SU = 0 
        a = 0
     
    


    

    

    
