import os


class User:
    credenciales:str|None
    def __init__(self,user,password,fullname,rol):
        self.user=user
        self.password=password
        self.fullname=fullname
        self.rol=rol
    def login(self):
        pass
        try:
            bd_path = os.path.join(os.path.dirname(__file__,),"..", 'bd', 'userv1.txt')
            with open(bd_path) as f:
                data=f.readlines()
                print(data)
            
            for i in data:
                dataTmp=i.split('|')
                (user,password)=(dataTmp[0],dataTmp[1])
                if(self.user==user and self.password==password):
                    print('existe usuario')
                    self.credenciales=dataTmp[3]
                    return True
                else:
                    print('usuario no existe')
        except Exception as e:
            print('el error es ',e)
    def verificar_rol(self):
        print(f'mi rol es {self.rol}')


##print( os.path.join(os.path.dirname(__file__,),"..", 'bd', 'userv1.txt'))