# Gerador-gorjetas

  * Esse projeto é baseado no sistema de inferência Fuzzy que é um método de raciocínio realizado pela máquina que é bem semelhante ao raciocínio humano, essa lógica
    imita a forma de tomadas de decisão dos seres humanos que envolve todas as respostas intermediarias entre o sim e o não. Neste caso, gera a decisão do pagamento da
    gorjeta para um garçom, levando em consideração duas entradas importantes que são a qualidade da comida e a qualidade do serviço prestado, e a classificação dessas 
    entradas são definidas pelas funções de pertinência que retornam resultados entre 0 e 1. O programa implementado apresenta a sua relação difusa entre as variáveis de
    entrada e de saída, fundamentada em três regras simples: 
            
            •	Se a comida for ruim OU o serviço for ruim, a gorjeta será baixa;
            •	Se o serviço for aceitável, a gorjeta será média;
            •	Se a comida for ótima OU o serviço for incrível, a gorjeta será alta;   
  
  * A utilização da biblioteca matplotlib.pyplot permite visualizar as regras implementadas nesse projeto e as funções de pertinência usadas para cada entrada, conforme é 
    mostrado na figura abaixo:
        
    ![Figure_11](https://user-images.githubusercontent.com/102812154/194731449-d65921e8-0085-4bf4-9155-dd2179142223.png)
