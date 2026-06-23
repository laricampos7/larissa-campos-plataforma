# Fase D: colocar os agentes no ar com Botpress

Guia de implementação. A ordem importa: primeiro construir e testar o agente (rápido e grátis), só depois
encarar a parte da Meta (que é mais burocrática). Assim você valida o cérebro antes de gastar tempo com API.

O "cérebro" que vai ser colado está em `_privado/PROMPT-COMPLETO.md` (vendedor) e
`_privado/AGENTE-COBRANCA-RENOVACAO.md` (renovação).

---

## D1. Construir e testar o agente no Botpress (sem WhatsApp ainda)
1. Crie uma conta no Botpress Cloud (botpress.com) e abra o Botpress Studio.
2. Crie um novo bot (pode começar de um template em branco).
3. Em "Instructions" (instruções/identidade do agente), cole TODO o conteúdo do `PROMPT-COMPLETO.md`
   (a partir do BLOCO 1). É isso que dá a persona, o método e o fluxo de venda.
4. Em "Knowledge Base", adicione como base de conhecimento:
   - o método técnico (pode colar o BLOCO 3 ou subir o `MATERIAL-DE-TREINO.md`),
   - as objeções e o pitch.
   Isso deixa o agente preciso e com a sua autoridade.
5. Clique em "Publish" e use o link de teste (web) pra conversar com o agente como se fosse uma aluna.
6. Rode o ciclo de correção: cada resposta que sair diferente de você, a gente ajusta o prompt e republica.

> Vantagem: D1 é grátis e instantâneo. Você valida o agente todo ANTES de mexer com a Meta.

## D2. Conectar ao WhatsApp pela API oficial (a parte burocrática)
Pré-requisitos (Meta):
- Conta Meta Business (business.facebook.com) com o seu negócio verificado.
- Um número de telefone DEDICADO ao agente. Importante: número na API oficial não funciona mais no app
  normal do WhatsApp. Recomendo um número novo (um chip barato) só pro agente, e manter o seu
  (21 99457-4488) no celular pra atendimento pessoal e pro handoff.
- A aprovação da Meta pode levar de horas a alguns dias.

No Botpress:
1. No bot, vá na aba de integrações e instale a integração "WhatsApp".
2. Na configuração, use o método "OAuth authentication" (é o mais simples: o Botpress conduz a conexão
   com a Meta pra você, sem ter que copiar tokens manualmente).
3. Autorize com a sua conta Meta Business e selecione o número dedicado.
4. (Se preferir o modo manual, dá pra colar os 5 dados da Meta: verify token, access token, client secret,
   phone number ID e WABA ID. Mas o OAuth evita isso.)

## D3. Handoff (passar pra Larissa) e ir ao ar
- Configure no fluxo do Botpress um ponto de "transferir pra humana": quando o agente disser "vou chamar a
  Larissa", ele te notifica (por e-mail, ou marca a conversa) e para de responder até você assumir.
- Teste de ponta a ponta com o seu próprio número antes de divulgar.
- Atualize o link do WhatsApp no site/Instagram pra apontar pro número do agente (se for número novo).

## D4. Renovação proativa (depois)
As mensagens de cobrança/renovação são proativas (o agente inicia). Pra automatizar:
- Precisam de TEMPLATES de mensagem aprovados pela Meta (HSM).
- Precisam de um gatilho por data (a sua planilha de gestão, via integração ou exportação).
Isso é uma segunda etapa. No começo, dá pra usar as mensagens de renovação no manual (a planilha aponta,
você copia e cola).

## Custos a considerar (transparência)
- Botpress: tem plano gratuito com limite de mensagens/uso de IA; acima disso é pago.
- Meta/WhatsApp: cobra por conversa iniciada (faixa gratuita mensal + tarifa depois).
Vale checar os valores atuais antes de escalar.

## Ordem recomendada
D1 agora (construir e testar, de graça) → validar o agente → D2/D3 (WhatsApp oficial) → D4 (renovação) depois.
