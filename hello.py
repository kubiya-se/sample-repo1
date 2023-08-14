def say_hello():
    print("Hello, World!")

def test_say_hello():
    assert say_hello() == "Hello, World!"

if __name__ == "__main__":
    say_hello()
