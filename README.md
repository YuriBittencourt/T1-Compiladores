## Como usar

Ao executar o makefile ele pode pedir sua senha de sudo
para atualizar o pip e instalar o ply.

Desenvolvido com Python 2.7.13

### Para executar apenas o analisar léxico
`make -f makefiles/make_lexer FILE="caminho_do_arquivo.ccc"`

- Exemplo:
`make -f makefiles/make_lexer FILE="examples/ex1.ccc"`

O resultado será uma lista de tokens

### Para executar apenas o analisar léxico

`make -f makefiles/make_syntatic FILE="caminho_do_arquivo.ccc"`

- Exemplo:
`make -f makefiles/make_syntatic FILE="examples/ex1.ccc"`
