import pymysql
class Data:

    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="api_flask"
        )

        self.cursor = self.conn.cursor()

    def InsertItems(self, element):
        #our element contend the name, age and the carreer of the student
        #in position 0,1,2
        sql= "insert into curso(Documento, Nombre, Creditos) values('{}', '{}', '{}')".format(element[0], element[1], element[2])
        #execute the query
        self.cursor.execute(sql)
        self.conn.commit()#guardamos cambios

    def ReturnOneItem(self, ref):
        #we have ref like document of elemnt
        sql= "select *from curso where Documento = '{}'".format(ref)
        self.cursor.execute(sql)
        #return of element or nill
        return self.cursor.fetchall()

    def ReturnForCarreer(self,ref):
        sql ="select * from curso where Creditos = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def returnAllElements(self):
        sql="select * from curso"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Delete(self, ref):
        sql="delete from curso where Documento ='{}'".format(ref)
        self.cursor.execute(sql)
        self.conn.commit()


    def  UpdateItenm(self, element, ref):
        #element contains the values and ref name of the the item that we want change
        sql = "update curso set Documento = '{}', Nombre ='{}', Creditos ='{}' where Documento = '{}'".format(element[0], element[1],element[2],ref)
        #execute the query
        self.cursor.execute(sql)
        self.conn.commit()#guardamos cambios