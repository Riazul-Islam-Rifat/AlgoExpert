def isPalindrome(string):
    left_pointer = 0
    right_pointer = len(string)-1

    while left_pointer < right_pointer:
        if string[left_pointer]!=string[right_pointer]:
            return False

        left_pointer+=1
        right_pointer-=1

    return True