from itertools import cycle

from .. import Provider as BaseProvider


def rut_check_digit(number: int) -> str:
    """
    Calculate the last character of a RUT number
    :return: RUT check digit
    """

    sum = 0
    for factor in cycle(range(2, 8)):
        if number == 0:
            break
        sum += factor * (number % 10)
        number //= 10
    mod = -sum % 11
    if mod == 11:
        return "0"
    elif mod == 10:
        return "K"
    else:
        return str(mod)


class Provider(BaseProvider):
    """
    A Faker provider for the Chilean VAT IDs, also known as RUTs.

    Sources:
    https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario
    https://presslatam.cl/2018/04/el-problema-de-la-escasez-y-stock-disponible-de-los-ruts-en-chile/
    """

    rut_format = "{:,d}-{:s}"

    def person_rut(self) -> str:
        """
        :return: a random Chilean RUT between a 10 and 31.999.999 range
        """
        return self.rut(10, 31999999)

    def company_rut(self) -> str:
        """
        :return: a random Chilean RUT between 32.000.000 and 99.999.999
        """
        return self.rut(32000000, 99999999)

    def rut(self, min: int = 10, max: int = 99999999) -> str:
        """
        Generates a RUT within the specified ranges, inclusive.

        :param min: Minimum RUT to generate.
        :param max: Maximum RUT to generate.
        :return: a random Chilean RUT between 35.000.000 and 99.999.999
        """

        digits = self.random_int(min, max)
        check = rut_check_digit(digits)
        return self.rut_format.format(digits, check).replace(",", ".")
