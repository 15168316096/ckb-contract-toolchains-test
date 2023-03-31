import random
import string


def generate_random_string(length: int = 8) -> str:
    """
    生成指定长度的随机字符串，包括大小写字母和数字
    """
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
