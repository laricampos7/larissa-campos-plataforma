# Guia do código — entenda tudo por trás da sua plataforma

Este guia é pra **você aprender** o que cada arquivo faz, sem precisar ser programadora.
Leia de cima pra baixo a primeira vez; depois use como consulta. Tudo aqui é pt-BR e sem enrolação.

> Dica de leitura no VS Code: abra este arquivo lado a lado com o arquivo que ele está explicando
> (clique direito na aba → "Split right"). Assim você lê a explicação e vê o código ao mesmo tempo.

---

## 1. A ideia em uma frase

Você preenche **uma planilha** com os treinos → roda **um programa** → ele gera um **app** pra cada aluna →
você publica → a aluna treina e registra as cargas → os dados voltam pra uma **planilha do Google**.

Não tem servidor, não tem banco de dados, não tem mensalidade de hospedagem. Tudo é arquivo.

---

## 2. As 3 partes do sistema

| Parte | Pra quem serve | Onde mora |
|-------|----------------|-----------|
| **Plataforma** | a aluna | `index.html` + `gerador/modelo-app.html` + `gerador/alunos/` |
| **Gestão** | você | `gerador/modelo-treinos.xlsx` + `gerador/gerar_treinos.py` + `google-sheets/` |
| **Agentes** | vender/atender (novo) | `agentes/` |

---

## 3. PLATAFORMA — o que a aluna vê

### `index.html` (na raiz)
É a **vitrine** (landing) do site. Logo + botão "Área do Aluno". Não lista as alunas (privacidade).
É a primeira página que abre em `laricampos7.github.io/larissa-campos-plataforma/`.

### `gerador/modelo-app.html` — o coração visual
É o **molde** do app da aluna (o arquivo mais comprido do projeto, ~1.165 linhas). Um arquivo só, com:
- **HTML** = a estrutura (as abas: Visão geral, Periodização, Treino, Evolução, Atividades, Check-in)
- **CSS** (dentro de `<style>`) = a aparência (cores, fontes, layout)
- **JavaScript** (dentro de `<script>`) = o que reage ao toque (trocar de aba, registrar carga, gráficos)

Coisas importantes pra NÃO quebrar:
- As **cores da marca** ficam no `:root{` lá no topo do `<style>`. Mexeu ali, mudou o tema inteiro.
- As **fontes** (Anton e Sora) e a **logo** estão "embutidas" no próprio arquivo (em base64). Isso faz o
  app funcionar offline e no celular. Não apague esses blocos.
- O que a aluna registra (metas, cargas, fotos) é salvo no **localStorage** — a "memória" do navegador
  dela. Fica no aparelho dela, não num servidor seu.

### `gerador/alunos/<nome>/index.html`
São os apps **já gerados**, um por aluna (joao-silva, mariana-costa, lara, karen-amor, jaqueline-galo).
Você **não edita esses à mão** — eles nascem do molde + da planilha quando você roda o gerador.

### `manifest.json` + `icon-*.png`
Fazem o app virar "instalável": quando a aluna escolhe "Adicionar à tela inicial", aparece com ícone e
nome, parecendo um aplicativo de verdade.

---

## 4. GESTÃO — o que você usa pra produzir

### `gerador/modelo-treinos.xlsx` — a planilha (seu painel de controle)
É **aqui que você trabalha**. Não precisa programar — é só preencher células. Abas:
- **Alunos**: uma linha por aluna (nome, plano, fase, descrição e os números do topo do app).
- **Treinos**: os exercícios. Repete o nome da aluna em cada linha; a ordem das linhas = ordem no app.
- **Biblioteca** (opcional): exercícios com grupo/dica/vídeo prontos pra reaproveitar.
- **Avaliacao** (opcional): avaliação física (composição corporal e circunferências) que vira os gráficos
  de evolução.

### `gerador/gerar_treinos.py` — o motor
É o programa em **Python** que faz a mágica: lê a planilha, pega o molde (`modelo-app.html`) e cria o app
de cada aluna dentro de `alunos/`. Você roda uma vez e ele atualiza todo mundo.

Como rodar (no terminal, dentro da pasta `gerador`):
```
pip install openpyxl
python gerar_treinos.py
```

Você não precisa entender o código dele pra usar — mas se tiver curiosidade, ele é dividido em
"funçõezinhas" com nomes do que fazem (ex.: `slug` transforma "Karen Amor" em "karen-amor"; `stat_inner`
monta os cards de Volume/Frequência do topo). Cada uma tem um comentário em português explicando.

### `google-sheets/Codigo.gs` — o recebedor (a "frequência")
É um script que mora **na sua planilha do Google** (em Extensões → Apps Script). Ele fica esperando os
apps das alunas mandarem dados: cada carga, check-in e foto vira uma linha na aba "Dados" (e as fotos vão
pra uma pasta no seu Google Drive). É assim que você acompanha quem está treinando de verdade.

### Os manuais (`*.md`)
- `gerador/COMO-USAR.md` — passo a passo de preencher a planilha e gerar os apps.
- `google-sheets/COMO-CONECTAR.md` — como ligar a planilha do Google.
- `README.md` — visão geral + como abrir no VS Code.
- `CLAUDE.md` — notas técnicas pra mim (o Claude) lembrar das regras do projeto.

---

## 5. AGENTES — a parte nova (em construção)

Fica na pasta `agentes/`. É onde vamos montar os robôs de IA que **vendem e atendem** (o plano dos 5
agentes: conteúdo → recepcionista → vendedor → boas-vindas → acompanhamento).

> ⚠️ Regra de ouro: **preço nunca vai pra internet.** Por isso existe a pasta `agentes/_privado/` — ela
> está no `.gitignore`, ou seja, fica **só no seu computador** e nunca sobe pro GitHub. Tudo que tiver
> valor de plano, link de pagamento ou dado de cliente mora lá dentro.

Veja `agentes/README.md` pra entender como essa pasta está organizada.

---

## 6. O caminho de uma atualização (pra fixar)

1. Você edita a planilha `modelo-treinos.xlsx`.
2. Roda `python gerar_treinos.py` → os apps em `alunos/` são reescritos.
3. Publica no GitHub (`git add -A`, `git commit`, `git push`).
4. A aluna dá um "puxão pra atualizar" (Ctrl+Shift+R) e vê o treino novo. O link dela nunca muda.

É só isso. Quando bater dúvida em qualquer arquivo, abre ele e me pergunta — a gente lê junto.
