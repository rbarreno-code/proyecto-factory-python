from .servicios import NotificacionEmail, NotificacionSMS, NotificacionTelegram, NotificacionWhatsApp

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo: str):
        tipo = tipo.lower()
        if tipo == "email":
            return NotificacionEmail()
        elif tipo == "sms":
            return NotificacionSMS()
        elif tipo == "telegram":
            return NotificacionTelegram()
        elif tipo == "whatsapp":
            return NotificacionWhatsApp()
        else:
            raise ValueError(f"Tipo de notificación '{tipo}' no soportado.")
