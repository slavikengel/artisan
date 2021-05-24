import os
from artisan.exceptions.exceptions import FileAlreadyExist


def generate_file(path: str, file: str, body: str = ""):
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(path + "/" + file):
        raise FileAlreadyExist(f"File {file} already exist!")

    with open(os.path.join(path, file), "w") as f:
        f.write(body)

