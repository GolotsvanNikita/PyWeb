from functools import reduce

def min_strategy(data: tuple, strategies: dict) -> dict:
    res = {k: v(data) for k, v in strategies.items()}
    min_key = min(res, key=lambda k: res[k])

    return {min_key: res[min_key]}

def main() -> None:
    data = (6, 9, 2, 7, 2000, 5, 3, 8)

    strategies = \
    {
        'Arithmetic': lambda data: reduce(lambda acc, e: acc + e, data, 0) / len(data),
        'Geometric': lambda data: reduce(lambda acc, e: acc * e, data, 1) ** (1 / len(data)),
        'Harmonic': lambda data: len(data) / reduce(lambda acc, e: acc + 1.0 / e, data, 0),
        'Median': lambda data: sorted(data)[len(data) // 2] if len(data) % 2 == 1 else (sorted(data)[len(data) // 2] +
                                                                                        sorted(data)[
                                                                                            len(data) // 2 - 1]) / 2,
    }

    print(min_strategy(data, strategies))

if __name__ == '__main__':
    main()