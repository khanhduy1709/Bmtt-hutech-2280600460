from flask import Flask, render_template, request, json
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text} <br/> Key: {key} <br/> encrypted_text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text} <br/> key: {key} <br/>decrypted text: {decrypted_text}"

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['plain_text']
    key = request.form['key']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> encrypted_text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['cipher_text']
    key = request.form['key']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> decrypted_text: {decrypted_text}"

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form['plain_text']
    key = request.form['key']
    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, playfair_matrix)
    return f"text: {text} <br/> Key: {key} <br/> encrypted_text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form['cipher_text']
    key = request.form['key']
    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, playfair_matrix)
    return f"text: {text} <br/> Key: {key} <br/> decrypted_text: {decrypted_text}"

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form['plain_text']
    key = int(request.form['key'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> encrypted_text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['cipher_text']
    key = int(request.form['key'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text} <br/> Key: {key} <br/> decrypted_text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)