import mysql.connector
class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            user='root',
            password='john',
            host='localhost',
            database='library_db'
        )

        self.cursor = self.con.cursor()

    # READ / LIST ALL BOOKS
    def list(self):
        query = "SELECT * FROM book"

        self.cursor.execute(query)

        data = self.cursor.fetchone()

        if data:
            for book in data:
                return True
        else:
            print("No records found")

    # CREATE / INSERT BOOK
    def create(self,id, title, author, price, pages, language):
        query = """
        INSERT INTO book(id,title, author, price, pages, language)
        VALUES(%s,%s, %s, %s, %s, %s)
        """

        data = (id,title, author, price, pages, language)

        self.cursor.execute(query,data)
        self.con.commit()

        print("Inserted data successfully")

    # RETRIEVE / READ ONE BOOK

    def retrieve(self, id):
        query = "SELECT * FROM book WHERE id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            return record
        else:
            print("No record found")

    # DELETE BOOK
    def delete(self, id):
        query = "DELETE FROM book WHERE id=%s"
        data = (id,)

        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False
    # def delete(self, id):
    #     query = "DELETE FROM book WHERE id=%s"
    #     data = (id,)
    #     self.cursor.execute(query, data)
    #     self.con.commit()
    #
    #     if self.cursor.rowcount > 0:
    #         print("Deleted record Successfully")
    #     else:
    #         print("No record found")
    # UPDATE BOOK
    def update(self, id, title, author, price, pages, language):
        query = """
        UPDATE book
        SET title=%s,
            author=%s,
            price=%s,
            pages=%s,
            language=%s
        WHERE id=%s
        """

        data = (title, author, price, pages, language, id)

        self.cursor.execute(query, data)
        self.con.commit()

        if self.cursor.rowcount > 0:
             print("Record updated successfully")
            # return True
        else:
            # return False
             print("No record found")

# CREATE OBJECT
book_instance = BookListCreateRetrieveUpdateDelete()


# LIST ALL BOOKS
# book_instance.list()
#
# #
# # # CREATE / INSERT A BOOK
# book_instance.create(id=101,
#     title='jilly',
#     author='jom',
#     price=400,
#     pages=500,
#     language='English'
# )


# RETRIEVE ONE BOOK
# book_instance.retrieve(101)


# UPDATE A BOOK
# book_instance.update(
#     101,
#     'Jilly Updated',
#     'Jom Updated',
#     500,
#     550,
#     'English'
# )
# DELETE A BOOK
book_instance.delete(101)