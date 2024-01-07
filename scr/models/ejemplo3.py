from scr.database.connectDB import get_connection_SQLSERVER
class ejemplo3:
    @staticmethod
    def get_productbrands():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = "SELECT P.NOMBRE as Product, M.DESCRIPCION as Brand," \
                        " CAST( ROUND((99 - 1) * RAND(CHECKSUM(NEWID())) + 1, 0) AS INTEGER)" \
                        " AS Stock " \
                        "FROM productos P" \
                        " INNER JOIN marcas M on M.IDMARCA = P.IDMARCA"
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []



