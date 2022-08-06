let updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        
        if (user === "AnonymousUser") {
            console.log('Not logged in.')
        } else {
            updateUserOrder(productId, action);
        }
    })
}

//this function will update the user order based on ProductID and the action made
function updateUserOrder(productId, action) {
    let url = '/update_item/'
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ productId: productId, action: action }),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
          console.log("data:", data);
          location.reload()
      });
}