
import os
import subprocess
import pickle
import hashlib


# SYCUR SECURITY TEST
# Intentionally vulnerable code — never use in production.


def unsafe_command(user_input):
    # B602: subprocess with shell=True
    return subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True,
    )


def unsafe_eval(user_input):
    # B307: unsafe eval
    return eval(user_input)


def unsafe_deserialization(data):
    # B301: unsafe pickle deserialization
    return pickle.loads(data)


def weak_password_hash(password):
    # B324: weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()


def hardcoded_password():
    # B105: hardcoded password
    password = "admin123"
    return password


def unsafe_os_command(user_input):
    # B605: shell command execution
    return os.popen(user_input).read()
