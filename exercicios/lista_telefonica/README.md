# Lista Telefônica - Algoritmos

Implementação de um sistema básico de contatos telefônicos, via terminal, utilizando discionários em Python.

### Funções Principais

| Função                                | Descrição                                 |
| :------------------------------------ | :---------------------------------------- |
| exibirLista()                         | Mostra todos os contatos com seus números |
| exibirTodosContatos()                 | Lista apenas os nomes dos contatos        |
| adicionarContato(nome, numero)        | Adiciona novo contato à lista             |
| removerContato(nome)                  | Remove contato existente                  |
| atualizarNumero(nome, numeroNovo)     | Atualiza número de contato existente      |
| procurarContato(nomeContatoProcurado) | Busca e exibe número específico           |

### Funções Secundárias

| Função                              | Descrição                      |
| :---------------------------------- | :----------------------------- |
| normalizarString(string)            | Padroniza entrada do usuário   |
| contatoExiste(nomeContatoProcurado) | Verifica existência de contato |
| mensagemListaVazia()                | Exibe mensagem de lista vazia  |
| opcaoEscolhidaValidada()            | Valida entrada do menu         |
| exibirMenu()                        | Mostra interface de opções     |

### Requisitos do Exercício

-   ✅ Uso de dicionário para mapeamento nome-número
-   ✅ Menu interativo com enumerate
-   ✅ Validação de entradas do usuário
-   ✅ Fragmentação do código em funções
-   ✅ Controle de fluxo sem uso de break
-   ✅ Normalização de strings para consistência
-   ✅ Mensagens informativas para o usuário
-   ✅ Tratamento de casos especiais
