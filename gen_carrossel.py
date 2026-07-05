# -*- coding: utf-8 -*-
import math, os

W, BAND, A = 1080, 1080, 360
OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """<style>
  :root{
    --grafite:#343434; --amarelo:#FFCC29; --cinza:#8A8A8A; --branco:#FFFFFF;
    --disp:"Bahnschrift","Oswald","Arial Narrow",sans-serif;
    --body:"Fira Sans","Segoe UI",system-ui,-apple-system,sans-serif;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#202020;font-family:var(--body)}
  .page{position:relative;width:1080px;height:1350px;overflow:hidden;margin:0 auto}
  .orbit{position:absolute;inset:0;width:1080px;height:1350px;display:block}
  .content{position:absolute;inset:0;display:flex;flex-direction:column;padding:111px 75px}
  .spacer{flex:1 1 auto}
  .s-graf{background:#343434}
  .s-amar{background:#FFCC29}
  .s-branco{background:#FFFFFF}
  .eyebrow{font-family:var(--disp);font-weight:600;text-transform:uppercase;letter-spacing:.24em;font-size:27px;line-height:1}
  .title{font-family:var(--disp);font-weight:600;line-height:.99;margin-top:46px;letter-spacing:-.01em}
  .lead{font-size:34px;line-height:1.32;margin-top:36px;max-width:660px}
  .s-graf .eyebrow{color:#FFCC29}   .s-graf .title{color:#fff}      .s-graf .lead{color:#d9d6cf}
  .s-amar .eyebrow{color:#343434}   .s-amar .title{color:#343434}   .s-amar .lead{color:#4a3f1c}
  .s-branco .eyebrow{color:#8A8A8A} .s-branco .title{color:#343434} .s-branco .lead{color:#5a5a5a}
  .capa .title{font-size:98px}
  .std .title{font-size:62px}
  .bot{display:flex;align-items:center;justify-content:space-between}
  .word{font-family:var(--disp);font-weight:600;font-size:37px}
  .s-graf .word{color:#fff} .s-amar .word{color:#343434} .s-branco .word{color:#343434}
  .word .p{color:#FFCC29}
  .s-amar .word .p{color:#343434}
  .sig{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:12px;font-size:25px}
  .s-graf .sig{color:#b4b0a8} .s-amar .sig{color:#4a3f1c} .s-branco .sig{color:#6a6a6a}
  .selo{font-size:32px;line-height:1}
  .s-graf .selo{color:#FFCC29} .s-amar .selo{color:#343434} .s-branco .selo{color:#FFCC29}
  .pager{font-size:25px;letter-spacing:.05em}
  .s-graf .pager{color:#8f8b83} .s-amar .pager{color:#5b4f26} .s-branco .pager{color:#a2a2a2}
  ul.frentes{list-style:none;margin-top:50px;display:flex;flex-direction:column;gap:30px}
  ul.frentes li{font-weight:600;font-size:44px;color:#343434;line-height:1}
  .s-graf ul.frentes li{color:#fff}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:54px 43px;margin-top:54px}
  .stat .big{font-family:var(--disp);font-weight:600;font-size:102px;line-height:.9;color:#343434}
  .stat .lbl{font-size:30px;color:#5a5a5a;margin-top:12px;line-height:1.2}
  .s-graf .stat .big{color:#FFCC29} .s-graf .stat .lbl{color:#d9d6cf}
  ul.difs{list-style:none;margin-top:40px;display:flex;flex-direction:column;gap:27px}
  ul.difs li{display:grid;grid-template-columns:24px 1fr;gap:16px;align-items:baseline;font-size:33px;line-height:1.25;color:#343434}
  ul.difs .dmk{font-weight:700;font-size:30px;color:#343434;line-height:1}
  ul.difs b{font-weight:600}
  .s-graf ul.difs li{color:#e9e6df} .s-graf ul.difs .dmk{color:#FFCC29} .s-graf ul.difs b{color:#fff}
  .cta-lines{margin-top:36px;font-size:31px;line-height:1.7;color:#d9d6cf}
  .s-amar .cta-lines{color:#4a3f1c}
  .cta-lines .h{color:#FFCC29;font-weight:600}
  .s-amar .cta-lines .h{color:#343434}
  .uf{font-family:var(--disp);font-weight:600;font-size:92px;margin-top:44px;letter-spacing:.01em}
  .s-graf .uf{color:#FFCC29} .s-amar .uf{color:#343434} .s-branco .uf{color:#343434}
</style>"""

def orbit(i, N, bg):
    TOTAL = N * W
    y = lambda X: BAND - A * math.sin(math.pi * X / TOTAL)
    pts = [(90*s, round(y(i*W + 90*s), 1)) for s in range(13)]
    d = "M" + " L".join("%s,%s" % (x, yy) for x, yy in pts)
    cx = W * (i + 1) / (N + 1)
    Xg = i * W + cx
    cy = round(y(Xg), 1)
    r = round(20 + 4 * math.sin(math.pi * Xg / TOTAL), 1)
    col = "#FFCC29" if bg == "graf" else "#343434"
    return ('<svg class="orbit" viewBox="0 0 1080 1350"><path d="%s" fill="none" stroke="%s" '
            'stroke-width="6" stroke-linecap="round"/><circle cx="%s" cy="%s" r="%s" fill="%s"/></svg>'
            % (d, col, round(cx), cy, r, col))

def foot_word(pager):
    return '<div class="bot"><div class="word">e<span class="p">&middot;</span>sol</div><div class="pager">%s</div></div>' % pager

def foot_sig(text, pager):
    return '<div class="bot"><div class="sig"><span class="selo">&bull;</span>%s</div><div class="pager">%s</div></div>' % (text, pager)

ENDOSSO = "Uma empresa do Grupo E-SOL"

# each block: (label, bg_pref, extra_class, top_html, footer_kind)
def b_capa():
    top = ('<div><div class="eyebrow">Grupo E-SOL</div>'
           '<h2 class="title">Sete empresas.<br>Um <span style="color:#FFCC29">ecossistema</span> completo.</h2>'
           '<p class="lead">Do projeto &agrave; manuten&ccedil;&atilde;o: energia solar com engenharia pr&oacute;pria.</p></div>')
    return ("1 &middot; Capa", "capa", top, ("word", "arraste &rarr;"))

def b_frentes():
    nomes = ["E-SOL Engenharia","OPEX Solar","ELEX Solu&ccedil;&otilde;es El&eacute;tricas","ELEX Material El&eacute;trico","Est&uacute;dio Paisagismo","E-SOL Eco","E-SOL Shop"]
    li = "".join("<li>%s</li>" % n for n in nomes)
    top = ('<div><div class="eyebrow">As 7 frentes</div>'
           '<h2 class="title" style="font-size:60px">Um grupo, sete especialidades</h2>'
           '<ul class="frentes">%s</ul></div>' % li)
    return ("As 7 frentes", "std", top, ("word", None))

def b_numeros():
    top = ('<div><div class="eyebrow">O grupo em n&uacute;meros</div><div class="grid2">'
           '<div class="stat"><div class="big">+10</div><div class="lbl">anos de opera&ccedil;&atilde;o</div></div>'
           '<div class="stat"><div class="big">+1.000</div><div class="lbl">usinas instaladas</div></div>'
           '<div class="stat"><div class="big">7</div><div class="lbl">empresas no ecossistema</div></div>'
           '<div class="stat"><div class="big">3</div><div class="lbl">estados &middot; MG &middot; ES &middot; RJ</div></div>'
           '</div></div>')
    return ("O grupo em n&uacute;meros", "std", top, ("word", None), "branco")

def b_diferenciais():
    it = [("Equipe pr&oacute;pria:"," t&eacute;cnico e engenheiro, sem terceirizar"),
          ("Pronta entrega:"," estoque pr&oacute;prio, instala&ccedil;&atilde;o em 30&ndash;60 dias"),
          ("App de controle"," e 6 meses de manuten&ccedil;&atilde;o inclusa"),
          ("Parceria banc&aacute;ria"," para financiar o seu projeto")]
    li = "".join('<li><span class="dmk">&bull;</span><span><b>%s</b>%s</span></li>' % (a,b) for a,b in it)
    top = ('<div><div class="eyebrow">Por que E-SOL</div>'
           '<h2 class="title" style="font-size:60px">Engenharia pr&oacute;pria, do come&ccedil;o ao fim</h2>'
           '<ul class="difs">%s</ul></div>' % li)
    return ("Diferenciais", "std", top, ("sig", ENDOSSO))

def b_cobertura():
    top = ('<div><div class="eyebrow">Onde atuamos</div>'
           '<h2 class="title" style="font-size:62px">Presen&ccedil;a regional em tr&ecirc;s estados</h2>'
           '<div class="uf">MG &middot; ES &middot; RJ</div>'
           '<p class="lead">Minas Gerais, Esp&iacute;rito Santo e Rio de Janeiro, com equipe pr&oacute;pria e engenharia de longo prazo.</p></div>')
    return ("Cobertura", "std", top, ("word", None))

def b_comofunciona():
    it = [("1. Projeto"," de engenharia sob medida"),
          ("2. Instala&ccedil;&atilde;o"," com equipe pr&oacute;pria, sem terceirizar"),
          ("3. App de controle"," e monitoramento da usina"),
          ("4. Manuten&ccedil;&atilde;o"," inclusa por 6 meses")]
    li = "".join('<li><span class="dmk">&bull;</span><span><b>%s</b>%s</span></li>' % (a,b) for a,b in it)
    top = ('<div><div class="eyebrow">Como funciona</div>'
           '<h2 class="title" style="font-size:60px">Do projeto &agrave; manuten&ccedil;&atilde;o</h2>'
           '<ul class="difs">%s</ul></div>' % li)
    return ("Como funciona", "std", top, ("word", None))

def b_destaque(eyebrow, title, items):
    li = "".join('<li><span class="dmk">&bull;</span><span>%s</span></li>' % t for t in items)
    top = ('<div><div class="eyebrow">%s</div>'
           '<h2 class="title" style="font-size:58px">%s</h2>'
           '<ul class="difs">%s</ul></div>' % (eyebrow, title, li))
    return (eyebrow, "std", top, ("sig", ENDOSSO))

def b_dest_eng():
    return b_destaque("E-SOL Engenharia &middot; carro-chefe", "Energia solar com engenharia pr&oacute;pria",
        ["Equipe pr&oacute;pria: t&eacute;cnico e engenheiro","Estoque e pronta entrega (30&ndash;60 dias)","App de controle e 6 meses de manuten&ccedil;&atilde;o"])
def b_dest_opex():
    return b_destaque("OPEX Solar &middot; p&oacute;s-venda", "Sua usina rende mais com p&oacute;s-venda",
        ["Manuten&ccedil;&atilde;o, limpeza e gest&atilde;o de usinas","Laborat&oacute;rio de inversores, &uacute;nico na regi&atilde;o","App vital&iacute;cio de acompanhamento"])
def b_dest_elex():
    return b_destaque("ELEX &middot; el&eacute;trica", "Projeto el&eacute;trico e material profissional",
        ["ELEX Solu&ccedil;&otilde;es: projeto, execu&ccedil;&atilde;o e laudo","ELEX Material: pronta entrega e pre&ccedil;o justo","Engenheiro no projeto, eletricista na obra"])

def b_cta():
    top = ('<div><div class="eyebrow">Fale com a E-SOL</div>'
           '<h2 class="title" style="font-size:88px">Solicite seu or&ccedil;amento</h2>'
           '<div class="cta-lines"><span class="h">@esolengenharia</span><br>esolengenharia.com.br</div></div>')
    return ("CTA", "capa", top, ("sig", "Energia solar com engenharia pr&oacute;pria"))

SEQS = {
    3:  [b_capa, b_frentes, b_cta],
    4:  [b_capa, b_frentes, b_numeros, b_cta],
    6:  [b_capa, b_frentes, b_numeros, b_diferenciais, b_cobertura, b_cta],
    7:  [b_capa, b_frentes, b_numeros, b_diferenciais, b_cobertura, b_comofunciona, b_cta],
    8:  [b_capa, b_frentes, b_numeros, b_diferenciais, b_cobertura, b_comofunciona, b_dest_eng, b_cta],
    9:  [b_capa, b_frentes, b_numeros, b_diferenciais, b_cobertura, b_comofunciona, b_dest_eng, b_dest_opex, b_cta],
    10: [b_capa, b_frentes, b_numeros, b_diferenciais, b_cobertura, b_comofunciona, b_dest_eng, b_dest_opex, b_dest_elex, b_cta],
}

def build(N):
    blocks = [f() for f in SEQS[N]]
    secs = []
    for i, blk in enumerate(blocks):
        label, extra, top, foot = blk[0], blk[1], blk[2], blk[3]
        forced = blk[4] if len(blk) > 4 else None
        bg = forced if forced else ("graf" if i % 2 == 0 else "amar")
        bgcls = {"graf":"s-graf","amar":"s-amar","branco":"s-branco"}[bg]
        pager = "%d / %d" % (i+1, N)
        if foot[0] == "word":
            fp = foot[1] if foot[1] else pager
            footer = foot_word(fp)
        else:
            footer = foot_sig(foot[1], pager)
        content = top + '<div class="spacer"></div>' + footer
        secs.append('<section class="page %s %s" data-document-role="page" data-label="%s">\n  %s\n  <div class="content">%s</div>\n</section>'
                    % (bgcls, extra, "%d &middot; %s" % (i+1, label.split(' &middot; ')[-1]), orbit(i, N, bg), content))
    html = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>Carrossel institucional Grupo E-SOL &mdash; %d slides</title>\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n'
            % (N, CSS, "\n".join(secs)))
    path = os.path.join(OUT, "carrossel-%d.html" % N)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path

for N in [3,4,6,7,8,9,10]:
    print(build(N))
print("OK")
