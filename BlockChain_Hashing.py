# Define Static Functions that help Hashing Blockchain Blocks

import hashlib
import json


# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption,
# then translate the Unicode into a hexidecimal string.
def custom_hash(block):
    string_object = json.dumps(block, sort_keys=True)
    block_string = string_object.encode()

    raw_hash = hashlib.sha256(block_string)
    hex_hash = raw_hash.hexdigest()

    return hex_hash
