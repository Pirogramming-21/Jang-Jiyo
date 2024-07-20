document.addEventListener('DOMContentLoaded', function() {
   const starBtns = document.querySelector('.fa-star');

   starBtns.forEach((starBtn) => {
      starBtn.addEventLister('click', function() {
         changeColor(starBtn);
         if (starBtn.style.color == 'yellow') {
            sendIdea(starBtn);
         } else {
            removeIdea(starBtn);
         }
      });
   });
});

function changeColor(element) {
   element.style.color = element.style.color == 'yellow' ? 'gray' : 'yellow';
}

function sortList() {
   const sortCriteria = document.getElementById('sortCriteria').value;
   const urlParams = new URLSearchParams(window.location.search);
   urlParams.set('sort_by', sortCriteria);
   window.location.search = urlParams.toString();
}