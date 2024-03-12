document.addEventListener('DOMContentLoaded', function () {
    const imagesPerPage = 1;
    let currentPage = 1;

    fetch('/successfulstudentdata')
        .then(response => response.json())
        .then(data => {
            const successfulstudentcardsContainer = document.getElementById('successfulstudent-cards-container');
            const totalImages = data.length;
            const totalPages = Math.ceil(totalImages / imagesPerPage);

            // Function to display images for the current page
            const displayImages = () => {
                // Clear existing content
                successfulstudentcardsContainer.innerHTML = '';

                // Calculate start and end index of images for the current page
                const startIndex = (currentPage - 1) * imagesPerPage;
                const endIndex = Math.min(startIndex + imagesPerPage, totalImages);

                // Loop through images for the current page and create image elements
                for (let i = startIndex; i < endIndex; i++) {
                    const successfulstudent_details = data[i];
                    const successfulstudentcard = document.createElement('div');
                    successfulstudentcard.classList.add('col-lg-3');
                    successfulstudentcard.classList.add('col-md-6');
                    console.log(successfulstudent_details.imagename);
                    successfulstudentcard.innerHTML = `
                    <div class="card card-item">
                    <div class="view view-cascade overlay text-center">
                    <img src="../static/images/successfulstudent/${successfulstudent_details.image_name}" class="card-img-top" alt="profile image">
                    </div>
                    <div class="card-body">
                      <h4 class="card-title"><strong>${successfulstudent_details.studentname}</strong>
                      </h4>
                      <p class="designation">${successfulstudent_details.studentdesignation}</p>
                      <p class="institute">${successfulstudent_details.studentinstitute}</p>
                    </div>
                  </div>
                    `;
                    successfulstudentcardsContainer.appendChild(successfulstudentcard);
                }

                // Update successfulpagination links
                updatesuccessfulpagination();
            };

            // Function to update successfulpagination links
            const updatesuccessfulpagination = () => {
                const successfulpaginationContainer = document.getElementById('successfulpagination');
                successfulpaginationContainer.innerHTML = '';

                // Add Previous button
                if (currentPage > 1) {
                    successfulpaginationContainer.innerHTML += `
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
                    successfulpaginationContainer.innerHTML += `
                        <li class="page-item${currentPage === i ? ' active' : ''}">
                            <button class="page-link" onclick="changePage(${i})">${i}</button>
                        </li>
                    `;
                }

                // Add Next button
                if (currentPage < totalPages) {
                    successfulpaginationContainer.innerHTML += `
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

            // Function to handle successfulpagination
            window.changePage = (page) => {
                currentPage = page;
                displayImages();
            };
        })
        .catch(error => console.error('Error fetching data:', error));
});
