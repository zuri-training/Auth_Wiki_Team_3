const openMenu = document.querySelector('.open-menu');
const closeMenu = document.querySelector('.close-menu');
const sidebar = document.querySelector('.sidebar');
const mainBody = document.querySelector('.main-body');

openMenu.addEventListener('click', () => {
    sidebar.style.display = 'block';
    mainBody.style.display =  'none';
})

closeMenu.addEventListener("click", () => {
    sidebar.style.display = "none";
    mainBody.style.display = "block";
});
