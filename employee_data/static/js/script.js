
const form = document.getElementById('form');
form.addEventListener('submit', function(Event){
    Event.preventDefault();
    form.reset();
})
