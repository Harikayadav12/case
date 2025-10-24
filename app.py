from flask import Flask, render_template, request

app = Flask(__name__)

# Static conversion rates (1 INR = ?)
conversion_rates = {
    "USD": 0.012,
    "EUR": 0.011,
    "JPY": 1.80,
    "GBP": 0.0095,
    "AUD": 0.018
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount_inr = float(request.form['amount'])
    currency = request.form['currency']

    converted_amount = amount_inr * conversion_rates.get(currency, 0)
    return render_template('result.html', amount=amount_inr, currency=currency, converted=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
