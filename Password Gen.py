

```python
import random
import string

def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters  # includes uppercase and lowercase letters
    digits = string.digits  # includes numbers 0-9
    punctuation = string.punctuation  # includes punctuation characters

    # Combine the characters into one string
    characters = letters + digits + punctuation

    # Generate the password
    password = "".join(random.choice(characters) for i in range(length))

    return password

# Test the function with a length of 10
password = generate_password(10)
print(password)
```

