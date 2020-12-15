# Fockus

Fockus é uma extensão para Google Chrome, voltada para ajudar no foco de executar atividades diárias.

Funcionalidades:

- Listar tarefas
- Temporizador

## Tecnologia

Seguem as linguagens usadas para criar Fockus:

- [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - A linguagem de script para páginas Web.
- [Chrome Extensions](https://developer.chrome.com/docs/extensions/mv3/) - Crie extensões para o navegador Chrome.

## Instalação

Para usar o aplicativo fockus 

### Passo 1

Copie o diretório de aplicativos para seu computador:

```bash
$ git clone https://github.com/lucasbguima/Aplicativos.git
```

### Passo 2

Para rodar no navegador entre na pasta de "Aplicativos", "Aplicativo Fockus" e execute o arquivo "fockus.html":

```bash
$ cd aplicativos
$ cd aplicativo fockus
$ fockus.html
```

### Passo 3 - Opcional

Para rodar como extensão do Chrome, crie um arquivo manifest.json:

```bash
$ touch manifest.json
```

Configure o manifest.json da seguinte forma:

```
{
  "name": "Fockus",
  "version": "1.0",
  "description": "Build an Extension!",
  "manifest_version": 3
}
```

Por fim, basta entrar no link [chrome://extensions] e carregar a aplicação para ser usada no navegador.

## Contribuições
Pull requests são bem-vindas. Para maiores discussões, por favor abra uma issue primeiro para discutir o que você gostaria de mudar na aplicação.

Certifique-se de atualizar os testes conforme apropriado.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
