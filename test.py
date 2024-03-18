from password_generator import Password

def test_password():
    password = Password(20)
    print(type(password))
    assert len(password)  >= 20
    print(password)

if __name__ == "__main__":
    test_password()
    print("Everything Passed")