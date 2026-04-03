const API_URL = "http://127.0.0.1:8000/items";

async function addItem() {

    const name = document.getElementById("itemName").value;
    const quantity = document.getElementById("itemQty").value;

    const item = {
        name: name,
        quantity: parseInt(quantity)
    };

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(item)
    });

    loadItems();
}

async function loadItems() {

    const response = await fetch(API_URL);
    const items = await response.json();

    const list = document.getElementById("inventoryList");
    list.innerHTML = "";

    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - Quantity: ${item.quantity}`;
        list.appendChild(li);
    });
}

window.onload = loadItems;