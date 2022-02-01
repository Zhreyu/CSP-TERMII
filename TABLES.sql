/* question 4 */
CREATE TABLE library
      ( Book_Id CHAR(10),
         Book_Name CHAR(15),
         Author_Name CHAR(17),
         Publishers CHAR(12),
         Price DECIMAL,
         Typee CHAR(10),
         Quantity INTEGER
       );
 INSERT INTO library VALUES ('C0001','Fast Cook','Lata Kapoor','EPB',355.00,'Cookery',5);
 INSERT INTO library VALUES ('F0001','The tears','Willian Hopkins','First pub.',650.00,'Fiction',20);
 INSERT INTO library VALUES ('T0001','My First C++','Brian & Broke','EPB',350.00,'Text',10);
 INSERT INTO library VALUES ('T0002','C++ Brain works','A.W. Rossaine','TDH',350.00,'Text',15);
 INSERT INTO library VALUES ('F0002','Thunderbolts','Anna Roberts','First pub',350.00,'Fiction',50);

CREATE TABLE Issued
          ( Book_Id CHAR(10),
            Issuedto CHAR(10),
            Quantity_Issued INTEGER
          );
INSERT INTO Issued VALUES ('T0001','Kamal',4);
INSERT INTO Issued VALUES ('C0001','Arvind',5);
INSERT INTO Issued VALUES ('F0001','Suresh',2);