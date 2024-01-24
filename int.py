sums = {}
for i in range(0, 10):
    for j in range(0, 10):
        sums[str(i)+str(j)]=str(i+j)
differences = {}
for i in range(0, 10):
    for j in range(0, 10):
        differences[str(i)+str(j)]=str(i-j)
# print(add)

class int:
    def __init__(self, num):
        self.value = str(num)
        self.negative = True if self.get_list.pop(False)=='-' else False
    def get_list(self):
        return list(self.value)
    def get_sign(self):
        return "negative" if self.negative else "positive"
    def add(self,  numObj):
        if numObj.get_sign() == 'negative':
            return self.sub(numObj)
        elif self.get_sign() == 'negative':
            return numObj.sub(self)
        val = self.get_list()
        num = numObj.get_list()
        fsum = ''
        while val:
            try:
                sum = list(sums[num.pop()+val.pop()])
            except IndexError:
                sum = list(val.pop())
            fsum = sum.pop()+fsum
            print(fsum)
            if sum:
              try:
                  val.append(str(int(val.pop()).add(int(sum.pop()))))
              except IndexError:
                  val.append(sum.pop())
        self.value =  fsum
        return fsum
    def sub(self, numObj):
        pass

print(int('19').add(int('19')))