fetch("https://fakestoreapi.com/products")
  .then(response => response.json())
  .then(data => {
    let productsDiv = document.getElementById("products");

    data.forEach(product => {

      let productDiv = document.createElement("div");
      productDiv.className = "product";


      let img = document.createElement("img");
      img.src = product.image;
      img.alt = product.title;

      let title = document.createElement("h3");
      title.textContent = product.title;


      let price = document.createElement("p");
      price.textContent = product.price + " $";

      productDiv.appendChild(img);
      productDiv.appendChild(title);
      productDiv.appendChild(price);

   
      productsDiv.appendChild(productDiv);
    });
  });
