from csv import reader

class ObstacleLoader:
    def __init__(self, file_path: str):
        """
        Inicializa la clase con la ruta del archivo de obstáculos.
        
        :param file_path: Ruta al archivo que contiene los datos de obstáculos.
        """
        self.file_path = file_path

    def load_obstacles(self) -> dict:
        """
        Lee el archivo y devuelve un diccionario con los obstáculos.

        :return: Diccionario donde las claves son índices y los valores son listas de coordenadas.
        :raises FileNotFoundError: Si el archivo no existe.
        :raises Exception: Si ocurre un error inesperado al leer el archivo.
        """
        obstacles = {}
        try:
            with open(self.file_path) as file:
                csv_reader = reader(file, delimiter=" ")
                for i, coordinate_group in enumerate(csv_reader):
                    obstacles[i] = [
                        tuple(map(int, coords.split(','))) for coords in coordinate_group[0].split(';')
                    ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: El archivo {self.file_path} no fue encontrado.")
        except Exception as e:
            raise Exception(f"Error al leer el archivo de obstáculos: {e}")
        
        return obstacles
