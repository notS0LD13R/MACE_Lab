import mysql.connector

class Database:
    def __init__(self,user:str,password:str,database:str,host="localhost"):
        self.conn=mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(self.conn)
    
    def insert_student(self,adm_no:str,name:str,hostel_id:int)->None:
        sql='call insert_student(%(adm_no)s,%(name)s,%(hostel_id)s)'
        val={
            'adm_no':adm_no,
            'name':name,
            'hostel_id':hostel_id
        }
        
        self.execute(sql,val)
    
    def alter_cut(self,adm_no:str,day:int,cut:bool):
        
        sql='update cut set {}={} where adm_no=\'{}\''.format('_'+str(day),'0' if cut else '1',adm_no)
        
        self.execute(sql)

    def get_cuts(self,adm_no:str)->tuple:
        sql='select * from cut where adm_no=%s'
        val=[adm_no]

        data=self.execute(sql,val)
        return data[0][1:]
    
    def monthly_reset(self):
        sql='call create_new_mess_cost();'
        self.execute(sql)
        sql='call reset_cut();'
        self.execute(sql)

    def calc_mess_bill(self):
        sql='call calc_mess_bill();'
        
        self.execute(sql)
    
    def set_mess_cost(self,cost):
        sql='call set_mess_cost(%s)'
        val=[cost]

        self.execute(sql,val)
    
    def authenticate(self,adm_no:str,password:str)->tuple:
        sql=('call authenticate(%s,%s)')
        val=[adm_no,password]

        data=self.execute(sql,val)
        return data[0]
    
    def execute(self, sql,val=None)->list:
        cur=self.conn.cursor()
        cur.execute(sql,val) if val else  cur.execute(sql)
        data=cur.fetchall()
        self.conn.commit() if not data else ()
        cur.close()

        return data

    


def main():
    obj=Database('root','root','mess_management')
    obj.get_cuts('b20ds063')

if __name__=='__main__':
    main()