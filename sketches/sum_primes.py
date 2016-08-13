from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if not number % i:
            return False
    return True


t = int(input())
questions = []
for i in range(t):
    questions.append(int(input()))

max_q = max(questions)
sorted_q = iter(sorted(set(questions)))
answers = dict()
current_q = next(sorted_q)
prime_sum = 0
for i in range(2, max_q + 1):
    if is_prime(i):
        prime_sum += i
    if i == current_q:
        answers[i] = prime_sum
        current_q = next(sorted_q, 0)
for q in questions:
    print(answers[q])
