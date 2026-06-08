# Conectar a plataforma ao Google Sheets (grátis)

Quando isso estiver ligado, cada **carga registrada**, **check-in** e **atividade** dos seus alunos
cai automaticamente numa planilha sua — seu painel central. Custo: **R$ 0**.

Você faz isto **uma vez**. Leva uns 10 minutos.

---

## Parte 1 — Criar a planilha e colar o código

1. Acesse **sheets.google.com** e crie uma planilha em branco (dê o nome que quiser, ex.: "Alunos Larissa").
2. No menu, clique em **Extensões → Apps Script**.
3. Vai abrir um editor de código. Apague o que estiver lá e **cole todo o conteúdo do arquivo `Codigo.gs`** (que está nesta pasta).
4. Clique no ícone de **salvar** (disquete).

## Parte 2 — Publicar (implantar) o código

1. No canto superior direito, clique em **Implantar → Nova implantação**.
2. Clique na engrenagem ⚙️ ao lado de "Selecionar tipo" e escolha **App da Web**.
3. Preencha:
   - **Executar como:** Eu (seu e-mail).
   - **Quem pode acessar:** **Qualquer pessoa**.
4. Clique em **Implantar**.
5. O Google vai pedir pra **autorizar** — siga: escolha sua conta → "Avançado" → "Acessar (nome do projeto)" → Permitir. (É normal, é o seu próprio script.)
6. No final aparece uma **URL do app da Web** terminando em **`/exec`**. **Copie essa URL.**

## Parte 3 — Colar a URL no app

1. Abra o arquivo **`index.html`** (no VS Code ou bloco de notas).
2. Procure por esta linha (logo no início do `<script>`):
   ```js
   var SHEETS_URL = '';
   ```
3. Cole sua URL entre as aspas:
   ```js
   var SHEETS_URL = 'https://script.google.com/macros/s/SEU-CODIGO/exec';
   ```
4. Salve.
5. **Importante:** se você usa o gerador de treinos, rode o `gerar_treinos.py` **depois** de colar a URL — assim os apps de todos os alunos já saem conectados.

## Pronto! Como testar

- Abra o app, vá em **Treino** e registre uma carga (ou faça um check-in).
- Abra sua planilha: deve aparecer uma nova linha na aba **"Dados"** com data, aluno, tipo, item, valor e detalhes.

---

## Observações honestas
- Funciona com o app **publicado** (hospedado) ou aberto direto no celular. Só **não** sincroniza se estiver sem internet na hora — mas o dado fica salvo no aparelho do aluno e você pode pedir pra ele reenviar.
- O app **não espera resposta** do Google (envia e segue), então nunca trava o aluno, mesmo se a internet falhar.
- Se quiser **desligar** a sincronização, é só deixar `var SHEETS_URL = '';` (vazio).
- Tudo isso é gratuito para o seu volume de alunos.
