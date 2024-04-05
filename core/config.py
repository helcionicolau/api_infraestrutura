from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "whoami"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    RSA_PRIVATE_KEY: str = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA4pfsiF6ItBQ3J...
...UqoAj2qYyyhXwQWm8p/FAWN6ew==
-----END RSA PRIVATE KEY-----
"""
    RSA_PUBLIC_KEY: str = """
-----BEGIN RSA PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0LaNh1J44p4sP00t6zI5
...qEYxkDNE0BgFAYVX9pJjbIExqM=
-----END RSA PUBLIC KEY-----
"""

settings = Settings()


