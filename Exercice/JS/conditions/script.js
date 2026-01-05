//exo 1
let age = 25;
if (age >= 18) {
    console.log("Vous êtes majeur.");
} else {
    console.log("Vous êtes mineur.");
}

console.log(`vous êtes` + (age >= 18 ? " majeur." : " mineur."));

//exo 2
let num = 42;
if (num % 2 === 1) {
    console.log("Le nombre est impair.");
} else {
    console.log("Le nombre est pair.");
}
console.log(`Le nombre est ` + (num % 2 === 1 ? "impair." : "pair."));

//exo 3
let mark = prompt('Entrez une note entre 0 et 10 :');
if (mark >= 0 && mark <= 3) {
    console.log("Mauvais");
} else if (mark >= 4 && mark <= 5) {
    console.log("Moyen");
} else if (mark >= 6 && mark <= 7) {
    console.log("Assez bien");
} else if (mark >= 8 && mark <= 9) {
    console.log("Bien");
} else if (mark == 10) {
    console.log("Excellent");
} else {
    console.log("Erreur de saisie.");
}

//exo 4
let day = 4

switch (day) {
    case 1:
        console.log("Lundi");
        break;
    case 2:
        console.log("Mardi");
        break;
    case 3:
        console.log("Mercredi");
        break;
    case 4:
        console.log("Jeudi");
        break;
    case 5:
        console.log("Vendredi");
        break;
    case 6:
        console.log("Samedi");
        break;
    case 7:
        console.log("Dimanche");
        break;
    default:
        console.log("Numéro de jour invalide.");
        break;
}

//exo 5
let value = true;
let tempo =  ``;
if (typeof(value) === 'string') {
    tempo = " une chaîne de caractères.";
} else if (typeof(value) === 'number') {
    tempo = " un nombre.";
} else if (typeof(value) === 'boolean') {
    tempo = " un booléen.";
}
console.log('La valeur est' + tempo);