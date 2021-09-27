import config.validation
validar = config.validation
def listado(db):
    try:
        sql = "SELECT * FROM paises"
        cur= db.connection.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.connection.cursor().close() 

def listadoID(db,id):
    try:
        sql = "SELECT * FROM paises WHERE id = {0}".format(id)
        cur= db.connection.cursor()
        cur.execute(sql)
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.connection.cursor().close() 

def guardarDatos(db,nombre,continente):
    if validar.validarNombre(nombre):
        return ["nombre","Nombre es requerido"]
    else:
        try:
            sql = "INSERT INTO paises (nombre,continente) VALUES('{0}','{1}')".format(nombre,continente)
            cur = db.connection.cursor()
            cur.execute(sql)
            db.connection.commit()
            return "Pais guardado correctamente"
        except Exception as e:
            return e
        finally:
            cur.close()
            db.connection.cursor().close() 

def actualizarDatos(db,nombre,continente,id):
    if validar.validarNombre(nombre):
        return ["nombre","Nombre es requerido"]
    else:
        try:
            sql = "UPDATE paises SET nombre ='{0}', continente ='{1}' WHERE id ={2}".format(nombre,continente,id)
            cur = db.connection.cursor()
            cur.execute(sql)
            db.connection.commit()
            return "Pais actualizado correctamente"
        except Exception as e:
            return e
        finally:
            cur.close()
            db.connection.cursor().close() 

def eliminarDatos(db,id):
    try:
        sql = "DELETE FROM paises WHERE id = {0}".format(id)
        cur= db.connection.cursor()
        cur.execute(sql)
        db.connection.commit()
        return "Pais eliminado correctamente"
    except Exception as e:
        return e
    finally:
        cur.close()
        db.connection.cursor().close() 

def unicoNombreG(db,nombre):
    try:
        sql = "SELECT * FROM paises WHERE nombre = '{0}'".format(nombre)
        cur= db.connection.cursor()
        cur.execute(sql)
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.connection.cursor().close() 

def unicoNombreU(db,nombre,id):
    try:
        sql = "SELECT COUNT(*) FROM paises WHERE nombre='{0}' OR id={1}".format(nombre,id)
        cur= db.connection.cursor()
        cur.execute(sql)
        return cur.fetchone()[0]
    except Exception as e:
        return e
    finally:
        cur.close()
        db.connection.cursor().close() 
