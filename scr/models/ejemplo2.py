from scr.database.connectDB import get_connection_SQLSERVER


class ejemplo2:
    @staticmethod
    def get_customerranking():
        connection = get_connection_SQLSERVER()
        with connection.cursor() as cursor:
            try:
                query = "SELECT TotalVentas.Total, C.NOMBRES, COUNT(D.IDOCVTA) as Conteo_Ventas, " \
                        " COUNT(D.IDOCVTA) * 100.0 / TotalVentas.Total as Porcentaje_Ventas " \
                        " ,SUM(D.TOTAL) GranTot FROM  DocumentoVenta_HEADER D " \
                        "INNER JOIN Clientes C on C.IDCLIENTE = D.IDCLIENTE " \
                        " CROSS JOIN ( SELECT COUNT(IDOCVTA) as Total FROM DocumentoVenta_HEADER " \
                        " WHERE ESTADO = 'ACT') as TotalVentas " \
                        "WHERE D.ESTADO = 'ACT' " \
                        " GROUP BY C.NOMBRES, TotalVentas.Total"
                cursor.execute(query)
                result = cursor.fetchall()
                return result

            except Exception as e:
                print(f"Error en la consulta: {str(e)}")
                return []