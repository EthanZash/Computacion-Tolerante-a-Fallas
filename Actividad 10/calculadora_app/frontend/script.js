let displayValue = '';

function appendToDisplay(value) {
    displayValue += value;
    updateDisplay();
}

function clearDisplay() {
    displayValue = '';
    updateDisplay();
}

function calculate() {
    try {
        const result = safeEval(displayValue);
        displayValue = result.toString();
        updateDisplay();
    } catch (error) {
        displayValue = 'Error';
        updateDisplay();
    }
}

function updateDisplay() {
    document.getElementById('display').value = displayValue;
}

function safeEval(expr) {
    return Function('"use strict";return (' + expr + ')')();
}

// Permitir entrada desde el teclado
document.addEventListener('keydown', function (event) {
    const key = event.key;
    if (/[0-9\/\*\-\+\.\=]/.test(key)) {
        event.preventDefault();
        if (key === '=' || key === 'Enter') {
            calculate();
        } else {
            appendToDisplay(key);
        }
    }
});
