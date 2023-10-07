from sdes import encrypt
from brute_force import generate_all_possible_keys

def find_collision(input_plaintext):
    # 给定的明文分组
    plaintext = input_plaintext  # 使用传入的明文

    # 生成所有可能的10位密钥
    possible_keys = generate_all_possible_keys()

    # 存储产生相同密文的密钥
    same_ciphertext_keys = []

    # 使用第一个密钥加密明文
    first_key = possible_keys[0]
    ciphertext1 = encrypt(plaintext, first_key)

    # 遍历所有其他密钥，与第一个密钥进行比较
    for key in possible_keys[1:]:
        ciphertext2 = encrypt(plaintext, key)

        # 如果两个密钥加密得到的密文相同，则记录这两个密钥
        if ciphertext1 == ciphertext2:
            same_ciphertext_keys.append(key)

    # 返回相同密文的密钥列表和相同的密文
    return same_ciphertext_keys, ciphertext1
