P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
LSHIFT1 = [2, 3, 4, 5, 1]
LSHIFT2 = [3, 4, 5, 1, 2]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP1 = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
S1 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
S2 = [[0, 1, 2, 3], [2, 3, 1, 0], [3, 0, 1, 2], [2, 1, 0, 3]]
SP = [2, 4, 3, 1]


def p10_permutation(key):
    # 执行 P10 置换
    result = ""
    for x in P10:
        result += key[x - 1]
    return result


def generate_subkey_k1(key):
    # 生成 K1 密钥
    key1 = key[:5]
    key2 = key[5:]
    key1 = key1[1:] + key1[0]
    key2 = key2[1:] + key2[0]
    k = key1 + key2
    k1 = ""
    for x in P8:
        k1 += k[x - 1]
    return k1


def generate_subkey_k2(key):
    # 生成 K2 密钥
    key1 = key[:5]
    key2 = key[5:]
    key1 = key1[2:] + key1[:2]
    key2 = key2[2:] + key2[:2]
    k = key1 + key2
    k2 = ""
    for x in P8:
        k2 += k[x - 1]
    return k2


def initial_permutation(plaintext):
    # 执行 IP 置换
    result = ""
    for x in IP:
        result += plaintext[x - 1]
    return result


def inverse_initial_permutation(ciphertext):
    # 执行 IP1 置换
    result = ""
    for x in IP1:
        result += ciphertext[x - 1]
    return result


def fk_function(p, subkey):
    # 执行 Feistel 函数 FK()
    left_half, right_half = p[:4], p[4:]
    expanded_right_half = ""
    for x in EP:
        expanded_right_half += right_half[x - 1]
    subkey_result = generate_subkey_k1(p10_permutation(subkey))
    xor_result = xor(expanded_right_half, subkey_result)
    t1, t2, t3, t4 = xor_result[0] + xor_result[3], xor_result[1:3], xor_result[4] + xor_result[7], xor_result[5:7]
    int1, int2, int3, int4 = binary_to_decimal(t1), binary_to_decimal(t2), binary_to_decimal(t3), binary_to_decimal(t4)
    s1, s2 = S1[int1][int2], S2[int3][int4]
    s1, s2 = decimal_to_binary(s1), decimal_to_binary(s2)
    s_result = s1 + s2
    s_result = straight_permutation(s_result)
    left_half_result = xor(s_result, left_half)
    return left_half_result


def swap(left, right):
    # 交换左右半部分
    return right + left


def fk_function_k2(p, subkey):
    # 执行 Feistel 函数 FK()，用于 K2 密钥
    left_half, right_half = p[:4], p[4:]
    expanded_right_half = ""
    for x in EP:
        expanded_right_half += right_half[x - 1]
    subkey_result = generate_subkey_k2(p10_permutation(subkey))
    xor_result = xor(expanded_right_half, subkey_result)
    t1, t2, t3, t4 = xor_result[0] + xor_result[3], xor_result[1:3], xor_result[4] + xor_result[7], xor_result[5:7]
    int1, int2, int3, int4 = binary_to_decimal(t1), binary_to_decimal(t2), binary_to_decimal(t3), binary_to_decimal(t4)
    s1, s2 = S1[int1][int2], S2[int3][int4]
    s1, s2 = decimal_to_binary(s1), decimal_to_binary(s2)
    s_result = s1 + s2
    s_result = straight_permutation(s_result)
    left_half_result = xor(s_result, left_half)
    return left_half_result


def binary_to_decimal(binary_str):
    # 二进制转十进制
    decimal = 0
    for i, bit in enumerate(binary_str[::-1]):
        decimal += int(bit) * (2 ** i)
    return decimal


def decimal_to_binary(decimal):
    # 十进制转二进制
    binary = bin(decimal)[2:].zfill(2)
    return binary


def straight_permutation(binary_str):
    # 执行 SP 置换
    result = ""
    for x in SP:
        result += binary_str[x - 1]
    return result


def xor(binary1, binary2):
    # 执行异或操作
    result = ""
    for b1, b2 in zip(binary1, binary2):
        if b1 == b2:
            result += "0"
        else:
            result += "1"
    return result


def encrypt(plaintext, key):
    p = initial_permutation(plaintext)
    k1 = fk_function(p, key)
    q = swap(k1, p[4:])
    k2 = fk_function_k2(q, key)
    q = inverse_initial_permutation(k2 + k1)
    return q


def decrypt(ciphertext, key):
    p = initial_permutation(ciphertext)
    k1 = fk_function_k2(p, key)
    q = swap(k1, p[4:])
    k2 = fk_function(q, key)
    q = inverse_initial_permutation(k2 + k1)
    return q

