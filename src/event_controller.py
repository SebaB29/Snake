from graphics.gamelib import EventType, wait
from src.constant import PAUSE, BUTTON_SIDES

class EventController:    
    def handle_key_events(self, events, game):
        """
        Maneja los eventos de teclado y pausa.
        """
        for event in events:
            if event.type == EventType.KeyPress:
                event.key = event.key.upper()
                game.set_move(event.key)

                # Maneja la pausa
                if event.key == PAUSE:
                    wait(EventType.KeyPress)

    def is_restart_button_pressed(self, event) -> bool:
        """
        Verifica si el botón de reinicio fue presionado.

        :param event: Evento detectado, puede ser None.
        :return: True si el botón fue presionado, False si no es un evento válido o no corresponde al botón.
        """
        if event is None:
            return False  # Si no hay evento, no se presionó el botón

        return (
            event.type == EventType.ButtonPress
            and BUTTON_SIDES["left"] <= event.x <= BUTTON_SIDES["right"]
            and BUTTON_SIDES["up"] <= event.y <= BUTTON_SIDES["down"]
        )
