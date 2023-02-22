# Run as python ./mptest.py > mptest.out

import multiprocessing as mp


class Particle:
    def __init__(self, x):
        self.x = x


def f1(p):
    p.x = 5


def f2(p):
    p.x = 10


def f3(p):
    p.x = 20
    return p


def f4(p, a, b):
    p.x = p.x + a + b
    return p


def main():
    print("init")
    particles = []
    for kk in range(4):
        particles.append(Particle(1))

    print("particles[p.x] after init")
    for p in particles:
        print(p.x)

    print("serial f1")
    for p in particles:
        f1(p)

    print("particles[p.x] after serial f1")
    for p in particles:
        print(p.x)

    print("parallel f2")
    pool = mp.Pool(1)
    pool.map(f2, particles)

    print("particles[p.x] after parallel f2")
    for p in particles:
        print(p.x)

    print("parallel f3")
    pool = mp.Pool(1)
    particles_f3 = pool.map(f3, particles)

    print("particles_f3[p.x] after parallel f3")
    for p in particles_f3:
        print(p.x)

    print("parallel f4")
    pool = mp.Pool(1)
    particles_f4 = pool.starmap(
        f4, zip(particles, [10] * len(particles), [400] * len(particles))
    )

    print("particles_f4[p.x] after parallel f4")
    for p in particles_f4:
        print(p.x)


if __name__ == "__main__":
    main()
