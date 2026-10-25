from notificaciones.factory import NotificacionFactory

def main():
    servicio = NotificacionFactory.crear_notificacion("email")
    servicio.enviar("¡Hola! Tu código ha sido desplegado exitosamente.")

if __name__ == "__main__":
    main()
