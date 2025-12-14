import time
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
       Декоратор, который пишет сообщения о работе функции.

       Если файл не указан, выводит текст в консоль.
       Если файл указан, записывает текст в этот файл.

       Логирует:
       - что функция вызвана и с какими аргументами
       - что функция вернула результат
       - если была ошибка, пишет её текст
       """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            current_time = time.strftime("%Y%m%d-%H%M%S")

            message = f'{current_time}: функция "{func_name}" вызвана с аргументами: args={args}, kwargs={kwargs}'
            if filename is None:
                print(message)
            else:
                with open(filename, 'a', encoding="utf-8") as f:
                    f.write(message)
            try:
                result = func(*args, **kwargs)
                message = f'{current_time}: функция "{func_name}" завершилась {result}'

                if filename is None:
                    print(message)
                else:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(message + '\n')
                return result
            except Exception as e:
                message = f'{current_time}: функция "{func_name}" вызвала ошибку {type(e).__name__}: {str(e)}'

                if filename is None:
                    print(message)
                else:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(message)
                raise

        return wrapper

    return decorator
