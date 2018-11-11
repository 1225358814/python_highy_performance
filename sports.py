# -*- coding=utf-8 -*-


class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        # x y 存储坐标
        self.y = y
        self.ang_vel = ang_vel
        # ang_vel存储移动方向

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
    
    def evolve(self, dt):
        timestep = 0.0001
        nsteps = int(dt/timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 计算方向
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y/norm
                v_y = p.x/norm
                # 计算位移
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 不断重复 知道时间过去t

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation

def visualize(simulator):
    x = [p.x for p in simulator.particles]
    y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line , = ax.plot(x, y, 'ro')

    # 指定坐标轴的取值范围
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # 这个方法将在动画开始时运行
    def init():
        line.set_data([],[])
        return line, # 这里逗号表示元组 不可少
    
    def animate(i):
        # 我们让例子运动 0.01个时间单位
        simulator.evolve(0.01)
        x = [p.x for p in simulator.particles]
        y = [p.y for p in simulator.particles]

        line.set_data(x,y)
        return line,
    anim = animation.FuncAnimation(fig, 
                                    animate, 
                                    init_func=init,
                                    blit=True,
                                     interval=10)

    plt.show()

def test_visualize():
    # 初始化存储位置和方向对象实例
    particles = [Particle(0.3, 0.5, 1),
                Particle(0.0, -0.5, -1),
                Particle(-0.1, -0.4, 3)]
    # 生成移动规则实例 准备绘画 并传入位置对象列表
    simulator = ParticleSimulator(particles)
    # 运行动画
    visualize(simulator)


from random import uniform

def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                        uniform(-1.0, 1.0),
                        uniform(-1.0, 1.0)) for i in range(1000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == '__main__':
    # test_visualize()
    import timeit
    result = timeit.timeit('benchmark()',setup='from __main__ import benchmark', number=10)
    print('总共运行时间%s:'%result)
    # benchmark()
    # command(unix system): time python sports.py

# timeit 命令行中 测试运行时间
# python -m timeit -s 'fromg you_model import your_func ' 'your_func()'
