function toggleStar() {
   const starElement = document.getElementById('star');
   starElement.classList.toggle('yellow-star');
}

function sortList() {
   const sortCriteria = document.getElementById('sortCriteria').value;
   const urlParams = new URLSearchParams(window.location.search);
   urlParams.set('sort_by', sortCriteria);
   window.location.search = urlParams.toString();
}