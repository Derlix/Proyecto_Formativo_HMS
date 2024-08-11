import secrets
import string

#Función para generar un ID de usuario aleatorio
def generateuser_id(length=30):
    # Caracteres posibles para el ID aleatorio
    characters = string.ascii_letters + string.digits

    # Genera un ID aleatorio de la longitud deseada
    random_id = ''.join(secrets.choice(characters) for _ in range(length))

    return random_id