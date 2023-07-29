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

<Exemplos em código>

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

<center>.....................................................................................................................................................................</center>

#### Expressões Lógicas:

- São formadas por operadores lógicos: 'or' (ou), 'and' (e) e 'not' (não).
- O resultado da avaliação é sempre True (verdadeiro) ou False (falso).
- A precedência é: primeiro 'not', depois 'and', e por último 'or'.

Exemplos:

- True and False → Resultado: False
- not (5 == 3) → Resultado: True
- (2 > 1) or (3 < 1) → Resultado: True

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



_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _













<center>............................................................................................................................................................................</center>

Glossário:

Interpretador:

Linguagem de Máquina:

