from flask import Flask
import json

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

@app.route('/prime_number/<int:number>')
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return json.dumps(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)