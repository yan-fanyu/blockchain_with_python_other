import hashlib as hl  # creating an alias to an import and then in the code we should use the alias
import json

# __all_ = ['hash_string_256', 'hash_block']

def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Hashes a block and returns a string representation of it.

        Arguments:
            :block: The block that should be hashed.
    """
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
