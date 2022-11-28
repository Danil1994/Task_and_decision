def sum_strings(one, two):
    if one == two == '':
        return '0'
    one = one.rjust(len(two), '0')
    two = two.rjust(len(one), '0')
    answer = []
    extra_digit = 0

    for i in range(1, len(one) + 1):
        digit_sum = str(int(one[-i]) + int(two[-i]) + extra_digit)
        if int(digit_sum) < 10:
            answer.append(digit_sum)
            extra_digit = 0
        else:
            answer.append(digit_sum[-1])
            extra_digit = int(digit_sum[0])

    if extra_digit != 0:
        answer.append(str(extra_digit))

    answer.reverse()

    if answer[0] == '0' and len(answer) > 1:
        answer.remove('0')

    return ''.join(answer)
