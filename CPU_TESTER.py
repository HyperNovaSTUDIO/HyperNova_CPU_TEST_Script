import time
import multiprocessing

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    return count

def benchmark():
    cores = multiprocessing.cpu_count()
    n = 100_000  # 계산량 조절 가능
    chunk = n // cores
    start_time = time.time()

    with multiprocessing.Pool(cores) as pool:
        results = pool.starmap(count_primes_in_range, [(i, i + chunk) for i in range(0, n, chunk)])

    total_primes = sum(results)
    end_time = time.time()
    elapsed = end_time - start_time
    score = int(total_primes / elapsed * cores)

    # ✅ 현실적인 등급 기준
    if score >= 900000:
        grade = "🚀 Ultra급 (워크스테이션 / M3 Pro, i9 이상)"
    elif score >= 500000:
        grade = "⚡ High급 (고성능 노트북 / M2, i7급)"
    elif score >= 200000:
        grade = "💻 Mid급 (보통 노트북 / M1, i5, 인텔 맥북 에어)"
    elif score >= 100000:
        grade = "🐢 Low급 (저가형 노트북 / i3, 구형 CPU)"
    else:
        grade = "🪫 Very Low급 (오래된 CPU, 기본 작업용)"

    print("\n=== 🧠 CPU Benchmark Result ===")
    print(f"✅ CPU CORES: {cores}")
    print(f"✅ PRIME COUNT: {total_primes}")
    print(f"✅ TIME: {elapsed:.2f} seconds")
    print(f"📊 CPU SCORE: {score}")
    print(f"🏆 CPU GRADE: {grade}")

if __name__ == "__main__":
    benchmark()
