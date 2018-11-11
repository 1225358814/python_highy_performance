# -*-coding=utf-8-*-
# Profile只提供函数粒度的信息 需要使用line_profiler得到函数中各行的时间花费
# 作为模块引入cProfile(Profile的C扩展实现)
from sports import test_visualize
import cProfile

# 直接传入需要测试的函数执行字符串 在mac上测试无效 无法读取到test_visualize
# cProfile.run("test_visualize()")


# 在cProfile实例调用enable()方法和disable()之中中插入一行需要测试的函数也可以实现测试
# print_stats()输出统计信息
# 这种方法测试ok
# pr = cProfile.Profile()
# pr.enable()
# # need_test_func()
# test_visualize()
# pr.disable()
# pr.print_stats()






# 使用cprofile在命令行中测试 
# python -m cProfile sports.py
# 指定排序 按照 tottime(执行函数话费的实际时间，不包含子调用)
# python -m cProfile -s tottime sports.py
# 保存结果到文件
# python -m cProfile -o prof.out sports.py

# KCachegrind提供用户界面来分析cProfile的输出
# 还需要用pyprof2calltree来转换cProfile输出文件到KCachegrind可读取的格式

# 递归函数示例 计算exp(x) sin(x)的泰勒展开式多项式系数

def factorial(n):
    if n == 0:
        return 1.0
    else:
        return n * factorial(n-1)
def taylor_exp(n):
    return [1.0/factorial(i) for i in range(n)]

def taylor_sin(n):
    res = []
    for i in range(n):
        if i % 2 == 1:
            res.append((-1)**((i-1)/2)/float(factorial(i)))
        else:
            res.append(0.0)
    return res

def benchmark():
    taylor_exp(500)
    taylor_sin(500)

if __name__ == "__main__":
    benchmark()
    # 生成测试信息文件
    # python -m cProfile -o prof.cout cProfile_test.py
	# 生成了测试信息需要转换
	# pyprof2calltree -i prof.out -o prof.calltree
	# 安装之后才能使用 
	# ubuntu 可以 sudo apt install KCachegrind
    # MAC 需要 ‘Install kcachegrind on MACOSX with ports’
    # windows可以 http://sourceforge. net/projects/qcachegrindwin/下载 Qt port——QCacheGrind
	# kcachegrind prof.calltree # 或使用命令 qcachegrind prof.calltree
