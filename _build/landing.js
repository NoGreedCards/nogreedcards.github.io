(function(){
  var int=new Intl.NumberFormat('de-DE');
  function $(id){return document.getElementById(id);}

  // Einzelkarten: 70 % vom Cardmarket-Preis
  var cm=$('cm-price'), cmOut=$('calc-val');
  function single(){var v=ngcNum(cm.value);cmOut.textContent=v?ngcFmt(Math.round(v*100*NGC_PREISE.quote)):'–';}
  cm.addEventListener('input',single);single();

  // Bulk-Rechner mit Kategorien
  var box=$('bulk-calc'), out=$('bulk-val'), hint=$('bulk-hint'), bonus=$('bulk-bonus'), hintText=hint.textContent;
  var ids=['cu','holo','ex','un'];
  function sortiert(){ return box.querySelector('input[name="bc-mode"]:checked').value==='sortiert'; }
  function bulk(){
    var s=sortiert(), m={sortiert:s};
    ids.forEach(function(k){ m[k]=Math.floor(ngcNum($('bc-'+k).value)); });
    $('bc-sorted').hidden=!s; $('bc-unsorted').hidden=s;
    var r=ngcBulk(m);
    ids.forEach(function(k){ if(r[k]!==undefined) $('bc-'+k+'-v').textContent=ngcFmt(r[k]); });
    if (s){
      $('bc-holo-r').textContent = r.holoRate===NGC_PREISE.holoBonus ? '2 ct je Karte (ab 500)' : '1,5 ct · ab 500: 2 ct';
      $('bc-ex-r').textContent   = r.exRate===NGC_PREISE.exBonus ? '35 ct je Karte (ab 20)' : '25 ct · ab 20: 35 ct';
    }
    if (!r.ok){ out.textContent='–'; box.classList.add('bad'); hint.textContent='Ich kaufe Bulk ab '+int.format(NGC_PREISE.MIN)+' Karten an. Du bist bei '+int.format(r.anzahl)+'.'; bonus.textContent=''; return; }
    box.classList.remove('bad'); hint.textContent=hintText; out.textContent=ngcFmt(r.cent); bonus.textContent=r.tipp;
  }
  ids.forEach(function(k){
    var el=$('bc-'+k);
    el.addEventListener('input',bulk);
    el.addEventListener('blur',function(){var n=Math.floor(ngcNum(el.value));el.value=int.format(n);bulk();});
  });
  box.querySelectorAll('input[name="bc-mode"]').forEach(function(r){r.addEventListener('change',bulk);});
  bulk();
})();
