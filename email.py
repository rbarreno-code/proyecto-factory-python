from .base import Notificacion

class EmailNotification(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")
