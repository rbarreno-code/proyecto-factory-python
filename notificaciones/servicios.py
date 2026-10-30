from .base import Notificacion

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[EMAIL] Enviando mensaje: {mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[SMS] Enviando mensaje: {mensaje}")

class NotificacionTelegram(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[TELEGRAM] Enviando mensaje: {mensaje}")

class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[WHATSAPP] Enviando mensaje: {mensaje}")