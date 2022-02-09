"""
如果输入的成绩在90分以上（含90分） 输出A;
80分-90分 输出 B;
70-80分  输出 C;
60-70分 输出 D;
60分一下 输出 E;
"""
mark = float(input('请输入成绩：'))

if mark >= 90:
    print('等级为：A')
elif mark <  90 and mark >= 80:
    print('等级为：B')
elif mark < 80 and mark >= 70:
    print('等级为：C')
elif mark < 70 and mark >= 60:
    print('等级为：D')
else:
    print('等级为:E')