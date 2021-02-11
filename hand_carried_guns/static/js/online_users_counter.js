let timer;
let start = window.onload = function () {
    fetch('/count-viewers',)
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            let counter = document.getElementById('viewers-counter')
            if (counter) {
                counter.innerText = `currently online: ${data.counter}`
            }

        })
        .catch(() => {
            alert('Failed counter')
        })
    clearInterval(timer)
    timer = setInterval(start, 120000)
};



