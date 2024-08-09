from cryptography.fernet import Fernet

chave_secreta = Fernet.generate_key()
fernet = Fernet(chave_secreta)

def criptografar(senha):
    return fernet.encrypt(senha.encode()).decode()

def descriptografar(senha_criptografada):
    return fernet.descrypt(senha_criptografada.encode()).decode()

senha_original = 'MinhaSenha'
senha_criptografada = criptografar(senha_original)
senha_descriptografa = descriptografar(senha_criptografada)

print(f'Senha Original: {senha_original}')
print(f'Senha Criptografada: {senha_criptografada}')
print(f'Senha Descriptografada: {senha_descriptografa}')