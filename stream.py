import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as anim
from matplotlib.animation import  FFMpegWriter, PillowWriter
import  streamlit as st
import streamlit.components.v1 as components
from plot import *
import os
import time

a1 = 4
a2 = 4
a3 = 1.3

b1 = 44
b2 = -17
b3 = -54

c1 = 0
c2= 0
c3 = 0

st.title("Welcome to Mathart")

#Inputs
option = st.selectbox(
    "What equation would you like to use for your art",
    ("first equation", "second equation"),
    index=None,
    placeholder="Select an equation",
)

if option == "first equation":
    labels = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = values

    fig, ax = plot.initFigureWindow()
    trace = plot.initLine(ax)

    z1 = st.number_input("Enter z1 (-z1*theta): ", value=5)
    z2 = st.number_input("Enter z2 (z2*theta): ", value=5)
    theta = np.linspace(-z1*np.pi, z2*np.pi, 2000)

    #axis
    st.write("Enter bounds [xmin, xmax, ymin, ymax]")

    xmin = st.number_input("xmin", value=-20.0)
    xmax = st.number_input("xmax", value=20.0)
    ymin = st.number_input("ymin", value=-20.0)
    ymax = st.number_input("ymax", value=20.0)

    bounds = [xmin, xmax, ymin, ymax]

    ax.axis(bounds) #[-x, x, -y, y] ask as input

    if st.button("Create Art"):

        eqn_1 = equations.first_eqn(a1,a2,a3,b1,b2,b3,c1,c2,c3,theta)
    #eqn_2 = equations.sec_eqn(8,-6,8,3,theta)
        myanimation = anim.FuncAnimation(fig, lambda frame:plot.animag(frame, trace,eqn_1),
                                     frames = 2000, interval = 10 )

        save_path = "Anim.mp4"
        myanimation.save(save_path, fps=10)

        # Display animation inline
        components.html(myanimation.to_jshtml(), height=600)

        # Add download button
        with open(save_path, "rb") as f:
            mp4_bytes = f.read()

        st.download_button(
            label="Download Animation",
            data=mp4_bytes,
            file_name="Anim.mp4",
            mime="video/mp4"
        )





