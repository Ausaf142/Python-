class RailwayForm:
    def Sum(self):
        d=self.a+self.b
        return d


App=RailwayForm
App.Sum()
sum.a=5
sum.b=6
print(App.Sum())