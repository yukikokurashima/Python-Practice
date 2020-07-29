while True:
    even_sum = 0
    odd_sum = 0   
    enter = input("Enter integer:  ")
    if enter!= "Done":
        for x in range(1, int(enter)+1):
            if x % 2 == 0:
                even_sum = even_sum + x
            elif x % 2 != 0:
                odd_sum = odd_sum + x
        print("The sum of even number in this range is ", even_sum)
        print("The sum of odd number in this range is ", odd_sum)

    else:
        break