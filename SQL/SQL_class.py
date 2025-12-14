import sqlite3

class SQL:
    # make or find the database
    def __init__(self, database_name = "mydata.db"):
        # initliaze conection on cursor
        self.conn = sqlite3.connect(database_name)
        self.cur = self.conn.cursor()
        # create the same table we used before
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
        """)
        self.conn.commit()

    # destructor cleanup connection and cursor
    def __del__(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    # clears the table and resets the autoincrement id counter
    def clearAll(self):
        self.cur.execute("DELETE FROM users")
        self.cur.execute("DELETE FROM sqlite_sequence WHERE name='users'")
        self.conn.commit()

    # returns an entry in the table by id
    def get(self, id):
        self.cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cur.fetchone()


    # returns all the data in the table
    def getAll(self):
        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()

    # add a new entry in the table
    def insert(self, name, age):
        self.cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()
            
    # updates an entry in the table
    # can update one attribute or both 
    def update(self, id, name=None, age=None):
        if name is not None:
            self.cur.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))
        if age is not None:
            self.cur.execute("UPDATE users SET age = ? WHERE id = ?", (age, id))
        self.conn.commit()

    # deletes an entry from the table
    def delete(self, id):
        self.cur.execute("DELETE FROM users WHERE id = ?", (id,))
        self.conn.commit()


# TESTING: test database operations
#
# create a database object
db = SQL()
# clear the table before testing
db.clearAll()

# insert some users
db.insert("Adrian", 25)
db.insert("Lina", 30)
db.insert("Sam", 22)

# get all users
print("All users:")
all_users = db.getAll()
for user in all_users:
    print(user)

# get a single user by ID
print("\nGet user with ID 2:")
print(db.get(2))

# update a user
print("\nUpdating Sam's age to 23")
db.update(3, age=23)
print(db.get(3))

# update a user's name
print("\nUpdating Adrian's name to 'Adrian R.'")
db.update(1, name="Adrian R.")
print(db.get(1))

# delete a user
print("\nDeleting Lina (ID 2)")
db.delete(2)
print("All users after deletion:")
for user in db.getAll():
    print(user)
