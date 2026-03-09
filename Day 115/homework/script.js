const container = document.getElementById("products");

getProducts().then(products => {

container.innerHTML = products.map(p => `
<div class="card">

<img src="${p.image}">
<h3>${p.title}</h3>

<p>$${p.price}</p>

<a href="product.html?id=${p.id}">
<button>View</button>
</a>

</div>
`).join("");
});