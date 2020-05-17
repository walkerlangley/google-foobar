def solution(total_lambs):
    generous = 0
    have_enough = True
    lambs_left = total_lambs - 1
    while have_enough:
      previous = 2**(generous - 1)
      s = 2**generous
      lambs_left -= s
      next_payment = 2**(generous + 1) 
      min_payment = s + previous
      generous += 1
      if lambs_left < next_payment:
        if lambs_left < min_payment:
          have_enough = False

    fib = 0
    first = 0
    second = 1
    fib_sum = 0
    stingy = 0
    while fib_sum < total_lambs:
        fib = first + second
        fib_sum += fib
        first = second 
        second = fib
        stingy += 1
    h = stingy - generous
    return h

  
print(solution(143))
print(solution(10))