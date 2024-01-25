async function populateTable()
{
    var response = await fetch('http://127.0.0.1:5001/products');
    var data = await response.json();
    var tablebody = document.getElementById('productTableBody');
    for (var index = 0 ; index < data.length ; index ++)
    {
        var product = data[index];
        var row = document.createElement('tr');
        row.innerHTML = `
                         <td>${product.name}</td>
                         <td>${product.description}</td>
                         <td>${product.price}</td>
                         <td>${product.rating}</td>
                         <td><button class="btn btn-primary"  onclick="editProduct(${index})" data-bs-toggle="modal" data-bs-target="#editModal">Edit</button></td>
          <td><button class="btn btn-danger" onclick="deleteProduct(${index})">Delete</button></td>
                         `;
        tablebody.appendChild(row);
    }

}

async function updateProduct()
{
    var pid = document.getElementById('pId').value;
    var pName = document.getElementById('pName').value;
    var pDescription = document.getElementById('pDescription').value;
    var pPrice = document.getElementById('pPrice').value;
    var pRating = document.getElementById('pRating').value;

    var product = {
        pid: pid,
        name: pName,
        description: pDescription,
        price: pPrice,
        rating: pRating,

    };

     response = await fetch('http://127.0.0.1:5001/products',
     {
        method: 'PATCH' ,
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify(product)

     }
     );
     populateTable();

}

async function saveProduct()
{
    const pid = document.getElementById('pIdAdd').value;
    const pName = document.getElementById('pNameAdd').value;
    const pDescription = document.getElementById('pDescriptionAdd').value;
    const pPrice = document.getElementById('pPriceAdd').value;
    const pRating = document.getElementById('pRatingAdd').value;
    const image = document.getElementById('pImageAdd').value;


    var product = {
        pid: pid,
        name: pName,
        description: pDescription,
        price: pPrice,
        rating: pRating,
        image: image,

    };

     var response = await fetch('http://127.0.0.1:5001/products' ,
     {
        method: 'POST' ,
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify(product)

     }
     );

    const form = document.getElementById('productForm');
    form.reset();
    populateTable();

}

async function deleteProduct(index)
{
    const response = await fetch('http://127.0.0.1:5001/products' ,
    {
        method: 'DELETE' ,
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify({pid : products[index].pid})

    }
    );
    populateTable();

}






