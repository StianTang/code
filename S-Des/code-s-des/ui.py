import tkinter as tk
from tkinter import ttk
import brute_force
import time
import ciphertext_collisions
from sdes import encrypt, decrypt

# 声明全局变量
input_entry = None
key_entry = None
output_label = None
mode_var = None
input_type_var = None

def encrypt_decrypt():
    global input_entry, key_entry, output_label, mode_var, input_type_var
    input_text = input_entry.get()
    key = key_entry.get()
    mode = mode_var.get()
    input_type = input_type_var.get()

    if input_type == "Binary":
        input_data = input_text
    elif input_type == "ASCII":
        # Convert ASCII input to binary (1 Byte groups)
        input_data = ''.join(format(ord(char), '08b') for char in input_text)
    else:
        return  # Handle invalid input type

    if mode == "Encrypt":
        result = encrypt(input_data, key)
    else:
        result = decrypt(input_data, key)

    if input_type == "Binary":
        output_text = result
    elif input_type == "ASCII":
        # Convert binary result to ASCII characters (1 Byte groups)
        output_text = ''.join(chr(int(result[i:i+8], 2)) for i in range(0, len(result), 8))
    else:
        return  # Handle invalid input type

    output_label.config(text=f"Result: {output_text}")

def main():
    global input_entry, key_entry, output_label, mode_var, input_type_var
    window = tk.Tk()
    window.title("S-DES Encryption and Decryption")
    window.geometry("400x300")  # 设置窗口大小

    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand='yes')

    # 创建选项卡1: 加密解密
    tab_encrypt_decrypt = ttk.Frame(notebook)
    notebook.add(tab_encrypt_decrypt, text="  加密解密  ")

    input_label = tk.Label(tab_encrypt_decrypt, text="Input:")
    input_label.pack()
    input_entry = tk.Entry(tab_encrypt_decrypt)
    input_entry.pack()

    key_label = tk.Label(tab_encrypt_decrypt, text="Key:")
    key_label.pack()
    key_entry = tk.Entry(tab_encrypt_decrypt)
    key_entry.pack()

    input_type_var = tk.StringVar(value="Binary")
    input_type_label = tk.Label(tab_encrypt_decrypt, text="Input Type:")
    input_type_label.pack()
    input_type_combobox = ttk.Combobox(tab_encrypt_decrypt, textvariable=input_type_var, values=["Binary", "ASCII"])
    input_type_combobox.pack()

    mode_var = tk.StringVar(value="Encrypt")
    mode_label = tk.Label(tab_encrypt_decrypt, text="Mode:")
    mode_label.pack()
    mode_combobox = ttk.Combobox(tab_encrypt_decrypt, textvariable=mode_var, values=["Encrypt", "Decrypt"])
    mode_combobox.pack()

    process_button = tk.Button(tab_encrypt_decrypt, text="Encrypt/Decrypt", command=encrypt_decrypt)
    process_button.pack()

    output_label = tk.Label(tab_encrypt_decrypt, text="Result:")
    output_label.pack()

    # 创建选项卡2: 暴力破解
    tab_bruteforce = ttk.Frame(notebook)
    notebook.add(tab_bruteforce, text="  暴力破解  ")
    # 添加已知的明文和密文输入框
    known_text_frame = ttk.LabelFrame(tab_bruteforce, text="已知的明文和密文")
    known_text_frame.pack(padx=10, fill='both', expand='yes')

    known_plaintexts_label = tk.Label(known_text_frame, text="明文:")
    known_plaintexts_label.pack()
    known_plaintexts_entry = tk.Entry(known_text_frame, width=40)  # 设置输入框宽度为40字符，可以根据需要调整
    known_plaintexts_entry.pack()

    known_ciphertexts_label = tk.Label(known_text_frame, text="密文:")
    known_ciphertexts_label.pack()
    known_ciphertexts_entry = tk.Entry(known_text_frame, width=40)  # 设置输入框宽度为40字符，可以根据需要调整
    known_ciphertexts_entry.pack()

    # 添加线程数输入框
    threads_label = tk.Label(tab_bruteforce, text="线程数:")
    threads_label.pack()
    threads_entry = tk.Entry(tab_bruteforce)
    threads_entry.pack()

    def start_bruteforce():
        known_plaintexts = known_plaintexts_entry.get().split(',')
        known_ciphertexts = known_ciphertexts_entry.get().split(',')
        num_threads = int(threads_entry.get())

        # 记录开始时间
        start_time = time.time()

        # 执行暴力破解
        found_keys = brute_force.brute_force_crack(known_plaintexts, known_ciphertexts, num_threads)

        # 记录结束时间
        end_time = time.time()

        # 显示结果，包括时间信息
        result.config(text=f"Found keys: {', '.join(found_keys)}\nTime taken: {end_time - start_time:.5f} seconds")

    start_button = tk.Button(tab_bruteforce, text="开始暴力破解", command=start_bruteforce)
    start_button.pack()

    result= tk.Label(tab_bruteforce, text="", wraplength=300)  # 设置换行宽度为100像素，可以根据需要调整
    result.pack()

    # 创建选项卡3: 密文碰撞
    tab_collision = ttk.Frame(notebook)
    notebook.add(tab_collision, text="  密文碰撞  ")

    # 添加输入明文的文本框
    plaintext_label = tk.Label(tab_collision, text="明文:")
    plaintext_label.pack()
    plaintext_entry = tk.Entry(tab_collision, width=40)  # 设置输入框宽度，可以根据需要调整
    plaintext_entry.pack()

    # 添加按钮来触发密文碰撞算法
    def start_collision():
        plaintext = plaintext_entry.get()
        same_ciphertext_keys, ciphertext = ciphertext_collisions.find_collision(plaintext)

        if same_ciphertext_keys:
            result_text.config(text=f"Same ciphertext keys: {', '.join(same_ciphertext_keys)}\nCiphertext: {ciphertext}")
        else:
            result_text.config(text="No keys found that produce the same ciphertext.")

    start_button = tk.Button(tab_collision, text="开始密文碰撞", command=start_collision)
    start_button.pack()

    result_text = tk.Label(tab_collision, text="", wraplength=300)
    result_text.pack()

    window.mainloop()

main()
