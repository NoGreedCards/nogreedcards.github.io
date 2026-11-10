"""Baut die Website. Aufruf: python3 build.py <repo-ausgabe> <artifact-ausgabe>"""
import sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_OUT, ART_OUT = sys.argv[1], sys.argv[2]
read = lambda n: open(os.path.join(HERE, n), encoding="utf-8").read()

BASE_CSS = read("base.css")

EXTRA_CSS = r"""
[hidden]{display:none!important}
/* ---- Unterseiten ---- */
.page-hero{padding-block:56px 32px;display:grid;gap:14px}
.page-hero h1{font-size:clamp(36px,5.6vw,60px);font-weight:900;font-stretch:118%}
.page-hero h1 em{font-style:normal;color:var(--gold)}
.crumbs{font-size:13px;color:var(--muted)}
.crumbs a{color:var(--muted)}
nav a[aria-current="page"]{color:var(--gold-soft)}

/* Fortschritt: die 5 Stationen des Ankaufs */
.stepper{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:0;padding:0;list-style:none}
.stepper li{display:grid;gap:8px;font-size:13px;color:var(--muted);min-width:0}
.stepper li::before{content:"";height:3px;border-radius:2px;background:var(--line)}
.stepper li.done::before{background:color-mix(in srgb, var(--gold) 55%, var(--line))}
.stepper li.now::before{background:var(--gold)}
.stepper li.now{color:var(--fg);font-weight:600}
.stepper b{font-family:var(--font-mono);font-weight:400;font-size:11px;letter-spacing:.08em;color:var(--gold)}
@media (max-width:560px){ .stepper span{display:none} .stepper li.now span{display:inline} }

/* Formular */
.form-grid{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.8fr);gap:32px;align-items:start;padding-bottom:80px}
@media (max-width:900px){ .form-grid{grid-template-columns:1fr} }
form{display:grid;gap:28px}
fieldset{border:1px solid var(--line-soft);border-radius:var(--r);background:var(--panel);padding:24px;margin:0;display:grid;gap:18px;min-width:0}
legend{font-family:var(--font-display);font-stretch:112%;font-weight:800;font-size:18px;padding:0 8px;margin-left:-8px}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media (max-width:560px){ .row2{grid-template-columns:1fr} }
.f{display:grid;gap:6px;min-width:0}
.f > span{font-size:14px;font-weight:500}
.f small{font-size:12px;color:var(--muted)}
.f input,.f select,.f textarea{font:inherit;font-size:15px;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:11px 12px;width:100%;min-width:0}
.f textarea{min-height:130px;resize:vertical;font-family:var(--font-mono);font-size:14px}
.f input:focus,.f select:focus,.f textarea:focus{outline:none;border-color:var(--gold)}
.f.bad input{border-color:var(--warn)}
.err{font-size:13px;color:var(--warn)}
.opts{display:flex;flex-wrap:wrap;gap:10px}
.opt{position:relative}
.opt input{position:absolute;opacity:0;inset:0;cursor:pointer}
.opt span{display:block;padding:10px 14px;border:1px solid var(--line);border-radius:8px;font-size:14px;cursor:pointer;transition:border-color .15s, background .15s}
.opt input:checked + span{border-color:var(--gold);background:color-mix(in srgb, var(--gold) 12%, transparent);color:var(--gold-soft)}
.opt input:focus-visible + span{outline:2px solid var(--green);outline-offset:2px}
.opt-tag{font-style:normal;font-weight:400;color:var(--muted);font-size:12px}
.check{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:var(--muted)}
.check input{margin-top:4px;accent-color:var(--gold)}
.tabs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.tab{font:inherit;text-align:left;cursor:pointer;background:var(--panel);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;color:var(--fg);display:grid;gap:4px}
.tab b{font-family:var(--font-display);font-stretch:112%;font-size:17px}
.tab span{font-size:13px;color:var(--muted)}
.tab[aria-selected="true"]{border-color:var(--gold);background:color-mix(in srgb, var(--gold) 9%, var(--panel))}
.submit-row{display:flex;flex-wrap:wrap;gap:16px;align-items:center}
.demo-note{font-size:13px;color:var(--muted)}
.side{position:sticky;top:96px;display:grid;gap:16px}
.side .receipt{padding:22px}
.side-note{font-size:14px;color:var(--muted);border-left:2px solid var(--line);padding-left:14px;display:grid;gap:6px}
.side-note b{color:var(--fg);font-weight:600}

/* Zeitleiste und Karten */
.timeline{list-style:none;margin:0;padding:0;display:grid;gap:0}
.timeline > li{display:grid;grid-template-columns:56px minmax(0,1fr);gap:20px;padding-bottom:36px;position:relative}
.timeline > li::before{content:"";position:absolute;left:27px;top:44px;bottom:0;border-left:1px dashed var(--line)}
.timeline > li:last-child::before{display:none}
.t-num{width:56px;height:56px;border-radius:50%;border:2px solid var(--gold);display:grid;place-items:center;font-family:var(--font-mono);color:var(--gold);background:var(--bg)}
.t-body{display:grid;gap:8px;padding-top:6px}
.t-body h3{font-size:22px}
.t-body p{color:var(--muted);max-width:62ch}
.t-meta{display:flex;flex-wrap:wrap;gap:8px}
.t-meta .chip{white-space:normal}
.card{background:var(--panel);border:1px solid var(--line-soft);border-radius:var(--r);padding:24px;display:grid;gap:12px;min-width:0}
.card p,.card li{color:var(--muted)}
.card ul{margin:0;padding-left:18px;display:grid;gap:6px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media (max-width:860px){ .grid2,.grid3{grid-template-columns:1fr} }
.terms{counter-reset:t;display:grid;gap:14px;margin:0;padding:0;list-style:none;max-width:72ch}
.terms li{counter-increment:t;display:grid;grid-template-columns:40px 1fr;gap:12px;color:var(--muted)}
.terms li::before{content:"§" counter(t);font-family:var(--font-mono);color:var(--gold)}
.terms b{color:var(--fg);font-weight:600}
details{border-bottom:1px dashed var(--line);padding-block:16px}
summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-family:var(--font-mono);color:var(--gold)}
details[open] summary::after{content:"–"}
details p{color:var(--muted);margin-top:10px;max-width:66ch}
.ticket{border:1px dashed var(--gold);border-radius:var(--r);padding:24px;display:grid;gap:6px;background:var(--panel)}
.ticket .id{font-family:var(--font-mono);font-size:clamp(24px,4vw,34px);color:var(--gold);letter-spacing:.04em}
.summary{display:grid;gap:0;margin:0}
.summary div{display:flex;justify-content:space-between;gap:16px;padding-block:10px;border-bottom:1px dashed var(--line-soft);font-size:15px}
.summary dt{color:var(--muted)}
.summary dd{margin:0;text-align:right;font-family:var(--font-mono);font-size:14px;overflow-wrap:anywhere}
.callout{border:1px solid color-mix(in srgb, var(--warn) 50%, transparent);background:color-mix(in srgb, var(--warn) 9%, transparent);border-radius:var(--r);padding:16px 18px;font-size:15px}
.callout b{color:var(--fg)}

/* Rechner mit Kategorien, Vertrauen, Sortierhilfe, Zwei-Schritt-Formular */
.text-link{font:inherit;font-weight:600;background:none;border:0;padding:0;cursor:pointer;color:var(--gold-soft);text-decoration:none}
.text-link:hover{text-decoration:underline}
.hero-actions{align-items:center}
.hero-actions .text-link{padding:12px 4px}
@media (max-width:420px){ header .btn-sm{white-space:nowrap;padding-inline:12px} header .brand span{font-size:15px} }
.seg{padding-top:14px}
.seg .opt{flex:1}
.seg .opt span{text-align:center;padding:8px 10px}
.calc-row{display:grid;grid-template-columns:minmax(0,1fr) 92px 70px;gap:10px;align-items:center;padding-block:8px;font-size:14px}
.calc-row > span:first-child{display:grid;gap:2px}
.calc-row small{font-size:12px;color:var(--muted)}
.calc-row .field input{font-size:16px;padding-block:7px;text-align:right}
.calc-row > .mono{text-align:right;font-size:14px}
#bc-sorted,#bc-unsorted{padding-block:6px}
#bulk-calc.bad .receipt-foot#bulk-hint{color:var(--warn)}
.bonus{color:var(--green)}
.bonus:empty{display:none}
.trustband{border-top:1px solid var(--line-soft);padding-block:28px}
.trust-grid{display:grid;grid-template-columns:minmax(0,1.5fr) repeat(2,minmax(0,.8fr)) minmax(0,1.3fr);gap:16px;align-items:stretch}
@media (max-width:980px){ .trust-grid{grid-template-columns:1fr 1fr} }
@media (max-width:560px){ .trust-grid{grid-template-columns:1fr} }
.who{display:flex;gap:14px;align-items:center}
.who div,.promise{display:grid;gap:4px;font-size:14px;color:var(--muted)}
.who b,.promise b{color:var(--fg);font-weight:600;font-size:15px}
.avatar{flex:none;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;background:var(--panel);border:2px solid var(--gold);font-family:var(--font-display);font-weight:900;font-size:22px;color:var(--gold)}
.mini-score{display:grid;gap:4px;align-content:center;background:var(--panel);border:1px solid var(--line-soft);border-radius:var(--r);padding:14px 16px;text-decoration:none;font-size:13px;color:var(--muted);transition:border-color .15s}
.mini-score:hover{border-color:var(--gold)}
.mini-score b{font-family:var(--font-display);font-stretch:112%;font-size:18px;color:var(--fg)}
.promise{border-left:2px solid var(--green);padding-left:14px;align-content:center}
.promise a{color:var(--gold-soft)}
.sort-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
@media (max-width:980px){ .sort-grid{grid-template-columns:1fr 1fr} }
@media (max-width:560px){ .sort-grid{grid-template-columns:1fr} }
.sym{font-family:var(--font-mono);font-size:22px;color:var(--gold)}
.sort-grid h3{font-size:19px}
.sort-foot{margin-top:24px;color:var(--muted)}
.source-note{margin-top:32px;border-top:1px dashed var(--line);border-bottom:0}
.source-note a{color:var(--gold-soft)}
.part{display:grid;gap:28px}
.part-head{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:baseline}
.part-head b{font-family:var(--font-display);font-stretch:112%;font-size:20px}
.part-bar{grid-column:1 / -1;height:3px;background:var(--line);border-radius:2px;overflow:hidden}
.part-bar i{display:block;height:100%;background:var(--gold)}
.row3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
@media (max-width:640px){ .row3{grid-template-columns:1fr} }
#f-menge:has(.err[hidden]){display:none}

/* Rechtstexte */
.legal{max-width:72ch;display:grid;gap:14px;padding-bottom:80px;color:var(--muted)}
.legal h2{font-size:22px;color:var(--fg);margin-top:22px}
.legal h3{font-size:17px;color:var(--fg);margin-top:8px}
.legal b{color:var(--fg);font-weight:600}
.legal a{color:var(--gold-soft)}
.legal ul{margin:0;padding-left:20px;display:grid;gap:6px}
.legal address{font-style:normal;color:var(--fg);line-height:1.6}
.reviews-main{grid-template-columns:minmax(0,2.2fr) minmax(0,1fr);align-items:start}
@media (max-width:860px){ .reviews-main{grid-template-columns:1fr} }
.ebay-box{background:var(--panel);border:1px solid var(--line-soft);border-radius:var(--r);padding:28px;display:grid;gap:8px;min-width:0}
.ebay-head{display:grid;grid-template-columns:auto 1fr;gap:6px 24px;align-items:center;padding-bottom:8px}
.ebay-head > div{display:grid;gap:4px}
.ebay-head .score-num{grid-row:auto}
@media (max-width:560px){ .ebay-head{grid-template-columns:1fr} .ebay-head .score-num{font-size:44px} .ebay-box{padding:20px} }
.stars{grid-column:1 / -1;font-size:13px;color:var(--muted)}
.stars span{color:var(--gold);letter-spacing:2px;margin-right:6px}
.ebay-head .score-name{font-family:var(--font-display);font-stretch:112%;font-weight:800;font-size:22px}
.ebay-box .quotes{grid-template-columns:1fr;gap:16px}
.ebay-box .score-link{text-decoration:none}
.ebay-box .score-link:hover span:first-child{text-decoration:underline}
.score-cm{padding:20px;gap:4px 16px}
.score-cm .score-num{font-size:34px}
.score-cm .score-name{font-size:15px}
.score-cm .score-meta{font-size:13px}
.quotes .quote{margin:0;border-left-color:var(--gold)}
.quotes .quote p{font-size:17px;color:var(--fg)}
"""

CSS = BASE_CSS.replace("--green:#39ff8c;", "--green:#39ff8c;\n  --warn:#e8896b;     /* Hinweise und Fehler */") + EXTRA_CSS

# Schriften liegen lokal in /fonts (keine Verbindung zu Google, Lizenz: SIL OFL 1.1)
FONT_CSS = """
@font-face{font-family:"Archivo";font-style:normal;font-display:swap;font-weight:100 900;font-stretch:62% 125%;src:url(fonts/archivo-latin-standard-normal.woff2) format("woff2")}
@font-face{font-family:"Figtree";font-style:normal;font-display:swap;font-weight:300 900;src:url(fonts/figtree-latin-wght-normal.woff2) format("woff2")}
@font-face{font-family:"JetBrains Mono";font-style:normal;font-display:swap;font-weight:400;src:url(fonts/jetbrains-mono-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"JetBrains Mono";font-style:normal;font-display:swap;font-weight:600;src:url(fonts/jetbrains-mono-latin-600-normal.woff2) format("woff2")}
"""
FONTS = '<link rel="preload" href="fonts/archivo-latin-standard-normal.woff2" as="font" type="font/woff2" crossorigin>'

SEAL = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12.5 L9.5 18 L20 6" stroke="var(--green)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def header(cur):
    def a(href, label, key):
        c = ' aria-current="page"' if key and key == cur else ''
        return f'<a class="nav-link" href="{href}"{c}>{label}</a>'
    return f'''<header>
  <div class="wrap bar">
    <a href="index.html" class="brand" aria-label="NoGreedCards Startseite">
      <span class="seal">{SEAL}</span>
      <span class="brand-name">NOGREEDCARDS</span>
    </a>
    <nav aria-label="Hauptnavigation">
      {a("ablauf.html","So läuft der Ankauf","ablauf")}
      {a("index.html#bewertungen","Bewertungen","")}
      {a("index.html#shops","Shops","")}
      <a class="btn btn-gold btn-sm" href="ankauf.html">Angebot holen</a>
    </nav>
  </div>
</header>'''

FOOTER = '''<footer>
  <div class="wrap foot">
    <div style="display:grid;gap:6px">
      <span class="foot-motto">Keep the Hobby Cheap.</span>
      <span>Faire Preise. Ehrlicher Bulk. Keine Abzocke.</span>
    </div>
    <nav aria-label="Fußzeile">
      <a href="ablauf.html">Ankauf</a>
      <a href="versand.html">Versand</a>
      <a href="https://www.youtube.com/@NoGreedCollector" target="_blank" rel="noopener">YouTube</a>
      <a href="https://playagainst.xyz" target="_blank" rel="noopener">Turniere</a>
      <!-- PLATZHALTER: Impressum und Datenschutz anlegen, bevor die Seite gewerblich live geht -->
      <a href="mailto:nogreedtcg@gmail.com">Kontakt</a>
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
    </nav>
  </div>
</footer>'''

STEPS = ["Anfrage", "Angebot", "Versand", "Prüfung", "Auszahlung"]
def stepper(now):
    items = []
    for i, s in enumerate(STEPS, 1):
        cls = "now" if i == now else ("done" if i < now else "")
        cur = ' aria-current="step"' if i == now else ''
        items.append(f'<li class="{cls}"{cur}><b>0{i}</b><span>{s}</span></li>')
    return '<ol class="stepper" aria-label="Fortschritt des Ankaufs">' + "".join(items) + '</ol>'

def page(name, title, desc, cur, body, script=""):
    head = f'''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="apple-touch-icon" href="icon-180.png">
{FONTS}
<style>{FONT_CSS}{CSS}</style>
'''
    content = f"{header(cur)}\n{body}\n{FOOTER}\n" + (f"<script>{script}</script>\n" if script else "")
    full = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n' + content + '</body>\n</html>\n')
    open(os.path.join(REPO_OUT, name), "w", encoding="utf-8").write(full)
    # Startseite im Artifact ohne eigenes Gerüst (wird beim Veröffentlichen ergänzt)
    open(os.path.join(ART_OUT, name), "w", encoding="utf-8").write(head + content if name == "index.html" else full)

# ---------------- Startseite ----------------
landing = read("landing_main.html")
landing = landing.replace('<a class="btn btn-gold" href="kontakt.html">Bulk anbieten</a>', '<a class="btn btn-gold" href="ankauf.html#bulk">Bulk anbieten</a>')
landing = landing.replace('<a class="btn btn-line" href="#verkaufen">Preise und Ablauf</a>', '<a class="btn btn-line" href="ablauf.html">So läuft der Ankauf</a>')
landing = landing.replace('<a class="btn btn-line" href="kontakt.html">Bulk anbieten</a>', '<a class="btn btn-line" href="ankauf.html#bulk">Bulk anbieten</a>')
landing = landing.replace('<a class="btn btn-gold" href="kontakt.html">Karten anfragen</a>', '<a class="btn btn-gold" href="ankauf.html#einzel">Karten anfragen</a>')
old_steps = landing[landing.index('      <ol class="steps"'):landing.index('      </ol>') + len('      </ol>')]
landing = landing.replace(old_steps, '''      <ol class="steps" aria-label="So läuft ein Ankauf ab">
        <li><b>Anfrage</b><span>Formular ausfüllen, dauert 2 Minuten.</span></li>
        <li><b>Angebot</b><span>Du bekommst ein Angebot per WhatsApp oder E-Mail.</span></li>
        <li><b>Versand</b><span>Du schickst die Karten per Post, mit Packanleitung.</span></li>
        <li><b>Prüfung und Auszahlung</b><span>Ich zähle nach und zahle dir den Betrag aus.</span></li>
      </ol>
      <p style="margin-top:24px"><a href="ablauf.html" style="color:var(--gold-soft)">Alle Schritte und Ankaufbedingungen ansehen →</a></p>''')
assert landing.count("kontakt.html") == 0
page("index.html", "NoGreedCards",
     "NoGreedCards aus dem Saarland kauft deine Pokémon-Sammlung und deinen Bulk zu festen Preisen und Einzelkarten zu 70 % des Cardmarket-Preises.",
     "", landing, read("prices.js") + read("landing.js"))

# ---------------- Anfrage ----------------
ankauf = f'''<main>
  <div class="wrap page-hero">
    <div class="crumbs"><a href="index.html">Start</a> / Ankauf-Anfrage</div>
    <h1>Was willst du <em>verkaufen</em>?</h1>
    <p class="lead">Zwei kurze Teile, etwa 2 Minuten. Du bekommst ein Angebot per WhatsApp oder E-Mail. Bitte schick noch keine Karten, bevor du das Angebot hast.</p>
    <div style="margin-top:12px">{stepper(1)}</div>
  </div>

  <div class="wrap form-grid">
    <!-- FORMULAR: Formspree-ID unten in FORM_ID eintragen. Ohne ID läuft das Formular im Vorschau-Modus. -->
    <form id="ankauf-form" novalidate>
      <div class="part" id="part1">
        <div class="part-head"><span class="eyebrow">Teil 1 von 2</span><b>Deine Karten</b><span class="part-bar"><i style="width:50%"></i></span></div>
        <div class="tabs" role="tablist" aria-label="Art des Ankaufs">
          <button type="button" class="tab" role="tab" id="tab-bulk" aria-controls="fs-bulk" aria-selected="true"><b>Bulk</b><span>ab 500 Karten, feste Preise</span></button>
          <button type="button" class="tab" role="tab" id="tab-einzel" aria-controls="fs-einzel" aria-selected="false"><b>Einzelkarten</b><span>70 % vom Cardmarket-Preis</span></button>
        </div>
        <input type="hidden" name="art" id="art" value="Bulk">
        <input type="hidden" name="anfragenummer" id="h-id">
        <input type="hidden" name="karten_gesamt" id="h-karten">
        <input type="hidden" name="schaetzung" id="h-schaetzung">
        <input type="hidden" name="_redirect" id="h-redirect">

        <fieldset id="fs-bulk" role="tabpanel" aria-labelledby="tab-bulk">
          <legend>Deine Bulk-Karten</legend>
          <div class="f"><span>Hast du sortiert?</span>
            <div class="opts">
              <label class="opt"><input type="radio" name="sortiert" value="sortiert" checked><span>Ja, grob sortiert</span></label>
              <label class="opt"><input type="radio" name="sortiert" value="unsortiert"><span>Nein, alles gemischt</span></label>
            </div>
            <small>Unsicher? <a href="index.html#sortieren" style="color:var(--gold-soft)">So sortierst du in 10 Minuten</a>. Grob schätzen reicht: ein voller Schuhkarton sind etwa 800 bis 1.000 Karten.</small>
          </div>
          <div class="row3" id="grp-sorted">
            <label class="f"><span>Common &amp; Uncommon</span><input id="cu" name="common_uncommon" type="text" inputmode="numeric" placeholder="z. B. 1.500" autocomplete="off"><small>0,7 ct je Karte</small></label>
            <label class="f"><span>Holo &amp; Reverse</span><input id="holo" name="holo_reverse" type="text" inputmode="numeric" placeholder="z. B. 400" autocomplete="off"><small>1,5 ct, ab 500: 2 ct</small></label>
            <label class="f"><span>EX, V, GX, ex</span><input id="ex" name="ex_v_gx" type="text" inputmode="numeric" placeholder="z. B. 10" autocomplete="off"><small>25 ct, ab 20: 35 ct</small></label>
          </div>
          <div id="grp-un" hidden>
            <label class="f"><span>Anzahl, alles gemischt</span><input id="un" name="unsortiert" type="text" inputmode="numeric" placeholder="z. B. 2.000" autocomplete="off"><small>0,6 ct je Karte</small></label>
          </div>
          <div class="f" id="f-menge"><span class="err" id="err-menge" hidden>Ich kaufe Bulk ab 500 Karten an.</span></div>
          <label class="check"><input type="checkbox" name="energien" value="ja"><span>Ich schicke auch Basis-Energien mit (kostenlos, ich nehme sie gern).</span></label>
          <div class="row2">
            <label class="f"><span>Sprache</span>
              <select id="sprache" name="sprache"><option>Deutsch</option><option>Englisch</option><option>Gemischt</option><option>Andere</option></select>
            </label>
            <label class="f"><span>Zustand</span>
              <select id="zustand" name="zustand"><option>Gut, wenig bespielt</option><option>Gemischt</option><option>Stark bespielt</option></select>
            </label>
          </div>
        </fieldset>

        <fieldset id="fs-einzel" role="tabpanel" aria-labelledby="tab-einzel" hidden>
          <legend>Deine Einzelkarten</legend>
          <label class="f" id="f-liste"><span>Kartenliste</span>
            <textarea id="liste" name="liste" placeholder="Glurak ex · Obsidianflammen 125 · NM · 1×&#10;Pikachu · Karmesin &amp; Purpur 151 · EX · 2×"></textarea>
            <small>Eine Karte pro Zeile: Name, Set, Nummer, Zustand, Anzahl. Fotos schickst du mir später per WhatsApp oder E-Mail.</small>
            <span class="err" id="err-liste" hidden>Bitte trag mindestens eine Karte ein.</span>
          </label>
          <label class="f"><span>Cardmarket-Wert aller Karten (optional)</span>
            <input id="wert" name="wert" type="text" inputmode="decimal" placeholder="z. B. 45,00" autocomplete="off">
            <small>Wenn du ihn kennst. Ich prüfe jede Karte trotzdem selbst nach.</small>
          </label>
        </fieldset>

        <div class="submit-row">
          <button class="btn btn-gold" type="button" id="next">Weiter zu Teil 2</button>
          <span class="demo-note">Noch unverbindlich.</span>
        </div>
      </div>

      <div class="part" id="part2" hidden>
        <div class="part-head"><span class="eyebrow">Teil 2 von 2</span><b>Kontakt und Auszahlung</b><span class="part-bar"><i style="width:100%"></i></span></div>
        <fieldset>
          <legend>Auszahlung</legend>
          <div class="f"><span>Wie willst du dein Geld?</span>
            <div class="opts">
              <label class="opt"><input type="radio" name="auszahlung" value="PayPal" checked><span>PayPal</span></label>
              <label class="opt"><input type="radio" name="auszahlung" value="Überweisung"><span>Überweisung</span></label>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>Kontakt</legend>
          <label class="f" id="f-name"><span>Vorname</span><input id="name" name="name" type="text" autocomplete="given-name"><span class="err" id="err-name" hidden>Bitte gib deinen Vornamen an.</span></label>
          <div class="f"><span>Wie soll ich mich bei dir melden?</span>
            <div class="opts">
              <label class="opt"><input type="radio" name="kontaktweg" value="WhatsApp" checked><span>WhatsApp</span></label>
              <label class="opt"><input type="radio" name="kontaktweg" value="E-Mail"><span>E-Mail</span></label>
            </div>
            <small id="kw-hint">Ich schreibe dir von meiner Geschäftsnummer. Fotos von Karten kannst du mir dort direkt schicken.</small>
          </div>
          <div class="row2">
            <label class="f" id="f-tel"><span>WhatsApp-Nummer <em class="opt-tag" id="tel-tag" hidden>(optional)</em></span><input id="tel" name="whatsapp" type="tel" autocomplete="tel" placeholder="z. B. 0151 23456789"><span class="err" id="err-tel" hidden>Bitte gib deine WhatsApp-Nummer an.</span></label>
            <label class="f" id="f-mail"><span>E-Mail <em class="opt-tag" id="mail-tag">(optional, für den Ankaufbeleg)</em></span><input id="mail" name="email" type="email" autocomplete="email"><span class="err" id="err-mail" hidden>Bitte gib eine gültige E-Mail an.</span></label>
          </div>
          <label class="f"><span>Nachricht (optional)</span><textarea id="nachricht" name="nachricht" style="min-height:90px;font-family:var(--font-body)"></textarea></label>
          <label class="check"><input type="checkbox" id="ok-18" name="volljaehrig"><span>Ich bin mindestens 18 Jahre alt oder meine Eltern sind einverstanden.</span></label>
          <label class="check"><input type="checkbox" id="ok-agb" name="bedingungen"><span>Ich habe die <a href="ablauf.html#bedingungen" style="color:var(--gold-soft)">Ankaufbedingungen</a> und die <a href="datenschutz.html" style="color:var(--gold-soft)">Datenschutzerklärung</a> gelesen.</span></label>
          <span class="err" id="err-ok" hidden>Bitte bestätige beide Punkte.</span>
        </fieldset>

        <div class="submit-row">
          <button class="btn btn-gold" type="submit" id="send">Anfrage senden</button>
          <button class="text-link" type="button" id="back">← Zurück zu Teil 1</button>
        </div>
        <span class="demo-note" id="demo-note">Unverbindlich. Du verkaufst erst, wenn du mein Angebot annimmst.</span>
      </div>
    </form>

    <aside class="side" aria-label="Deine Schätzung">
      <div class="receipt" aria-live="polite">
        <div class="receipt-head"><span class="eyebrow">Deine Schätzung</span><span class="seal">{SEAL}</span></div>
        <div id="s-rows"></div>
        <div class="receipt-total"><span>ca.</span><b id="s-total">–</b></div>
        <p class="receipt-foot" id="s-foot">Schätzung. Deinen festen Betrag bekommst du im Angebot.</p>
        <p class="receipt-foot bonus" id="s-tipp"></p>
      </div>
      <div class="side-note"><b>Fester Betrag</b><span>Sobald du mein Angebot annimmst, steht dein Betrag fest. Weicht deine Sendung stark ab, entscheidest du: angepasster Betrag oder Karten zurück. Details in den <a href="ablauf.html#bedingungen" style="color:var(--gold-soft)">Ankaufbedingungen</a>.</span></div>
      <div class="side-note"><b>Was danach passiert</b>Ich melde mich mit einem Angebot, per WhatsApp oder E-Mail. Erst wenn du zusagst, schickst du die Karten per Post.</div>
    </aside>
  </div>
</main>'''

ankauf_js = read("prices.js") + r"""
(function(){
  // Formspree-Formular-ID hier eintragen, z. B. "xabcdwxyz". Leer = Vorschau-Modus ohne Versand.
  var FORM_ID = "mzeenvdz";
  var P = NGC_PREISE;

  var int = new Intl.NumberFormat('de-DE');
  function $(id){ return document.getElementById(id); }

  var form=$('ankauf-form'), art=$('art');
  // Normaler Formular-Versand statt JavaScript-Fetch: Formspree leitet nach dem Senden
  // selbst auf danke.html weiter. Das braucht keine CORS- oder Domain-Freigabe bei Formspree.
  if (FORM_ID){ form.action='https://formspree.io/f/'+FORM_ID; form.method='POST'; }
  var tabs={bulk:$('tab-bulk'), einzel:$('tab-einzel')}, panels={bulk:$('fs-bulk'), einzel:$('fs-einzel')};
  var mode='bulk', last=null;

  function setMode(m){
    mode=m; art.value = m==='bulk' ? 'Bulk' : 'Einzelkarten';
    for (var k in tabs){ tabs[k].setAttribute('aria-selected', k===m); panels[k].hidden = k!==m; }
    if (location.hash !== '#'+m) { try { history.replaceState(null,'','#'+m); } catch(e){} }
    calc();
  }
  tabs.bulk.addEventListener('click', function(){ setMode('bulk'); });
  tabs.einzel.addEventListener('click', function(){ setMode('einzel'); });

  function sortiert(){ return form.querySelector('input[name="sortiert"]:checked').value==='sortiert'; }
  function n(id){ return Math.floor(ngcNum($(id).value)); }
  function row(l,v){ return '<div class="receipt-row"><span>'+l+'</span><span class="mono">'+v+'</span></div>'; }

  function calc(){
    var rows='', tipp='';
    if (mode==='bulk'){
      var s=sortiert(); $('grp-sorted').hidden=!s; $('grp-un').hidden=s;
      var r=last=ngcBulk({sortiert:s, cu:n('cu'), holo:n('holo'), ex:n('ex'), un:n('un')});
      if (s){
        rows+=row('Common &amp; Uncommon · '+int.format(n('cu')), ngcFmt(r.cu));
        rows+=row('Holo &amp; Reverse · '+int.format(n('holo')), ngcFmt(r.holo));
        rows+=row('EX, V, GX · '+int.format(n('ex')), ngcFmt(r.ex));
      } else rows+=row('Unsortiert · '+int.format(n('un')), ngcFmt(r.un));
      rows+=row('Karten gesamt', int.format(r.anzahl));
      $('s-total').textContent = r.ok ? ngcFmt(r.cent) : '–';
      $('s-foot').textContent = r.anzahl>0 && !r.ok ? 'Bulk kaufe ich ab '+int.format(P.MIN)+' Karten an.' : 'Schätzung. Deinen festen Betrag bekommst du im Angebot.';
      tipp = r.ok ? r.tipp : '';
    } else {
      var v=ngcNum($('wert').value);
      rows+=row('Cardmarket-Wert', v?ngcFmt(Math.round(v*100)):'–');
      rows+=row('Ankaufsquote', '70 %');
      $('s-total').textContent = v ? ngcFmt(Math.round(v*100*P.quote)) : '–';
      $('s-foot').textContent='Ich prüfe jede Karte und ihren aktuellen Cardmarket-Preis selbst.';
    }
    $('s-rows').innerHTML=rows; $('s-tipp').textContent=tipp;
  }
  ['cu','holo','ex','un','wert'].forEach(function(id){
    $(id).addEventListener('input', calc);
    if (id!=='wert') $(id).addEventListener('blur', function(){ var x=n(id); this.value = x ? int.format(x) : ''; });
  });
  form.querySelectorAll('input[name="sortiert"]').forEach(function(r){ r.addEventListener('change', calc); });

  if (!FORM_ID) $('demo-note').textContent = 'Vorschau: Die Anfrage wird noch nicht verschickt, solange keine Formspree-ID eingetragen ist.';

  function flag(fid, eid, bad){ var f=$(fid); if(f) f.classList.toggle('bad', bad); $(eid).hidden=!bad; return bad; }

  // Teil 1 prüfen, dann Teil 2 zeigen
  function part(p){
    $('part1').hidden = p!==1; $('part2').hidden = p!==2;
    var h=$(p===1?'part1':'part2'); window.scrollTo({top: h.getBoundingClientRect().top + window.scrollY - 110, behavior:'smooth'});
  }
  $('next').addEventListener('click', function(){
    calc();
    if (mode==='bulk'){
      if (flag('f-menge','err-menge', !last.ok)){ $('err-menge').textContent='Ich kaufe Bulk ab '+int.format(P.MIN)+' Karten an. Du bist bei '+int.format(last.anzahl)+'.'; $(sortiert()?'cu':'un').focus(); return; }
    } else if (flag('f-liste','err-liste', !$('liste').value.trim())){ $('liste').focus(); return; }
    part(2); $('name').focus({preventScroll:true});
  });
  $('back').addEventListener('click', function(){ part(1); });

  function kontaktweg(){ var r=form.querySelector('input[name="kontaktweg"]:checked'); return r?r.value:'WhatsApp'; }
  function setKontakt(){
    var wa=kontaktweg()==='WhatsApp';
    $('tel-tag').hidden=wa;
    $('mail-tag').hidden=!wa;
    $('kw-hint').textContent = wa ? 'Ich schreibe dir von meiner Geschäftsnummer. Fotos von Karten kannst du mir dort direkt schicken.'
                                  : 'Du bekommst Angebot, Versandadresse und Ankaufbeleg per E-Mail.';
    flag('f-tel','err-tel',false); flag('f-mail','err-mail',false);
  }
  form.querySelectorAll('input[name="kontaktweg"]').forEach(function(r){ r.addEventListener('change', setKontakt); });
  setKontakt();

  form.addEventListener('submit', function(ev){
    ev.preventDefault();
    if (!$('part1').hidden){ $('next').click(); return; }   // Enter in Teil 1 = Weiter
    var bad=false, first=null;
    function chk(fid,eid,cond,focusId){ if(flag(fid,eid,cond)){ bad=true; if(!first) first=$(focusId); } }
    chk('f-name','err-name',!$('name').value.trim(),'name');
    var kw=kontaktweg(), mailV=$('mail').value.trim(), telV=$('tel').value.replace(/[^0-9]/g,'');
    var mailOk=/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mailV);
    chk('f-tel','err-tel', kw==='WhatsApp' ? telV.length<8 : (telV.length>0 && telV.length<8),'tel');
    chk('f-mail','err-mail', kw==='E-Mail' ? !mailOk : (mailV.length>0 && !mailOk),'mail');
    $('err-ok').hidden = $('ok-18').checked && $('ok-agb').checked;
    if (!$('err-ok').hidden){ bad=true; if(!first) first=$('ok-18'); }
    if (bad){ first.focus(); return; }

    var d=new Date(), pad=function(x){return String(x).padStart(2,'0');};
    var id='NGC-'+String(d.getFullYear()).slice(2)+pad(d.getMonth()+1)+pad(d.getDate())+'-'+Math.random().toString(36).slice(2,6).toUpperCase();
    $('h-id').value=id;
    if (mode==='bulk'){ $('h-karten').value=last.anzahl; $('h-schaetzung').value=$('s-total').textContent; }
    var data=new FormData(form);
    var summary={ id:id, art:art.value, name:$('name').value.trim(), mail:$('mail').value.trim(), tel:$('tel').value.trim(), kontaktweg:kontaktweg(),
      auszahlung:data.get('auszahlung'), schaetzung:$('s-total').textContent,
      menge: mode==='bulk' ? int.format(last.anzahl)+(sortiert()?' Karten, sortiert':' Karten, unsortiert') : null,
      karten: mode==='einzel' ? $('liste').value.trim().split('\n').filter(Boolean).length : null };
    try { sessionStorage.setItem('ngc-anfrage', JSON.stringify(summary)); } catch(e){}

    var btn=$('send'); btn.disabled=true; btn.textContent='Wird gesendet …';
    if (!FORM_ID){ location.href='danke.html'; return; }
    // Formspree leitet nach erfolgreichem Versand selbst hierhin weiter.
    $('h-redirect').value=new URL('danke.html', location.href).href;
    form.submit();
  });

  setMode(location.hash==='#einzel' ? 'einzel' : 'bulk');
  window.addEventListener('hashchange', function(){ setMode(location.hash==='#einzel'?'einzel':'bulk'); });
})();
"""
page("ankauf.html", "Ankauf-Anfrage · NoGreedCards", "Verkauf deinen Pokémon-Bulk oder deine Einzelkarten an NoGreedCards: Anfrage in 2 Minuten.", "", ankauf, ankauf_js)

# ---------------- Danke ----------------
danke = f'''<main>
  <div class="wrap page-hero">
    <div class="crumbs"><a href="index.html">Start</a> / Anfrage gesendet</div>
    <h1>Danke, deine Anfrage ist <em>da</em>.</h1>
    <p class="lead" id="hello">Ich schaue sie mir an und melde mich mit einem Angebot auf dem Weg, den du gewählt hast.</p>
    <div style="margin-top:12px">{stepper(2)}</div>
  </div>
  <div class="wrap grid2" style="padding-bottom:80px;align-items:start">
    <div style="display:grid;gap:20px">
      <div class="ticket">
        <span class="eyebrow">Deine Anfragenummer</span>
        <span class="id" id="anfrage-id">NGC-······</span>
        <span style="color:var(--muted);font-size:14px">Notier sie dir und leg sie später deinem Paket bei.</span>
      </div>
      <div class="callout"><b>Bitte noch nichts verschicken.</b> Warte auf mein Angebot. Erst wenn du zusagst, bekommst du die Versandadresse.</div>
      <dl class="summary" id="summary" hidden></dl>
    </div>
    <div class="card">
      <h3>So geht es weiter</h3>
      <ol class="timeline" style="margin-top:8px">
        <li><span class="t-num">02</span><div class="t-body"><b>Angebot per WhatsApp oder E-Mail</b><p>Mit Preis und den nächsten Schritten. Bei Einzelkarten frage ich eventuell nach Fotos.</p></div></li>
        <li><span class="t-num">03</span><div class="t-body"><b>Du sagst zu</b><p>Dann bekommst du die Versandadresse und schickst die Karten mit deiner Anfragenummer.</p><a href="versand.html" style="color:var(--gold-soft)">So verpackst du richtig →</a></div></li>
        <li><span class="t-num">04</span><div class="t-body"><b>Prüfung und Auszahlung</b><p>Ich zähle nach, prüfe den Zustand und zahle dir den Betrag aus.</p></div></li>
      </ol>
    </div>
  </div>
</main>'''
danke_js = r"""
(function(){
  var s=null; try { s=JSON.parse(sessionStorage.getItem('ngc-anfrage')||'null'); } catch(e){}
  if(!s) return;
  document.getElementById('anfrage-id').textContent=s.id;
  var wo = s.kontaktweg==='WhatsApp' ? 'per WhatsApp unter '+s.tel : 'per E-Mail an '+s.mail;
  if(s.name) document.getElementById('hello').textContent='Danke, '+s.name+'. Ich schaue mir deine Anfrage an und melde mich mit einem Angebot '+wo+'.';
  var rows=[['Art',s.art]];
  if(s.menge) rows.push(['Anzahl',s.menge]);
  if(s.karten) rows.push(['Einzelkarten',s.karten+' Zeilen']);
  rows.push(['Kontakt über',s.kontaktweg],['Auszahlung',s.auszahlung],['Schätzung',s.schaetzung]);
  var dl=document.getElementById('summary');
  rows.forEach(function(r){ var d=document.createElement('div'), t=document.createElement('dt'), v=document.createElement('dd'); t.textContent=r[0]; v.textContent=r[1]||'–'; d.append(t,v); dl.append(d); });
  dl.hidden=false;
})();
"""
page("danke.html", "Anfrage gesendet · NoGreedCards", "Deine Ankauf-Anfrage bei NoGreedCards ist eingegangen.", "", danke, danke_js)

# ---------------- Versand ----------------
versand = f'''<main>
  <div class="wrap page-hero">
    <div class="crumbs"><a href="index.html">Start</a> / <a href="ablauf.html">Ankauf</a> / Versand</div>
    <h1>So kommen deine Karten <em>sicher</em> an.</h1>
    <p class="lead">Diese Seite brauchst du erst, wenn du mein Angebot angenommen hast. Die Versandadresse bekommst du mit dem Angebot per WhatsApp oder E-Mail.</p>
    <div style="margin-top:12px">{stepper(3)}</div>
  </div>
  <div class="wrap" style="display:grid;gap:56px;padding-bottom:80px">
    <div class="grid2">
      <div class="card">
        <span class="chip" style="justify-self:start">Per Post</span>
        <h3>Bulk verpacken</h3>
        <ul>
          <li>Karten stapelweise in einen stabilen Karton, nicht lose in einen Umschlag.</li>
          <li>Hohlräume mit Zeitungspapier füllen, damit nichts rutscht.</li>
          <li>Karton mit einer Plastiktüte innen gegen Nässe schützen.</li>
          <li>Zettel mit deiner <b style="color:var(--fg)">Anfragenummer</b> obenauf legen.</li>
          <li>Paket mit Sendungsnummer verschicken und Foto vom Inhalt machen.</li>
        </ul>
      </div>
      <div class="card">
        <span class="chip" style="justify-self:start">Per Post</span>
        <h3>Einzelkarten verpacken</h3>
        <ul>
          <li>Jede Karte in eine Hülle (Sleeve), wertvolle zusätzlich in einen Toploader.</li>
          <li>Zwischen zwei Pappen legen und mit Klebeband fixieren, nicht direkt auf die Karte.</li>
          <li>Ab einem Wert von 25 € bitte versichert verschicken.</li>
          <li>Zettel mit Anfragenummer und deiner Kartenliste beilegen.</li>
        </ul>
      </div>
    </div>
    <div class="grid2">
      <div class="card">
        <h3>Nach dem Versand</h3>
        <p>Schick mir die Sendungsnummer, einfach als Antwort im selben Chat oder per E-Mail. Sobald das Paket da ist, bekommst du eine kurze Eingangsbestätigung.</p>
        <p>Danach prüfe ich die Sendung. Passt sie zu deiner Anfrage, zahle ich dir den zugesagten Betrag innerhalb von 2 Werktagen aus.</p>
      </div>
      <div class="card">
        <h3>Wer zahlt das Porto?</h3>
        <p>Das Porto zahlst du. Ab 5.000 Karten erstatte ich dir bis zu 6,99 € mit der Auszahlung.</p>
        <p>Geht ein Paket verloren, gilt die Sendungsverfolgung. Deshalb nie ohne Sendungsnummer verschicken.</p>
      </div>
    </div>
  </div>
</main>'''
page("versand.html", "Versand · NoGreedCards", "So verpackst du deine Karten für den Ankauf bei NoGreedCards.", "", versand)

# ---------------- Ablauf + Bedingungen + FAQ ----------------
ablauf = f'''<main>
  <div class="wrap page-hero">
    <div class="crumbs"><a href="index.html">Start</a> / So läuft der Ankauf</div>
    <h1>Vom Karton zum <em>Geld</em> in fünf Schritten.</h1>
    <p class="lead">Kein Feilschen und keine Überraschungen. Du weißt bei jedem Schritt, was passiert und was du bekommst.</p>
    <div class="hero-actions" style="margin-top:8px"><a class="btn btn-gold" href="ankauf.html">Anfrage starten</a></div>
  </div>

  <section style="padding-top:24px">
    <div class="wrap">
      <ol class="timeline">
        <li><span class="t-num">01</span><div class="t-body"><h3>Anfrage</h3><p>Du füllst das Ankauf-Formular aus: Bulk ab 500 Karten oder eine Liste deiner Einzelkarten. Das dauert etwa 2 Minuten.</p><div class="t-meta"><span class="chip">Du</span><span class="chip">2 Min.</span></div></div></li>
        <li><span class="t-num">02</span><div class="t-body"><h3>Angebot</h3><p>Ich schicke dir ein Angebot mit festem Betrag per WhatsApp oder E-Mail, je nachdem, was du im Formular gewählt hast. Bulk nach Preisliste, Einzelkarten zu 70 % des aktuellen Cardmarket-Preises. Bei Einzelkarten frage ich eventuell nach Fotos.</p><div class="t-meta"><span class="chip">Ich</span><span class="chip">meist in 2 Tagen</span></div></div></li>
        <li><span class="t-num">03</span><div class="t-body"><h3>Versand</h3><p>Du sagst zu und schickst die Karten per Post mit deiner Anfragenummer. <a href="versand.html" style="color:var(--gold-soft)">Versandanleitung</a></p><div class="t-meta"><span class="chip">Du</span></div></div></li>
        <li><span class="t-num">04</span><div class="t-body"><h3>Prüfung</h3><p>Ich kontrolliere Bulk nach Gewicht und Stichprobe und prüfe Einzelkarten auf Zustand und Echtheit. Passt die Sendung, bleibt es beim zugesagten Betrag. Weicht sie stark ab, entscheidest du: angepasster Betrag oder Karten zurück.</p><div class="t-meta"><span class="chip">Ich</span><span class="chip">bis 2 Werktage nach Eingang</span></div></div></li>
        <li><span class="t-num">05</span><div class="t-body"><h3>Auszahlung</h3><p>Du bekommst dein Geld per PayPal oder Überweisung. Dazu einen Ankaufbeleg als PDF.</p><div class="t-meta"><span class="chip chip-gold">Fertig</span></div></div></li>
      </ol>
    </div>
  </section>

  <hr class="tear">

  <section id="bedingungen">
    <div class="wrap">
      <div class="sec-head">
        <div class="eyebrow">Ankaufbedingungen</div>
        <h2>Die Regeln, kurz und klar.</h2>
      </div>
      <ol class="terms">
        <li><span><b>Nur Originale.</b> Ich kaufe nur echte Pokémon-Karten. Fälschungen, Proxies, andere Kartenspiele und stark beschädigte Karten zählen nicht und werden nicht bezahlt. Geht der Rest ohnehin zurück, lege ich sie bei, sonst entsorge ich sie.</span></li>
        <li><span><b>Fester Betrag:</b> Ich schicke dir ein Angebot mit festem Betrag, berechnet aus deinen Angaben. Sagst du zu, gilt dieser Betrag, solange deine Sendung zu deinen Angaben passt. Bis zur Auszahlung bleiben die Karten dein Eigentum.</span></li>
        <li><span><b>Versand auf dein Risiko:</b> Du verschickst die Karten auf eigene Gefahr und nur mit Sendungsnummer. Ab einem Wert von 25 € bitte versichert. Geht ein Paket ohne Sendungsnummer verloren, kann ich dafür nicht haften. Bei einem verfolgten Paket hilft dir die Sendungsnummer, den Schaden beim Versanddienst geltend zu machen.</span></li>
        <li><span><b>Mindestmenge Bulk:</b> 500 Karten. Bulk zählt ohne Hüllen, Toploader und Sammelalben.</span></li>
        <li><span><b>Sortierung:</b> Ich prüfe deine Sortierung. Falsch einsortierte Karten zähle ich in der passenden Kategorie. Full Arts und Karten ab 1 € Marktwert biete ich dir als Einzelkarten zu 70 % an. Gemischte Kisten zählen als unsortiert.</span></li>
        <li><span><b>Toleranz:</b> Ich kontrolliere Bulk nach Gewicht und Stichprobe. Weicht die Menge um bis zu 10 % ab oder sind wenige Karten falsch einsortiert, zahle ich trotzdem den vollen zugesagten Betrag.</span></li>
        <li><span><b>Mehr Karten:</b> Schickst du mehr als 10 % mehr Karten als angegeben, zahle ich die Mehrmenge nach Preisliste dazu.</span></li>
        <li><span><b>Zustand:</b> Stark beschädigt heißt: Knicke, Risse oder Wasserschäden. Einzelkarten bewerte ich nach der Cardmarket-Zustandsskala.</span></li>
        <li><span><b>Preis:</b> Bei Einzelkarten gilt der Cardmarket-Preis am Tag der Prüfung, für den passenden Zustand und die passende Sprache.</span></li>
        <li><span><b>Größere Abweichungen:</b> Fehlen mehr als 10 % der Karten oder ist viel falsch einsortiert, berechne ich den Betrag nach Preisliste neu und schicke dir Fotos und das Gewicht als Beleg. Du hast 7 Tage Zeit und wählst: angepasster Betrag oder Rücksendung deiner Karten, das Rückporto zahlst du. Antwortest du nicht, erinnere ich dich nach 7 Tagen und zahle dir nach 14 Tagen den angepassten Betrag aus.</span></li>
        <li><span><b>Auszahlung:</b> Passt die Sendung, zahle ich innerhalb von 2 Werktagen nach Eingang per PayPal oder Überweisung aus.</span></li>
        <li><span><b>Minderjährige</b> verkaufen nur mit Einverständnis der Eltern.</span></li>
        <li><span><b>Beleg:</b> Für jeden Ankauf stelle ich einen Ankaufbeleg mit Name, Datum, Karten und Preis aus.</span></li>
      </ol>
    </div>
  </section>

  <div class="band">
    <section id="fragen">
      <div class="wrap">
        <div class="sec-head"><div class="eyebrow">Häufige Fragen</div><h2>Noch Fragen?</h2></div>
        <div style="max-width:780px">
          <details><summary>Muss ich meine Karten vorher sortieren?</summary><p>Nein. Dann wählst du im Formular „Unsortiert“ und bekommst 6 € je 1.000 Karten. Sortiert bekommst du mehr, <a href="index.html#sortieren" style="color:var(--gold-soft)">so geht es in 10 Minuten</a>.</p></details>
          <details><summary>Wie schätze ich die Anzahl?</summary><p>100 Karten wiegen etwa 180 g. Ein voller Schuhkarton sind ungefähr 800 bis 1.000 Karten.</p></details>
          <details><summary>Kaufst du auch englische oder japanische Karten?</summary><p>Englische ja. Bei anderen Sprachen schreib es bitte in die Nachricht, dann mache ich ein eigenes Angebot.</p></details>
          <details><summary>Was ist mit Karten in Sammelalben?</summary><p>Bitte nimm sie vorher heraus. Alben und Hüllen kann ich nicht mit ankaufen.</p></details>
          <details><summary>Warum WhatsApp?</summary><p>Weil es schneller geht. Du kannst mir Fotos deiner Karten direkt schicken, und Rückfragen sind in einer Minute geklärt. Wer lieber nicht chattet, wählt im Formular E-Mail.</p></details>
          <details><summary>Bin ich nach der Anfrage zum Verkauf verpflichtet?</summary><p>Nein. Die Anfrage ist unverbindlich. Verkauft ist erst, wenn du mein Angebot annimmst.</p></details>
        </div>
      </div>
    </section>
  </div>
</main>'''
page("ablauf.html", "So läuft der Ankauf · NoGreedCards", "Ablauf, Ankaufbedingungen und häufige Fragen zum Kartenankauf bei NoGreedCards.", "ablauf", ablauf)

# ---------------- Impressum ----------------
ADRESSE = """Steven Lars Schmitt<br>NoGreedCards<br>Mühlenbergring 2<br>66793 Saarwellingen<br>Deutschland"""
impressum = f'''<main>
  <div class="wrap page-hero">
    <div class="crumbs"><a href="index.html">Start</a> / Impressum</div>
    <h1>Impressum</h1>
  </div>
  <div class="wrap legal">
    <h2>Angaben gemäß § 5 DDG</h2>
    <address>{ADRESSE}</address>
    <h2>Kontakt</h2>
    <p>E-Mail: <a href="mailto:nogreedtcg@gmail.com">nogreedtcg@gmail.com</a><br>Ankauf-Anfragen auch über das <a href="ankauf.html">Ankauf-Formular</a>.</p>
    <h2>Verantwortlich für den Inhalt</h2>
    <p>Steven Lars Schmitt, Anschrift wie oben.</p>
    <h2>Verbraucherstreitbeilegung</h2>
    <p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
    <h2>Hinweis</h2>
    <p>NoGreedCards ist ein unabhängiger Händler und steht in keiner Verbindung zu The Pokémon Company, Nintendo, Creatures oder GAME FREAK. Pokémon ist eine Marke der jeweiligen Rechteinhaber.</p>
  </div>
</main>'''
page("impressum.html", "Impressum · NoGreedCards", "Impressum von NoGreedCards.", "", impressum)

# ---------------- Datenschutz ----------------
datenschutz = open(os.path.join(HERE, "datenschutz.html"), encoding="utf-8").read()
page("datenschutz.html", "Datenschutz · NoGreedCards", "Datenschutzerklärung von NoGreedCards.", "", datenschutz)

print("ok")
