import os
import time

import modules.cryptography
from modules.normalize_path_name import normalize_path_name


def test_decryption_key(key_input, possible_key):

    time.sleep(2)   # to harden brute-force attacks

    main_dir = os.path.expanduser('~')
    message = 'System configuration file'

    file_path = normalize_path_name(main_dir, 'system_config.txt')

    with open(file_path, 'w+') as new_file:
        new_file.write(message)

    modules.cryptography.encrypt(key_input['key'], file_path)

    modules.cryptography.decrypt(possible_key, file_path + '.encrypted')

    with open(file_path, encoding='latin-1') as decrypted_file:
        read = decrypted_file.read()

        if read != message:
            return False
        else:
            return True


if __name__ == '__main__':
    # create_file()
    pass
