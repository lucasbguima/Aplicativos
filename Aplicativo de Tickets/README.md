# Tickets

Tickets é um aplicativo para criar eventos e permitir a venda de ingressos (cinema, festas, shows, eventos esportivos, etc) via terminal de comando.

Funcionalidades:

Modo Administrador:

- Definir Senha
- Definir Nome do Evento
- Definir Quantidade de Ingressos
- Definir Valor dos Ingressos
- Ver Saldo da Máquina

Modo Usuário:

- Ver ingressos (Evento, Quantidade Disponível e Valor)
- Comprar Ingressos

## Tecnologia

Seguem as linguagens usadas para criar o Ticket:

- [Linguagem C](https://docs.microsoft.com/pt-br/cpp/c-language/?view=msvc-160) - Uma linguagem de programação compilada de propósito geral, estruturada, imperativa, procedural e padronizada.

## Instalação

Requisitos:

Para usar o aplicativo de Tickets tenha o MinGW.

### Passo 1

Copie o diretório de aplicativos para seu computador:

```bash
$ git clone https://github.com/lucasbguima/Aplicativos.git
```

### Passo 2

Entre entre na pasta de "Aplicativos", "Aplicativo de Tickets":

```bash
$ cd aplicativos
$ cd aplicativo de tickets
```

### Passo 3

Adicione Acentuação UTF-8 no terminal:
```bash
$ chcp 65001
```

### Passo 4

Crie o arquivo executavel:
```bash
$ gcc -o executavel ticket.c
```

### Passo 5

Rode o arquivo executavel:
```bash
$ executavel.exe
```

### Passo 6 - Opcional

Caso tenha interesse em rodar no VS Code, instale os plugins para C:
- C/C++
- C/C++ Compile Run

Para compilar no terminal do VS Code basta pressionar F6 com os plugins instalados.

## Contribuições
Pull requests são bem-vindas. Para maiores discussões, por favor abra uma issue primeiro para discutir o que você gostaria de mudar na aplicação.

Certifique-se de atualizar os testes conforme apropriado.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
