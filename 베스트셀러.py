books = dict()

N = int(input())
for _ in range(N):
    book = str(input())
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

check = max(books.values())

result = []

for key, value in books.items():
    if value == check:
        result.append(key)

result = sorted(result)
print(result[0])

