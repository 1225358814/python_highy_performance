from sports import Particle, ParticleSimulator
from random import uniform

# require pytest,pytest-benchmark
# 添加了形参benchmark 然后在最后 加入benchmark(simulator.evole, 0.1)
# 这被称为加入测试夹具fixture 最后把主要的执行传入测试夹具benchmark
def test_benchmark(benchmark):
    particles = [Particle(uniform(-1.0, 1.0),
                        uniform(-1.0, 1.0),
                        uniform(-1.0, 1.0)) for i in range(1000)]
    simulator = ParticleSimulator(particles)
    # simulator.evolve(0.1)
    benchmark(simulator.evolve,0.1)

# 运行这个测试
# pytest test_sport.py
# or
# pytest test_sport.py::test_benchmark