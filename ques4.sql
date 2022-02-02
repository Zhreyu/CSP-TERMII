/* Shreyas XIIB 52 2021-2022*/
/*            |QUESTIONS|
1. To show Book id, Book name, Author name and price of books of First Pub Publisher
2. To display the names and price of books in ascending order of their prices.
3. Display the price of book which has price between 300 to 500.
4. To increase the price of all books of EPB publishers by 50.
5. To display the Book_Id, Book_Name and quantity issued for all books which have been issued.
6. To display the Bookname and Price of Books for all books having ‘C++’ in the bookname
7. Delete the book whose book id is T0002
8. Show all book whose book name started with character ‘T’ 
Give the output of the following
9. Select Count(*) from Book;
10. Select Max(Price) from Book where Quantity >=15;
11. Select Book_Name, Author_Name from Book where Publisher=’First Pub’;
12. Select count(distinct Publisher) from Book where Price>=400;
13. Select count(distinct(Publisher)) from book; */

/*        |ANSWERS|                     */
/* 1st 
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
