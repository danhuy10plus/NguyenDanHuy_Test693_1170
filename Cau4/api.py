from flask import Flask, request, jsonify
from cipher.ecc import ECCCipher

app = Flask(__name__)

# ECC_CIPHER_ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    """Tạo cặp khóa ECC mới"""
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    """Ký thông điệp bằng khóa bí mật (Private Key)"""
    data = request.json
    message = data['message']
    
    # Load keys và lấy private key
    keys = ecc_cipher.load_keys()
    private_key = keys["private_key"]
    
    # Thực hiện ký
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()

    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    """Xác minh chữ ký bằng khóa công khai (Public Key)"""
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    
    # Load keys và lấy public key
    keys = ecc_cipher.load_keys()
    public_key = keys["public_key"]
    
    # Chuyển signature từ hex về bytes và xác minh
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    
    return jsonify({'is_verified': is_verified})

if __name__ == '__main__':
    # Chạy server tại port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)