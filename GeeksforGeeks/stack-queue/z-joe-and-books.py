'''
Joe has recently got his new collection of sci-fi novels. He arranges all books in a shelf. Because of his crazy rules, he only reads book from one of the ends of the shelf. Thus, each book Joe reads is either leftmost or rightmost book from the shelf.

Joe cannot read a book if it has more than K chapters, again a crazy rule.

When Joe has read a book, he removes it from the shelf. Joe stops when he is unable to read any book from any end of the shelf.

How many books are still present in the shelf?

Input:

The first line of the input contains two integers N, the total number of books and K, the maximum number of chapters in a book which Joe can read.

The next  N lines denote the number of chapters in the ith book. 

Output:

Print the number of books left in the shelf, when Joe stops reading.

sample input 

8 4
4
3
4
2
5
1
6
4

output 
3
'''


def left_books(books, n, k):
    start = 0
    end = n - 1
    count = 0
    while end > start:
        f_chap = books[start]
        if k >= f_chap:
            start += 1 
            count += 1

        b_chap = books[end]
        if k >= b_chap:
            end -= 1
            count += 1

        if k < f_chap and k < b_chap:
            break

    return n - count





if __name__ == '__main__':
    n, k = map(int, input().split())
    books = []
    for i in range(n):
        books.append(int(input()))
    print(left_books(books, n, k))