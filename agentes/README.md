# Agentes de IA — vender e atender a consultoria

Esta pasta guarda o "cérebro" dos agentes de IA da consultoria. Não é código de programa: são
**instruções em português** que a gente cola dentro de uma ferramenta de chatbot (WhatsApp/Instagram)
ou de uma IA. Quanto melhores as instruções, mais profissional e vendedor o agente fica.

## O plano dos 5 agentes (funil)

1. **Conteúdo** — atrai (posts, reels, legendas)
2. **Recepcionista** — capta no Instagram e leva pro WhatsApp
3. **Vendedor** — qualifica, tira dúvidas e fecha a venda  ← **começamos por aqui (Fase 1)**
4. **Boas-vindas** — recebe a aluna nova (onboarding)
5. **Acompanhamento** — retém e pede indicações

## Como esta pasta está organizada

```
agentes/
├── README.md              ← este arquivo
├── vendedor/              ← Fase 1: o agente que vende no WhatsApp
│   ├── 01-persona.md      ← quem ele é, tom de voz, regras (PÚBLICO, sem preço)
│   └── 02-roteiro.md      ← como ele conduz a conversa e quebra objeções (PÚBLICO, sem preço)
└── _privado/              ← 🔒 SÓ NO SEU PC (no .gitignore, nunca vai pro GitHub)
    └── PLANOS-E-PRECOS.md ← seus planos, valores e formas de pagamento
```

## ⚠️ A regra mais importante: privacidade

- **Preço, link de pagamento e dado de cliente** ficam **só** na pasta `_privado/`.
- Essa pasta está no `.gitignore` do projeto → ela **nunca** é publicada no GitHub.
- Os arquivos `persona` e `roteiro` podem subir tranquilos: eles falam *como* vender, não *quanto* custa.
- Quando você for configurar o agente na ferramenta, aí sim você junta o roteiro **+** os preços do
  `_privado/` na cabeça do agente. O cliente só vê o resultado da conversa, nunca o arquivo.

## Status

- [x] Estrutura criada
- [x] `_privado/PLANOS-E-PRECOS.md` preenchido (5 perguntas da Fase 1 ✅)
- [x] `02-roteiro.md` finalizado
- [x] Prompt pronto pra colar: `_privado/PROMPT-COMPLETO.md`
- [ ] Agente vendedor montado na ferramenta (WhatsApp) ← próximo passo (Fase 2)
