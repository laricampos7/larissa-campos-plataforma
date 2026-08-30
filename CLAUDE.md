# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Contexto do projeto

Plataforma web de acompanhamento de uma consultoria esportiva (personal trainer **Larissa de Campos**).
Dois papéis distintos: a Larissa produz conteúdo via planilha + gerador Python; o aluno consome o app gerado.

## Arquitetura geral (3 partes)

```
index.html                  → landing page pública (quem é a Larissa, botão "Área do Aluno")
gerador/modelo-app.html     → MOLDE do app do aluno (~1.200 linhas, HTML+CSS+JS num único arquivo)
gerador/gerar_treinos.py    → lê modelo-treinos.xlsx + modelo-app.html → gera gerador/alunos/<slug>/index.html
gerador/alunos/<slug>/      → apps gerados (um por aluno) — NÃO editar à mão
google-sheets/Codigo.gs     → Apps Script na planilha Google que recebe check-ins e cargas dos alunos
```

**`gerador/modelo-app.html` é o arquivo mais importante.** Quase toda mudança visual ou funcional do app do aluno vai aqui, não no `index.html` da raiz (que é só a landing).

## Como rodar / visualizar

Sem build. Abrir diretamente no navegador:
- `index.html` → landing
- `gerador/modelo-app.html` ou `gerador/alunos/<nome>/index.html` → app do aluno

Dentro do VS Code: clique direito → **Open with Live Server** (extensão Live Server).

## Como gerar os apps dos alunos

```bash
cd gerador
pip install openpyxl   # só na primeira vez
python gerar_treinos.py
```

O script reescreve toda a pasta `gerador/alunos/`. Depois: `git add -A && git commit && git push` para publicar no GitHub Pages.

## Regras que NÃO podem ser quebradas

- **Arquivo único por app**: `modelo-app.html` e cada `alunos/*/index.html` são HTML+CSS+JS num só arquivo. Sem imports externos em tempo de execução.
- **Fontes embutidas em base64**: Anton e Sora estão em `@font-face` no topo do `<style>` de `modelo-app.html`. NÃO remover.
- **Logo embutida em base64**: `<img class="brand-logo">` no cabeçalho do `modelo-app.html`. NÃO substituir sem um novo arquivo de imagem.
- **Persistência via localStorage**: cargas, check-ins e metas são salvos no navegador do aluno (com try/catch). Manter esse padrão; não introduzir chamadas de rede.
- **Apps gerados não se editam diretamente**: `gerador/alunos/*/index.html` é sempre sobrescrito pelo gerador. Mudanças devem ir em `modelo-app.html` (visual/funcional) ou `gerar_treinos.py` (dados).

## Identidade visual (modelo-app.html)

Variáveis de cor no `:root` do `<style>`. Marca: vermelho `#FF1940`. Para mudar tema, editar só as variáveis:
```css
:root {
  --brand: #FF1940;
  --on-brand: #fff;  /* texto sobre vermelho */
  /* --bg, --card, --line, --txt, --dim … */
}
```
Títulos grandes: fonte **Anton**. Corpo de texto: **Sora**.

## Estrutura de abas (modelo-app.html)

Painéis controlados por JS: `.panel` + `.active`. IDs das abas:
`dash` | `periodizacao` | `treino` | `evolucao` | `atividades` | `checkin`

Gráficos são SVG desenhados à mão em JS: `drawChart`, `drawMethod`, `drawSuperc`, `renderActChart`. Recalculam ao abrir a aba (dependem da largura atual do container).

## Gerador Python (gerar_treinos.py)

Funções-chave:
- `slug(s)` — normaliza nome para pasta ("Karen Amor" → "karen-amor")
- `stat_inner(raw, suffix)` — formata conteúdo dos cards de Volume/Frequência
- `nums_in(s)` — extrai números de strings como "7-8 reps" ou "3x12"
- `linhas(ws)` — lê aba da planilha como lista de dicts (cabeçalho da linha 1)

Planilha `modelo-treinos.xlsx` tem abas: **Alunos**, **Treinos**, **Biblioteca** (opcional), **Avaliacao** (opcional).

## Pasta agentes/

Em construção. Contém personas e roteiros para agentes de IA (vendas/atendimento via Botpress).
`agentes/_privado/` está no `.gitignore` — nunca sobe ao GitHub (contém preços e dados de clientes).

## Ao fazer mudanças

- Manter pt-BR na interface.
- Preservar responsividade (já há media queries) e o tema escuro/claro via variáveis CSS.
- Se a mudança afeta o visual/lógica do app do aluno, editar `gerador/modelo-app.html`, depois rodar o gerador para propagar aos `alunos/`.
- Se a mudança afeta só a landing, editar `index.html` na raiz.
