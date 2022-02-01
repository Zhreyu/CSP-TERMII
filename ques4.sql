/* question 4 */
/* creating table */
CREATE DATABASE TERM2
USE TERM2
CREATE TABLE Book
      ( Book_Id CHAR(10),
         Book_Name CHAR(15),
         Author_Name CHAR(17),
         Publishers CHAR(12),
         Price DECIMAL,
         Typee CHAR(10),
         Quantity INTEGER
       );
 INSERT INTO Book VALUES ('C0001','Fast Cook','Lata Kapoor','EPB',355.00,'Cookery',5);
 INSERT INTO Book VALUES ('F0001','The tears','Willian Hopkins','First pub',650.00,'Fiction',20);
 INSERT INTO Book VALUES ('T0001','My First C++','Brian & Broke','EPB',350.00,'Text',10);
 INSERT INTO Book VALUES ('T0002','C++ Brain works','A.W. Rossaine','TDH',350.00,'Text',15);
 INSERT INTO Book VALUES ('F0002','Thunderbolts','Anna Roberts','First pub',350.00,'Fiction',50);

CREATE TABLE Issued
          ( Book_Id CHAR(10),
            Issuedto CHAR(10),
            Quantity_Issued INTEGER
          );
INSERT INTO Issued VALUES ('T0001','Kamal',4)
INSERT INTO Issued VALUES ('C0001','Arvind',5)
INSERT INTO Issued VALUES ('F0001','Suresh',2)
/*
1. To show Book id, Book name, Author name and price of books of First Pub Publisher
2. To display the names and price of books in ascending order of their prices.
3. Display the price of book which has price between 300 to 500.
4. To increase the price of all books of EPB publishers by 50.
5. To display the Book_Id, Book_Name and quantity issued for all books which have been issued.
6. To display the Bookname and Price of Books for all books having ‘C++’ in the bookname
7. Delete the book whose book id is T0002
8. Show all book whose book name started with character ‘T’ 
*/
/* 1st answer
SELECT Book_Id,Book_Name,Author_name,Price
FROM Book
WHERE Publishers = 'First pub' */

/* 2nd
SELECT Book_Name,Price
FROM Book
ORDER BY Price ASC
*/

/* 3rd
SELECT Price
FROM Book
WHERE Price >= 300 AND Price <= 500
*/
/* 4th 
 UPDATE Libaray
 SET Price = Price + 50
 WHERE Publisher = 'EPB'
*/

/* 5th 
SELECT LI.Book_Id,Book_Name, issued.Quantity_Issued AS Issued
FROM Book LI
JOIN issued ON LI.Book_Id = issued.Book_Id

*/

/* 6th
SELECT Book_Name,Price 
FROM Book 
WHERE Book_Name LIKE '%C++%'
*/

/* 7th
DELETE FROM Book
WHERE Book_ID = 'T0002'

*/

/* 8th
SELECT *
FROM Book
WHERE Book_Name LIKE 'T%'
*/

/*
9.)5
10.)650
11.)Thunderbolts	Anna Roberts and 
    The tears	Willian Hopkins

12.)1
13.)4
*/