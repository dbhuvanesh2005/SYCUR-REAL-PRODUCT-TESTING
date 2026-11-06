
"""
SYCUR Security Scanner Test
WARNING: Intentionally vulnerable code.
For security scanner testing only.
Do not execute or deploy.
"""

import os
import subprocess
import pickle
import hashlib
import sqlite3


# TEST 1: Hardcoded password
DATABASE_PASSWORD = "SuperSecretPassword123!"


# TEST 2: SQL Injection
def get_user(username):
    conn = sqlite3.connect(":memory:")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchall()


# TEST 3: Command Injection
def execute_command(user_input):
    return os.system(user_input)


# TEST 4: Unsafe subprocess execution
def run_shell(command):
    return subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )


# TEST 5: Insecure deserialization
def load_user_data(payload):
    return pickle.loads(payload)


# TEST 6: Weak cryptographic hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# TEST 7: Disabled TLS certificate verification
def insecure_request(url):
    import requests
    return requests.get(url, verify=False)


# TEST 8: Unsafe dynamic code execution
def evaluate_user_code(user_input):
    return eval(user_input)


# TEST 9: Unsafe temporary file
def write_temp_data(data):
    with open("/tmp/sycur_test.txt", "w") as file:
        file.write(data)


# TEST 10: Hardcoded cryptographic key
ENCRYPTION_KEY = "hardcoded-encryption-key-123456"
