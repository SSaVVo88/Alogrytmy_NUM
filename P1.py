import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
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