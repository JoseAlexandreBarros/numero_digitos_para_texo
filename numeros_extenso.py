from numeros import Numero

number=Numero()


while True :

    numero=input("digite um numero entre 0 e 999 , ou 'saida' para encerrar  \n")
    if numero=='saida':
        print('programa encerrado')
        break
    num = int(numero)
    
    if num < 0 or num > 999:
        print('numero invalido!')

    if num >=0 and num <= 9:
      print(number.um_digito(num))

    elif num>9 and num<100:
       print(number.dois_digitos(num))
    
    else:
       print(number.tres_digitos(num))
    