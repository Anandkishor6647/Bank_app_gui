def pass_hash(data):
    hash_obj = hashlib.sha256(data.encode())
    hex_dig = hash_obj.hexdigest()
    return hex_dig