def validate_and_parse(data):
    if not data:
        raise ValueError("Brak danych wejściowych.")

    # n
    try:
        n = int(data[0].strip())
    except ValueError:
        raise ValueError("Pierwsza linia musi zawierać liczbę całkowitą n.")

    if n < 1:
        raise ValueError("n musi być ≥ 1.")

    if len(data) < 3:
        raise ValueError("Zbyt mało linii danych – oczekiwane: n, x, y.")

    # x
    try:
        x = list(map(float, data[1].split()))
    except ValueError:
        raise ValueError("Linia 2 musi zawierać wartości liczbowe x.")

    if len(x) != n + 1:
        raise ValueError(f"Dla n={n} należy podać dokładnie {n+1} wartości x (podano {len(x)}).")

    if len(set(x)) != len(x):
        raise ValueError("Wartości x muszą być unikalne.")

    # y
    try:
        y = list(map(float, data[2].split()))
    except ValueError:
        raise ValueError("Linia 3 musi zawierać wartości liczbowe y.")

    if len(y) != n + 1:
        raise ValueError(f"Dla n={n} należy podać dokładnie {n+1} wartości y (podano {len(y)}).")

    # t
    t_values = []
    for line in data[3:]:
        try:
            t_values.extend(map(float, line.split()))
        except ValueError:
            raise ValueError("W liniach z t muszą znajdować się liczby.")

    if not t_values:
        raise ValueError("Brak punktów t do obliczenia interpolacji.")

    return n, x, y, t_values
