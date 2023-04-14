import heapq

n, m = map(int, input().split())
books = list(map(int, input().split()))

neg_books = []
pos_books = []

largest = max(max(books), -min(books))

for book in books:
    if book < 0:
        heapq.heappush(neg_books, book)
    elif book > 0:
        heapq.heappush(pos_books, -book)
        
result = 0

while neg_books:
    result += heapq.heappop(neg_books)
    for _ in range(m-1):
        if neg_books:
            heapq.heappop(neg_books)
            
while pos_books:
    result += heapq.heappop(pos_books)
    for _ in range(m-1):
        if pos_books:
            heapq.heappop(pos_books)
            
print(-result * 2 - largest)