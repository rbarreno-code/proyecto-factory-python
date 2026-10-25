from .servicios import NotificacionEmail, NotificacionSMS, NotificacionTelegram

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
        else:
            raise ValueError(f"Tipo de notificación '{tipo}' no soportado.")
