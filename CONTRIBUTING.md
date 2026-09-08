# Guia de Contribuição

Este documento descreve o padrão adotado para contribuir com o **CodeFactory To-Do API**.

## Padrão de commits

O projeto segue o padrão [Conventional Commits](https://www.conventionalcommits.org/), utilizando os seguintes prefixos:

| Prefixo | Uso |
|---|---|
| `feat:` | nova funcionalidade |
| `fix:` | correção de bug |
| `docs:` | alteração em documentação |
| `test:` | inclusão ou ajuste de testes |
| `chore:` | tarefas de configuração/manutenção |
| `merge:` | commits de merge entre branches |

Exemplo: `feat: adiciona endpoint de atualização de tarefas`

## Fluxo de branches

- `main`: versão estável e publicada;
- `desenvolvimento`: integração das features antes de ir para `main`;
- `feature/<nome>`: uma branch por funcionalidade, criada a partir de `main` ou `desenvolvimento`.

## Como contribuir

1. Crie uma branch a partir de `main` com o padrão `feature/<nome-da-feature>`;
2. Faça commits pequenos e coerentes, seguindo o padrão acima;
3. Abra um **Pull Request** descrevendo a mudança;
4. Aguarde a revisão antes do merge.
