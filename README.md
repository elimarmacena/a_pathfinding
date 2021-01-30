# A ✰ Pathfinding

## O Algoritmo

O A* (lê-se A estrela) é um algoritmo utilizado para efetuar a busca de menor distância possível entre dois pontos (em nosso caso chamado de nós). O algoritmo realiza buscas com base em informação, uma vez que a procura é realizada através de informações para que seja possível nortear as escolhas realizadas pelo computador.

A informação que o algoritmo necessita para o seu funcionamento é o custo do deslocamento realizado de um ponto a outro e a utilização de alguma heurística, informação esta que tende a variar o modo no qual é obtido dependendo do problema proposto.

## Problema Proposto

O algoritmo apresentado deverá realizar suas operações com base em um arquivo de entrada composto por uma matriz de valores 0’s e 1’s, onde 0 representa espaços passíveis de movimentação e 1 representando obstáculos. Tendo a matriz de entrada, será calculado o menor caminho possível entre A e B, valores esses também passados como entrada.

## Solução

### Linguagem Utilizada

Para a solução do problema proposto foi utilizada a linguagem Python, versão 3.8.7.

### Execução do código
![Commandline](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/command_line.png)

* map_directory: diretório do arquivo texto (.txt) contendo a matriz representando o mapa de entrada.
* start_x: inteiro >= 0 representando o valor X do ponto inicial.
* start_y: inteiro >= 0 representando o valor Y do ponto inicial.
* end_x: inteiro >= 0 representando o valor X do ponto final.
* end_y: inteiro >= 0 representando o valor Y do ponto final.

### Saída Esperada
Ao receber uma entrada onde o caminho é possível ser alcançado, o presente código irá retornar uma matriz de informações, como mostra a figura logo a baixo, onde cada símbolo apresenta os seguintes resultados.

* ⊗ : Campo não válido para movimento.
* ✰ : Campo livre para movimento.
* ✱ : Campo que compõe o caminho encontrado.
* ☖ : Campo inicial.
* ☗ : Campo final.

![Map Output](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/output_sample.png)


Além de exibir a matriz final, representação visual, também é apresentada a ordem dos indexes para que seja possível alcançar o objetivo.

Caso a entrada não resulte em um caminho, é levantada uma exceção com a seguinte mensagem: "The end destination was not found”.

### Implementação

Para a implementação da solução foi utilizado como heurística a distância de Manhattan, escolha dada pela simplicidade da abordagem e por também por abranger de modo geral os problemas desse tipo. O valor calculado através dessa heurística representa a distância de um ponto (x,y) até um ponto (a,b) de uma matriz.

A distância de Manhattan, como exposto no material de apoio disponibilizado para a elaboração do trabalho (A * Pathfinding para Iniciantes), trabalha com uma superestimação da distância, porém esse problema não se aplica em nosso cenário.

A heurística foi implementada da seguinte forma:

![Manhattan](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/manhattan.png)

A implementação segue a fórmula básica da heurística, onde temos o módulo de de X na posição A subtraído de X na posição B somado com o módulo de Y na posição A subtraído de Y na posição B.


O funcionamento geral do algoritmo tem como centro o arquivo src\pathfinding.py, como o próprio nome dá a entender, esse arquivo tem o objetivo de encontrar o caminho entre os dois pontos. No trecho exibido a seguir temos a ideia básica do algoritmo A*, como descrito no material de apoio.

![Core step](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/core_step.png)

Da linha 14-16 temos a escolha e remoção do ponto de menor valor na lista aberta e em seguida sua adição na lista fechada, após verificado se é o ponto de chegada, da linha 23 até a 38 temos a busca dos vizinhos do nó corrente e a verificação dos custos de tais pontos, caso já esteja na lista aberta, porém com outro ponto relacionado como pai, atualizamos os valores do vizinho com base no ponto corrente e alteramos a sua referência de pai. esse processo se estende até que acabe as opções de pontos de navegação ou que o ponto de chegada seja encontrado.

Entre as linhas 40 e 49 temos o processo de reconstrução do caminho percorrido para que o objetivo tenha sido alcançado, essa etapa ocorre verificando os pontos pais de cada ponto a partir do ponto de chegada de nossa entrada.

### Estruturas de dados

Em todo o código foram utilizadas apenas 2 duas classes, map e node, disponíveis em \entities\map.py e \entities\node.py respectivamente. Essas classes foram utilizadas para estruturar e organizar da melhor forma os dois principais tipos de dados trabalhados no problema, o ponto (ou nó, como comumente chamado) e o plano contendo as informações de espaço (em nosso caso, uma matriz).

A classe node possui a seguinte construção de atributos:

![Node Classe](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/node_classe.png)

location_x e location_y combinados representam a posição do ponto na matriz, os value_g é o custo do movimento para do ponto, value_h guarda o valor estimado do ponto apresentado até o ponto final (ou ponto de chegada), o atributo father guarda um outro objeto do tipo node, esse valor é utilizado para mantermos a rastreabilidade de movimento entre os pontos. Para o valor f, que é a soma dos atributos value_g e value_h, optou-se por criar apenas uma função que retorna tal operação, foi feita essa escolha pois se trata de uma operação simples e o valor de f muda a cada verificação de ponto vizinho.

Como mostra a imagem a seguir, nossa classe map tem um papel de mediador/facilitador de encontro de pontos, primeiramente temos a matriz guardada no atributo surface, temos um acesso rápido de cada ponto nela presente através do atributo node_indexes, com esse atributo podemos acessar as informações de determinado ponto apenas informando a tupla de sua localização sem a necessidade de uma varredura na matriz.

![Node Classe](https://github.com/elimarmacena/a_pathfinding/blob/main/resources/map_classe.png)

Nessa classe também guardamos os passos dados para criação do caminho final, podendo ser acessado a qualquer momento após calculado.

### Bibliotecas

Para a elaboração do código brevemente apresentado não foi utilizada nenhuma biblioteca externa, apenas a sys do próprio python para que fosse possível trabalhar com os argumentos enviados via linha de comando.
