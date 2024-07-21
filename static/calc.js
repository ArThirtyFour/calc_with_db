function calculate () {
    let num_1 = Number(document.getElementById('first_num').value) 
    console.log('First number:', num_1)
    let num_2 = Number(document.getElementById('second_num').value)
    let operation = document.getElementById('action').value
    let result = 0.0

    if (operation === '+') {
        result = num_1 + num_2
    } else if (operation === '-') {
        result = num_1 - num_2
    } else if (operation === '*') {
        result = num_1 * num_2
    } else if (operation === '/' && num_2 !== 0) {
        result = num_1 / num_2
    } else if (operation === '**') {
        result = Math.pow(num_1, num_2)
    }

    let res_e = document.createElement('h2') 
    res_e.className = 'text_suka'
    res_e.textContent = 'Результат: ' + result
    document.body.appendChild(res_e)
}
    
