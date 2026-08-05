import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def main():
    name = input("Ismingizni kiriting: ")
    password = input("Parolni kiriting: ")

    hashed = hash_password(password)

    print()
    print(f"Ism: {name}")
    print(f"Parol (hash): {hashed}")


if __name__ == "__main__":
    main()