def _fib(n, result):
    if n<=1:
        print(result)
        return n
    else:
        a=_fib(n-1, result)
        b=_fib(n-2, result)
        if not result[n-1]:
            result[n-1]=a
        if not result[n-2]:
            result[n-2]=b
        return(_fib(n-1, result) + _fib(n-2, result))

n = 10
result = [None] * n
_fib(n, result)
