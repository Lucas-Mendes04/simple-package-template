import random as rd

def password_generator():

    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '%', '&', '*', '+',
                '-', '.', '*', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 't', 'm', 'n', 'z', 'x']


    num_list = int(len(caracteres)+1)


    num_char = int(input("Digite a quantidade de caracteres da senha: "))


    i = 0


    n_list = []


    while i < num_char:
        n_list.append(caracteres[rd.randint(0,num_list)])
        i+=1

    senha = ",".join(n_list)


    print("\nSeu senha:",senha.replace(",",""))

password_generator()    