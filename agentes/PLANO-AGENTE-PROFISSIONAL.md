# Plano do agente profissional — vendas + técnica + individualidade

Documento de estratégia. Objetivo: construir um agente **bem planejado**, focado em **vendas consultivas**,
que preserve a **voz técnica e individual da Larissa** e que **escale** (hoje: consultoria; depois: ebook).
Não é pra ser rápido — é pra ser perfeito por iteração.

## 1. Posicionamento do agente
- Não é "robô de tirar dúvida". É um **vendedor consultivo especialista** que conduz a pessoa do interesse
  ao fechamento, ensinando no caminho (autoridade gera confiança gera venda).
- Tom: especialista que ensina. Preserva as expressões e o método reais da Larissa.

## 2. Arquitetura do prompt (modular — cada camada é um "tijolo")
Um prompt profissional é organizado em blocos. Facilita treinar, corrigir e escalar:

1. **Identidade & posicionamento** — quem é, 20 anos de experiência, foco, voz.
2. **Método técnico da Larissa** — o conhecimento que gera autoridade (periodização, papel do
   fortalecimento, individualização, segurança/saúde). ← é o que mais "destigeneriza".
3. **Framework de venda consultiva (o método DELA, formalizado):**
   - **Diagnóstico** — perguntas curtas pra entender objetivo, rotina, histórico, dores.
   - **Educação** — explicar o PORQUÊ ligado ao caso da pessoa.
   - **Solução** — apresentar a consultoria como resposta sob medida (pitch estruturado).
   - **Fechamento** — conduzir com firmeza ao próximo passo (anamnese) + handoff pra Larissa.
4. **Catálogo de produtos (modular, pronto pra escalar):**
   - Hoje: consultoria (plano mensal / trimestral).
   - Depois: **ebook** (produto de entrada / para quem não está pronto pra consultoria → vira lead).
5. **Banco de objeções** — respostas no tom da Larissa (preço, tempo, "será que funciona", saúde).
6. **Guardrails** — nunca prometer resultado, não prescrever no chat, quando chamar a Larissa, API oficial.
7. **Exemplos few-shot reais** — conversas verdadeiras (a da Juliana é a primeira). Quanto mais, melhor.

## 3. Roadmap de treino (até ficar "perfeito")
"Perfeito" não vem no dia 1 — vem do ciclo. Fases:

- **Fase A — Base técnica** (preencher): método/técnica da Larissa em profundidade + 3–5 conversas reais
  + 3 resultados/provas. (É o que mais falta hoje.)
- **Fase B — Montar o prompt modular** (eu monto a partir do material).
- **Fase C — Ciclo de teste e correção** — simular leads variados, corrigir cada desvio. Repetir até soar
  inquestionavelmente como a Larissa.
- **Fase D — Escolher a plataforma e subir** (requisitos no item 5).
- **Fase E — Escalar** — integrar o ebook, follow-up de leads frios, captação no Instagram.

## 4. Critérios de qualidade (como saber que está profissional)
- Uma pessoa de fora não percebe que é IA.
- Toda resposta tem técnica (o porquê) + próximo passo.
- O agente nunca promete o que não deve, e chama a Larissa na hora certa.
- Em testes, ele responde como a Larissa responderia em ≥ 9 de 10 mensagens.

## 5. Plataforma (decidir DEPOIS do cérebro pronto) — requisitos
Pra ser profissional e escalável, a ferramenta precisa de:
- **API oficial do WhatsApp** (sem risco de banimento).
- **Base de conhecimento / RAG** (pra carregar o método técnico e o agente consultar).
- **Funil de vendas + follow-up** (recuperar lead que sumiu) e **handoff humano** (passar pra Larissa).
- **Multicanal** (WhatsApp + Instagram) e suporte a **link de pagamento** (importante pro ebook).
- Candidatas: Botpress (controle/técnico), ChatVolt/ManyChat (no-code). Decidir na Fase D.

## 6. O que preciso da Larissa (Fase A — começa aqui)
1. **Seu método/técnica em profundidade** — como você pensa um treino (avaliação, periodização, progressão,
   como adapta pra lesão/condição). Pode ser por áudio transcrito.
2. **Mais conversas reais** — de preferência uma que FECHOU e uma que NÃO fechou (pra ensinar os dois lados).
3. **Provas/resultados** — casos reais com números, quando possível.
4. **Visão do ebook** — tema, pra quem é, faixa de preço pensada (mesmo que rascunho).
