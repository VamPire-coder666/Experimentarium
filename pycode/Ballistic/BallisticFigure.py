from math import sin, radians, cos


class BallisticFigure:
    def __init__(self, mass: int, speed: int, corner: int, color: str):
        self.mass = mass
        self.v = speed
        self.corner = corner
        self.rcorner = radians(corner)
        self.color = color
    
    def rgb(self) -> tuple[int]:
        """ Функция для получения цвета тела в формате rgb

        Returns:
            tuple[int]: цвет тела в формате rgb
        """
        
        color = self.color
        return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16))
    
    def length(self, g: float) -> float:
        """ Функция для получения длины полёта тела

        Args:
            g (float): ускорение свободного падения

        Returns:
            float: длиня полёта тела
        """
        
        return (self.v ** 2 * sin(radians(2 * self.corner))) / g
    
    def main_time(self, g: float) -> float:
        """ Функция возвращает время полёта тела

        Args:
            g (float): ускорения свободного падения

        Returns:
            float: время полёта тела
        """
        
        return (2 * self.v * sin(self.rcorner)) / g
    
    def max_high(self, g: float) -> float:
        """ Функция для получения максимальной высоты полёта

        Args:
            g (float): ускорение свободного падения

        Returns:
            float: максимальная высота, на которую поднимется тело
        """
        
        t = self.main_time(g)
        return (self.v * sin(self.rcorner) * t / 2) - (g * t ** 2 / 8)
    
    def get_coord(self, g: float, t: float) -> tuple:
        """ Функция для получения координаты тела от времени

        Args:
            g (float): ускорение свободного падения
            t (float): время

        Returns:
            tuple: координата (x, y) в момент времени t
        """
        
        x = self.v * cos(self.rcorner) * t
        y = (self.v * sin(self.rcorner) * t) - (g * t ** 2 / 2)
        return x, y
    
    def get_y(self, x: float, g: float) -> float:
        """ Функция для получения координаты y

        Args:
            x (float): координата x
            g (float): ускорение свободного падения

        Returns:
            float: координата y(x)
        """
        
        t = x / (self.v * cos(self.rcorner))
        return (self.v * sin(self.rcorner) * t) - (g * t ** 2 / 2)