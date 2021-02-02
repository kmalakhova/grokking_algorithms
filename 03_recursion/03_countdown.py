def countdown(i):
    print(i)
        if i <= 0: # base case
        return
    else:      # recursive case
        countdown(i-1)