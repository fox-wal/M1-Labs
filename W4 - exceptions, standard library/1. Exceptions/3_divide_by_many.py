def div_by_many(p: float, qs: list[float]) -> list[float]:
    results = []
    try:
        for q in qs:
            results.append(p / q)
    except ZeroDivisionError:
        return []
    else:
        return results