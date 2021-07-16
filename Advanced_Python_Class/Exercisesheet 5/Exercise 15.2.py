import tensorflow as tf
import numpy as np


x = tf.Variable(initial_value=1.0, dtype=tf.float64)
y = tf.Variable(initial_value=0.5, dtype=tf.float64)

"""
with tf.GradientTape() as g:
    g.watch(x)
    with tf.GradientTape() as h:
        h.watch(x)
        with tf.GradientTape() as n:
            n.watch(y)
            with tf.GradientTape() as k:
                k.watch(y)
                with tf.GradientTape() as j:
                    f = (x+y**3)*tf.math.exp(-x**2+y**2)
                    dfx_tf = g.gradient(f, x)
                    dfx2_tf = h.gradient(dfx_tf, x)
                    dfy_tf = n.gradient(f, y)
                    dfy2_tf = k.gradient(dfy_tf, y)
                    dfxy_tf = j.gradient(dfx_tf, y)
"""
with tf.GradientTape(persistent=True) as g:
    with tf.GradientTape(persistent=True) as gg:
        f = (x + y ** 3) * tf.math.exp(-x ** 2 + y ** 2)
        df_dx = gg.gradient(f, x)
        df_dy = gg.gradient(f, y)


df_d2x = g.gradient(df_dx, x)
df_d2y = g.gradient(df_dy, y)

df_dxy = g.gradient(df_dx, y)


def dfx(x, y):
    return (-2*(x**2)-2*x*(y**3)+1)*np.exp(-x**2+y**2)


def dfy(x, y):
    return (2*x*y+2*(y**4)+3*(y**2))*np.exp(-x**2+y**2)


def dfx2(x, y):
    return (4*(x**3)+4*(x**2)*(y**3)-6*x-2*(y**3))*np.exp(-x**2+y**2)


def dfy2(x, y):
    return (4*x*(y**2)+6*y+2*x+4*(y**5)+14*(y**3))*np.exp(-x**2+y**2)


def dfxy(x, y):
    """Nach Satz von Schwarz sind beide gleich"""
    return (-2*y*(2*(x**2)+x*y*(2*(y**2)+3)-1))*np.exp(-x**2+y**2)


def hess(x, y):
    return [dfx2(x, y), dfxy(x, y), dfxy(x, y), dfy2(x, y)]


def hess_tf():
    return np.array([df_d2x, df_dxy, df_dxy, df_d2y])

# .numpy() makes tensorflow varialbe into numerical value


print(hess(1.0, 0.5))
print(hess_tf())
