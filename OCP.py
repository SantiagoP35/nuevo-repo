# ============================================================
# 🟡 2. O — Open/Closed Principle (Abierto/Cerrado)
# ------------------------------------------------------------
# El código debe estar ABIERTO para extensión (nuevas funciones)
# pero CERRADO para modificación (no tocar código existente).

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f'Enviado mensaje por EMAIL a {self.usuario.email}')
        
class NotificadorSMS(Notificador):
    def Notificador(self):
        print(f'Enviado SMS a {self.usuario.sms}')
        
class NotificadorWhatsApp(Notificador):
    def Notificador(self):
        print(f'Enviado por wasap {self.usuario.whatsapp}')
        
class NotificadorTwiter(Notificador):
    def Notificador(self):
        print(f'Enviado por twiter {self.usuario.twiter}')