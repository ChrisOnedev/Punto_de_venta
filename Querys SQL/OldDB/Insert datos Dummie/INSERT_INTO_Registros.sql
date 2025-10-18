
/****** Llenado de las Tablas  ******/


--EMPLEADO
INSERT INTO [PuntoVenta].[Person].[EMPLEADO] SELECT TOP (30)
      [FirstName]
      ,[LastName]
	  ,'N/E'
	  ,'N/E'
  FROM [AdventureWorks2019].[Person].[Person] 


