import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root"
)

cursor = conn.cursor()

cursor.execute("CREATE USER IF NOT EXISTS 'patrasche'@'localhost' IDENTIFIED BY '!strongPassword123!'")
cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO 'patrasche'@'localhost'")

# cursor.execute("USE test_db")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#     student_id  INT           NOT NULL AUTO_INCREMENT,
#     name        VARCHAR(100)  NOT NULL,
#     year        TINYINT       NOT NULL,
#     course      VARCHAR(100)  NOT NULL,
#     PRIMARY KEY (student_id)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

# """)

for row in cursor.fetchall():
    print(row)

conn.commit()