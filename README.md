# Password Manager using Fernet Encryption

This Python script implements a simple password manager using Fernet encryption, a symmetric encryption algorithm provided by the `cryptography` library.
Find detailed explanation from my blog post, by clicking [here](https://azarmamiyev.me/projects/password_manager/).

## Features

- **Generate and Load Master Key**: The script allows the user to either generate or load a master key for encryption and decryption of passwords.
- **Add Passwords**: Users can add passwords for different accounts along with their respective site names and usernames.
- **View Passwords**: Users can view the stored passwords along with their corresponding site names and usernames.

## Usage

1. Clone the repository or download the script files.
2. Install the required dependencies using `pip install cryptography`.
3. Run the script using Python.
4. Follow the prompts to generate or load the master key and perform operations such as adding or viewing passwords.

## Operations

### 1. Generate or Load Master Key

- If it's the first run, the script prompts the user to generate a master key.
- Otherwise, it loads the master key from the `key.key` file.

### 2. Add Password

- Users can add passwords by providing the site name, account name (username/email), and password.
- The provided information is encrypted using Fernet encryption and stored in the `vault.txt` file.

### 3. View Password

- Users can view the stored passwords along with their corresponding site names and usernames.
- The stored information is decrypted and displayed to the user.

## Implementation Details

- The script utilizes the `cryptography.fernet` module for symmetric encryption and decryption.
- Passwords are stored in a plaintext file (`vault.txt`) using "|" as a delimiter.
- The master key is stored in the `key.key` file.

## Example Output

- See below for an example output of the script in action:

```plaintext
Welcome to password manager!
If this is your first run, we need to generate a master key. Do you want to generate it? (y/n): y
This is you main password vault (Find it on key.key file) (DO NOT LOSE IT!!!): <random generated password here>
Select the operation (add, view): add
Enter site name (Facebook, Google): Facebook
Enter account name (Username/E-mail): example@example.com
Enter password: strongpassword
Password added!

This is you main password vault (Find it on key.key file) (DO NOT LOSE IT!!!): <random generated password here>
Select the operation (add, view): 
```

## Note

This project serves as an educational resource to understand basic password management techniques using encryption in Python. It is not intended for use in production environments and should not be used to manage sensitive data.
