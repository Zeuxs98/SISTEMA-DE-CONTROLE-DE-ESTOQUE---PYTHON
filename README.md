# Sistema de Controle de Estoque

Aplicativo de linha de comando (terminal) feito em Python para o trabalho
da disciplina de Coding. Ele ajuda a controlar os produtos de um estoque,
com suas quantidades e preços.

## Descrição

O programa mostra um menu interativo que continua rodando até o usuário
escolher a opção de sair. Os dados ficam guardados **apenas na memória**,
ou seja, são apagados quando o programa é fechado.

### Funcionalidades

| Opção | O que faz |
|-------|-----------|
| 1 | Cadastra um produto (nome, preço e quantidade inicial) |
| 2 | Lista todos os produtos do estoque (avisa quando o estoque está baixo) |
| 3 | Registra a entrada de unidades de um produto |
| 4 | Registra a saída de unidades (não deixa retirar mais do que existe) |
| 5 | Busca um produto pelo nome |
| 6 | Calcula o valor total do estoque (preço x quantidade) |
| 0 | Sai do programa |

### Validações

- Não aceita nome de produto vazio nem produto repetido
- Não aceita preço ou quantidade negativos, zerados ou com letras
  (a validação usa `float()` / `int()` com `try`/`except`)
- Não permite retirar mais itens do que há disponível
- Avisa quando o estoque está vazio ou a opção do menu é inválida

### Observações

- Os preços devem ser digitados com **ponto** (ex: `2.50`).
- A busca diferencia maiúsculas de minúsculas ("Caneta" é diferente de "caneta").

## Conceitos de Python utilizados

- Laço `while` para manter o menu ativo e repetir validações
- Condicionais `if`, `elif` e `else`
- Funções com `def`, parâmetros e `return`
- `try` / `except` simples para validar números
- Listas e dicionários
- `input()` e `print()` para interação com o usuário
- Programação procedural (sem classes e sem bibliotecas externas)
