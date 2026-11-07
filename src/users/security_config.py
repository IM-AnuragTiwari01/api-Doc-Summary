from pwdlib import PasswordHash
from pwdlib.exceptions import PwdlibError

password_hash = PasswordHash.recommended()

def get_password(password: str) -> str:
    try:
        return password_hash.hash(password)
    except PwdlibError as e:
        # /catches error specific to pwdlib config or hashing failure
        print(f"Hashing error occured: {e}")
        raise
    except TypeError as e:
        # Catches errors if the password is not a string/bytes
        print(f"Invalid input type: {e}")
        raise
    
def verify_password(plain_password, hash_password):
    return password_hash.verify(plain_password, hash_password)
