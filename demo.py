str = 'I am a student of machine learning at Aptech Learning Institute.'
print(str)


def fibonacci_series(n):
    first_term = 0
    second_term = 1
    next_term = 0
    for i in range(n):
        print(first_term)
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
        
fibonacci_series(10)
