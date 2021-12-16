n = input('Digite aqui o seu nome :').strip()
e = n.replace(" ", "")
s = n.split()
qt = len(s[0])
print(f"""
Entendi.
Então seu nome em maiúsculas é: {n.upper()};
E em letras minúsculas fica: {n.lower()};
Seu nome tem ao todo {len(e)} letras;
Seu primeiro nome tem {qt} letras.""")
