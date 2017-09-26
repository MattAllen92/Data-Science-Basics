def iq_test(numbers):
    evens = 0
    odds = 0
    nums = list(numbers.split())
    for num in nums:
        if int(num) % 2 == 0:
            evens += 1
            if odds > 1:
                return nums.index(num)+1
        else:
            odds += 1     
            if evens > 1:
                return nums.index(num)+1

print iq_test("2 4 7 8 10")