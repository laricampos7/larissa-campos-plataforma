# Contexto do projeto (para o Claude Code)

Plataforma web de acompanhamento de uma consultoria esportiva (personal trainer **Larissa de Campos**).
O cliente (aluno) acessa para ver treino, periodização, evolução, gasto energético e fazer check-in.

## Stack e regras importantes
- **Arquivo único**: `index.html`. Contém HTML + CSS (dentro de `<style>`) + JavaScript (dentro de `<script>`). NÃO há build, framework ou dependências externas em tempo de execução.
- **Fontes embutidas**: Anton e Sora estão embutidas em base64 via `@font-face` no topo. NÃO remover — é o que faz o visual funcionar offline e no celular.
- **Logo embutida**: a logo da Larissa está embutida em base64 no `<img class="brand-logo">` do cabeçalho. NÃO substituir nem alterar as letras da logo. Se precisar trocar a imagem, peça o novo arquivo.
- **Persistência**: metas e atividades são salvas via `localStorage` (com try/catch). Manter esse padrão.
- **Sem armazenamento externo / sem chamadas de rede.** Tudo roda local no navegador.

## Identidade visual
- Variáveis de cor no `:root` (topo do `<style>`). Marca: vermelho `#FF1940`. Fundo: cinza. Texto sobre vermelho: branco (`--on-brand`).
- Para mudar o tema, editar APENAS as variáveis em `:root` quando possível.
- Títulos grandes usam a fonte **Anton**; texto usa **Sora**.

## Estrutura (abas)
Painéis controlados por JS, classe `.panel` + `.active`. Abas: Visão geral (`dash`), Periodização (`periodizacao`), Treino (`treino`), Evolução (`evolucao`), Atividades (`atividades`), Check-in (`checkin`).
- Gráficos são SVG desenhados à mão em JS (`drawChart`, `drawMethod`, `drawSuperc`, `renderActChart`). Recalculam ao abrir a aba (dependem da largura).
- Periodização traz os modelos linear/ondulatória/em blocos/conjugada com gráfico de volume × intensidade.
- Atividades calcula gasto calórico por MET × peso × tempo.

## Ao fazer mudanças
- Manter o português (pt-BR) na interface.
- Preservar responsividade (já há media queries) e o tema escuro/claro consistente via variáveis.
- Testar abrindo `index.html` no navegador (ou Live Server) e conferir cada aba.
