const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 5000;
const cors = require('cors');
app.use(cors());
app.get('/predict', (req, res) => {
    const inputData = req.query.data;
    if (!inputData) {
        return res.json('No input data provided' );
    }
    const inputArgs = inputData.split(',');

    // Ensure 8 inputs are provided
    if (inputArgs.length !== 8) {
        return res.json('Input data must contain 8 values.');
    }
    const pythonProcess = spawn('python', ['predict_diabetes.py', ...inputArgs]);

    pythonProcess.stdout.on('data', (data) => {
        const result = data.toString().trim();
        res.json({ result });
    });

    pythonProcess.on('exit', (code) => {
        console.log(`Python script exited with code ${code}`);
    });
});
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
}); 
