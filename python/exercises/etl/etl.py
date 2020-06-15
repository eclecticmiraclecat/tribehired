from collections import defaultdict

def transform(old):
    char_to_points = defaultdict(int)
    try:
        for points, letters in old.items():
            for letter in letters:
                char_to_points[letter.lower()] = points
        return char_to_points
    except AttributeError:
        raise Exception("Arguments must dictionary type")
    except TypeError:
        raise Exception("Letters must be iterable type")