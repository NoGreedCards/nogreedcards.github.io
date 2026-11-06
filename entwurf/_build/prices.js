// PREISE in Cent je Karte. Vorschlag aus der Preisgestaltung, noch nicht final.
// Gleiche Werte stehen in der Preistabelle auf der Startseite.
var NGC_PREISE = {
  MIN: 500,                         // Mindestmenge Bulk, alle Karten zusammen
  cu: 0.7,                          // Common & Uncommon
  holo: 1.5, holoBonus: 2, holoAb: 500,
  ex: 25, exBonus: 35, exAb: 20,    // EX, V, GX, VMAX, ex unter 1 € Marktwert
  un: 0.6,                          // unsortiert
  quote: 0.7                        // Einzelkarten: 70 % vom Cardmarket-Preis
};
function ngcNum(s){ var v=parseFloat(String(s).replace(/\./g,'').replace(',','.')); return isFinite(v)&&v>0?v:0; }
// m: {sortiert:bool, cu, holo, ex, un} -> Teilbeträge in Cent, Anzahl, Summe
function ngcBulk(m){
  var P=NGC_PREISE, r={};
  if (m.sortiert){
    r.holoRate = m.holo>=P.holoAb ? P.holoBonus : P.holo;
    r.exRate   = m.ex>=P.exAb ? P.exBonus : P.ex;
    r.cu=Math.round(m.cu*P.cu); r.holo=Math.round(m.holo*r.holoRate); r.ex=Math.round(m.ex*r.exRate);
    r.anzahl=m.cu+m.holo+m.ex; r.cent=r.cu+r.holo+r.ex;
    r.tipp = m.holo>0&&m.holo<P.holoAb ? 'Noch '+(P.holoAb-m.holo).toLocaleString('de-DE')+' Holos, dann zahle ich 2 ct je Holo.'
           : m.ex>0&&m.ex<P.exAb ? 'Noch '+(P.exAb-m.ex)+' EX/V-Karten, dann zahle ich 35 ct je Karte.' : '';
  } else { r.un=Math.round(m.un*P.un); r.anzahl=m.un; r.cent=r.un; r.tipp=''; }
  r.ok = r.anzahl>=P.MIN;
  return r;
}
var ngcEur=new Intl.NumberFormat('de-DE',{style:'currency',currency:'EUR'});
function ngcFmt(cent){ return ngcEur.format(cent/100); }
