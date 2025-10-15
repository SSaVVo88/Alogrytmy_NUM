def divided_differences(x, y):
    """
    Oblicza ilorazy różnicowe na podstawie węzłów x i wartości y.
    Zwraca listę współczynników a[0], a[1], ..., a[n] wielomianu Newtona.
    """
    n = len(y)
    # Kopiujemy y, bo będziemy modyfikować tablicę w miejscu
    a = y[:]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (x[i] - x[i - j])
    return a  # a[0], a[1], ..., a[n-1] to współczynniki Newtona


def newton_interpolate(x, a, t):
    """
    Oblicza wartość wielomianu interpolacyjnego Newtona w punkcie t.
    x: lista węzłów [x0, x1, ..., xn]
    a: współczynniki Newtona (ilorazy różnicowe)
    t: punkt, w którym liczymy wartość
    """
    n = len(a)
    result = a[-1]
    for k in range(n - 2, -1, -1):
        result = result * (t - x[k]) + a[k]
    return result


def main():
    # Wczytywanie danych
    n = int(input("Podaj n (liczbę węzłów minus 1): "))
    print(f"Podaj {n + 1} węzłów x (oddzielone spacjami):")
    x = list(map(float, input().split()))
    print(f"Podaj {n + 1} wartości y (oddzielone spacjami):")
    y = list(map(float, input().split()))

    if len(x) != n + 1 or len(y) != n + 1:
        print("Błąd: niepoprawna liczba danych!")
        return

    # Obliczanie współczynników Newtona
    coeffs = divided_differences(x, y)

    # Wczytywanie punktów t i obliczanie P(t)
    print("Podaj punkty t, dla których chcesz obliczyć P(t) (oddzielone spacjami):")
    t_values = list(map(float, input().split()))

    print("\nWyniki:")
    for t in t_values:
        p_t = newton_interpolate(x, coeffs, t)
        print(f"P({t}) = {p_t:.6f}")


if __name__ == "__main__":
    main()