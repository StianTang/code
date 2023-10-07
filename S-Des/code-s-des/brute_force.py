import threading  # 导入多线程模块
from sdes import encrypt  # 导入S-DES加密函数

def generate_all_possible_keys():
    # 生成所有可能的密钥，共1024个
    possible_keys = []
    for i in range(1024):
        key = format(i, '010b')  # 将整数i转换为10位的二进制字符串
        possible_keys.append(key)
    return possible_keys

def brute_force_crack_part(known_plaintexts, known_ciphertexts, possible_keys, start_idx, end_idx, found_keys, lock):
    # 部分暴力破解函数，用于处理密钥范围的一部分
    for i in range(start_idx, end_idx):
        key = possible_keys[i]  # 从可能的密钥中获取当前密钥
        valid_key = True

        for j in range(len(known_plaintexts)):
            plaintext = known_plaintexts[j]  # 已知明文
            ciphertext = known_ciphertexts[j]  # 已知密文

            encrypted_text = encrypt(plaintext, key)  # 使用当前密钥加密明文

            if encrypted_text != ciphertext:
                valid_key = False
                break

        if valid_key:
            with lock:
                found_keys.append(key)  # 如果当前密钥有效，则将其添加到找到的密钥列表中

def brute_force_crack(known_plaintexts, known_ciphertexts, num_threads=4):
    # 主要的暴力破解函数，使用多线程并发处理
    possible_keys = generate_all_possible_keys()  # 生成所有可能的密钥
    found_keys = []  # 存储找到的有效密钥的列表
    lock = threading.Lock()  # 创建一个线程锁以确保安全的共享数据
    threads = []

    chunk_size = len(possible_keys) // num_threads  # 计算每个线程应处理的密钥范围大小

    for i in range(num_threads):
        start_idx = i * chunk_size  # 计算当前线程的起始索引
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else len(possible_keys)  # 计算当前线程的结束索引
        thread = threading.Thread(target=brute_force_crack_part,
                                  args=(known_plaintexts, known_ciphertexts, possible_keys, start_idx, end_idx, found_keys, lock))
        threads.append(thread)  # 创建线程并将其添加到线程列表中

    for thread in threads:
        thread.start()  # 启动所有线程

    for thread in threads:
        thread.join()  # 等待所有线程完成

    return found_keys  # 返回找到的有效密钥列表
