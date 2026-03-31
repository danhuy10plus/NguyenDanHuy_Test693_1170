import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        # Tạo key cột
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(self, text, key):
        # Tính số cột và hàng cần thiết
        num_cols = math.ceil(len(text) / key)
        num_rows = key
        num_shaded_boxes = (num_cols * num_rows) - len(text)
        
        # Tạo danh sách các hàng (mỗi hàng tương ứng với 1 chuỗi trong ciphertext ban đầu)
        plaintext = [''] * num_cols
        col = 0
        row = 0
        
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            
            # Nếu đi hết số cột hoặc chạm vào ô trống (shaded boxes) ở hàng cuối
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        return ''.join(plaintext)