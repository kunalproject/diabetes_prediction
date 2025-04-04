const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = process.env.PORT || 5000; // Render provides PORT env variable
const cors = require('cors');
const path = require('path');

app.use(cors());
app.use(express.json());

app.get('/predict', (req, res) => {
    const inputData = req.query.data;
    
    if (!inputData) {
        return res.status(400).json({ error: 'No input data provided' });
    }

    const inputArgs = inputData.split(',');

    if (inputArgs.length !== 8) {
        return res.status(400).json({ error: 'Input data must contain 8 values' });
    }

    // Use absolute path to Python script
    const pythonScriptPath = path.join(__dirname, 'predict_diabetes.py');
    const pythonProcess = spawn('python', [pythonScriptPath, ...inputArgs]);

    let result = '';
    let error = '';

    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        error += data.toString();
    });

    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.error(`Python script exited with code ${code}: ${error}`);
            return res.status(500).json({ error: 'Prediction failed', details: error });
        }
        res.json({ result: result.trim() });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});