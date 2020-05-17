def solution(total_lambs):
    def generous_number(total_lambs):
      generous = 1
      b_sum = 1
      have_enough = True
      lambs_left = total_lambs - 1
      while have_enough:
        generous += 1
        # print('Generous: ', generous)
        s = 2**(generous - 1)
        # print('S: ', s)
        lambs_left -= s
        b_sum += s
        next_payment = 2**(generous)
        if lambs_left < next_payment:
          previous = 2**(generous - 2)
          min_payment = previous + s
          if (lambs_left >= min_payment):
            generous += 1
          have_enough = False
      return (generous, lambs_left, next_payment)
      # return generous

    def stingy_number(total_lambs):
      first = 0
      second = 1
      stingy = 0
      have_enough = True
      lambs_left = total_lambs
      next_payment = 1
      while have_enough:
          lambs_left -= second
          stingy += 1
          next_payment = first + second
          first = second 
          second = next_payment
          if lambs_left < next_payment:
            have_enough = False
      return (stingy, lambs_left, next_payment)

    (generous, gen_remainder, next_max_payment) = generous_number(total_lambs)
    (stingy, stingy_remainder, next_min_payment) = stingy_number(total_lambs)
    print('generous / remainder / next: ', generous, ' ', gen_remainder, ' ', next_max_payment)
    print('stingy / remainder / next: ', stingy, stingy_remainder, ' ', next_min_payment)

    # total_remainder = gen_remainder + stingy_remainder
    # min_payment = min(next_max_payment, next_min_payment)
    h = stingy - generous
    # print('Total Remainder: ', total_remainder)
    # print('H before: ', h)
    # if total_remainder > min_payment:
    #   h -= 1
    print('H: ', h)
    return h

solution(143)
# 3

solution(10)
# 1

# solution(33)