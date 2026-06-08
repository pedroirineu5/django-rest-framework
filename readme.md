# utilizando o flake 8 no projeto

Flake8 é um linter que vai verificar se o código está escrito dentro dos padrões da PEP08. Que são uma série de regras para facilitar a leitura e compreensão do código escrito.

```pip install flake8```

a instalação é igual a uma biblioteca normal, após instalar. Vai ser rodado o comando `flake8`.
E ele deve retornar todos os erros de linter.

## Arquivo de config.

crie um arquivo chamado: `.flake8`

dentro dele

```bash
[flake8]
exclude = venv # vai ignorar a pasta de venv, o linter n vai passar por lá.
ignore = e501 # vai ignorar o erro e501(quando passa de 79 caracteres uma linha) quando for rodar o comando.
```
