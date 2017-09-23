class YuChen:
    'yuchen的测试类'
    def __int__(self):
        pass
    def test_list(self):
        '列表函数'
        list1 = ['go','to','school','by','bus'];
        list2 = ['1','2','3','4','5','6'];
        print(list1[0]);
        del list1[0]; #删除列表元素  remove()方法
        print(list1[0]);

        list2[0]= 99; #更新列表元素  append()方法
        print(list2[0])

    def test_tup(self):
        '元组函数'
        tup0 = ();   #空元组
        tup1 = ('My','name','is','yuchen');
        tup2 = (10.11,12,13,14,15,16);
        tup3 = (99999999,);    #只有一个元素的元组，在元素后面添加逗号

        print("访问tuop1元组的第一个元素：",tup1[0]);
        print("访问tuop1元组：", tup1);
        print("访问tup0空元组：",tup0);
        print("计算元素个数打印出来结果为：",len((tup3)));
        del tup2;#删除tup2元组，只能删除元组，不能删除元组的元素


    def test_for(self):
        'for循环函数'
        for aa in range(20,-20,-2):
            #print("aa",aa);
            for bb in range(-30,30,1):
                #//print("bb",bb);
                a=aa/10;
                b=bb/10;
                if(a*a+b*b-1)*(a*a+b*b-1)*(a*a+b*b-1)<=b*b*a*a*a:
                    print("*",end=" ")
                else:
                    print(' ',end=" ");
            print();

    def test_for2(self):
        'for循环函数'
        for aa in range(20,-20,-2):
            #print("aa",aa);
            for bb in range(-30,30,1):
                #//print("bb",bb);
                a=aa/10;
                b=bb/10;
                c=aa*a+b*b-1;
                print("aa*a+b*b-1=",c*c*c);

    def test_dict(self):
        '字典函数'
        dict1 = {'key1':12345,'key2':678910,'key':'zyc'};
        dict2 = {'name':'yuchen','age':23,'birth':19940401,'dress':'重庆市'};
        #访问字典的值
        print("访问dict1的key1键:",dict1['key1']);

        #修改字典
        dict2['age'] = 99;
        print("访问dict2的age键:",dict2['age']);
        #添加
        dict2['School'] = '重庆邮电大学';
        print("访问dict2新添加的键:",dict2['School']);

        #删除字典
        del dict2['dress'];#删除字段的某一键值
        dict2.clear();#清空字典
        del dict2;#直接删除字典

    def test_datetime(self):
        '日期函数'
        import time;  #引入time模块
        ticks = time.time();  #函数time.time()用于获取当前时间戳
        print("当前的时间:",ticks);

        #获取当前时间(从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。)
        localtime1 = time.localtime(time.time());
        print("本地时间为:", localtime1);
        localtime2 = time.localtime(ticks);
        print("本地时间为:",localtime2);

        #获取格式化的时间（最简单的获取可读的时间模式的函数是asctime()）
        localtime3 = time.asctime(time.localtime(time.time()));
        print("这种模式的时间为:",localtime3);

        #格式化日期（利用strftime方法）
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()));
        # 格式化成Sat Mar 28 22:24:24 2016形式
        print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()));

        #获取某月日历(利用calendar模块)
        import calendar;
        cal = calendar.month(2017,9);
        print("输出2017年9月的日历:",cal);

    #匿名函数
    # 可写函数说明
    sum = lambda arg1, arg2: arg1 + arg2;
    # 调用sum函数
    print("相加后的值为 : ", sum(10, 20));
    print("相加后的值为 : ", sum(20, 20));

YuChen().test_datetime();
#YuChen().test_dict();
#YuChen().test_tup()
#YuChen().test_list();
#YuChen().test_for2();
'''YuChen().test_for()
YuChen().test_list();
A=YuChen();
A.test_list();
测试但是大家都把时间可是大家思考的
'''
