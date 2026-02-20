class Mother:
    def cooking(self):
        print("Cooking skills")

class Father:
    def programming(self):
        print("Programming skills")

class Child(Mother, Father):
    def sports(self):
        print("Football skills")

c1 = Child()
c1.cooking()      # Output: Cooking skills
c1.programming()  # Output: Programming skills
c1.sports()       # Output: Football skills