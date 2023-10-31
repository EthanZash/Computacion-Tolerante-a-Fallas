function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculateResult() {
    const expression = document.getElementById('display').value;
    try {
        const result = eval(expression);
        document.getElementById('display').value = result.toFixed(2); // Limitar a 2 decimales
    } catch (error) {
        document.getElementById('display').value = 'Error';
    }
}

function calculateSquareRoot() {
    const number = parseFloat(document.getElementById('display').value);
    if (number >= 0) {
        const result = Math.sqrt(number).toFixed(2);
        document.getElementById('display').value = result;
    } else {
        document.getElementById('display').value = 'Error';
    }
}

function calculateSine() {
    const number = parseFloat(document.getElementById('display').value);
    const result = Math.sin(number * (Math.PI / 180)).toFixed(2);
    document.getElementById('display').value = result;
}

function calculateCosine() {
    const number = parseFloat(document.getElementById('display').value);
    const result = Math.cos(number * (Math.PI / 180)).toFixed(2);
    document.getElementById('display').value = result;
}

function calculateNaturalLog() {
    const number = parseFloat(document.getElementById('display').value);
    if (number > 0) {
        const result = Math.log(number).toFixed(2);
        document.getElementById('display').value = result;
    } else {
        document.getElementById('display').value = 'Error';
    }
}
