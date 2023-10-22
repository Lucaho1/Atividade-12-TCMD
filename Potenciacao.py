def main():
    a = int()
    x = int()
    y = int()
    a = int(input("Insira o valor de a: "))
    x = int(input("Insira o valor de x: "))
    y = 1
    i = 0
    while i < x:
        y = y * a
        i = i + 1
    print("O valor de a^x eh: %d"%(y))





if "__main__" == __name__:
    main()