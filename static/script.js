// static/script.js

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var nodeCopy = document.getElementById(data).cloneNode(true);
    nodeCopy.id = data + "-copy"; // Change id to avoid duplicates
    ev.target.appendChild(nodeCopy);
}

function calculate() {
    let breakfastRecipes = Array.from(document.getElementById('breakfast-box').children).map(item => item.id.replace('-copy', ''));
    let lunchRecipes = Array.from(document.getElementById('lunch-box').children).map(item => item.id.replace('-copy', ''));
    let dinnerRecipes = Array.from(document.getElementById('dinner-box').children).map(item => item.id.replace('-copy', ''));
    let allRecipes = breakfastRecipes.concat(lunchRecipes, dinnerRecipes);
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({recipes: allRecipes})
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<h5>食材總量</h5>';
        let ul = document.createElement('ul');
        let totalIngredientsCount = 0;
        for (let [ingredient, amount] of Object.entries(data)) {
            let li = document.createElement('li');
            let encodedIngredient = encodeURIComponent(ingredient); // 對 ingredient 做編碼
            li.innerHTML = `<img src="/static/images/${encodedIngredient}.png" alt="${ingredient}" style="width: 50px;"> ${ingredient}: ${amount}`;
            ul.appendChild(li);
            totalIngredientsCount += amount;
        }
        resultDiv.appendChild(ul);
        let totalDiv = document.createElement('div');
        totalDiv.innerHTML = `<h5>總共使用食材數量: ${totalIngredientsCount}</h5>`;
        resultDiv.appendChild(totalDiv);
    });
}

function resetPage() {
    document.getElementById('breakfast-box').innerHTML = '<h2>早餐</h2>';
    document.getElementById('lunch-box').innerHTML = '<h2>午餐</h2>';
    document.getElementById('dinner-box').innerHTML = '<h2>晚餐</h2>';
    document.getElementById('result').innerHTML = '<h5>結果</h5>';
}
