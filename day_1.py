def main():
    print('Hello')
        
    # robot=Robot('s',2)
    # robot1=Robot('s',1)
    
    # print(robot==robot1)
    mega=Megatron('Transformers')
    print(mega)
    
    
    
    
    
    
    
class Robot:
  
    def __init__(self,name:str,types:str):
        self.name=name
        self.types=types  
    def __eq__(self, __value: object) -> bool:
        if self.name==__value.name and self.types==__value.types:
            return True
        else:
            return False
    def __str__(self) -> str:
        return f"I am {self.name} and I am a {self.types}"
    
class Megatron(Robot):
    def __init__(self,types:str):
        super().__init__('Megatron',types)
    def __str__(self) -> str:
        return super().__str__()
    

if __name__=="__main__":
    main()
    
