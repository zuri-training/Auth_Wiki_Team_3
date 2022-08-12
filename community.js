const openMenu = document.querySelector(".open-menu");
const closeMenu = document.querySelector(".close-menu");
const sidebar = document.querySelector(".sidebar");
const mainBody = document.querySelector(".main-body");
const filterIcon = document.querySelector('.sliders');
const form = document.querySelector('.form');
const cancelButton = document.querySelector('.btn-cancel');
// const applyButton = document.querySelector('.btn-apply');
const filterIconMobile = document.querySelector('.sliders-mobile');
const formMobile = document.querySelector('.form-mobile');
const cancelButtonMobile = document.querySelector('.btn-cancel-mobile');
// const applyButtonMobile = document.querySelector('.btn-apply-mobile');

openMenu.addEventListener("click", () => {
  sidebar.style.display = "block";
  mainBody.style.display = "none";
});

closeMenu.addEventListener("click", () => {
  sidebar.style.display = "none";
  mainBody.style.display = "block";
});

filterIcon.addEventListener("click", () => {
  form.classList.toggle('hidden');
});

cancelButton.addEventListener('click', () =>{
  form.classList.toggle('hidden');
});

filterIconMobile.addEventListener("click", () => {
  formMobile.classList.toggle('hidden');
});

cancelButtonMobile.addEventListener('click', () =>{
  formMobile.classList.toggle('hidden');
});

