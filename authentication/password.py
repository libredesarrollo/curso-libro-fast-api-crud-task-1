
import bcrypt
import secrets


def get_password_hash(password: str) -> str:
    # Convertimos la contraseña a bytes
    pwd_bytes = password.encode('utf-8')
    # Generamos el salt y el hash
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # Retornamos como string para guardar en la BD
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_enc)

def generate_token() -> str:
    return secrets.token_urlsafe(32)