def validate_hello(greetings):
    if 'hello' or 'ciao' or 'salut' or 'hallo' or 'hola' or 'ahoj' or 'czesc' in greetings:
        return True


validate_hello('hello')