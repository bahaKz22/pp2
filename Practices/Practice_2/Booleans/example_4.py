#Some Values are False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
