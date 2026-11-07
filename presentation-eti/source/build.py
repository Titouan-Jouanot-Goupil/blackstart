"""Assemble la présentation ETI (diapos de source/slides/) en une page autonome :
../black-start-eti.html (polices et image en base64, une diapo 1920 × 1080 par page imprimée).
Source : copie de l'Artifact « Black Start, présentation ETI »
(https://claude.ai/artifact/YaDY3A4bSGRMX5KHfvkgTa), à republier si on modifie les diapos.
Usage : python3 presentation-eti/source/build.py
PDF   : node livrables/source/convertir.mjs eti"""
import base64, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir, os.pardir))
OUT = os.path.join(HERE, os.pardir, "black-start-eti.html")

# Fichiers téléversés dans l'Artifact → fichiers du dépôt.
BLOBS = {
    "/_blob/45c6e648b46ef291506cea075f8244b3": ("landing/img/rapport-synthese.jpg", "image/jpeg"),
}
CLASH = "identite/source/clash-display-700.ttf"
PLEX = "landing/fonts/plex.css"  # IBM Plex Sans et Mono, déjà en base64

# Icônes <x-icon> du format Artifact, redessinées en SVG (traits, couleur héritée).
ICONES = {
    "Check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "Lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7.5a4 4 0 0 1 8 0V11"/>',
    "Home": '<path d="M4 11l8-7 8 7"/><path d="M6 9.5V20h12V9.5"/>',
}


def b64(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return base64.b64encode(f.read()).decode()


def icone(m):
    nom, style = m.group(1), m.group(2)
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
            f'stroke-linecap="round" stroke-linejoin="round" style="flex:none;{style}" aria-hidden="true">'
            f'{ICONES[nom]}</svg>')


def diapo(chemin):
    html = open(chemin, encoding="utf-8").read()
    html = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)  # notes de l'orateur
    html = re.sub(r'<x-icon name="(\w+)" style="([^"]*)"></x-icon>', icone, html)
    for blob, (rel, mime) in BLOBS.items():
        html = html.replace(blob, f"data:{mime};base64,{b64(rel)}")
    if "/_blob/" in html or "<x-" in html:
        raise SystemExit(f"{chemin} : élément non converti (/_blob/ ou <x-…>)")
    return html.strip()


def main():
    deck = json.load(open(os.path.join(HERE, "deck.json"), encoding="utf-8"))
    slides = "\n".join(diapo(os.path.join(HERE, "slides", f"{i}.html")) for i in deck["order"])
    plex = open(os.path.join(ROOT, PLEX), encoding="utf-8").read()
    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{deck["title"]}</title>
<style>
{plex}
@font-face{{font-family:"Clash Display";font-weight:700;src:url(data:font/ttf;base64,{b64(CLASH)}) format("truetype")}}
@page{{size:1920px 1080px;margin:0}}
*{{box-sizing:border-box;margin:0}}
html{{background:#2A3530}}
body{{margin:0;-webkit-font-smoothing:antialiased}}
h1,h2,h3{{font-weight:700}}
#pile{{width:1920px;transform-origin:0 0}}
section{{position:relative;width:1920px;height:1080px;overflow:hidden;break-after:page}}
section:last-child{{break-after:auto}}
@media print{{#pile{{transform:none!important}} body{{height:auto!important}} section{{margin:0}} html{{background:none}}}}
</style>
</head>
<body>
<div id="pile">
{slides}
</div>
<script>
// À l'écran : les diapos 1920 × 1080 sont réduites à la largeur de la fenêtre.
function ajuster(){{const p=document.getElementById('pile'),k=Math.min(1,innerWidth/1920);
p.style.transform='scale('+k+')';document.body.style.height=(p.offsetHeight*k)+'px';}}
addEventListener('resize',ajuster);ajuster();
</script>
</body>
</html>
"""
    open(OUT, "w", encoding="utf-8").write(page)
    print(f"{os.path.normpath(OUT)} : {len(page) / 1e6:.2f} Mo, {len(deck['order'])} diapos")


if __name__ == "__main__":
    main()
