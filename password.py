import secrets


def create_new_password(lenght, characters):
    return "".join(secrets.choice(characters) for _ in range(lenght))

