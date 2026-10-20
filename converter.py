class Converter:
    @staticmethod
    def do(x: float) -> int:
        """
        Преобразует вещественное число x в целое по заданным правилам.

        :param x: вещественное число (точность 1 знак после запятой)
        :return: целое число
        :raises ValueError: если x == 0.0
        """
        if x >= 100.7:
            return 1000
        elif x > 0:
            return int(x)
        elif x == 0.0:
            raise ValueError("x не может быть равен 0.0")
        elif x >= -30.4:
            return int(x) - 5
        else:  # x <= -30.5
            return -2000