import sys
from validation import validate_and_parse

def main():
    print(
        "Podaj dane w następującym formacie:\n"
        "n\n"
        "x0 x1 ... xn\n"
        "y0 y1 ... yn\n"
        "t1 t2 ... (opcjonalnie kolejne linie z t)\n\n"
        "Po zakończeniu wpisywania danych naciśnij:\n"
        " - Ctrl+D  (Linux/Mac)\n"
        " - Ctrl+Z+Enter  (Windows)\n"
    )
    data = sys.stdin.read().splitlines()
    try:
        n, x, y, t_values = validate_and_parse(data)
    except ValueError as e:
        print("Błąd:", e)
        return
    
    n = int(data[0].strip())
    x = list(map(float, data[1].split()))
    y = list(map(float, data[2].split()))
    t_values = []
    
    for line in data[3:]:
        t_values.extend(map(float, line.split()))
    
    m = n + 1
    coeffs = y.copy()
    
    for i in range(1, m):
        for j in range(m - 1, i - 1, -1):
            coeffs[j] = (coeffs[j] - coeffs[j - 1]) / (x[j] - x[j - i])
    
    results = []
    for t in t_values:
        result = coeffs[-1]
        for i in range(m - 2, -1, -1):
            result = coeffs[i] + (t - x[i]) * result
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()