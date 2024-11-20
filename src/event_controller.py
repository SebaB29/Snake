from graphics.gamelib import EventType, wait
from src.constant import PAUSE, BUTTON_SIDES
from src.game import Game


class EventController:
    """
    Controlador de eventos para manejar la entrada del usuario durante el juego.

    Esta clase se encarga de procesar eventos de teclado, incluyendo el movimiento de la serpiente y la pausa del juego,
    así como verificar si el botón de reinicio ha sido presionado.
    """

    def handle_key_events(self, events, game: Game):
        """
        Procesa los eventos de teclado, actualizando el movimiento de la serpiente o pausando el juego si es necesario.

        Este método recorre una lista de eventos y verifica si son eventos de tipo `KeyPress`. En función de la tecla presionada,
        se actualiza el movimiento de la serpiente o se activa la pausa.

        :param events: Lista de eventos detectados durante el ciclo del juego. Cada evento puede ser de distintos tipos (teclado, ratón, etc.).
        :param game: Instancia del objeto `Game` que se utiliza para actualizar el estado del juego (en particular, el movimiento de la serpiente).

        :return: None
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
        Verifica si el botón de reinicio ha sido presionado en la interfaz gráfica.

        Este método recibe un evento y comprueba si es un evento de tipo `ButtonPress` dentro de las coordenadas del botón de reinicio.
        Si el evento es válido y corresponde al área del botón, retorna `True`; de lo contrario, retorna `False`.

        :param event: El evento que se verifica, puede ser `None` si no se detectó ningún evento.
        :return: `True` si el evento corresponde al botón de reinicio, `False` si no es un evento válido o no corresponde al botón.
        """
        if event is None:
            return False

        return (
            event.type == EventType.ButtonPress
            and BUTTON_SIDES["left"] <= event.x <= BUTTON_SIDES["right"]
            and BUTTON_SIDES["up"] <= event.y <= BUTTON_SIDES["down"]
        )
