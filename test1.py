
class Test:
    '测试训练'
    def demo01(self):
        '''
        题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
        '''

        for a in range(1,5,1):
            for b in range(1,5,1):
                for c in range(1,5,1):
                    if(a!=b)and(b!=c)and(a!=c):
                        print(a,b,c);

Test().demo01();