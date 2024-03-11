document.addEventListener('DOMContentLoaded', function () {
    const imagesPerPage = 2;
    let currentPage = 1;

    fetch('/galleryimagedata')
        .then(response => response.json())
        .then(data => {
            const galleryimagecardsContainer = document.getElementById('galleryimage-cards-container');
            const totalImages = data.length;
            const totalPages = Math.ceil(totalImages / imagesPerPage);

            // Function to display images for the current page
            const displayImages = () => {
                // Clear existing content
                galleryimagecardsContainer.innerHTML = '';

                // Calculate start and end index of images for the current page
                const startIndex = (currentPage - 1) * imagesPerPage;
                const endIndex = Math.min(startIndex + imagesPerPage, totalImages);

                // Loop through images for the current page and create image elements
                for (let i = startIndex; i < endIndex; i++) {
                    const galleryimage_details = data[i];
                    const galleryimagecard = document.createElement('div');
                    galleryimagecard.classList.add('col-lg-6');
                    galleryimagecard.classList.add('col-md-6');
                    galleryimagecard.innerHTML = `
                        <div class="img-card" style="height: 300px;">
                            <img src="../static/images/gallery/${galleryimage_details.imagename}" class="card-img-top" alt="profile image" style="width: 100%; height: 100%; object-fit: cover; border-radius: 20px;">
                        </div>
                    `;
                    galleryimagecardsContainer.appendChild(galleryimagecard);
                }

                // Update pagination links
                updatePagination();
            };

            // Function to update pagination links
            const updatePagination = () => {
                const paginationContainer = document.getElementById('pagination');
                paginationContainer.innerHTML = '';

                // Add Previous button
                if (currentPage > 1) {
                    paginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="changePage(${currentPage - 1})" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                        </li>
                    `;
                }

                // Add numbered pages
                for (let i = 1; i <= totalPages; i++) {
                    paginationContainer.innerHTML += `
                        <li class="page-item${currentPage === i ? ' active' : ''}">
                            <button class="page-link" onclick="changePage(${i})">${i}</button>
                        </li>
                    `;
                }

                // Add Next button
                if (currentPage < totalPages) {
                    paginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="changePage(${currentPage + 1})" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </li>
                    `;
                }
            };

            // Initial display
            displayImages();

            // Function to handle pagination
            window.changePage = (page) => {
                currentPage = page;
                displayImages();
            };
        })
        .catch(error => console.error('Error fetching data:', error));
});
