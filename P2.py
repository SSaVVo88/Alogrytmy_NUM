import sys

def f(x):
    """Funkcja dla której szukamy pierwiastka: x^3 + x - 100 = 0"""
    return x**3 + x - 100

def bisection(eps):
    """
    Metoda siecznych (bisekcji) do rozwiązania równania f(x) = 0
    Przyjmuje dokładność eps i zwraca liczbę kroków
    """
    # Początkowy przedział [a, b] gdzie f(a) i f(b) mają przeciwne znaki
    a, b = 4.0, 5.0  # f(4) = -32, f(5) = 30
    
    steps = 0
    while b - a > eps:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1
    return steps

def fixed_point(eps):
    """
    Metoda iteracji prostych do rozwiązania równania x = (100 - x)^(1/3)
    Przyjmuje dokładność eps i zwraca liczbę kroków
    """
    x0 = 4.5  # Początkowe przybliżenie
    steps = 0
    
    while True:
        x1 = (100 - x0) ** (1/3)
        if abs(x1 - x0) < eps:
            break
        x0 = x1
        steps += 1
    return steps

def validate_input(eps_str):
    """Waliduje wejście - sprawdza czy to liczba z przedziału (0,1)"""
    if not eps_str:
        raise ValueError("Brak danych wejściowych.")
    
    try:
        eps = float(eps_str)
    except ValueError:
        raise ValueError("Dokładność musi być liczbą.")
    
    if eps <= 0 or eps >= 1:
        raise ValueError("Dokładność musi spełniać warunek 0 < ε < 1.")
    
    return eps

def main():
    """Główna funkcja - obsługuje wejście i wyświetla wyniki"""
    try:
        # Czytaj wejście
        eps_str = sys.stdin.readline().strip()
        
        # Waliduj wejście
        eps = validate_input(eps_str)
        
        # Oblicz wyniki
        bis_steps = bisection(eps)
        fp_steps = fixed_point(eps)
        
        # Wyświetl wyniki
        print(f"Metoda siecznych: {bis_steps} kroków")
        print(f"Metoda iteracji prostych: {fp_steps} kroków")
    
    except ValueError as e:
        print("Błąd:", e)

if __name__ == "__main__":
    main()