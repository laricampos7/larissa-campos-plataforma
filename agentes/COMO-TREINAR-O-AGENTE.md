# Como treinar o agente pra fazer tudo que a Larissa faria

> "Treinar" aqui **não** é re-treinar o modelo de IA (fine-tuning) — isso é caro, exige milhares de
> exemplos e quase nunca compensa pra um negócio. O que realmente funciona é **engenharia de contexto**:
> dar à IA a sua persona + seus fatos + exemplos reais de como você responde, e ir **testando e corrigindo**
> até ela soar como você. É um ciclo, não um botão.

## A ideia em uma frase
Quanto mais exemplos reais e regras específicas você der, menos "genérico" o agente fica. O segredo é o
**material de treino** (que só você tem) + um **ciclo de correção**.

---

## As 5 camadas que tiram o "genérico"

1. **Persona e voz** — quem ele é e como ele fala (já temos em `vendedor/01-persona.md`).
2. **Fatos** — planos, preços, inclusos, formas de pagamento (já temos em `_privado/PLANOS-E-PRECOS.md`).
3. **Base de conhecimento (FAQ + casos especiais)** — respostas pra dúvidas reais e situações que exigem
   cuidado (fibromialgia, lesão, gestante, iniciante total, pós-cirúrgico...).
4. **Few-shot (exemplos reais)** — a camada mais poderosa. Pares de **"o que a lead diz" → "como você
   responde"**. A IA copia seu ritmo, suas palavras, sua pontuação. 5–10 exemplos bons já mudam tudo.
5. **Regras de borda** — quando NÃO responder sozinho (chamar a Larissa), o que nunca prometer, etc.

---

## O método (o ciclo de treino)

### Passo 1 — Coletar matéria-prima (sua "mente" no papel)
Junte, em `_privado/MATERIAL-DE-TREINO.md`:
- **Conversas reais** suas com leads (copie do WhatsApp, pode anonimizar o nome). Quanto mais real, melhor.
- **Perguntas frequentes** que você recebe — com a resposta do seu jeito.
- **Resultados reais** que você pode citar como prova (ex.: "aluna X: 32% → 18,8% de gordura em N meses").
- **Casos especiais** e como você conduz cada um (saúde, iniciante, "sumiu e voltou", "tá caro mesmo").
- **Seu método** em 2–3 frases, com suas palavras (o que te diferencia de verdade).

### Passo 2 — Transformar em exemplos (few-shot)
Pra cada situação, vire um par. Exemplo:
```
Lead: "achei caro"
Você: "[escreva AQUI, com as SUAS palavras, exatamente como você responderia no zap]"
```
Cubra pelo menos: saudação, dúvida de preço, objeção de tempo, "será que funciona", caso de saúde,
lead decidido, lead frio/que enrola, fechamento.

### Passo 3 — Testar (simular conversas)
Converse com o agente fingindo ser tipos diferentes de lead:
- a decidida (quer fechar logo) — ele conduz sem enrolar?
- a desconfiada ("será que funciona?") — ele dá prova específica?
- a que enrola/some — ele faz follow-up sem ser chato?
- a com questão de saúde — ele acolhe e te chama?
Você pode fazer isso comigo aqui, ou dentro da própria ferramenta depois.

### Passo 4 — Corrigir (a parte que é "treino" de verdade)
**Toda vez que ele responder diferente de como você responderia, isso é uma correção.** Anote o que saiu
errado e conserte de um destes 3 jeitos:
- ajustar uma frase da **persona** (tom), ou
- adicionar um **fato/regra** que faltava, ou
- adicionar um **exemplo few-shot** mostrando a resposta certa.
Depois teste de novo. Repete até ele te surpreender pela semelhança.

### Passo 5 — Versionar
Cada vez que melhorar, anote a data e o que mudou no fim do `PROMPT-COMPLETO.md`. Assim você sabe o que
funcionou e pode voltar atrás se piorar.

---

## Erros comuns (pra evitar)
- **Querer perfeição no dia 1.** Agente bom é resultado de uns 3–4 ciclos de teste/correção.
- **Exemplos inventados.** Use conversas REAIS — é o que carrega sua voz.
- **Prompt gigante e bagunçado.** Organizado em seções (persona / fatos / FAQ / exemplos / regras) a IA
  segue melhor do que um textão.
- **Esquecer as bordas.** O que ele faz quando não sabe? Quando é saúde? Defina sempre.

## Próximo passo
Preencha `_privado/MATERIAL-DE-TREINO.md` (nem que seja aos poucos) e me traga — eu transformo em persona +
FAQ + few-shot e atualizo o `PROMPT-COMPLETO.md`. Aí entramos no ciclo de teste e correção.
