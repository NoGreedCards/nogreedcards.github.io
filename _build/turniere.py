# Turnierseite (CollectorsGuild). Wird von build.py per exec() eingebunden und nutzt dessen
# FONT_CSS, FONTS, typo() und REPO_OUT/ART_OUT. Eigenes Design: Grün aus dem NGC-Logo, Lila, Weiß, Glas-Optik.

T_CSS = r"""
:root{
  --t-bg:#150d27; --t-bg2:#20123d;
  --t-violet:#8b5cf6; --t-lilac:#c4b0ff;
  --t-green:#56c09f; --t-green-lt:#abe9ca; --t-green-dk:#1d816c; --t-check:#a8e070;
  --t-fg:#ffffff; --t-muted:rgba(255,255,255,.74); --t-dim:rgba(255,255,255,.56);
  --glass:rgba(255,255,255,.075); --glass-2:rgba(255,255,255,.12); --glass-line:rgba(255,255,255,.2);
  --r-xl:32px; --r-lg:24px;
  --font-display:"Archivo", "Arial Narrow", system-ui, sans-serif;
  --font-body:"Figtree", -apple-system, "Segoe UI", sans-serif;
  --font-mono:"JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;min-height:100vh;position:relative;color:var(--t-fg);font-family:var(--font-body);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;
  background:var(--t-bg);overflow-x:hidden}
/* weiche Farbflächen hinter dem Glas */
.orbs{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden;
  background:radial-gradient(1200px 800px at 50% -10%, var(--t-bg2), var(--t-bg) 70%)}
.orbs i{position:absolute;border-radius:50%;filter:blur(90px);opacity:.5;animation:drift 22s ease-in-out infinite alternate}
.orbs i:nth-child(1){width:min(560px,120vw);aspect-ratio:1;left:-180px;top:40px;background:var(--t-green)}
.orbs i:nth-child(2){width:min(620px,130vw);aspect-ratio:1;right:-220px;top:-160px;background:var(--t-violet);animation-delay:-8s}
.orbs i:nth-child(3){width:min(480px,110vw);aspect-ratio:1;right:-120px;top:38%;background:#3fae8f;opacity:.3;animation-delay:-4s}
.orbs i:nth-child(4){width:min(520px,120vw);aspect-ratio:1;left:-160px;top:66%;background:var(--t-violet);opacity:.32;animation-delay:-12s}
@keyframes drift{to{transform:translate3d(40px,30px,0) scale(1.08)}}
::selection{background:rgba(86,192,159,.45);color:#fff}
:focus-visible{outline:2px solid var(--t-green-lt);outline-offset:3px;border-radius:8px}
a{color:var(--t-green-lt);text-underline-offset:3px;text-decoration-thickness:1px}
h1,h2,h3{font-family:var(--font-display);font-stretch:112%;line-height:1.08;margin:0;text-wrap:balance;letter-spacing:-.01em}
p{margin:0;text-wrap:pretty}
.wrap{width:min(1120px,100% - 40px);margin-inline:auto}
.nobr{white-space:nowrap}

/* Glas: halbtransparent, weichgezeichnet, helle Oberkante */
.glass{position:relative;isolation:isolate;background:linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.05) 55%,rgba(255,255,255,.08));
  border:1px solid var(--glass-line);border-radius:var(--r-xl);
  -webkit-backdrop-filter:blur(22px) saturate(160%);backdrop-filter:blur(22px) saturate(160%);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.35),inset 0 -1px 0 rgba(255,255,255,.06),0 24px 60px -28px rgba(8,4,20,.75)}
.glass::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;z-index:-1;
  background:linear-gradient(180deg,rgba(255,255,255,.16),rgba(255,255,255,0) 38%)}

/* Kopfzeile als schwebende Glas-Pille */
.t-head{position:sticky;top:max(12px, env(safe-area-inset-top));z-index:10;margin-top:12px}
.t-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:8px 8px 8px 12px;border-radius:999px}
.t-brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-family:var(--font-display);font-stretch:118%;font-weight:800;letter-spacing:.02em;font-size:16px;min-width:0}
.t-brand img{width:36px;height:36px;flex-shrink:0}
.t-nav{display:flex;align-items:center;gap:6px}
.t-nav a.t-link{color:var(--t-muted);text-decoration:none;font-size:14px;padding:10px 12px;border-radius:999px;transition:color .15s, background .15s}
.t-nav a.t-link:hover{color:#fff;background:var(--glass-2)}
@media (max-width:640px){ .t-nav a.t-link{display:none} }

/* Knöpfe: Gel-Optik wie das Logo */
.pill{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-family:var(--font-body);font-weight:700;font-size:15px;
  padding:13px 22px;border-radius:999px;text-decoration:none;border:1px solid transparent;cursor:pointer;position:relative;
  transition:transform .15s ease-out, filter .15s ease-out, background .15s}
.pill-green{color:#0b3a30;background:linear-gradient(165deg,#c6f3dc 0%,#77d4b1 42%,#43b293 78%,#2f9c80 100%);border-color:rgba(255,255,255,.6);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.75),inset 0 -3px 0 rgba(29,129,108,.55),0 10px 24px -10px rgba(67,178,147,.9)}
.pill-green:hover{filter:brightness(1.06);transform:translateY(-1px)}
.pill-glass{color:#fff;background:var(--glass-2);border-color:var(--glass-line);box-shadow:inset 0 1px 0 rgba(255,255,255,.3);
  -webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px)}
.pill-glass:hover{background:rgba(255,255,255,.18)}
.pill:active{transform:scale(.98)}
.pill-sm{padding:9px 16px;font-size:14px}

/* Kopfbereich */
.t-hero{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:40px;align-items:center;padding-block:clamp(56px,9vw,104px) 40px}
@media (max-width:820px){ .t-hero{grid-template-columns:1fr;gap:24px;padding-top:40px} .t-hero .logo-orb{order:-1;max-width:168px;justify-self:start} }
.kicker{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--t-lilac);
  padding:6px 12px;border-radius:999px;background:rgba(139,92,246,.18);border:1px solid rgba(196,176,255,.35);width:max-content;max-width:100%}
.kicker::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--t-green);box-shadow:0 0 10px var(--t-green)}
.t-hero h1{font-size:clamp(34px,6.2vw,72px);font-weight:900;font-stretch:120%;margin-top:18px;line-height:1.02}
.t-hero h1 small{display:block;font-size:.62em;font-stretch:112%;color:#fff;margin-top:4px}
.t-hero h1 span{background:linear-gradient(120deg,var(--t-green-lt),var(--t-green) 45%,var(--t-lilac));-webkit-background-clip:text;background-clip:text;color:transparent}
.t-hero .lead{font-size:18px;color:var(--t-muted);max-width:52ch;margin-top:18px}
.t-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.logo-orb{justify-self:center;width:100%;max-width:340px;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;padding:12%;position:relative}
.logo-orb{background:radial-gradient(circle at 50% 38%,rgba(139,92,246,.35),rgba(139,92,246,.08) 70%)}
.logo-orb img{width:100%;height:auto;filter:drop-shadow(0 18px 30px rgba(10,40,32,.55))}

/* Abschnitte */
section{padding-block:clamp(36px,6vw,64px)}
.sec-head{display:grid;gap:10px;margin-bottom:24px}
.sec-head h2{font-size:clamp(28px,4vw,40px);font-weight:800}
.sec-head p{color:var(--t-muted);max-width:60ch}
.eyebrow{font-family:var(--font-mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--t-green-lt)}

/* Nächstes Turnier */
.event{padding:clamp(22px,4vw,36px);display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(20px,4vw,40px);align-items:center}
@media (max-width:700px){ .event{grid-template-columns:1fr;justify-items:start} .date-orb{width:120px;height:120px} .date-orb b{font-size:44px} }
.date-orb{width:156px;height:156px;border-radius:50%;display:grid;place-content:center;text-align:center;color:#0b3a30;
  background:radial-gradient(circle at 32% 26%,#e3fbef 0%,#97e0c3 32%,#56c09f 62%,#2f9c80 100%);
  border:3px solid #fff;box-shadow:inset 0 -8px 16px rgba(29,129,108,.45),inset 0 6px 10px rgba(255,255,255,.6),0 18px 36px -14px rgba(67,178,147,.85)}
.date-orb b{font-family:var(--font-display);font-stretch:118%;font-weight:900;font-size:56px;line-height:.95}
.date-orb span{font-family:var(--font-mono);font-weight:600;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
.event h3{font-size:clamp(24px,3.2vw,32px);font-weight:800}
.event .when{color:var(--t-muted);margin-top:6px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(130px,40%),1fr));gap:10px;margin:22px 0 0;padding:0;list-style:none}
.facts li{padding:12px 14px;border-radius:18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);display:grid;gap:4px;align-content:start;justify-items:start;min-width:0}
.facts small{font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--t-dim)}
.facts b{font-weight:600;font-size:15px}
.soon{display:inline-block;width:max-content;font-size:13px;line-height:1.5;font-weight:600;color:var(--t-lilac);border:1px dashed rgba(196,176,255,.55);border-radius:999px;padding:1px 10px}
.countdown{display:inline-flex;align-items:center;gap:6px;margin-top:18px;font-size:14px;color:var(--t-muted);padding:6px 14px 6px 10px;border-radius:999px;background:rgba(86,192,159,.14);border:1px solid rgba(171,233,202,.3)}
.countdown::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--t-green);box-shadow:0 0 10px var(--t-green)}
.countdown b{font-weight:700;color:#fff}

/* Season-Leiste */
.season{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin:0;padding:0;list-style:none}
@media (max-width:900px){ .season{grid-template-columns:1fr;gap:10px}
  .season li{grid-template-columns:auto minmax(0,1fr);column-gap:14px;row-gap:2px;padding:16px 18px;border-radius:22px}
  .season .dot{grid-row:1 / span 3;align-self:center}
}
.season li{padding:20px;border-radius:var(--r-lg);display:grid;gap:8px;align-content:start;min-width:0;transition:transform .2s ease-out, border-color .2s}
.season li:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.32)}
.season .m{font-family:var(--font-mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--t-dim)}
.season h3{font-size:19px;font-weight:800}
.season p{font-size:14px;color:var(--t-muted)}
.season .dot{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font-family:var(--font-mono);font-weight:600;font-size:13px}
.dot-g{color:#0b3a30;background:linear-gradient(160deg,#c6f3dc,#56c09f);box-shadow:inset 0 1px 0 rgba(255,255,255,.7)}
.dot-v{color:#fff;background:linear-gradient(160deg,#c4b0ff,#7c4fe0);box-shadow:inset 0 1px 0 rgba(255,255,255,.55)}
.dot-w{color:#2a1650;background:linear-gradient(160deg,#ffffff,#ddd3f7);box-shadow:inset 0 1px 0 #fff}
.season li.final{background:linear-gradient(160deg,rgba(139,92,246,.32),rgba(139,92,246,.12));border-color:rgba(196,176,255,.4)}

/* Punkte */
.pd{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
@media (max-width:820px){ .pd{grid-template-columns:1fr} }
.pd-box{padding:clamp(20px,3vw,30px);display:flex;flex-direction:column;gap:14px}
.pd-box .empty{flex:1}
.pd-title{display:flex;align-items:center;gap:12px}
.coin{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;flex-shrink:0;color:#0b3a30;
  background:radial-gradient(circle at 32% 26%,#e3fbef 0%,#97e0c3 34%,#56c09f 66%,#2f9c80 100%);border:2px solid #fff;
  box-shadow:inset 0 -4px 8px rgba(29,129,108,.45),0 8px 18px -8px rgba(67,178,147,.9)}
.coin svg{height:22px;width:auto}
.pd-sym{display:inline-block;height:.9em;width:auto;vertical-align:-.08em;margin-left:.25em}
h2 .pd-sym{height:.82em;margin-left:.2em}
.pd-box h3{font-size:22px;font-weight:800}
.pd-box p{color:var(--t-muted);font-size:15px}
.ptable{width:100%;border-collapse:collapse;font-size:15px}
.ptable td{padding:10px 0;border-bottom:1px solid rgba(255,255,255,.1)}
.ptable tr:last-child td{border-bottom:0}
.ptable td:last-child{text-align:right;font-family:var(--font-mono);font-variant-numeric:tabular-nums;font-weight:600;color:var(--t-green-lt);white-space:nowrap}
.ptable tr:first-child td:last-child{color:#fff}
.ptable td:first-child{padding-right:14px;color:var(--t-muted)}
.ptable td:last-child{white-space:normal;font-family:var(--font-body);font-weight:700}
.facts b{overflow-wrap:anywhere}
.empty{display:grid;place-items:center;align-content:center;text-align:center;gap:8px;padding:34px 20px;border-radius:var(--r-lg);border:1px dashed rgba(255,255,255,.25);color:var(--t-muted);font-size:15px}
.empty b{color:#fff;font-size:17px}

/* PlayAgainst: Ticket & Anmeldung */
.pa{padding:clamp(22px,4vw,40px);display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(24px,4vw,48px);align-items:center}
@media (max-width:860px){ .pa{grid-template-columns:1fr} }
.pa-text{display:grid;gap:16px;min-width:0}
.pa-text h2{font-size:clamp(28px,4vw,40px);font-weight:800}
.pa-text p{color:var(--t-muted);max-width:56ch}
.pa-badge{display:inline-flex;align-items:center;gap:10px;width:max-content;max-width:100%;padding:6px 14px 6px 6px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid var(--glass-line);font-weight:700;font-size:14px}
.pa-badge i{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-family:var(--font-display);font-weight:900;font-size:12px;color:#fff;background:linear-gradient(160deg,#c4b0ff,#7c4fe0);box-shadow:inset 0 1px 0 rgba(255,255,255,.55)}
.pa-steps{list-style:none;margin:8px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;position:relative;counter-reset:st}
.pa-steps::before{content:"";position:absolute;left:21px;right:calc(25% - 24px);top:20px;height:2px;background:linear-gradient(90deg,var(--t-green),var(--t-violet));opacity:.6;z-index:0}
.pa-steps li{position:relative;z-index:1;display:grid;gap:8px;justify-items:start;align-content:start;min-width:0}
.pa-steps .n{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;font-family:var(--font-mono);font-weight:600;font-size:14px;color:#0b3a30;background:linear-gradient(160deg,#c6f3dc,#56c09f);border:2px solid #fff;box-shadow:0 8px 18px -8px rgba(67,178,147,.9)}
.pa-steps li:last-child .n{color:#fff;background:linear-gradient(160deg,#c4b0ff,#7c4fe0)}
.pa-steps b{font-size:15px}
.pa-steps span{font-size:14px;color:var(--t-muted);line-height:1.5}
/* senkrechte Schrittliste: Handy und schmale Zweispalter (861–1180 px) */
@media (max-width:640px), (min-width:861px) and (max-width:1180px){
  .pa-steps{grid-template-columns:1fr;gap:16px}
  .pa-steps::before{display:none}
  .pa-steps li{grid-template-columns:auto minmax(0,1fr);column-gap:14px;row-gap:2px}
  .pa-steps .n{grid-row:1 / span 2}
  .pa-steps li:not(:last-child)::after{content:"";position:absolute;left:20px;top:42px;bottom:-16px;width:2px;background:linear-gradient(180deg,var(--t-green),var(--t-violet));opacity:.6;z-index:-1}
}
.pa-cta{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.pa-note{font-size:13px;color:var(--t-dim)}
/* Handy-Ansicht als Bild für "so sieht das auf PlayAgainst aus" */
.phone{justify-self:center;width:100%;max-width:300px;border-radius:36px;padding:12px;background:linear-gradient(160deg,rgba(255,255,255,.22),rgba(255,255,255,.06));border:1px solid var(--glass-line);box-shadow:0 30px 60px -30px rgba(8,4,20,.9)}
.phone-in{border-radius:26px;background:#0f0a1d;padding:16px 14px 18px;display:grid;gap:12px;border:1px solid rgba(255,255,255,.1)}
.ph-top{display:flex;justify-content:space-between;align-items:center;font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;color:var(--t-dim)}
.ph-card{border-radius:18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);padding:14px;display:grid;gap:8px}
.ph-card h4{margin:0;font-family:var(--font-display);font-stretch:112%;font-size:17px;font-weight:800}
.ph-row{display:flex;justify-content:space-between;gap:8px;font-size:13px;color:var(--t-muted)}
.ph-row b{color:#fff;font-weight:600;font-family:var(--font-mono);font-variant-numeric:tabular-nums}
.ph-bar{height:6px;border-radius:999px;background:rgba(255,255,255,.1);overflow:hidden}
.ph-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--t-green),var(--t-green-lt))}
.ph-btn{display:grid;place-items:center;padding:11px;border-radius:999px;font-weight:700;font-size:14px;color:#0b3a30;background:linear-gradient(165deg,#c6f3dc 0%,#77d4b1 42%,#43b293 78%,#2f9c80 100%)}
.ph-list{display:grid;gap:6px;margin:0;padding:0;list-style:none}
.ph-list li{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--t-muted)}
.ph-list li::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--t-check);flex-shrink:0}
.ph-cap{text-align:center;font-size:12px;color:var(--t-dim)}

/* Fußzeile */
.t-foot{padding-block:40px 56px}
.t-foot .glass{border-radius:var(--r-lg);padding:22px 24px;display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between}
.t-foot nav{display:flex;flex-wrap:wrap;gap:4px 18px}
.t-foot a{color:var(--t-muted);text-decoration:none;font-size:14px;display:inline-block;padding-block:6px}
.t-foot a:hover{color:#fff}
.t-foot .motto{font-family:var(--font-display);font-stretch:118%;font-weight:800}
@media (max-width:480px){ .t-hero h1{font-stretch:100%;font-size:clamp(32px,9.6vw,44px)} }
@media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto} *,*::before,*::after{transition:none!important;animation:none!important} .pill:hover,.pill:active{transform:none} }
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){ .glass{background:rgba(40,26,72,.92)} }
"""

T_BODY = '''<div class="orbs" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
<div class="wrap t-head">
  <header class="glass t-bar">
    <a class="t-brand" href="turniere.html" aria-label="CollectorsGuild Turniere">
      <img src="ngc-logo.png" alt="" width="36" height="36">
      <span>CollectorsGuild</span>
    </a>
    <nav class="t-nav" aria-label="Turnier-Navigation">
      <a class="t-link" href="#anmeldung">Anmeldung</a>
      <a class="t-link" href="#termin">Termin</a>
      <a class="t-link" href="#season">Season</a>
      <a class="t-link" href="#punkte">Punkte</a>
      <a class="pill pill-glass pill-sm" href="index.html">NoGreedCards</a>
    </nav>
  </header>
</div>

<main>
  <div class="wrap t-hero">
    <div>
      <span class="kicker">Pokémon-TCG · Saarland</span>
      <h1><span>CollectorsGuild</span><small>Turniere</small></h1>
      <p class="lead">Die Pokémon-TCG-Liga von NoGreedCards in der Trading Card Cave in Dillingen. Standard, Swiss, Best of 3: drei Turniere, eine Trade Night und ein Finale. Punkte und Rangliste laufen über PlayAgainst.</p>
      <div class="t-cta">
        <a class="pill pill-green" href="#anmeldung">Ticket &amp; Anmeldung</a>
        <a class="pill pill-glass" href="#termin">Zum ersten Turnier</a>
      </div>
    </div>
    <div class="logo-orb glass"><img src="ngc-logo.png" alt="NGC-Logo von NoGreedCards" width="320" height="319"></div>
  </div>

  <section id="anmeldung" style="scroll-margin-top:96px;padding-top:0">
    <div class="wrap">
      <div class="glass pa">
        <div class="pa-text">
          <span class="pa-badge"><i>PA</i>Läuft über PlayAgainst</span>
          <h2>Ticket und Anmeldung auf PlayAgainst</h2>
          <p>Für alle CollectorsGuild-Turniere kaufst du dein Ticket und meldest dich auf PlayAgainst an. Dort siehst du die freien Plätze, und am Turniertag laufen Paarungen, Ergebnisse und die Rangliste der Season ebenfalls über PlayAgainst. Du brauchst nur einen kostenlosen Account, keine App.</p>
          <ol class="pa-steps">
            <li><span class="n">1</span><b>Account anlegen</b><span>Kostenlos auf playagainst.xyz registrieren.</span></li>
            <li><span class="n">2</span><b>Turnier wählen</b><span>CollectorsGuild&nbsp;#1 öffnen und anmelden. Ist es voll, rückst du von der Warteliste automatisch nach. Anmeldeschluss ist Samstag, 26.12.2026.</span></li>
            <li><span class="n">3</span><b>Ticket sichern</b><span>9&nbsp;€ pro Termin, auch fürs Finale. Bezahlweg <span class="soon">folgt</span></span></li>
            <li><span class="n">4</span><b>Einchecken</b><span>Am Turniertag im Laden einchecken und losspielen.</span></li>
          </ol>
          <div class="pa-cta">
            <a class="pill pill-green" href="https://playagainst.xyz" target="_blank" rel="noopener">Ticket auf PlayAgainst sichern&nbsp;↗</a>
            <span class="pa-note">Öffnet playagainst.xyz in einem neuen Tab.</span>
          </div>
        </div>
        <figure class="phone" aria-label="So sieht das Turnier auf PlayAgainst aus (Beispielansicht)" style="margin:0">
          <div class="phone-in">
            <div class="ph-top"><span>PLAYAGAINST</span><span>Event</span></div>
            <div class="ph-card">
              <h4>CollectorsGuild #1</h4>
              <div class="ph-row"><span>So, 27.12.2026</span><span>Dillingen/Saar</span></div>
              <div class="ph-row"><span>Plätze frei</span><b>16 / 16</b></div>
              <div class="ph-bar"><i></i></div>
              <div class="ph-btn">Anmelden</div>
            </div>
            <ul class="ph-list">
              <li>Paarungen und Rundenuhr live</li>
              <li>Ergebnis melden, beide bestätigen</li>
              <li>Erinnerung am Vortag per E-Mail</li>
              <li>Rangliste der Season</li>
            </ul>
            <figcaption class="ph-cap">Beispielansicht</figcaption>
          </div>
        </figure>
      </div>
    </div>
  </section>

  <section id="termin" style="scroll-margin-top:96px">
    <div class="wrap">
      <div class="sec-head">
        <span class="eyebrow">Nächstes Turnier</span>
        <h2>CollectorsGuild #1</h2>
      </div>
      <article class="glass event">
        <div class="date-orb" aria-hidden="true"><b>27</b><span>Dez 2026</span></div>
        <div>
          <h3>Sonntag, <span class="nobr">27. Dezember 2026</span></h3>
          <p class="when">Trading Card Cave, Marktstraße 13, Dillingen/Saar</p>
          <ul class="facts">
            <li><small>Format</small><b>Standard · Swiss · Bo3</b></li>
            <li><small>Plätze</small><b>max. 16</b></li>
            <li><small>Startzeit</small><span class="soon">folgt</span></li>
            <li><small>Ticket</small><b>9&nbsp;€ über PlayAgainst</b></li>
            <li><small>Anmeldeschluss</small><b>Sa, 26.12.2026</b></li>
            <li><small>Anmeldung</small><b><a href="#anmeldung">über PlayAgainst</a></b></li>
          </ul>
          <p class="when">Mitbringen: dein Standard-Deck in Hüllen, Schadensmarker und Münze oder Würfel. Runden: 3 bei 4–8 Spielern, 4 bei 9–12, 5 bei 13–16. Unter 4 Anmeldungen wird abgesagt und das Ticket erstattet.</p>
          <p class="countdown" id="countdown" hidden>Noch <b id="cd-days"></b> bis zum Turnier</p>
        </div>
      </article>
    </div>
  </section>

  <section id="season" style="scroll-margin-top:96px">
    <div class="wrap">
      <div class="sec-head">
        <span class="eyebrow">Season 1</span>
        <h2>Drei Turniere, eine Trade Night, ein Finale</h2>
        <p>Fest ist bisher nur Turnier #1 am 27.12.2026. Die übrigen Termine stehen hier, sobald sie feststehen. Du musst nicht bei jedem Termin mitspielen.</p>
      </div>
      <ol class="season">
        <li class="glass"><span class="dot dot-g">1</span><span class="m">So, 27.12.2026</span><h3>Turnier #1</h3><p>Swiss, Best of 3. Punkte für die Rangliste.</p></li>
        <li class="glass"><span class="dot dot-g">2</span><span class="m">Termin folgt</span><h3>Turnier #2</h3><p>Swiss, Best of 3. Punkte für die Rangliste.</p></li>
        <li class="glass"><span class="dot dot-w">3</span><span class="m">Termin folgt</span><h3>Trade Night</h3><p>Kostenlos. Tauschen ja, Verkaufen nein.</p></li>
        <li class="glass"><span class="dot dot-g">4</span><span class="m">Termin folgt</span><h3>Turnier #3</h3><p>Swiss, Best of 3. Punkte für die Rangliste.</p></li>
        <li class="glass final"><span class="dot dot-v">5</span><span class="m">Termin folgt</span><h3>Finale</h3><p>Die Top 8 der Rangliste. Swiss, Best of 3, Ticket 9&nbsp;€.</p></li>
      </ol>
    </div>
  </section>

  <section id="punkte" style="scroll-margin-top:96px">
    <div class="wrap">
      <div class="sec-head">
        <span class="eyebrow">Rangliste</span>
        <h2>Punkte</h2>
        <p>Die Punkte laufen direkt über PlayAgainst. Größere Turniere bringen damit mehr Punkte, kleine weniger.</p>
      </div>
      <div class="pd">
        <div class="glass pd-box">
          <h3>Pro Turnier</h3>
          <table class="ptable">
            <tbody>
              <tr><td>Platz 1</td><td>so viele Punkte, wie Leute mitspielen</td></tr>
              <tr><td>Jeder weitere Platz</td><td>1 Punkt weniger</td></tr>
              <tr><td>Beispiel 16 Spieler</td><td>16, 15 … 1</td></tr>
              <tr><td>Fürs Mitspielen</td><td>+2</td></tr>
              <tr><td>Wertung</td><td>deine besten 2 Turniere</td></tr>
            </tbody>
          </table>
          <p>Disqualifikation: 0 Punkte für das Turnier, je nach Fall Bann für die Season.</p>
        </div>
        <div class="glass pd-box">
          <h3>Finale</h3>
          <p>Die Top 8 der Rangliste sind qualifiziert. Sagt jemand ab, rückt Platz 9 nach, dann Platz 10. Gespielt wird wie bei den anderen Turnieren: Swiss, Best of 3.</p>
          <div class="empty"><b>Noch keine Ergebnisse</b>Die Rangliste startet nach dem ersten Turnier am 27.12.2026 und steht auf PlayAgainst.</div>
        </div>
      </div>
      <p style="margin-top:18px;color:var(--t-muted)">Die Regeln stehen vor dem ersten Turnier fest und ändern sich während der Season nicht. Anfänger sind willkommen.</p>
    </div>
  </section>
</main>

<footer class="wrap t-foot">
  <div class="glass">
    <span class="motto">Keep the Hobby Cheap.</span>
    <nav aria-label="Fußzeile">
      <a href="index.html">NoGreedCards</a>
      <a href="ablauf.html">Ankauf</a>
      <a href="https://www.youtube.com/@NoGreedCollector" target="_blank" rel="noopener">YouTube</a>
      <a href="mailto:nogreedtcg@gmail.com">Kontakt</a>
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
    </nav>
  </div>
</footer>'''

T_JS = r"""(function(){
  var start=new Date(2026,11,27), now=new Date(); now.setHours(0,0,0,0);
  var d=Math.round((start-now)/864e5);
  if(d>0){ document.getElementById('cd-days').textContent=d===1?'1 Tag':d+' Tage'; document.getElementById('countdown').hidden=false; }
})();"""

def turnier_page():
    head = f'''<title>CollectorsGuild Turniere · NoGreedCards</title>
<meta name="description" content="CollectorsGuild: die Pokémon-TCG-Turnierliga von NoGreedCards in der Trading Card Cave, Dillingen/Saar. Erstes Turnier am 27.12.2026.">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="theme-color" content="#150d27">
{FONTS}
<style>{FONT_CSS}{T_CSS}</style>
'''
    content = typo(T_BODY) + f"\n<script>{T_JS}</script>\n"
    full = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + head + '</head>\n<body>\n' + content + '</body>\n</html>\n')
    for out in (REPO_OUT, ART_OUT):
        open(os.path.join(out, "turniere.html"), "w", encoding="utf-8").write(full)

turnier_page()
