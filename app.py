from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)

# Установите соединение с вашим Ethereum узлом
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/xXHSCYu_RpFYYlnIzS_mzn-kNvd66YAS/getNFTs/?owner=vitalik.eth'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quests')
def quests():
    # Логика для обработки квестов
    return render_template('quests.html')

@app.route('/profile')
def profile():
    # Логика для обработки профиля
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
