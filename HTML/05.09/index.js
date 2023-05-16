document.getElementById("spinner").style.display = "none";
const cardsContainer = document.getElementById('cContain');
document.getElementById("alerts").style.display = "none";
var loggedin = false;

var url = "";

function listSearch(url) {
    var search = document.getElementById("searchbar").value;
    let cardsContainer = document.getElementById("cContain");
    let spinner = document.getElementById("spinner");
    spinner.style.display = "block";
    cardsContainer.innerHTML = "";
    cardsContainer.className = "cardcontainer row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3";



    fetch(`${url}${search}`)
        .then(response => response.json())
        .then(data => {
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
                            <div class="card-body"> `;


                if (product.images.length > 0) {
                    card += `
                        <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
                            <div class="carousel-inner">`;


                    product.images.forEach((image, index) => {

                        if (index === 0) {
                            card += `
                                <div class="carousel-item active">
                                    <img src="${image}" class="d-block w-100 cImage" alt="...">
                                </div> `;

                        } else {

                            card += `
                                <div class="carousel-item">
                                    <img src="${image}" class="d-block w-100 cImage" alt="...">
                                </div> `;

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
                        </div> `;

                }

                card += `
                                <h5 class="card-title">${product.brand} ${product.title}</h5>
                                <p class="card-text">${product.description}</p>
                            </div>
                            <div class="card-footer">
                                <i id="stockid" class="bi bi-stack">${product.stock} in stock</i> <br>
                                <small id="price" class="text-muted">${product.price} $</small> <br>
                                <button class="btn btn-primary" onclick="addToCart(${product.id})">Buy Now</button>
                            </div>
                        </div>
                    </div> `;

                cardsContainer.innerHTML += card;
            });
            spinner.style.display = "none";
            document.getElementById("searchresultbar").innerHTML = `<b> "${search}" találatok ${data.products.length} db</b>`;
            document.getElementById("searchresultbar").innerHTML += `<hr>`;
        })
        .catch(error => console.log(error));
}

function listAll(url) {
    cardsContainer.innerHTML = "";
    cardsContainer.className = "cardcontainer row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3";
    document.getElementById("searchresultbar").innerHTML = "";

    document.getElementById("spinner").style.display = "block";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (url == 'https://dummyjson.com/products') {
                data.products.slice(0, 10).forEach(product => {
                    var card = `
          <div class="col">
            <div class="card h-100">
              <div class="card-body">`;


                    if (product.images.length > 0) {
                        card += `
            <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
              <div class="carousel-inner"> `;

                        product.images.forEach((image, index) => {
                            if (index == 0) {
                                card += `
                <div class="carousel-item active">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>`;

                            } else {
                                card += `
                <div class="carousel-item">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>`;

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
            </div>`;


                        card += `
                <h5 class="card-title">${product.brand} ${product.title}</h5>
                <p class="card-text">${product.description}</p>
              </div>
              <div class="card-footer">
                <i id="stockid" class="bi bi-stack">${product.stock} in stock</i> <br>
                <small id="price" class="text-muted">${product.price} $</small> <br>
                <button class="btn btn-primary" onclick="addToCart(${product.id})">Buy Now</button>
                <br>
              </div>
            </div>
          </div>`;

                    }
                    cardsContainer.innerHTML += card;
                    document.getElementById("spinner").style.display = "none";
                });
            }
        });
}

function chechEnter() {
    if (event.keyCode == 13) {
        listSearch('https://dummyjson.com/products/search?q=');
    }
}


function listOne(url) {
    cardsContainer.innerHTML = "";
    cardsContainer.className = "cardcontainer row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3";

    document.getElementById("searchresultbar").innerHTML = "";

    document.getElementById("spinner").style.display = "block";

    fetch(url).then(response => response.json()).then(product => {

        var card = `
          <div class="col">
            <div class="card h-100">
              <div class="card-body">  `;


        if (product.images.length > 0) {
            card += `
            <div id="carouselExampleFade-${product.id}" class="carousel slide carousel-fade">
              <div class="carousel-inner"> `;

            product.images.forEach((image, index) => {
                if (index == 0) {
                    card += `
                <div class="carousel-item active">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div>`;

                } else {
                    card += `
                <div class="carousel-item">
                  <img src="${image}" class="d-block w-100 cImage" alt="...">
                </div> `;

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
            </div>`;


            card += `
                <h5 class="card-title">${product.brand} ${product.title}</h5>
                <p class="card-text">${product.description}</p>
              </div>
              <div class="card-footer">
              <i id="stockid" class="bi bi-stack">${product.stock} in stock</i> <br>
              <small id="price" class="text-muted">${product.price} $</small> <br>
              <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="addToCart(${product.id})">Buy Now</button>

              </div>
            </div>
          </div> `;

        }
        cardsContainer.innerHTML += card;
        document.getElementById("spinner").style.display = "none"
    })
}
document.getElementById("logout").className = "form";
document.getElementById("logout").style.display = "none";

document.getElementById("login").className = "form d-flex";
document.getElementById("login").style.display = "block";
var profKep;

function login() {
    let Uname = document.getElementById("username").value;
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
                profKep = data.image;
                document.getElementById("profilkep").src = profKep;
                document.getElementById("profile").innerHTML = data.firstName + " " + data.lastName;
                document.getElementById("logout").className = "form d-flex";
                document.getElementById("logout").style.display = "block";
                loggedin = true;

            } else {
                document.getElementById("alerts").innerHTML = "Hibás adatok";
                document.getElementById("alerts").style.display = "flex";
                let alertInterval = setInterval(() => {
                    document.getElementById("alerts").style.display = "none";
                    clearInterval(alertInterval);
                }, 3000);
            }
        });
}

function logout() {
    document.getElementById("login").style.display = "block";
    document.getElementById("login").className = "form d-flex";

    document.getElementById("profilkep").src = "";
    document.getElementById("profile").innerHTML = "";
    document.getElementById("logout").className = "form";
    document.getElementById("logout").style.display = "none";
    loggedin = false;
}

function loadData() {
    document.getElementById("username").value = "atuny0";
    document.getElementById("password").value = "9uQFF1Lh";

}


let cart = [];

function addToCart(index) {

    fetch(`https://dummyjson.com/products/${index}`).then(response => response.json()).then(function(data) {

        let item = { "title": data.title, "stock": data.stock, "price": data.price, "link": data.images[0], "description": data.description, "kep": data.image };
        cart.push(item);
    })
    console.log(cart);
}

function displayCart() {

    document.getElementById("cContain").innerHTML = "";
    document.getElementById("cContain").className = "";
    let items = cart.length;

    var oldal = `<section class="h-100 h-custom" style="background-color: #eee;">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col">
                    <div class="card">
                        <div class="card-body p-4">

                            <div class="row">

                                <div class="col-lg-6">
                                    <h5 class="mb-3"><a href="index.html" class="text-body"><i
                        class="fas fa-long-arrow-alt-left me-2"></i>Continue shopping</a></h5>
                                    <hr>

                                    <div class="d-flex justify-content-between align-items-center mb-4">
                                        <div>
                                            <p class="mb-1">Shopping cart</p>
                                            <p class="mb-0">You have ${items} items in your cart</p>
                                        </div>
                                        <div>
                                            <p class="mb-0"><span class="text-muted">Sort by:</span> <a href="#!" class="text-body">price <i class="fas fa-angle-down mt-1"></i></a></p>
                                        </div>
                                    </div>`;

    let osszar = 0;
    for (item of cart) {
        oldal += `
        <div class="card mb-6">
        <div class="card-body">
            <div class="d-flex justify-content-between">
                <div class="d-flex flex-row align-items-center">
                    <div>
                        <img src="${item.link}" class="img-fluid rounded-3" alt="Shopping item" style="width: 80px;">
                    </div>
                    <div class="ms-3">
                        <h5>${item.title}</h5>
                        <p class="small mb-0">${item.description}</p>
                    </div>
                </div>
                <div class="d-flex flex-row align-items-center">
                    <div style="width: 50px;">
                        <h5 class="fw-normal mb-0">1</h5>
                    </div>
                    <div style="width: 80px;">
                        <h5 class="mb-0">${item.price} $</h5>
                    </div>
                    <a href="#!" style="color: #cecece;"><i class="fas fa-trash-alt"></i></a>
                </div>
                </div>
            </div>
         </div>`;
        osszar += item.price;
    }


    oldal += `</div>
                                <div class="col-lg-6">

                                    <div class="card bg-primary text-white rounded-3">
                                        <div class="card-body">
                                            <div class="d-flex justify-content-between align-items-center mb-4">
                                                <h5 class="mb-0">Card details</h5>
                                                <img src="${profKep}" class="img-fluid rounded-3" style="width: 45px; background-color:grey; border:1px solid black" alt="Avatar">
                                            </div>

                                            <p class="small mb-2">Card type</p>
                                            <a href="#!" type="submit" class="text-white"><i
                          class="fab fa-cc-mastercard fa-2x me-2"></i></a>
                                            <a href="#!" type="submit" class="text-white"><i
                          class="fab fa-cc-visa fa-2x me-2"></i></a>
                                            <a href="#!" type="submit" class="text-white"><i
                          class="fab fa-cc-amex fa-2x me-2"></i></a>
                                            <a href="#!" type="submit" class="text-white"><i class="fab fa-cc-paypal fa-2x"></i></a>

                                            <form class="mt-4">
                                                <div class="form-outline form-white mb-4">
                                                    <input type="text" id="typeName" class="form-control form-control-lg" siez="17" placeholder="Cardholder's Name" />
                                                    <label class="form-label" for="typeName">Cardholder's Name</label>
                                                </div>

                                                <div class="form-outline form-white mb-4">
                                                    <input type="text" id="typeText1" class="form-control form-control-lg" siez="17" placeholder="1234 5678 9012 3457" minlength="19" maxlength="19" />
                                                    <label class="form-label" for="typeText2">Card Number</label>
                                                </div>

                                                <div class="row mb-4">
                                                    <div class="col-md-6">
                                                        <div class="form-outline form-white">
                                                            <input type="text" id="typeExp" class="form-control form-control-lg" placeholder="MM/YYYY" size="7" id="exp" minlength="7" maxlength="7" />
                                                            <label class="form-label" for="typeExp">Expiration</label>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-outline form-white">
                                                            <input type="password" id="typeText" class="form-control form-control-lg" placeholder="&#9679;&#9679;&#9679;" size="1" minlength="3" maxlength="3" />
                                                            <label class="form-label" for="typeText">Cvv</label>
                                                        </div>
                                                    </div>
                                                </div>

                                            </form>

                                            <hr class="my-4">

                                            <div class="d-flex justify-content-between">
                                                <p class="mb-2">Subtotal</p>
                                                <p class="mb-2">${osszar}$</p>
                                            </div>

                                            <div class="d-flex justify-content-between">
                                                <p class="mb-2">Shipping</p>
                                                <p class="mb-2">$20.00</p>
                                            </div>

                                            <div class="d-flex justify-content-between mb-4">
                                                <p class="mb-2">Total(Incl. taxes)</p>
                                                <p class="mb-2">${osszar+20}$</p>
                                            </div>

                                            <button type="button" class="btn btn-info btn-block btn-lg">
                        <div class="d-flex justify-content-between">
                          <span>${osszar+20}$ </span>
                          <span>Checkout <i class="fas fa-long-arrow-alt-right ms-2"></i></span>
                        </div>
                      </button>

                                        </div>
                                    </div>

                                </div>

                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>`;

    document.getElementById("cContain").innerHTML = oldal;
}