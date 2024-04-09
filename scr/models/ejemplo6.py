from scr.database.connectDB import get_connection_SQLSERVER


class ejemplo6:
    @staticmethod
    def get_exportProductList():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = (
                    "SELECT P.NOMBRE as ProductName, M.DESCRIPCION AS Brand, F.DESCRIPCION as Manufacturer,"
                    " FAM.DESCRIPCION AS Family, P.ALTURA AS Height, P.UNMED AS Unit_Measure, "
                    " CAST(ROUND((99-1)* RAND(CHECKSUM(NEWID())+1 ) ,0)AS int) AS Stock"
                    " FROM Productos P "
                    " INNER JOIN Marcas M on M.IDMARCA= P.IDMARCA"
                    " INNER JOIN Fabricantes F ON F.IDFABRICANTE= P.IDFABRICANTE "
                    " INNER JOIN Familia FAM on FAM.IDFAMILIA = P.IDFAMILIA"
                )
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []
