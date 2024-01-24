sums = {}
for i in range(0, 10):
    for j in range(0, 10):
        sums[str(i)+str(j)]=str(i+j)
# print(add)

class int:
    def __init__(self, num):
        self.value = str(num)
    def get_list(self):
        return list(self.value)
    def add(self,  numObj):
        val = self.get_list()
        num = numObj.get_list()
        # valC = val.copy()
        # numC = num.copy()
        # bigger = '?'
        # try:
        #     while True:
        #         valC.pop()
        #         numC.pop()
        # except IndexError:
        #     if valC:
        #         bigger = 'v'
        #     else:
        #         bigger = 'n'
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

print(int('19').add(int('19')))