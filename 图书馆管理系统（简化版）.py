# 请你定义一个 Book 类和一个 Library 类
# 输出时写明哪些书被借了、哪些还在
# 方法内部加点提示语打印出来（比如“你借走了xxx”）


class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = [] # 定义Library为空列表

    def add_book(self,book):
        self.books.append(book)
        print(f"成功添加书籍《{book.title}》")

    def borrow_book(self,title):
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                if book.available:
                    print(f"成功借出《{book.title}》")
                    book.available = False
                    return
                else:
                    print(f"你要借的书《{book.title}》已经借出去了")
                    return
        print(f"图书馆没有你要借的那本书")

    def return_book(self,title):
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                if not book.available:
                    book.available = True
                    print(f"成功归还《{title}》，此书可借")
                    return
        print(f"《{title}》似乎不是我们图书馆的书！")

    # 打印所有当前可以借的书名列表
    def list_available_books(self):
        available = [book.title for book in self.books if book.available]
        # available 此时是个可借书籍的书名列表，循环打印
        if available:
            print("当前可借书籍：")
            for title in available:
                print(f"- {title}")
        else:
            print("没有书可以借")

# 实例
book1 = Book("《Python进阶指南》","小张")
book2 = Book("《雅思英语听力》","小林")
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)

library1.borrow_book("《雅思英语听力》")
library1.list_available_books()
library1.return_book("《雅思英语听力》")
library1.list_available_books()






