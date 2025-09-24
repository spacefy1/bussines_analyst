from math import sqrt
import concurrent.futures
import multiprocessing
from timeit import default_timer as timer

def eh_primo(x):
    if x < 2:
        return False
    if x == 2:
        return x
    if x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False

    return x

def sol_concorrente(n_workers, numeros):
    print('Numero de processadores: %i.' % n_workers)
    start = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(eh_primo, i) for i in numeros]
        sub_start = timer()

        for future in concurrent.futures.as_completed(futures):
            r = future.result()
            if r:
                result.append(r)

        sub_duration = timer() - sub_start

    duration = timer() - start
    print('Duracao Intermediaria: %.4f segundos.' % sub_duration)
    print('Duracao Total: %.4f segundos.' % duration)

if __name__ == '__main__':
    numeros = [i for i in range(10**13, 10**13 + 1000)]
    for n_workers in range(1, multiprocessing.cpu_count() + 1):
        sol_concorrente(n_workers, numeros)
        print('_' * 30)