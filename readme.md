# Olá, bem-vindo ao Constructor

O **Constructor** é uma automação para criação de arquivos padronizados,
desenvolvida totalmente em **Python**.

# Requisitos

O projeto utiliza principalmente bibliotecas que já acompanham a
instalação oficial do Python:

https://www.python.org/downloads/

A única biblioteca que precisa ser instalada manualmente é o
**colorama**.

``` python
subprocess
colorama
typing
time
json
```

# Utilização

Ao executar o comando abaixo no terminal:

``` cmd
python <caminho_do_constructor>
```

será exibida a seguinte tela:

``` cmd
=== GERADOR DE ARQUIVOS (Visualg) ===

Instruções :
┌───────────────────────────────────────────────────┐
│ - Informe (0) para encerrar o programa.           │
│ - Informe (c) para acessar as configurações.      │
└───────────────────────────────────────────────────┘

- Informe o nome do projeto:
```

Caso seja informado qualquer valor diferente da **flag de encerramento**
(por padrão `"0"`) ou `c`, o Constructor entenderá que o valor informado
é o nome do novo projeto.

``` cmd
- Informe o nome do projeto: Código
- Informe a descrição desse projeto:
```

Após informar o nome do projeto, o Constructor solicitará uma descrição,
que será inserida automaticamente no arquivo gerado.

Ao finalizar esse processo, o arquivo será criado na pasta em que o
Constructor foi executado.

# Configurações

Para acessar o menu de configurações, basta informar `c` no campo de
nome do projeto.

``` cmd
=== GERADOR DE ARQUIVOS (Configurações) ===

Configurações :
┌──────────────────────────────────────────┐
│ - Molde (m) : visualg                    │
│ - Nome do usuário (u) : Erick Alves      │
│ - Tamanho máximo de linha (t) : 60       │
│ - Cooldown (c) : 1.0                     │
│ - Flag (f) : "0"                         │
└──────────────────────────────────────────┘

- Informe (0) para retornar ao menu.
- Informe a configuração que deseja alterar:
```

Para alterar um valor, basta informar a chave correspondente.

Por exemplo, a chave `u` altera o nome do usuário.

``` cmd
Configurações :

- Informe a configuração que deseja alterar: u
- Informe o novo valor para u: Erick Alves

- Configuração aplicada com sucesso!
```

A única configuração que possui um fluxo diferente é a alteração do
**molde** (`m`).

``` cmd
Configurações :

- Informe a configuração que deseja alterar: m

| Moldes disponíveis:
| - visualg
| - python
| - javascript
| - c

- Informe o novo valor para m: javascript

- Configuração aplicada com sucesso!
```

# Criando novos moldes

Novos moldes podem ser adicionados ao arquivo `config.json`, na seção
`patterns`.

``` json
"Nome_do_molde": {
    "extension": "...",
    "comment": "...",
    "template": "..."
}
```

Onde:

-   **Nome_do_molde**: nome que identificará o molde.
-   **extension**: extensão do arquivo (ex.: `js`).
-   **comment**: comentário da linguagem (ex.: `//`).
-   **template**: conteúdo inicial do arquivo.

Palavras-chave disponíveis:

  Palavra-chave   Descrição
  --------------- ----------------------------------------------------
  `!T`            Nome do projeto estilizado (`=== Meu Projeto ===`)
  `!n`            Nome do projeto sem espaços
  `!f`            Nome do projeto exatamente como informado
  `!d`            Descrição do projeto
  `!s`            Nome do usuário
  `!t`            Data de criação (`DD/MM/AAAA`)
  `\n`            Quebra de linha

## Exemplo

### Molde

``` json
"Molde_JS": {
    "extension": "js",
    "comment": "//",
    "template": "// Projeto : !n\n// - Aluno : !s\n// - Dia : !t\n// - !d\n\n// - Var\n\n\n\n// - Programa:\n"
}
```

### Entrada

``` cmd
- Informe o nome do projeto: CodigoJS
- Informe a descrição desse projeto: Exemplo de projeto criado com o molde "Molde_JS"
```

### Resultado

``` javascript
// Projeto : CodigoJS

// - Aluno : Erick Alves
// - Dia : 17/07/2026
// - Exemplo de projeto criado com o molde "Molde_JS"

// - Var


// - Programa:
```
