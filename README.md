# [Analisador Léxico e Analisador Sintático](/Enunciado.pdf)
#### Trabalho 1 da disciplina de Construção de Compiladores @ UFSC 19/2

### TODO
- [ ] Analisador Léxico
- [ ] Analisador Sintático
- [ ] Relatório
- [ ] README
- [ ] Makefile

### Entrada e Saída
A Entrada será um arquivo .ccc escrito na linguagem derivada de **CCC-2019-2**.

#### Analisador Léxico:
* Se não houver erros léxicos ->  uma lista de tokens (na mesma ordem em que eles ocorrem no arquivo dado na entrada) e uma tabela de símbolos;
* Se houver erros léxicos -> uma mensagem simples de erro léxico indicando a linha e a coluna do arquivo de entrada  onde ele ocorre

#### Analisador Sintático:
* Se não houver erros sintáticos -> uma mensagem de sucesso
* Se houver erros sintáticos -> uma mensagem de insucesso indicando qual é a entrada na tabela de reconhecimento sintático que está vazia (qual é a forma sentencial α, qual o símbolo não-terminal mais á esquerda de α e qual o token de entrada).

O Trabalho será desenvolvido em `Python 3`, devendo ser compatível com a `versão 3.6.8`
