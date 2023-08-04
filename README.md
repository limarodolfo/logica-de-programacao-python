# Lógica de Programação 

Este repositório tem como objetivo compartilhar um pouco dos meus estudos de lógica de programação utilizando o Python. No momento, vou passar por algumas informações introdutórias sobre, mas, deixarei um link com a história e detalhes sobre a mesma. 

**Link:** [Ebook - Introdução ao Python - Editora IFRN](https://memoria.ifrn.edu.br/bitstream/handle/1044/2090/EBOOK%20-%20INTRODU%C3%87%C3%83O%20A%20PYTHON%20%28EDITORA%20IFRN%29.pdf?sequence=1&isAllowed=y)

Primeiro de tudo, **instalação**. Se em sua máquina já tiver o python instalado, então tudo certo xD

No entanto, o passo a passo a seguir é eficaz para ajudar aqueles que não possuem o Python instalado.

OBS: Também pode servir para quem não sabe (esqueceu) é só verificar se você tem o Python instalado na sua máquina.



**NO CMD:**

**Digite:** `python --version`

O retorno esperado para (caso) você tiver o python instalado, seria o nome a versão: `python3.11.2 `

Caso contrário, vamos ver agora um passo a passo da instalação (depois irei adicionar uma imagens e deixar mais claro no que for possível):

1. Acesse o site oficial do Python (<https://www.python.org>) e procure a seção de downloads.
2. Na página de downloads, escolha a versão mais recente estável (por exemplo, `Python 3.9.6`). Não esqueça que deve corresponder ao seu sistema operacional(x64, x86). Se você estiver em um ambiente Windows, é só baixar o instalador executável para ele.
3. Clique no link de download para iniciar o download do instalador.
4. Depois de concluído o download, execute o instalador.
5. <span style="color:red">IMPORTANTE -</span> Na primeira tela do instalador, marque a opção "Add Python to PATH" (Adicionar Python ao PATH). Isso adicionará automaticamente o Python ao PATH do sistema, que é o que permite executar comandos Python em qualquer diretório no prompt de comando ou terminal.
6. Selecione a opção "Customize installation" (Personalizar instalação) para ter mais controle sobre as opções de instalação. Aqui você pode escolher os recursos adicionais que deseja instalar (como pip, IDLE etc.) e selecionar o diretório de instalação.
7. Depois de fazer as seleções desejadas, clique em "Next" (Avançar) e aguarde a instalação ser concluída.
8. Após a instalação ser concluída, você pode abrir o prompt de comando (no Windows, pressione Win + R, digite "cmd" e pressione Enter) e digitar "python" para verificar se o Python foi instalado corretamente, como fizemos inicialmente.


------

### Linguagem Pyton

##### Interpretador IDLE

Bem... há varias formas de utilizarmos na prática o python. Aqui, utilizei o IDLE para testes iniciais com a linguagem e para aprender um pouco sobre a IDE que vem junto a instalação padrão do Pyhton. Segue apenas um resuminho sobre:

*IDLE* oferece uma interface gráfica simples que facilita a interação com o interpretador Python. Ele inclui recursos como um editor de texto com realce de sintaxe, suporte para execução interativa de código, histórico de comandos, visualização de resultados, depuração passo a passo, a capacidade de abrir múltiplos editores de código, autocompletar, exibição da árvore de análise sintática e suporte a extensões de terceiros. Uma das principais características do IDLE é a capacidade de executar código Python interativamente, o que significa que você pode digitar instruções e ver os resultados imediatamente. 

------

### Resumão Sobre Variáveis e Atribuição de Valores

**Declaração de variáveis:**

1. Em Python, você não precisa declarar explicitamente o tipo de dado de uma variável. Apenas atribua um valor a ela e Python cuidará do resto.
2. **Atribuição de valores:**
   Para atribuir um valor a uma variável, utilize o operador de atribuição (=) seguido pelo valor que deseja armazenar.
3. **Nomes de variáveis:**

- O nome de uma variável pode conter letras, números e o caractere de sublinhado (_).
- O primeiro caractere do nome da variável não pode ser um número.
- Python é sensível a maiúsculas e minúsculas, ou seja, diferencia maiúsculas de minúsculas. Por exemplo, "valor" e "Valor" são duas variáveis diferentes.

4. **Reatribuição de valores:**
   Você pode alterar o valor de uma variável simplesmente atribuindo um novo valor a ela.
5. **Tipos de dados**
   As variáveis em Python podem conter diferentes tipos de dados, como 
   inteiros (int), números de ponto flutuante (float), strings (str), 
   listas (list), dicionários (dict), entre outros. O tipo de dado é 
   inferido automaticamente quando você atribui um valor à variável.

<Exemplos em código - ex001>

------

### Expressões em Python

Expressões são combinações válidas de variáveis, constantes e operadores que retornam um resultado após a sua avaliação. Existem três tipos principais de expressões em Python: aritméticas, lógicas e relacionais.

#### **Expressões Aritméticas:**

- Operam sobre valores inteiros ou reais.
- Os operadores aritméticos são: + (adição), - (subtração), * (multiplicação), / (divisão), // (parte inteira da divisão), % (resto da divisão) e ** (exponenciação).
- A precedência dos operadores é: primeiro **, depois *, /, // e %, e por último + e -.
- Parênteses podem ser usados para forçar a avaliação de operadores com menor precedência.

Exemplos:

- 5 + 3 → Resultado: 8
- 10 * 2 / 5 → Resultado: 4.0
- 2 ** 3 + 4 → Resultado: 12
- (5 + 3) * 2 → Resultado: 16

<Exemplos em código - ex002>

<center>.....................................................................................................................................................................</center>

#### Expressões Lógicas:

- São formadas por operadores lógicos: 'or' (ou), 'and' (e) e 'not' (não).
- O resultado da avaliação é sempre True (verdadeiro) ou False (falso).
- A precedência é: primeiro 'not', depois 'and', e por último 'or'.

Exemplos:

- True and False → Resultado: False
- not (5 == 3) → Resultado: True
- (2 > 1) or (3 < 1) → Resultado: True

<Exemplos em código - ex003>

<center>.....................................................................................................................................................................</center>

#### Expressões Relacionais:

- São usadas para fazer comparações entre expressões.
- Os operadores relacionais são: == (igual a), > (maior que), < (menor que), >= (maior ou igual a), <= (menor ou igual a) e != (diferente de).
- O resultado da comparação é True se a condição for satisfeita, ou False caso contrário.

Exemplos:

- 5 == 5 → Resultado: True
- 10 > 5 → Resultado: True
- 7 <= 6 → Resultado: False

É importante entender a ordem de precedência dos operadores para avaliar corretamente as expressões. Se necessário, é possível usar parênteses para controlar a ordem de avaliação.

Lembre-se de que as expressões são fundamentais para realizar cálculos, comparações e testes em Python, tornando-se uma parte essencial na programação com essa linguagem.

<Exemplos em código - ex001, ex002, ex003>

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

### Controle de Fluxo

O controle de fluxo em Python é essencial para direcionar a execução do código, permitindo que certas partes do programa sejam executadas apenas sob determinadas condições ou repetidas várias vezes. As principais estruturas de controle de fluxo em Python são:

#### Estrutura Condicional (if, elif, else):

- Permite executar um bloco de código somente se uma condição for verdadeira.
- A estrutura é composta por um "if" seguido por uma condição. Se a condição for verdadeira, o bloco de código dentro do "if" é executado. Caso contrário, o programa verifica se existem cláusulas "elif" (abreviação de "else if") com condições adicionais. Se alguma dessas condições for verdadeira, o bloco de código associado à primeira condição verdadeira "elif" é executado. Caso nenhuma das condições anteriores seja verdadeira, o bloco de código dentro de "else" (opcional) é executado.

#### Estrutura de Repetição (for):

- Permite executar um bloco de código repetidamente para cada elemento de uma sequência (por exemplo, uma lista, string, tupla, etc.).
- O loop "for" itera sobre os elementos da sequência, e a cada iteração, o bloco de código associado é executado.

#### Estrutura de Repetição (while):

- Permite executar um bloco de código repetidamente enquanto uma condição for verdadeira.
- O bloco de código é executado repetidamente até que a condição especificada seja falsa.

#### Controle de Loop (break e continue):

- O "break" é usado para interromper um loop prematuramente, quando uma condição é atendida.
- O "continue" é usado para pular a iteração atual de um loop e passar para a próxima iteração.

#### Cores no Terminal

Os códigos ANSI são uma forma de adicionar formatação de texto ao imprimir no terminal, permitindo que você altere cores de fundo, cores do texto, estilo do texto e até mesmo a posição do cursor. No Python, você pode utilizar esses códigos ANSI para adicionar cores e outros efeitos visuais ao seu texto.

Códigos ANSI para cores no terminal:Os códigos ANSI são sequências de escape que começam com o caractere de escape `\033` (também representado como `\x1b` ou `\u001b`). Eles são seguidos por um conjunto de números separados por ponto e vírgula, que especificam as propriedades de formatação. Para adicionar cores, geralmente usamos códigos ANSI que começam com `\033[`, seguidos por um número para representar a cor desejada.

Exemplo:

- `\033[31m` para cor vermelha
- `\033[32m` para cor verde
- `\033[33m` para cor amarela

1. Estilos de texto:Você pode usar códigos ANSI para adicionar estilos ao texto, como negrito, sublinhado e piscando. Alguns exemplos:

- `\033[1m` para negrito
- `\033[4m` para sublinhado
- `\033[5m` para piscando

1. Resetar a formatação:Após usar códigos ANSI para formatar o texto, é recomendado que você adicione `\033[0m` para redefinir as configurações e evitar que a formatação se aplique ao texto posterior.

<Exemplos em código - ex004>

------

### Estrutura de Repetição - FOR

Em Python, existem duas estruturas principais de repetição: `while` e `for`. Ambas permitem que você execute um bloco de código várias vezes com base em uma condição ou em um conjunto de elementos.

**Estrutura de repetição com while:**

O `while` repete um bloco de código enquanto uma condição específica for verdadeira. ssa estrutura de repetição executa um ciclo para cada elemento do objeto que está sendo iterado. Nas vezes em que precisamos que determinada variável seja incrementado ou decrementada a cada ciclo, a forma mais simples, é gerando uma lista com a função **range()**.

Sintaxe do comando **WHILE** em Python é a seguinte:

**while** condição:

​           **comando_verdadeiro**

Os comandos (ou instruções) dentro do corpo da estrutura **while** são executados (ou repetidos) ENQUANTO a condição for verdadeira 
(True).
​                    Quando a condição se torna falsa (False), os 
comandos não são executados e o programa continua depois da instrução **while**.

**Estrutura de repetição com for:**

O `for` é usado para percorrer uma sequência de elementos, como uma lista, tupla ou string. Ele executará um bloco de código para cada elemento na sequência.

Sintaxe do comando **FOR** em Python é a seguinte:

**for** item **in range**(início, fim, passo):

​           **item **    

Podemos usar o `break` para sair de um loop antes que a condição seja falsa, e o `continue` para pular a iteração atual e ir para a próxima.

<Exemplos em código - ex006, ex007>

------













------

Glossário:

Interpretador:

Linguagem de Máquina:

