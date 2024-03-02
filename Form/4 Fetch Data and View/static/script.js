document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
    .then(response => response.json())
    .then(data => {
        const cardsContainer = document.getElementById('cards-container');
        data.forEach(person => {
            const card = document.createElement('div');
            card.classList.add('col-md-4');
            card.innerHTML = `
                <div class="card">
                    <div class="card-body text-center">
                        <img src="../static/images/${person.imagename}" class="img rounded-circle mb-4" alt="profile image">
                        <h4>${person.studentname}</h4>
                        <p class="text-muted mb-0">${person.designation}</p>
                        <p class="text-muted mb-0">${person.institute}</p>
                    </div>
                </div>
            `;
            cardsContainer.appendChild(card);
        });
    })
    .catch(error => console.error('Error fetching data:', error));
});
