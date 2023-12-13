
from PIL import Image


class Filter:
    """
    Базовый класс для создания фильтров.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        """
        Применяет фильтр к одному пикселю.
        :param r:
        :param g:
        :param b:
        :return: Новый цвет пикселя
        """
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению.
        :param img: Исходное изображение
        :return: новое изображение
        """
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                r, g, b = img.getpixel((i, j))

                # как-либо меняем цвет
                new_pixel = self.apply_to_pixel(r, g, b)

                # сохраняем пиксель обратно
                img.putpixel((i, j), new_pixel)
        return img


class BrightFilter(Filter):
    """
    Фильтр, который делает изображение ярче.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = min(r + 80, 255)
        new_g = min(g + 80, 255)
        new_b = min(b + 80, 255)
        return new_r, new_g, new_b


class DarkFilter(Filter):
    """
    Фильтр, который делает изображение темнее.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = max(r - 80, 0)
        new_g = max(g - 80, 0)
        new_b = max(b - 80, 0)
        return new_r, new_g, new_b


class RedFilter(Filter):
    """
    Фильтр, который делает изображение краснее.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = min(r + 80, 255)
        new_g = g
        new_b = b
        return new_r, new_g, new_b


class GreenFilter(Filter):
    """
    Фильтр, который делает изображение зеленее.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = r
        new_g = min(g + 80, 255)
        new_b = b
        return new_r, new_g, new_b


class BlueFilter(Filter):
    """
    Фильтр, который делает изображение синее.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = r
        new_g = g
        new_b = min(b + 80, 255)
        return new_r, new_g, new_b


class InverseFilter(Filter):
    """
    Фильтр, который инвертирует изображение.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        return new_r, new_g, new_b
