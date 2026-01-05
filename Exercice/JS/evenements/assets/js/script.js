
let text    =   document.getElementsByTagName('p')[0];

function setToItalique(event){
    //this.style.fontStyle    =   'italic';
    this.setAttribute('class', 'italique');
    this.innerHTML = "test";
}
text.addEventListener('click', setToItalique )



let img =   document.getElementsByTagName('img')[0];
img.addEventListener('mouseenter', function(){
    this.setAttribute('src', './assets/img/haut-de-la-page-vue-rapprochee-des-pates-italiennes-crues-peu-formees-sur-un-espace-sombre.jpg')
})
img.addEventListener('mouseleave', function(){
    this.setAttribute('src', './assets/img/vue-de-dessus-du-modele-de-pates-penne.jpg')
    
})