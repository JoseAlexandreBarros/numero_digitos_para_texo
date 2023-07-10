class Numero():

 

    def tres_digitos(self,numero):
        extenso=''
        unidades=numero%10
        numero=int(numero/10)
        dezenas=numero%10
        centenas=int(numero/10)
        if centenas==1 and dezenas==0 and unidades == 0:
            extenso='cem'
            return extenso
        
        
        match centenas:
                case  1 :
                    extenso ='cento '

                case 2 :
                    extenso ='duzentos '

                case 3:
                    extenso ='trezentos '

                case 4:
                    extenso ='quatrocentos '

                case 5:
                    extenso ='quinhentos '

                case 6 :
                    extenso ='seicentos '

                case 7 :
                    extenso ='setecentos '

                case 8:
                    extenso ='oitocentos '
        


                case 9:
                    extenso ='novecentos '

        if dezenas==1:
            match unidades:
                case 0:
                    extenso= extenso + 'e dez'
                case 1:
                    extenso= extenso + 'e onze'
                case 2:
                    extenso= extenso + 'e doze'
                case 3:
                    extenso= extenso + 'e treze'
                case 4:
                    extenso= extenso + 'e quatorze'
                case 5:
                    extenso= extenso + 'e quinze'
                case 6:
                    extenso= extenso + 'e dezesseis'
                case 7:
                    extenso= extenso + 'e dezessete'
                case 8:
                    extenso= extenso + 'e dezoito'
                case 9:
                    extenso= extenso + 'e dezenove'

            return extenso
                    
        match dezenas:
                case  0 :
                    extenso = extenso

                case 2:
                    extenso= extenso + 'e vinte '

                case 3:
                    extenso =extenso + 'e trinta '

                case 4:
                    extenso =extenso + 'e quarenta'

                case 5:
                    extenso =extenso + 'e cinquenta '

                case 6 :
                    extenso = extenso + 'e secenta '

                case 7 :
                    extenso = extenso + 'e setenta '

                case 8:
                    extenso = extenso + 'e oitenta '

                case 9:
                    extenso = extenso + 'e noventa '

        
        match unidades:
                case  0 :
                    extenso = extenso

                case 2:
                    extenso= extenso + 'e dois'

                case 3:
                    extenso =extenso + 'e tres'

                case 4:
                    extenso =extenso + 'e quatro'

                case 5:
                    extenso =extenso + 'e cinco'

                case 6 :
                    extenso = extenso + 'e seis'

                case 7 :
                    extenso = extenso + 'e sete'

                case 8:
                    extenso = extenso + 'e oito'

                case 9:
                    extenso = extenso + 'e nove'
        

        return extenso

    def dois_digitos(self,numero):
        extenso=''
        unidades=numero%10
        numero=int(numero/10)
        if numero == 1:
            match unidades:
                case  0:
                    extenso ='dez'

                case 1 :
                    extenso ='onze'

                case 2:
                    extenso ='doze'

                case 3:
                    extenso ='treze'

        
                case 4:
                    extenso ='quatorze'

                case 5 :
                    extenso ='quinze'

                case 6 :
                    extenso ='dezeseis'

                case 7:
                    extenso ='dezessete'

                case 8:
                    extenso ='dezoito'

                case 9:
                    extenso='dezenove'
            return extenso
        else:
            match numero:
                case  2:
                    extenso ='vinte '

                case 3 :
                    extenso ='trinta '

                case 4:
                    extenso ='quarenta '

                case 5:
                    extenso ='cinquenta '

        
                case 6:
                    extenso ='sessenta '

                case 7 :
                    extenso ='setenta '

                case 8 :
                    extenso ='oitenta '

                case 9:
                    extenso ='noventa '
            match unidades:
                case 0:
                    return extenso

                case 1:
                    return extenso + 'um'

                case 2:
                    return extenso + 'dois'

                case 3:
                    return extenso + 'tres'

        
                case 4:
                    return extenso + 'quatro'

                case 5:
                    return extenso + 'cinco'

                case 6:
                    return extenso + 'seis'

                case 7:
                    return extenso + 'sete'

                case 8:
                    return extenso + 'oito'

                case 9:
                    return extenso + 'nove'
        
        
            
        

    def um_digito(self,numero):
        match numero:
            case 0:
                return'zero'

            case 1:
                return 'um'

            case 2:
                return 'dois'

            case 3:
                return 'tres'

        
            case 4:
                return 'quatro'

            case 5:
                return 'cinco'

            case 6:
                return 'seis'

            case 7:
                return 'sete'

            case 8:
                return 'oito'

            case 9:
                return 'nove'


        



