
class Test:
    '测试训练'
    def demo01(self):
        '''
        题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        '''

        for a in range(1,5,1):
            for b in range(1,5,1):
                for c in range(1,5,1):
                    if(a!=b)and(b!=c)and(a!=c):
                        print(a,b,c);


    def demo02(self):
        '''
        企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
        20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
        高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
        
        思路1：
        if判断逐句判断
        '''
        profit = int(input("输入当月利润(万元)："));
        if(profit>0 and profit<=10):
            account = profit*0.1;
        elif(profit>10 and profit<=20):
            account = 10*0.1+(profit-10)*0.075
        elif(profit>20 and profit<=40):
            account = 10*0.1+10*0.075+(profit-20)*0.05
        elif(profit>40 and profit<=60):
            account = 10*0.1+10*0.075+20*0.05+(profit-40)*0.03
        elif(profit>60 and profit<=100):
            account = 10*0.1+10*0.075+20*0.05+20*0.03+(profit-60)*0.015
        elif(profit>100):
            account = 10*0.1+10*0.075+20*0.05+20*0.03+40*0.01+(profit-100)*0.01
        elif(profit<=0):
            account = 0;
        print("奖金总数:",account);

        '''
        思路2：
        使用列表
        '''
        lirunqujian = [100,60,40,20,10,0];
        chunlirun = [0.4,0.6,1,0.75,1,0];
        lilv = [0.01,0.01,0.03,0.05,0.075,0.1];
        jiangjin = 0;
        lirun = int(input("输入当月利润(万元)："));
        for aa in range(0,6):
            if(lirun>=lirunqujian[aa]):
                jiangjin += lilv[aa]*(lirun-lirunqujian[aa]);
                lirun = lirunqujian[aa];
        print("奖金总数:",jiangjin)

    def demo03(self):
        '''
        一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
        '''


    def demo04(self):
        '''
        输入某年某月某日，判断这一天是这一年的第几天？
        :return:
        '''
        year = int(input("年份："));
        month = int(input("月份："));
        day = int(input("日："));
        days = 0;

        months = [0,31,28,31,30,31,30,31,31,30,31,30,31];
        for aa in range(1, 13):
            if (month > aa):
                days += months[aa];
            else:
                if (year % 4 == 0 and days >= 59):
                    days += 1;
                days += day;
                break;
        print("该日期是今年弟",days,"天");







#Test().demo01();
Test().demo04();