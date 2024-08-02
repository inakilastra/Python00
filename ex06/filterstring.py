import sys
from ft_filter import ft_filter

def main():
  try:
    if len(sys.argv) == 3:
      string = sys.argv[1]
      number = int(sys.argv[2])
      result = ft_filter(lambda word: len(word) > number, string.split())
      print(result)    
    else:                         # Si no se ha proporcionado el número de argumentos (3), muestra un mensaje de error.
      print("AssertionError: Only three arguments is allowed.")
  except ValueError:              # Si ocurre un ValueError, significa que el argumento (2) no se pudo convertir a un entero
      print("AssertionError: argument is not an integer")

if __name__ == "__main__":
  main()

'''
import sys
from ft_filter import ft_filter


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Exactly two arguments \
                (string and integer) are required.")

        text = sys.argv[1]
        n = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(n, int):
            raise AssertionError("Invalid argument types.")

        filtered_words = \
            list(ft_filter(lambda word: len(word) > n, text.split()))

        print(filtered_words)

    except ValueError as error:
        print("ValueError:", error)
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
'''