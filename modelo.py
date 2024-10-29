from conexion import Conexion

def ingreso_vehiculo(patente, hora, fecha, cochera):
    try:
        conexion=Conexion()
        cursor=conexion.conectar()
        sql="insert into vehiculos (cochera, patente, hora, fecha) values("+str(cochera)+",'"+patente+",'"+hora+"','"+fecha+"';"
        cursor.execute(sql)
        cursor.execute('commit')
        return True
    except Exception as e:
        print(e)
        return False
    
def egreso_vehiculo(patente,hora, fecha, tarifa, medio_pago):
    try:
        conexion=Conexion()
        cursor=conexion.conectar()
        sql="update vehiculos set hora='"+hora+"', fecha='"+fecha+"', tarifa="+str(tarifa)+", medio_pago='"+medio_pago+"', where patente='"+patente+"';"
        cursor.execute(sql)
        cursor.execute('commit')
        return True
    except Exception as e:
        print(e)
        return False
    

        
        