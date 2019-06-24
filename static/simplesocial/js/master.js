let form = document.getElementById( "create-update-form" );
form.addEventListener( "click", ( evt ) => {
  let trg = evt.target,
      trg_par = trg.parentElement;
  if ( trg.type === "radio" && trg_par && trg_par.tagName.toLowerCase() === "label" ) {
    let prior = form.querySelector( 'label.checked input[name="' + trg.name + '"]' );
    if ( prior ) {
      prior.parentElement.classList.remove( "checked" );
    }
    trg_par.classList.add( "checked" );
  }
}, false );


radio = document.getElementsByTagName("input");

for (var trv = 0; trv < radio.length; trv++) {
  if (radio[trv].checked) {
    let trg = radio[trv],
      trg_par = trg.parentElement;
    if (trg.type === "radio" && trg_par && trg_par.tagName.toLowerCase() === "label") {
      console.log(trg);
      trg_par.classList.add("checked");
    }
  }
}
