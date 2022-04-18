# You are given a moment in time and space. What you must do is break it down into time and space, to determine if that moment is from the past, present or future.
# Time is the sum of characters that increase time (i.e. numbers in range ['1'..'9'].
# Space in the number of characters which do not increase time (i.e. all characters but those that increase time).
# The moment of time is determined as follows:
# If time is greater than space, than the moment is from the future. If time is less than space, then the moment is from the past. Otherwise, it is the present moment.
# You should return an array of three elements, two of which are false, and one is true. The true value should be at the 1st, 2nd or 3rd place for past,
# present and future respectively.

def moment_of_time_in_space(moment):
    past = False
    present = False
    future = False
    moment_in_time = moment.split(' ')
    moment_in_space = 4
    moment_in_time = 0
    for el in moment:
        if el.isdigit():
            moment_in_time += int(el)
        if el == '0':
            moment_in_space += 1
    if moment_in_time > moment_in_space:
        future = True
    elif moment_in_time < moment_in_space:
        past = True
    else:
        present = True           
    return [past,present,future]

print(moment_of_time_in_space("12:30 am"))  #[False, False, True])
print(moment_of_time_in_space("12:02 pm"))  #[False, True, False])
print(moment_of_time_in_space("01:00 pm"))  #[True, False, False])
print(moment_of_time_in_space("11:12 am"))  #[False, False, True])
print(moment_of_time_in_space("05:20 pm"))  #[False, False, True])
print(moment_of_time_in_space("04:20 am"))  #[False, True, False])