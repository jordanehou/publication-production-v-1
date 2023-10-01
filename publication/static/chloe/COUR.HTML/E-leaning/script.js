const btnConnexion = document.querySelector("#btn-connexion");
const modalConnexion = document.querySelector("#modal-connexion");
const closeModalConnexion = document.querySelector("#modal-connexion .close");
const btnInscription = document.querySelector("#btn-inscription");
const modalInscription = document.querySelector("#modal-inscription");
const closeModalInscription = document.querySelector("#modal-inscription .close");

btnConnexion.addEventListener("click", function() {
  modalConnexion.style.display = "block";
  console.log();
});

closeModalConnexion.addEventListener("click", function() {
  modalConnexion.style.display = "none";
});

window.addEventListener("click", function(event) {
  if (event.target == modalConnexion) {
    modalConnexion.style.display = "none";
  }
});

btnInscription.addEventListener("click", function() {
  modalInscription.style.display = "block";
});

closeModalInscription.addEventListener("click", function() {
  modalInscription.style.display = "none";
});

window.addEventListener("click", function(event) {
  if (event.target == modalInscription) {
    modalInscription.style.display = "none";
  }
});