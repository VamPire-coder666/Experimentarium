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
    
    @overload
    def get_P(self, n: float, T: float) -> float:
        """ Функция для получения давления газа на стенки сосуда
        по концентрации и температуре
        
        Формула: P = nkT - одно из трёх основных уравнений МКТ
        
        k = 1.38 * 10 ** -23 - постоянная Больцмана

        Args:
            n (float): концентрация в-ва (количество молекул делить объём)
            T (float): температура, в Кельвинах

        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях
        """
        
        return n * k * T
    
    @overload
    def get_P(
        self,
        n: float,
        avr_v: float
        ) -> float:
        """ Функция для получения давления газа на стенки сосуда
        по концентрации и средней квадратичной скорости
        
        Формула: P = 1 / 3 * mo * n * avr_v ** 2 - одно из трёх основных уравнений МКТ

        Args:
            n (float): концентрация в-ва (количество молекул делить объём)
            avr_v (float): средняя квадратичная скорость молекул, в м/с

        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях
        """
        
        return 1 / 3 * self._mo * n * avr_v ** 2
    
    @overload
    def get_P(self, n: float, Ek: float) -> float:
        """ Функция для получения давления газа на стенки сосуда
        по концентрации и средней кинетической энергии молекул
        
        Формула: P = 2 / 3 * n * Ek - одно из трёх основных уравнений МКТ

        Args:
            n (float): концентрация в-ва (количество молекул делить объём)
            Ek (float): средняя кинетическая энергия молекул, в Джоулях

        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях
        """
        
        return 2 / 3 * n * Ek
    
    @overload
    def get_P(
        self,
        m: float,
        T: float,
        V: float
        ) -> float:
        """ Функция для получения давления газа на стенки сосуда
        по массе, температуре и объёму
        
        Формула: P = (m * R * T) / (V * M) - из уравнения Менделеева
        
        R = 8.31 - универсальная газовая постоянная

        Args:
            m (float): масса газа, в кг
            T (float): температура, в Кельвинах
            V (float): объём, в метрах кубических
        
        Returns:
            float: P - давление газа на стенки сосуда, в Паскалях 
        """
        
        return (m * R * T) / (V * self._M)
    
    @overload
    def get_N(self, mode='m', m: float = 0) -> float:
        """ Функция возвращает число молекул в одном моль в-ва
        по массе в-ва
        
        Формула: N = m / M * Na
        
        Na = 6.022 * 10 ** 23 - число Авагадро

        Args:
            m (float): масса в-ва, в кг

        Returns:
            float: число молекул в одном моль в-ва
        """
        ...
    
    @overload
    def get_N(self, mode='pV', p: float = 0, V: float = 0) -> float:
        """ Функция возвращает число молекул в одном моль в-ва
        по объёму и плотности
        
        Формула: N = p * V / M * Na
        
        Na = 6.022 * 10 ** 23 - число Авагадро

        Args:
            p (float): плотность в-ва, в кг / метр кубический
            V (float): плотность в-ва, в метрах кубических

        Returns:
            float: число молекул в одном моль в-ва
        """
        ...
    
    
    def get_N(self, mode: str, input1_: float, input2_: float | None) -> float:
        if mode == 'm':
            return input1_ / self._M * Na
        elif mode == 'pV':
            return input1_ * input2_ / self._M * Na
    
    @overload
    def get_v(self, mode='N', N: float = 0) -> float:
        """ Функция возвращает количество в-ва в моль
        по количеству молекул
        
        Формула: v = N / Na
        
        Na = 6.022 * 10 ** 23 - число Авагадро

        Args:
            N (float): количество молекул в-ва

        Returns:
            float: количество в-ва, в моль
        """
        ...
    
    @overload
    def get_v(self, mode='m', m: float = 0) -> float:
        """ Функция возвращает количество в-ва в моль
        по его массе
        
        Формула: v = m / M

        Args:
            m (float): масса в-ва, в кг

        Returns:
            float: количество в-ва, в моль
        """
        ...
    
    def get_v(self, mode: str, input_: float):
        if mode == 'N':
            return input_ / Na
        elif mode == 'm':
            return input_ / self._M


gas = Ideal_Gas(32, 'O2')
print(gas.get_N('m', 20))