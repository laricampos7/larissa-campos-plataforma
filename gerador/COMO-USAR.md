# Gerador de treinos — como usar

Você preenche **uma planilha** e o gerador cria o **app personalizado de cada aluno**, pronto pra enviar.
Tudo offline, sem banco de dados e sem custo. A **carga** é registrada pelo próprio aluno no app (fica salva no celular dele).

## O que tem nesta pasta
- `modelo-treinos.xlsx` — a planilha onde você monta os treinos.
- `gerar_treinos.py` — o script que gera os apps.
- `alunos/` — onde os apps gerados aparecem (uma pasta por aluno).

## Passo a passo

### 1. Preencha a planilha `modelo-treinos.xlsx`
- **Aba "Alunos"**: um aluno por linha (nome, plano, fase atual, descrição e os números do topo).
- **Aba "Treinos"**: liste os exercícios. Repita o nome do aluno em cada linha e use a coluna `dia` (A, B, C, D…).
  A **ordem das linhas** é a ordem que aparece no app. O `titulo_dia` é o nome do botão do dia.
- **Aba "Biblioteca"** (opcional): cadastre exercícios com grupo/dica/vídeo. Se você deixar essas
  colunas em branco na aba "Treinos", o gerador preenche sozinho pela Biblioteca (pelo nome do exercício).
- A coluna `video` aceita um link do YouTube. Se ficar vazia, o app abre uma busca pelo nome do exercício.

### 2. Rode o gerador
No computador, com Python instalado, abra o terminal nesta pasta e rode:

```
pip install openpyxl
python gerar_treinos.py
```

(no Mac/Linux pode ser `python3 gerar_treinos.py`)

Vai aparecer algo assim:
```
  ✓ João Silva  ->  alunos/joao-silva/index.html  (4 dias, 16 exercícios)
  ✓ Mariana Costa -> alunos/mariana-costa/index.html (2 dias, 6 exercícios)
```

### 3. Envie pra cada aluno
Dentro de `alunos/` haverá uma pasta por aluno com um `index.html`. Envie esse arquivo pelo WhatsApp
(ou publique online — veja o README do projeto). O aluno abre, vê o treino dele e **registra a carga** a cada série.

## Observações
- Mexer na planilha **não exige** saber programar — é só preencher as células.
- Rodou de novo o gerador? Ele atualiza os apps. As cargas que o aluno já registrou ficam no aparelho dele.
- Quer um painel central com os dados de todos os alunos? Esse é o passo do **Google Sheets** (combinado) —
  fazemos depois de publicar o app.
