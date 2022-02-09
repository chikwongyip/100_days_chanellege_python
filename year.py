year = int(input('请输入年份：'))
if ( ( year // 4 ) == 0 ):

    print('年份：%d 是润年',year)
else:
    print('年份:%d 不是润年',year)