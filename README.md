# TaxiProblem
Agente Autonomo que resolve o problema do taxi.

## Descrição do problema.
O problema consiste em um mapa 5x5 com certos obstaculos. O taxista começa em uma posição aleatória. O passageiro e seu destino tem 4 posições possíveis. Dado a posição do passegeiro e seu destino, o agente autônomo acha o melhor caminho.

## Heuristica
A heuristica usada no problema é simples: quando o taxista precisa buscar o passageiro a heuristica é a distância euclidiana entre o possível próximo movimento e o local do passageiro. Quando o passageiro já esta no taxi a heuristica é a disntância euclidiana entre o possível próximo movimento e o destino.

## Sucessores
Os sucessores são todos os movimentos possíveis do taxi. Ou seja, ele chega se está em alguma borda do mapa, se existe alguma barreira e se pode pegar o passageiro