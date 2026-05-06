# Reconhecimento de Imagem - Testes e Assistência de Código

## Descrição Geral

Este projeto contém exemplos e testes relacionados a assistência de código, debugging e refatoração de scripts Python. Inclui demonstrações práticas de conceitos como validação de números primos, técnicas de debug e otimização de código.

## Estrutura do Repositório

```
reconhecimento-imagem/
├── index.html                          # Página inicial do projeto
└── teste-code-assistent/               # Diretório principal com exemplos
    ├── index.html                      # Página HTML do módulo
    ├── debug.py                        # Script de demonstração de debug
    ├── num_primo.py                    # Script para validar números primos
    ├── explicacao_num_primo.py         # Versão documentada com explicações
    ├── refatoração.py                  # Script refatorado com melhorias
    ├── explicacao_debug.md             # Documentação sobre técnicas de debug
    ├── explicacao_num_primo.md         # Explicação detalhada de números primos
    └── explicacao_refatoracao.md       # Guia de refatoração de código
```

## Tecnologias e Ferramentas

- **Python** 3.8+
- **Git Bash** - Terminal e controle de versão
- **HTML5** - Interface web
- **Visual Studio Code** - Editor recomendado
- **GitHub Copilot** - Assistência de código

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado
- Git Bash instalado
- Acesso ao terminal/PowerShell

### Executar Scripts

#### 1. Script de Números Primos
Valida se um número é primo ou composto:

```bash
cd c:\Users\h.tic04\Desktop\reconhecimento-imagem\teste-code-assistent
python num_primo.py
```

#### 2. Script Explicado de Números Primos
Versão com documentação e exemplos:

```bash
python explicacao_num_primo.py
```

#### 3. Script de Debug
Demonstra técnicas de debugging e rastreamento de erros:

```bash
python debug.py
```

#### 4. Script Refatorado
Versão otimizada com melhorias de código:

```bash
python refatoração.py
```

### Visualizar no Navegador

Abra os arquivos HTML em seu navegador:

```bash
start index.html
start teste-code-assistent\index.html
```

## Documentação

Cada funcionalidade possui documentação dedicada em formato Markdown:

- **explicacao_debug.md** - Técnicas de debugging em Python
- **explicacao_num_primo.md** - Teoria e implementação de validação de números primos
- **explicacao_refatoracao.md** - Boas práticas de refatoração de código

## Exemplos de Uso

### Validar Número Primo

```python
from num_primo import eh_primo

resultado = eh_primo(17)
print(f"17 é primo? {resultado}")  # True

resultado = eh_primo(4)
print(f"4 é primo? {resultado}")   # False
```

## Notas Adicionais

- Todos os scripts podem ser executados diretamente pelo terminal
- A documentação em Markdown fornece explicações detalhadas de cada conceito
- Use o VS Code com GitHub Copilot para assistência durante o desenvolvimento

## Autor

Desenvolvido como material de aprendizado e teste de assistência de código.