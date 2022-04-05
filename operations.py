from cryptography.hazmat.primitives import hashes
from base64 import b64encode
class Operations:

    def b64encode(self, msg:str)->str:
        return b64encode(msg.encode("utf-8")).decode("utf-8")

    def sha256(self, msg:str)->str:
        digest = hashes.Hash(hashes.SHA256())
        digest.update(msg.encode("utf-8"))
        return digest.finalize().hex()