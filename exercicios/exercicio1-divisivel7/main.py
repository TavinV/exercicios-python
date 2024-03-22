# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def main ():
    """
    Função principal do programa, dentro dela estão armazenados todos os códigos que deverão
    ser executados quando o programa for iniciado.
    """

    # Divisiveis por 7 nao multiplos de 5

    def divisivel_por_7_nao_multiplo_de_5(Start: int, End: int):
        """
        Retorna todos os os numeros não multiplos de 5 que são divisiveis por 7 entre determinados parametros (inclusivo)

        Parametros:
        
        [int] Start : Numero inicial da sequencia;
        [int] End : Numero final da sequencia.

        Returns:

        None.

        Outputs:
        
        *Linha unica com todos os numeros que se enquadram, separados por vírgula.
        """
        def print_formatado(lista_numeros):
            """
            Essa função imprime os valores na formatação pedida (unica linha, separado por virgula)
            
            Parametros:

            [int list]
            
            Returns:

            None

            Outputs:
            *Linha unica com todos os numeros que se enquadram, separados por vírgula.
            """

            string_formatada = ""

            for x in lista_numeros:
                string_formatada += str(x) + ", "
            
            print(string_formatada)

        temp_list = []

        for x in range(Start, (End + 1)):
            if (x % 7) == 0:
                # x divisivel por 7
                if (x % 5) != 0:
                    # x não multiplo de 5
                    temp_list.append(x)
        
        print_formatado(temp_list)

    
    divisivel_por_7_nao_multiplo_de_5(2000,3200)

if __name__ == "__main__":
    main()