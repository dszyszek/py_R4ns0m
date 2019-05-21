from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
import os
import ntpath


def encrypt(key, file_path):
    filename = ntpath.basename(file_path)
    new_name = filename + '.encrypted'

    chunk_size = 16*1024
    file_size_info = str(os.path.getsize(file_path)).zfill(16)

    iv = Random.new().read(AES.block_size)
    encipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as input_file:
        new_file_path = os.path.join(os.path.dirname(file_path), new_name) # set up new .encrypted file path

        with open(new_file_path, 'wb') as output_file:
            output_file.write(file_size_info.encode('utf-8'))
            output_file.write(iv)
            while True:
                r = input_file.read(chunk_size)

                if len(r) == 0:
                    break
                elif len(r) % 16 != 0:
                    r += b' ' * (16 - (len(r) % 16))

                encrypted = encipher.encrypt(r)
                output_file.write(encrypted)

    os.remove(file_path)


def decrypt(key_in, file_path):
    key = normalize_key(key_in)

    filename = ntpath.basename(file_path)

    restored_name = filename[:-10]
    chunk_size = 16*1024

    with open(file_path, 'rb') as input_file:
        restored_file_path = os.path.join(os.path.dirname(file_path), restored_name) # set up restored file path
        file_size_info = int(input_file.read(16))
        iv = input_file.read(16)

        decipher = AES.new(key, AES.MODE_CBC, iv)

        with open(restored_file_path, 'wb') as output_file:

            while True:
                r = input_file.read(chunk_size)

                if len(r) == 0:
                    break

                decrypted = decipher.decrypt(r)
                output_file.write(decrypted)

            output_file.truncate(file_size_info)

    os.remove(file_path)


def generate_key(passwd):
    sha = SHA256.new(passwd.encode('utf-8'))
    return sha.digest()


if __name__ == '__main__':
    pass