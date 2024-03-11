document.addEventListener('DOMContentLoaded', function () {
    fetch('/galleryimagedata')
        .then(response => response.json())
        .then(data => {
            const galleryimagecardsContainer = document.getElementById('galleryimage-cards-container');
            data.forEach(galleryimage_details => {
                const galleryimagecard = document.createElement('div');
                galleryimagecard.classList.add('col-lg-4');
                galleryimagecard.classList.add('col-md-6');
                galleryimagecard.innerHTML = `
                    <div class="card card-item" style="width: 450px; height: 250px; border-radius: 20px;">
                        <img src="../static/images/${galleryimage_details.imagename}" class="card-img-top" alt="profile image" style="width: 100%; height: 100%; object-fit: cover; border-radius: 20px; border: 5px solid #fff;">
                    </div>
                `;
                galleryimagecardsContainer.appendChild(galleryimagecard);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

