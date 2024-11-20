from graphics.gamelib import EventType

class EventController:
    def __init__(self, button_sides: dict):
        """
        Inicializa el controlador de eventos con las coordenadas del botón de reinicio.

        :param button_sides: Diccionario que define los límites del botón de reinicio.
        """
        self.button_sides = button_sides

    def is_restart_button_pressed(self, event) -> bool:
        """
        Verifica si el botón de reinicio fue presionado.

        :param event: Evento detectado, puede ser None.
        :return: True si el botón fue presionado, False si no es un evento válido o no corresponde al botón.
        """
        if event is None:
            return False

        return (
            event.type == EventType.ButtonPress
            and self.button_sides["left"] <= event.x <= self.button_sides["right"]
            and self.button_sides["up"] <= event.y <= self.button_sides["down"]
        )
