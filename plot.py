
import numpy as np
import matplotlib.pylab as plt


class plot():
    def initLine(ax):
      return ax.plot([], [], color = 'white')[0]

    def animag(frame, trace, z):
      trace.set_data(np.real(z)[:frame], np.imag(z)[:frame])
      return trace

    def animate(frame, trace,z):
      trace.set_data(z[0][:frame], z[1][:frame])
      return trace

    def initFigureWindow():
      fig, ax = plt.subplots(figsize = (5,5))
      #fig.canvas.manager.window.geometry('+1400+100')
      fig.patch.set_facecolor('k')
      ax.patch.set_facecolor('k')
      return fig,ax

#equations
class equations():

    def first_eqn(a1,a2,a3,b1,b2,b3,c1,c2,c3,theta):
      z = (a1 * np.exp((theta * b1 + c1) * 1j)
           + a2 * np.exp((theta * b2 + c2) * 1j)
           + a3 * np.exp((theta * b3 + c3) * 1j))

      return z


    def sec_eqn(a,b,c,d,theta):
        x = a * np.cos(theta) - b * (np.cos(c * theta / d))
        y = a * np.sin(theta) - b * (np.sin(c * theta / d))
        return x, y

