import unittest

from converter import Converter


class TestConverterDo(unittest.TestCase):
    """Тесты для Converter.do(x)."""

    # ---------- 1. Ветка x >= 100.7 -> 1000 ----------

    def test_upper_range_boundary_100_7(self):
        """Граница [100.7; +∞): ровно 100.7 -> 1000."""
        self.assertEqual(Converter.do(100.7), 1000)

    def test_upper_range_just_above_boundary(self):
        """Чуть больше границы: 100.8 -> 1000."""
        self.assertEqual(Converter.do(100.8), 1000)

    def test_upper_range_large_value(self):
        """Большое значение: 1000.0 -> 1000."""
        self.assertEqual(Converter.do(1000.0), 1000)

    def test_upper_range_very_large_value(self):
        """Очень большое значение: 1_000_000.0 -> 1000."""
        self.assertEqual(Converter.do(1_000_000.0), 1000)

    # ---------- 2. Ветка (0; 100.7) -> int(x) ----------

    def test_positive_range_just_above_zero(self):
        """Минимум интервала: 0.1 -> 0 (int(0.1) == 0)."""
        self.assertEqual(Converter.do(0.1), 0)

    def test_positive_range_typical_value_65_7(self):
        """Пример из задания: 65.7 -> 65."""
        self.assertEqual(Converter.do(65.7), 65)

    def test_positive_range_integer_value(self):
        """Целое значение в интервале: 50.0 -> 50."""
        self.assertEqual(Converter.do(50.0), 50)

    def test_positive_range_just_below_boundary(self):
        """Максимум интервала: 100.6 -> 100."""
        self.assertEqual(Converter.do(100.6), 100)

    def test_positive_range_value_close_to_one(self):
        """Значение чуть больше 1: 1.9 -> 1."""
        self.assertEqual(Converter.do(1.9), 1)

    # ---------- 3. Ветка x == 0.0 -> ValueError ----------

    def test_zero_raises_value_error(self):
        """x == 0.0 должен бросать ValueError."""
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    def test_zero_raises_value_error_message(self):
        """Проверяем, что тип исключения — именно ValueError."""
        with self.assertRaises(ValueError) as ctx:
            Converter.do(0.0)
        # При необходимости можно проверить текст сообщения:
        self.assertIn("0.0", str(ctx.exception))

    # ---------- 4. Ветка [-30.4; 0) -> int(x) - 5 ----------

    def test_negative_range_boundary_minus_30_4(self):
        """Граница [-30.4; 0): -30.4 -> int(-30.4) - 5 = -30 - 5 = -35."""
        self.assertEqual(Converter.do(-30.4), -35)

    def test_negative_range_just_above_boundary(self):
        """Чуть правее границы: -30.3 -> int(-30.3) - 5 = -30 - 5 = -35."""
        self.assertEqual(Converter.do(-30.3), -35)

    def test_negative_range_typical_value_minus_10_5(self):
        """Типичное значение: -10.5 -> int(-10.5) - 5 = -10 - 5 = -15."""
        self.assertEqual(Converter.do(-10.5), -15)

    def test_negative_range_just_below_zero(self):
        """Минимум по модулю: -0.1 -> int(-0.1) - 5 = 0 - 5 = -5."""
        self.assertEqual(Converter.do(-0.1), -5)

    def test_negative_range_integer_value(self):
        """Целое значение: -20.0 -> int(-20.0) - 5 = -20 - 5 = -25."""
        self.assertEqual(Converter.do(-20.0), -25)

    def test_negative_range_example_minus_5_0(self):
        """-5.0 -> int(-5.0) - 5 = -5 - 5 = -10."""
        self.assertEqual(Converter.do(-5.0), -10)

    # ---------- 5. Ветка (-∞; -30.5] -> -2000 ----------

    def test_lower_range_boundary_minus_30_5(self):
        """Граница (-∞; -30.5]: ровно -30.5 -> -2000."""
        self.assertEqual(Converter.do(-30.5), -2000)

    def test_lower_range_just_below_boundary(self):
        """Чуть левее границы: -30.6 -> -2000."""
        self.assertEqual(Converter.do(-30.6), -2000)

    def test_lower_range_example_minus_94_5(self):
        """Пример из задания: -94.5 -> -2000."""
        self.assertEqual(Converter.do(-94.5), -2000)

    def test_lower_range_large_negative(self):
        """Большое по модулю: -1000.0 -> -2000."""
        self.assertEqual(Converter.do(-1000.0), -2000)

    # ---------- 6. Проверка возвращаемого типа ----------

    def test_return_type_is_int_all_branches(self):
        """Метод всегда должен возвращать int (не bool, не float)."""
        for value in (100.7, 65.7, -10.5, -30.5, -94.5):
            with self.subTest(value=value):
                result = Converter.do(value)
                self.assertIsInstance(result, int)
                self.assertNotIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main() #лл