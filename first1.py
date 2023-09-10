CREATE DEFINER=`root`@`localhost` FUNCTION `new_SUM`(N1 INT,N2 INT) RETURNS int
    DETERMINISTIC
BEGIN
	DECLARE SUM INT;
    SET SUM =N1+N2;
RETURN SUM;
END
 branch1
-----------hello world------------

----print sum of values----------------
master
