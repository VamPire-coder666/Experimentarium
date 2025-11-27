from typing import overload

# Константы МКТ:
R = 8.31 # - универсальная газовая постоянная
k = 1.38 * 10 ** -23 # - постоянная Больцмана
Na = 6.022 * 10 ** 23 # - число Авагадро


class Ideal_Gas:
    """ Основной класс идеальных газов для экспериментов типа МКТ """
    
    def __init__(self, Mr: float, name: str):
        """ Инициализация

        Args:
            Mr (float): молекулярная масса в-ва
            name (str): название в-ва
        """
        
        self._Mr = Mr
        self._M = Mr / 1000
        self._mo = 1.66 * 10 ** -27 * Mr
        self._name = name
    
    def get_mo(self) -> float:
        """ Функция возвращает массу одно молекулы

        Returns:
            float: масса одной молекулы в-ва, в кг
        """
        
        return self._mo
    
    def get_M(self) -> float:
        """ Функция возвращает молярную массу в-ва

        Returns:
            float: молярная масса в-ва, в кг / моль
        """
        
        return self._M
    
    def get_name(self) -> str:
        """ Функция взвразает название в-ва

        Returns:
            str: название газа
        """
        
        return self._name
    
    def get_Mr(self) -> int:
        """ Функция возвращает молекулярную массу в-ва

        Returns:
            float: молекулярная масса в-ва
        """
        
        return self._Mr
    
    def get_avgV(self, T: float) -> float:
        """ Функция возвращает среднюю квадратичную скорость молекул в газе

        Формула: avg_V = √(3 * R * T / M)
        R = 8.31 - универсальная газовая постоянная

        Args:
            T (float): температура, в Кельвинах

        Returns:
            float: средняя квадратичная скорость молекул, м/с
        """
        
        return (3 * R * T / self._M) ** 0.5

    @overload
    def get_P(self, n: float, T: float, mode='nT') -> float:
        """ Функция для получения давления газа на стенки сосуда
        по концентрации и температуре
        
        Формула: P = n * k * T - одно из трёх основных уравнений МКТ
        
        k = 1.38 * 10 ** -23 - постоянная Больцмана

        Args:
            n (float): концентрация в-ва (количество молекул делить объём)
            T (float): температура, в Кельвинах

        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях
        """
        
        ...
    
    @overload
    def get_P(self, V: float, T: float, mode='VT') -> float:
        """ Функция для получения давления газа на стенки сосуда
        по концентрации и температуре
        
        При условии: m = const!
        
        Формула: P = T / V - из уравнения Менделеева-Клопейрона

        Args:
            V (float): объём газа, в метрах кубических
            T (float): температура, в Кельвинах

        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях
        """
        
        ...
    
    def get_P(self, input1_: float, input2_: float, mode: str) -> float:
        if mode == 'VT':
            return input2_ / input1_
        elif mode == 'nT':
            return input1_ * k * input2_