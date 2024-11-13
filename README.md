# Phishing Email Detection Using LSTM Model

This project implements a phishing email detection system using a Long Short-Term Memory (LSTM) neural network. The system takes raw email text as input and returns a prediction indicating whether the email is likely phishing or legitimate.

For a full detailed write-up and algorithm analysis, refer to the notebook [`phishing_email_detection.ipynb`](phishing_email_detection.ipynb).

## Installation

1. **Ensure you have Python 3.7+ installed.**
2. Clone the repository and navigate to the project directory:

    ```bash
    git clone https://github.com/atishayd/LSTM-phishing-detection.git
    cd phishing-detection-project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Making Predictions

To get a prediction for a sample email, send a POST request with raw text content.

### Using Postman
- Set up a **POST** request to `http://127.0.0.1:5000/predict`.
- Go to the **Body** tab, select **raw** and **Text** from the dropdown.
- Paste the email content as plain text in the body.

The response will be a JSON object with a `"prediction"` key, showing a probability score between 0 and 1, where a higher value indicates a greater likelihood of phishing.

## Files

- `app.py`: Flask application that serves the phishing detection API, handling preprocessing, prediction, and response formatting.
- `lstm_model.keras`: Trained LSTM model file, used for making predictions on input email text.
- `tokenizer.pkl`: Serialized tokenizer file to ensure consistent text preprocessing (e.g., tokenization and padding).
- `requirements.txt`: List of required Python packages.
- `README.md`: Project description and usage instructions.

### Using `curl`

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: text/plain" --data "Your phishing email here.."

