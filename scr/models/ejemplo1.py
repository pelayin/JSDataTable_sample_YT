from scr.database.connectDB import get_connection_SQLSERVER


class ejemplo1:
    @staticmethod
    def get_items():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = "SELECT IDPRODUCTO, NOMBRE, ALTURA, UNMED FROM Productos"
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []
