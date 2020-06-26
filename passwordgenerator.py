import random
getnum = int(input("Pick a number greater than 7:  "))
if (getnum <= 7):
    print("Run again.")
    exit()
lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','#', '@', '!', '%','^', '//', '\\']
def main(lista, getnum):
    password = ''
    for i in range(0, getnum):
        passchar = random.choice(lista)
        password = password + passchar
        passwordagain()
    
    
