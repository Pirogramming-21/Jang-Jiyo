function toggleStar(ideaId) {
   const form = document.createElement('form');
   form.method = 'post';
   form.action = `{% url 'ideas:toggle_star' '' %}${ideaId}/`;
   const csrfToken = document.createElement('input');
   csrfToken.type = 'hidden';
   csrfToken.name = 'csrfmiddlewaretoken';
   csrfToken.value = '{{ csrf_token }}';
   form.appendChild(csrfToken);
   document.body.appendChild(form);
   form.submit();
}

function sortList() {
   const sortCriteria = document.getElementById('sortCriteria').value;
   const urlParams = new URLSearchParams(window.location.search);
   urlParams.set('sort_by', sortCriteria);
   window.location.search = urlParams.toString();
}