from csv import reader


class ObstacleLoader:
    def __init__(self, file_path: str):
        """
        Inicializa la clase con la ruta del archivo que contiene los datos de los obstáculos.

        :param file_path: Ruta al archivo de texto con las coordenadas de los obstáculos.
        :type file_path: str
        """
        self.file_path = file_path

    def load_obstacles(self) -> dict:
        """
        Carga los obstáculos desde el archivo especificado y devuelve un diccionario con los índices
        de los obstáculos como claves y sus coordenadas como valores.

        El archivo debe tener un formato en el que cada línea contenga coordenadas separadas por punto y coma,
        y cada coordenada esté representada como un par de enteros.

        :return: Diccionario con las coordenadas de los obstáculos.
        :rtype: dict
        :raises FileNotFoundError: Si el archivo no se encuentra en la ruta especificada.
        :raises Exception: Si ocurre un error al procesar el archivo.
        """
        obstacles = {}
        try:
            with open(self.file_path) as file:
                csv_reader = reader(file, delimiter=" ")
                for i, coordinate_group in enumerate(csv_reader):
                    obstacles[i] = [
                        tuple(map(int, coords.split(",")))
                        for coords in coordinate_group[0].split(";")
                    ]
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Error: El archivo {self.file_path} no fue encontrado."
            )
        except Exception as e:
            raise Exception(f"Error al leer el archivo de obstáculos: {e}")

        return obstacles
