const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('frontend')); // Servir archivos estáticos desde el frontend

// Rutas del API
app.post('/api/calculate', (req, res) => {
    const expression = req.body.expression;
    try {
        const result = safeEval(expression);
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: 'Error evaluating expression' });
    }
});

app.listen(port, () => {
    console.log(`Backend server listening at http://localhost:${port}`);
});

function safeEval(expr) {
    return Function('"use strict";return (' + expr + ')')();
}
