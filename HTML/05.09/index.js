
document.getElementById("spinner").style.display="none";
const cardsContainer = document.getElementById('cContain');
document.getElementById("alerts").style.display = "none";

 var url="";

 function listSearch(url) {
    let search = document.getElementById("searchbar").value;
    let cardsContainer = document.getElementById("cContain");
    let spinner = document.getElementById("spinner");
    let alert = document.getElementById("alerts");
    spinner.style.display = "block";
    cardsContainer.innerHTML = "";

    fetch(`${url}${search}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.products);
            if (data.products.length === 0) {
               document.getElementById("alerts").style.display = "flex";
                let alertInterval = setInterval(() => {
        document.getElementById("alerts").style.display = "none";
        clearInterval(alertInterval);
    }, 3000);
            }
            data.products.forEach(product => {
                let card = `
                    <div class="col">
                        <div class="card h-100">
                            <div class="card-body">
                `;

                if (product.images.length > 0) {
                    card += `
                        <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
                            <div class="carousel-inner">
                    `;

                    product.images.forEach((image, index) => {
                       
                        if (index === 0) {
                            card += `
                                <div class="carousel-item active">
                                    <img src="${image}" class="d-block w-100 cImage" alt="...">
                                </div>
                            `;
                        } else {
                            
                            card += `
                                <div class="carousel-item">
                                    <img src="${image}" class="d-block w-100 cImage" alt="...">
                                </div>
                            `;
                        }
                    });
                    card += `
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    `;
                }

                card += `
                                <h5 class="card-title">${product.brand} ${product.title}</h5>
                                <p class="card-text">${product.description}</p>
                            </div>
                            <div class="card-footer">
                                <small class="text-muted">${product.price}</small>
                            </div>
                        </div>
                    </div>
                `;
                cardsContainer.innerHTML += card;
            });
            spinner.style.display = "none";
        })
        .catch(error => console.log(error));
}

function listAll(url) {
    cardsContainer.innerHTML="";
   console.log(url);    
    document.getElementById("spinner").style.display="block";
   fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data);
     if(url=='https://dummyjson.com/products'){
      data.products.slice(0,23).forEach(product => {
        var card = `
          <div class="col">
            <div class="card h-100">
              <div class="card-body">
        `;
       
        if (product.images.length > 0) {
          card += `
            <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
              <div class="carousel-inner">
          `;
          product.images.forEach((image, index) => {
            if (index == 0) {
              card += `
                <div class="carousel-item active">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>
              `;
            } else {
              card += `
                <div class="carousel-item">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>
              `;
            }
          });
          card += `
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          `;
      
        card += `
                <h5 class="card-title">${product.brand} ${product.title}</h5>
                <p class="card-text">${product.description}</p>
              </div>
              <div class="card-footer">
                <small class="text-muted">${product.price}</small>
              </div>
            </div>
          </div>
        `;
        // Add card to container
    }
        cardsContainer.innerHTML += card;
document.getElementById("spinner").style.display="none";});
    }
    }
    );
}



function listOne(url){
    cardsContainer.innerHTML="";
    document.getElementById("spinner").style.display="block";

        fetch(url).then(response=>response.json()).then(product=>{

            console.log(product);
            var card = `
          <div class="col">
            <div class="card h-100">
              <div class="card-body">
        `;
       
        if (product.images.length > 0) {
          card += `
            <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
              <div class="carousel-inner">
          `;
          product.images.forEach((image, index) => {
            if (index == 0) {
              card += `
                <div class="carousel-item active">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>
              `;
            } else {
              card += `
                <div class="carousel-item">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>
              `;
            }
          });
          card += `
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade-${product.id}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          `;
      
        card += `
                <h5 class="card-title">${product.brand} ${product.title}</h5>
                <p class="card-text">${product.description}</p>
              </div>
              <div class="card-footer">
                <small class="text-muted">${product.price}</small>
              </div>
            </div>
          </div>
        `;
        // Add card to container
    }
        cardsContainer.innerHTML += card;
document.getElementById("spinner").style.display="none"
        })
    }
        document.getElementById("logout").className = "form";
        document.getElementById("logout").style.display = "none";

        document.getElementById("login").className = "form d-flex";
        document.getElementById("login").style.display = "block";

        function login() {
            let Uname = document.getElementById("email").value;
            let Upassword = document.getElementById("password").value;

            fetch('https://dummyjson.com/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({

                        username: Uname,
                        password: Upassword,

                    })
                })
                .then(res => res.json())
                .then(function(data) {
                    if (data.message == undefined) {
                        document.getElementById("login").style.display = "none";
                        document.getElementById("login").className = "form";

                        document.getElementById("profilkep").src = data.image;
                        document.getElementById("profile").innerHTML = data.firstName + " " + data.lastName;
                        document.getElementById("logout").className = "form d-flex";
                        document.getElementById("logout").style.display = "block";
                        console.log(data);

                    } else {
                        alert("Hibás adatok!");
                    }
                });
        }