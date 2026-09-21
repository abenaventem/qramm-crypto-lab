import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
def hash_user_password(password: str) -> str:
    # VULNERABLE: Broken hash function
    return hashlib.md5(password.encode()).hexdigest()
def generate_legacy_keypair():
    # VULNERABLE TO QUANTUM: RSA-2048 key generation
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key
def encrypt_sensitive_payload(data: bytes, key: bytes):
    # TRANSITIONAL/SAFE: AES-256 GCM
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext, cipher.nonce, tag
def experimental_pqc_kem():
    # POST-QUANTUM SAFE: Reference implementation for ML-KEM-768
    print("Initializing ML-KEM-768 post-quantum key encapsulation...")
