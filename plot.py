import streamlit as st
import numpy as np
import matplotlib.pylab as plt


class plot():
    def initLine(ax):
      return ax.plot([], [], color = 'white')[0]

    def initLine_imp(ax):
      return []

    def animag(frame, trace, z):
      trace.set_data(np.real(z)[:frame], np.imag(z)[:frame])
      return trace

    def animate(frame, trace,z):
      trace.set_data(z[0][:frame], z[1][:frame])
      return trace

    def animatimp(frame, trace, eqn):
        X, Y, F = eqn

        ax = plt.gca()

        # Remove previous frame’s contour
        if trace is not None:
            for c in trace:
                c.remove()

        # Recompute updated implicit function for this frame
        updated_F = F + 0.01 * frame  # <-- animate however you want

        # Draw new contour
        contour = ax.contour(X, Y, updated_F, levels=[0], colors="white")

        return contour

    def initFigureWindow():
      fig, ax = plt.subplots(figsize = (5,5))
      #fig.canvas.manager.window.geometry('+1400+100')
      fig.patch.set_facecolor('k')
      ax.patch.set_facecolor('k')
      return fig,ax



#equations

class equations():

    def hypospirograph(params,theta):
      a, b , c  = params
      x = (a-b)*np.cos(theta) + c*np.cos(((a-b)/b)*theta)
      y = (a-b)*np.sin(theta) - c*np.sin(((a-b)/b)*theta)

      return x, y

    def epispirograph(params,theta):
      a, b , c  = params
      x = (a + b) * np.cos(theta) + c * np.cos(((a + b) / b) * theta)
      y = (a + b) * np.sin(theta) + c * np.sin(((a + b) / b) * theta)

      return x, y


    def sec_eqn(params,theta):
        a, b, c, d = params
        x = a * np.cos(theta) - b * (np.cos(c * theta / d))
        y = a * np.sin(theta) - b * (np.sin(c * theta / d))
        return x, y


    def Lissajous(params,theta):
        a,b,c,d = params
        x  = a * np.sin(b*theta + np.pi/2)
        y = c * np.sin(d*theta)
        return x, y


    def third_eqn(params, theta):
        a, b, c, d= params
        x = a*np.sin(theta) + b*np.cos(c*theta + np.pi/2)
        y = a*np.cos(d*theta)
        return x,y


    def butterfly(params,theta):
        """
        a = 2, b = 4, c =5
        :param theta:
        :return:
        """
        a, b, c= params
        x = np.sin(theta)*(np.exp(np.cos(theta)) - a*np.cos(b*theta) - np.sin(theta/c)**5)
        y = np.cos(theta)*(np.exp(np.cos(theta)) - a*np.cos(b*theta) - np.sin(theta/c)**5)
        return x,y


    def fourth_eqn(params,theta):
        a, b = params
        x = np.sin(theta)*(np.tan((a*theta)/b))
        y = np.cos(theta)*(np.tan((a*theta)/b))
        return x,y


    def fifth_eqn(params, theta):
        a, b, c, d = params
        x = a*np.cos(theta) - b*np.cos(c*theta/d)
        y = a*np.sin(theta) - b*np.sin(c*theta/d)
        return x,y


    def sixth_eqn(params,theta):
        a, b, c = params
        x = a * np.sin(b * theta) * np.cos(np.cos(c * theta))
        y = a * (np.cos(b * theta) ** 2) * np.sin(np.sin(c * theta))
        return x, y


    def seventh_eqn(params,theta):
        a, b = params
        x = a*theta + b*np.cos(b*theta) + 1/theta
        y = a * theta + b * np.sin(b * theta) + 1 / theta
        return x,y


    def Eigth_eqn(params,theta):
        a, b, c = params
        x = np.cos(theta) + (1/a)*(np.cos(b*theta) + np.sin(c*theta))
        y = np.sin(theta) + (1/a)*(np.sin(b*theta) + np.cos(c*theta))
        return x,y

    def nineth_eqn(params, theta):
        """
        a =20, b = 17
        :param theta:
        :return:
        """
        a , b = params
        x = np.tan(b*theta)
        y = a*x + 1/x
        #z = a * (np.tan(b*theta)) + 1/np.tan(b*theta)
        return x, y

    def tenth_eqn(params, theta):
        """
        a = 9
        :param theta:
        :return:
        """
        a = params
        x = theta
        y = np.exp(x/a)
        #z = np.exp(theta/a)
        return x , y

    def eleventh_eqn(theta):
        """

        :param theta:
        :return:
        """
        x = theta
        y = np.sqrt(x)
        #z = np.sqrt(theta)
        return x,y

    def twelfth_eqn(params,theta):
        """

        :param theta: -4<=theta<=4
        :a=4, b=1.88, c=2, d=4.3,
        :return:
        """
        a,b,c,d= params
        x = a*np.abs((np.cos(b*theta/np.pi)))**2.5
        y = c*np.sin(np.sin(d*theta/np.pi))*(np.cos(b*theta/np.pi))**2

        return x,y

    def thirteenth_eqn(params, theta):
        """
        a = 7, b=3.48
        :param theta:
        :return:
        """
        a, b  = params
        x = a*((np.sin(b*theta/np.pi))/(1+np.round((np.sin(theta/np.pi))**2)))
        y = a*np.cos(np.round(theta/np.pi))*(np.sin(b*theta/np.pi))**4

        return x,y

    def fourteenth_eqn(params, theta):
        """
        a = 6, b=9.52, c = 4.8
        :param theta: -8<=theta<=8
        :return:
        """
        a, b ,c = params
        x = a*np.sin(b*theta/np.pi)*np.round(np.sqrt(np.cos(np.cos(c*theta/np.pi))))
        y = a*(np.cos(b*theta/np.pi)**4)*np.sin(np.sin(c*theta/np.pi))

        return x,y

    def fifteenth_eqn(params, theta):
        """

        :param theta:
        :return:
        """
        a, b, c, d = params
        x = a*np.sin(np.sin(a*theta/np.pi))*np.cos(np.cos(a*b*theta/np.pi)**2)
        y = c*np.cos(d*theta/np.pi)**2*3*np.sin(theta)


    def sixteenth(params,theta):
      a, b , c  = params
      x = (a-b)*np.cos(theta) + c*np.cos(((a-b)/a)*theta)
      y = (a-b)*np.sin(theta) - c*np.sin(((a-b)/a)*theta)

      return x, y

    def seventeenth(params,theta):
      a, b , c  = params
      x = (a + b) * np.cos(theta) + c * np.cos(((a + b) / a) * theta)
      y = (a + b) * np.sin(theta) + c * np.sin(((a + b) / a) * theta)

      return x, y
    ######## Implicit eqn

    def imp_1(params):
        a = params
        x = np.linspace(-a[0], a[0], 400 )
        y = np.linspace(-a[0], a[0], 400)
        X, Y = np.meshgrid(x, y)

        # Define the implicit function
        F = Y ** 2 + np.sin(X + Y ** 2) - 1

        return X,Y,F

