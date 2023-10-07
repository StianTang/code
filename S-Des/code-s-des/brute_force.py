import threading
from sdes import encrypt

def generate_all_possible_keys():
    possible_keys = []
    for i in range(1024):
        key = format(i, '010b')
        possible_keys.append(key)
    return possible_keys

def brute_force_crack_part(known_plaintexts, known_ciphertexts, possible_keys, start_idx, end_idx, found_keys, lock):
    for i in range(start_idx, end_idx):
        key = possible_keys[i]
        valid_key = True

        for j in range(len(known_plaintexts)):
            plaintext = known_plaintexts[j]
            ciphertext = known_ciphertexts[j]

            encrypted_text = encrypt(plaintext, key)

            if encrypted_text != ciphertext:
                valid_key = False
                break

        if valid_key:
            with lock:
                found_keys.append(key)

def brute_force_crack(known_plaintexts, known_ciphertexts, num_threads=4):
    possible_keys = generate_all_possible_keys()
    found_keys = []
    lock = threading.Lock()
    threads = []

    chunk_size = len(possible_keys) // num_threads

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else len(possible_keys)
        thread = threading.Thread(target=brute_force_crack_part,
                                  args=(known_plaintexts, known_ciphertexts, possible_keys, start_idx, end_idx, found_keys, lock))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return found_keys


