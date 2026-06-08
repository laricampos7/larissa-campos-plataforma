#!/usr/bin/env python3
# Gera o app de cada aluno a partir da planilha modelo-treinos.xlsx
# Uso:  python gerar_treinos.py
import json, re, os, unicodedata, sys
from openpyxl import load_workbook

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(BASE, "..", "index.html")     # o app serve de modelo
XLSX = os.path.join(BASE, "modelo-treinos.xlsx")
OUT = os.path.join(BASE, "alunos")

DESC_PADRAO = ("Você está na fase de maior intensidade do seu ciclo. Foco em cargas "
               "progressivas, técnica impecável e recuperação de qualidade. Estamos "
               "construindo o pico do seu desempenho.")

def slug(s):
    s = unicodedata.normalize("NFD", str(s)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "aluno"

def linhas(ws):
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []
    head = [str(h).strip() if h is not None else "" for h in rows[0]]
    out = []
    for r in rows[1:]:
        if all(c is None or str(c).strip() == "" for c in r):
            continue
        out.append({head[i]: ("" if r[i] is None else str(r[i]).strip()) for i in range(len(head))})
    return out

def main():
    if not os.path.exists(XLSX):
        sys.exit("Planilha não encontrada: " + XLSX)
    if not os.path.exists(TEMPLATE):
        sys.exit("Modelo index.html não encontrado em " + TEMPLATE)

    wb = load_workbook(XLSX, data_only=True)
    alunos = linhas(wb["Alunos"]) if "Alunos" in wb.sheetnames else []
    treinos = linhas(wb["Treinos"]) if "Treinos" in wb.sheetnames else []
    biblio = {}
    if "Biblioteca" in wb.sheetnames:
        for b in linhas(wb["Biblioteca"]):
            biblio[b.get("exercicio", "").lower()] = b

    template = open(TEMPLATE, encoding="utf-8").read()
    os.makedirs(OUT, exist_ok=True)
    gerados = 0

    for al in alunos:
        nome = al.get("nome", "").strip()
        if not nome:
            continue
        # monta os dias preservando a ordem das linhas
        dias, ordem = {}, []
        for t in treinos:
            if t.get("aluno", "").strip().lower() != nome.lower():
                continue
            d = t.get("dia", "").strip() or "A"
            if d not in dias:
                dias[d] = {"dia": d, "titulo": t.get("titulo_dia", "").strip() or ("Dia " + d),
                           "label": t.get("titulo_dia", "").strip() or ("Dia " + d), "exercicios": []}
                ordem.append(d)
            ref = biblio.get(t.get("exercicio", "").lower(), {})
            dias[d]["exercicios"].append({
                "nome": t.get("exercicio", "").strip(),
                "grupo": t.get("grupo", "").strip() or ref.get("grupo", ""),
                "series": t.get("series", "").strip(),
                "reps": t.get("reps", "").strip(),
                "rpe": t.get("rpe", "").strip(),
                "dica": t.get("dica", "").strip() or ref.get("dica", ""),
                "video": t.get("video", "").strip() or ref.get("video", ""),
            })
        treino = [dias[d] for d in ordem]
        if not treino:
            print("  (sem treinos para %s — pulando)" % nome)
            continue

        html = template
        html = html.replace("João Silva", nome)
        # iniciais do avatar
        ini = "".join(w[0] for w in nome.split()[:2]).upper() or "AL"
        html = html.replace('<div class="avatar">JS</div>', '<div class="avatar">%s</div>' % ini)
        if al.get("plano"):     html = html.replace("Plano Premium · 12ª semana", al["plano"])
        if al.get("bloco"):     html = html.replace("Mesociclo atual · Bloco 3 de 4", al["bloco"])
        if al.get("fase"):      html = html.replace("<h2>FASE DE FORÇA</h2>", "<h2>%s</h2>" % al["fase"])
        if al.get("descricao"): html = html.replace(DESC_PADRAO, al["descricao"])
        # números do topo (check-in / aderência / treinos / PRs)
        if any(al.get(k) for k in ("proximo_checkin", "aderencia", "treinos_mes", "prs")):
            hm = ('<div class="hero-meta">'
                  '<div><span>Próximo check-in</span><b>%s</b></div>'
                  '<div><span>Aderência (30d)</span><b style="color:var(--pos)">%s</b></div>'
                  '<div><span>Treinos no mês</span><b>%s</b></div>'
                  '<div><span>PRs no ciclo</span><b>%s</b></div>'
                  '</div>') % (al.get("proximo_checkin") or "—", al.get("aderencia") or "—",
                               al.get("treinos_mes") or "—", al.get("prs") or "0")
            html = re.sub(r'<div class="hero-meta">.*?</div>\s*</section>',
                          lambda m: hm + "\n  </section>", html, count=1, flags=re.S)
        novo_treino = "var TREINO = " + json.dumps(treino, ensure_ascii=False, separators=(",", ":")) + ";"
        html = re.sub(r"^var TREINO = .*;$", lambda m: novo_treino, html, count=1, flags=re.M)

        pasta = os.path.join(OUT, slug(nome))
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        gerados += 1
        print("  ✓ %s  ->  alunos/%s/index.html  (%d dias, %d exercícios)" %
              (nome, slug(nome), len(treino), sum(len(d["exercicios"]) for d in treino)))

    print("\nPronto! %d app(s) gerado(s) na pasta 'alunos/'." % gerados)
    print("Envie a pasta de cada aluno (ou só o index.html) pra ele abrir no celular.")

if __name__ == "__main__":
    main()
