# Plataforma Larissa de Campos — Consultoria Esportiva

Plataforma de acompanhamento de alunos (treino, periodização, evolução, atividades e check-in).
É um único arquivo `index.html` (HTML + CSS + JavaScript), sem nada para instalar ou compilar.

---

## 1. Abrir o projeto no VS Code

1. Baixe e extraia esta pasta (`larissa-campos-plataforma`) no seu computador.
2. Abra o **VS Code**.
3. Menu **Arquivo → Abrir Pasta...** e escolha a pasta `larissa-campos-plataforma`.

## 2. Ver a plataforma funcionando (pré-visualização)

Jeito mais simples:
- Clique duas vezes em `index.html` no seu computador → abre no navegador.

Dentro do VS Code (atualiza sozinho enquanto você edita):
1. Abra a aba **Extensões** (`Ctrl+Shift+X` no Windows/Linux, `Cmd+Shift+X` no Mac).
2. Procure por **Live Server** e clique em **Install**.
3. Clique com o botão direito em `index.html` → **Open with Live Server**.

## 3. Colocar o Claude trabalhando dentro do VS Code

Pré-requisitos: VS Code versão 1.98 ou superior + uma conta Anthropic.

1. Na aba **Extensões** (`Ctrl+Shift+X` / `Cmd+Shift+X`), procure por **Claude Code** e clique em **Install**.
2. Abra o painel do Claude: clique no ícone **✱ Claude Code** no canto inferior direito do VS Code
   (ou no ícone da faísca no canto superior direito quando um arquivo está aberto).
3. Na primeira vez, clique em **Sign in** e faça o login pelo navegador.
4. Peça o que quiser em português. Exemplos:
   - "Troque a cor de fundo por um cinza um pouco mais escuro."
   - "Adicione uma aba de Nutrição com um registro de refeições."
   - "Coloque minha foto no cabeçalho" (e arraste a foto para o chat).
5. Quando o Claude propõe uma mudança, ele mostra um **antes/depois** lado a lado e pede sua
   permissão. Você pode **aceitar, recusar ou pedir ajuste**.

> Dica: deixe o arquivo `index.html` aberto e selecione um trecho antes de pedir algo — o Claude
> entende exatamente a parte que você quer mudar.

---

## Como editar você mesma (sem o Claude)

Tudo que muda com frequência está bem no começo do `index.html`:

- **Cores da marca**: procure por `:root{` no topo do arquivo. Há um bloco marcado com
  `>>> TROQUE AQUI PELAS CORES DO SEU LOGO <<<`.
- **Nome / textos do cabeçalho**: procure por `LARISSA CAMPOS` / `CONSULTORIA ESPORTIVA`.
- **Dados de exemplo do aluno**: estão no `<script>` no final do arquivo (metas, atividades, etc.).

As metas e as atividades que você cadastra ficam salvas no navegador do computador onde a
plataforma for aberta.
