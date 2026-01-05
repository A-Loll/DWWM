//exo1
const bouton = document.getElementById("btn");

bouton.addEventListener("click", function () {
    console.log("Click");
});
//exo2
const image = document.getElementById("image");

image.addEventListener("mouseover", () => {
    console.log(image.src);
});
//exo3
document.addEventListener("keydown", function (event) {
    console.log(event.keyCode + ' -> "' + event.key + '"');
});
//exo4
const liste = document.getElementById("metiers");

liste.addEventListener("click", (event) => {
    if (event.target.tagName === "LI") {
        console.log(event.target.textContent);
    }
});
//exo5
const form = document.getElementById("form");

form.addEventListener("submit", (event) => {
    event.preventDefault();

const firstName = document.getElementById("FirstName").value;
const lastName = document.getElementById("LastName").value;
    console.log("Prénom : " + firstName + ", Nom : " + lastName);
});
//exo6
let inputs=form.querySelectorAll("input");

        function background(evt) {
            evt.currentTarget.classList.toggle("rose");
        }

        inputs.forEach((input)=> {
            input.addEventListener("focus",background);
            input.addEventListener("blur",background);
});
//exo7
let select=form.querySelector("#select");

        select.addEventListener("change",function(evt){
            console.log(this.value);
});