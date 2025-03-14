class book:
    def__init__(self,name,category,cost):
        self.name=name
        self.category=category
        self._cost=cost
    def get_detail(self):
        return f"name:{self.name},category:{self.category},cost:{self.cost}"
    def discount(self):
        retutn self_cost*0.1

class novel(book):
    def__init__(self,name,category,cost):
        self.name=name
        self.category=category
        self._cost=cost
    def get_detail(self):
        return f"name:{self.name},category:{self.category},cost:{self.cost}"
    def discount(self):
        retutn self_cost*0.05

novel1=novel("rivers of babylon",fictional,3500)

print(novel1.getdetails(),"discount:"novel1.discount())

       