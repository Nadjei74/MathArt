

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as anim
from matplotlib.animation import FFMpegWriter, PillowWriter
import streamlit as st
import streamlit.components.v1 as components
from plot import *
import plotly.graph_objects as go
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import os
import time


st.title("Welcome to Mathart")

#Place_holders
eqn_func = None
opt_transform =None
values = []
x = None
y = None

# Inputs
option = st.selectbox(
    "What equation would you like to use for your art",
    ("hypospirograph", "epispirograph", "second equation", "Lissajous","third equation", "butterfly equation",
     "fourth equation", "fifth equation", "sixth equation", "seventh equation", "eighth equation","nineth equation",
     "tenth equation", "eleventh equation", "twelfth equation", "thirteenth equation","fourteenth equation", "fifteenth equation",
     "sixteenth equation", "seventeenth equation"
     ),
    index=None,
    placeholder="Select an equation",
)

if option == "hypospirograph":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned} x &= (a-b)\cos(\theta) + c\cos\!\left(\frac{a-b}{b}\,\theta\right) \\ 
                y &= (a-b)\sin(\theta) - c\sin\!\left(\frac{a-b}{b}\,\theta\right) \end{aligned}
            """)
    labels = ['a','b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.hypospirograph
    opt_transform = "No"

elif option == "epispirograph":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned} x &= (a+b)\cos(\theta) + c\cos\!\left(\frac{a+b}{b}\,\theta\right) \\
                 y &= (a+b)\sin(\theta) + c\sin\!\left(\frac{a+b}{b}\,\theta\right) \end{aligned}
            """)
    labels = ['a','b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.epispirograph
    opt_transform = "No"

elif option == "second equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                   x = a \cos(\theta) - b \cos\left(\frac{c \theta}{d}\right)\\                   
                   y = a \sin(\theta) - b \sin\left(\frac{c \theta}{d}\right)
               """)
    labels = ['a', 'b', 'c', 'd']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.sec_eqn
    opt_transform = "No"

elif option == "Lissajous":
    with st.expander("Parametric equation"):
        st.latex(r"""
                    \begin{aligned}
                    x &= a \sin\left(b\theta + \frac{\pi}{2}\right) \\
                    y &= c \sin(d\theta)
                    \end{aligned}\\
                    Hints: a =5 , b= 5, c = 3, d = 4\\
                           a= 5 , b= 5, c =3 , d=2\\
                           a= 5 , b= 3, c= 3, d =4 \\
                           a= 5 , b= 3, c= 3, d =5 
                    """)
    labels = ['a', 'b', 'c','d']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.Lissajous
    opt_transform = "No"

elif option == "third equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= a \sin(\theta) +  b \cos\left(c\theta + \frac{\pi}{2}\right) \\
                y &= a \cos(d\theta)
                \end{aligned}\\
                Hints: a =5 , b= 7, c = 5, d = 3 (beetle)\\
                           a= 5 , b= 3, c =5 , d=7\\
                           a =5 , b= 7, c = 5, d = 4 \\
                           a= 5 , b= 3, c= 3, d =5 
                """)
    labels = ['a', 'b', 'c', 'd']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.third_eqn
    opt_transform = "No"


elif option == "butterfly equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                    \begin{aligned}
                    x &= \sin(\theta)\Big(\exp(\cos(\theta)) - a\cos(b\theta) - \sin\!\left(\tfrac{\theta}{c}\right)^{5}\Big) \\
                    y &= \cos(\theta)\Big(\exp(\cos(\theta)) - a\cos(b\theta) - \sin\!\left(\tfrac{\theta}{c}\right)^{5}\Big)
                    \end{aligned}\\
                    Hints: a =5 , b= 3, c = 3 , (3-winged),\\
                           a= 5 , b= 4, c =3 ,(6-winged)\\
                           a =5 , b= 4, c = 2,(6-winged) \\
                           a= 5 , b= 4, c= 7, (6-winged)
                    
""")
    labels = ['a', 'b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.butterfly
    opt_transform = "No"

elif option == "fourth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= \sin(\theta)\,\tan\!\left(\frac{a\theta}{b}\right) \\
                y &= \cos(\theta)\,\tan\!\left(\frac{a\theta}{b}\right)
                \end{aligned}
                     Hints: a =5 , b= 9,\\
                           a= 5 , b= 4, \\
                           a =7 , b= 9,  \\
                           a= 9 , b= 7,               
                """)
    labels = ['a', 'b',]
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.fourth_eqn
    opt_transform = "No"

elif option == "fifth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= a \cos(\theta) - b \cos\left(\frac{c\theta}{d}\right) \\
                y &= a \sin(\theta) - b \sin\left(\frac{c\theta}{d}\right)
                \end{aligned}
                """)
    labels = ['a', 'b', 'c', 'd']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.fifth_eqn
    opt_transform = "No"

elif option == "sixth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= a \sin(b\theta)\,\cos\!\big(\cos(c\theta)\big) \\
                y &= a \cos^{2}(b\theta)\,\sin\!\big(\sin(c\theta)\big)
                \end{aligned}
                """)
    labels = ['a', 'b', 'c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.sixth_eqn
    opt_transform = "No"

elif option == "seventh equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= a\theta + b\cos(b\theta) + \frac{1}{\theta} \\
                y &= a\theta + b\sin(b\theta) + \frac{1}{\theta}
                \end{aligned}
                """)
    labels = ['a', 'b',]
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.seventh_eqn
    opt_transform = "No"

elif option == "eighth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned}
                x &= \cos(\theta) + \frac{1}{a}\Big(\cos(b\theta) + \sin(c\theta)\Big) \\
                y &= \sin(\theta) + \frac{1}{a}\Big(\sin(b\theta) + \cos(c\theta)\Big)
                \end{aligned}
                """)
    labels = ['a', 'b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.Eigth_eqn
    opt_transform = "No"

elif option == "nineth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        z = a \tan(b\theta) + \frac{1}{\tan(b\theta)}
        """)
    labels = ['a', 'b']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.nineth_eqn
    opt_transform = "No"

elif option == "tenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        z = e^{\tfrac{\theta}{a}}
        """)
    labels = ['a']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.tenth_eqn
    opt_transform = "No"

elif option == "eleventh equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        z = \sqrt{\theta}
        """)
    labels = []
    values = []
    eqn_func = equations.eleventh_eqn
    opt_transform = "No"

elif option == "twelfth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        \begin{aligned}
        x &= a \big(\cos(b\theta)\big)^{2.5} \\
        y &= c \,\sin\!\Big(\sin\!\left(\tfrac{d\theta}{\pi}\right)\Big)\,\big(\cos\!\left(\tfrac{b\theta}{\pi}\right)\big)^{2}
        \end{aligned}
        """)
    labels = ['a', 'b', 'c', 'd']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.twelfth_eqn
    opt_transform = st.selectbox("Would you like to perform a rotational transformation",
                                 ("Yes", "No"),
                                 index=None, )

elif option == "thirteenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        \begin{aligned}
        x &= a \left(\frac{\sin\!\left(\tfrac{b\theta}{\pi}\right)}{1 + \operatorname{round}\!\Big(\sin^{2}\!\left(\tfrac{\theta}{\pi}\right)\Big)}\right) \\
        y &= a \cos\!\Big(\operatorname{round}\!\left(\tfrac{\theta}{\pi}\right)\Big)\,\Big(\sin\!\left(\tfrac{b\theta}{\pi}\right)\Big)^{4}
        \end{aligned}
        """)
    labels = ['a', 'b']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.thirteenth_eqn
    opt_transform = st.selectbox("Would you like to perform a rotational transformation",
                                 ("Yes", "No"),
                                 index=None, )


elif option == "fourteenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        \begin{aligned}
        x &= a \,\sin(b\theta)\,\operatorname{round}\!\Big(\sqrt{\cos\!\big(\cos(\tfrac{c\theta}{\pi})\big)}\Big) \\
        y &= a \,\cos(b\theta)\,\sin\!\Big(\sin(c\theta)\Big)
        \end{aligned}
        """)
    labels = ['a', 'b', 'c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.fourteenth_eqn
    opt_transform = st.selectbox("Would you like to perform a rotational transformation",
                                 ("Yes", "No"),
                                 index=None, )

elif option == "fifteenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
        \begin{aligned}
        x &= a \big(\cos(b\theta)\big)^{2.5} \\
        y &= c \,\sin\!\Big(\sin\!\left(\tfrac{d\theta}{\pi}\right)\Big)\,\big(\cos\!\left(\tfrac{b\theta}{\pi}\right)\big)^{2}
        \end{aligned}
        """)
    labels = ['a', 'b', 'c', 'd']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.fifth_eqn
    opt_transform = st.selectbox("Would you like to perform a rotational transformation",
                                 ("Yes", "No"),
                                 index=None, )


elif option == "sixteenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned} x &= (a-b)\cos(\theta) + c\cos\!\left(\frac{a-b}{a}\,\theta\right) \\ 
                y &= (a-b)\sin(\theta) - c\sin\!\left(\frac{a-b}{a}\,\theta\right) \end{aligned}
            """)
    labels = ['a','b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.sixteenth
    opt_transform = "No"

elif option == "seventeenth equation":
    with st.expander("Parametric equation"):
        st.latex(r"""
                \begin{aligned} x &= (a+b)\cos(\theta) + c\cos\!\left(\frac{a+b}{a}\,\theta\right) \\
                 y &= (a+b)\sin(\theta) + c\sin\!\left(\frac{a+b}{a}\,\theta\right) \end{aligned}
            """)
    labels = ['a','b','c']
    values = [st.number_input(f"Enter {label}", min_value=-100.0, step=0.1) for label in labels]
    eqn_func = equations.seventeenth
    opt_transform = "No"


#fig, ax = plot.initFigureWindow()
#trace = plot.initLine(ax)

z1 = st.number_input("Enter z1 (-z1*theta): ", value=5)
z2 = st.number_input("Enter z2 (z2*theta): ", value=5)
theta = np.linspace(-z1 * np.pi, z2 * np.pi, 1800)


# axis
st.write("Enter bounds [xmin, xmax, ymin, ymax]")

xmin = st.number_input("xmin", value=-20.0)
xmax = st.number_input("xmax", value=20.0)
ymin = st.number_input("ymin", value=-20.0)
ymax = st.number_input("ymax", value=20.0)

bounds = [xmin, xmax, ymin, ymax]


if eqn_func is not None and values:
    x, y = eqn_func(values, theta)

#############if here

#Initial traces
if opt_transform =="Yes":
    angle = st.text_input("Enter the angeles for transformation (e.g 15, 30, 45) ")
    origin = st.text_input("Enter the origin of rotation (e.g   0, 0)")
    angle_list, origin_list = [], []
    if angle:
        try:
            angle_list = [float(x.strip()) for x in angle.split(',')]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")

    if origin:
        try:
            origin_list = [float(x.strip()) for x in origin.split(',')]
        except ValueError:
            st.error("Please enter valid numbers for origin.")


    rotated_list = []

    coords = np.vstack((x,y))
    if len(origin_list) == 2:
        coords = coords - np.array(origin_list).reshape(2,1)
    else:
        st.warning("Please enter two numbers for the origin (e.g. 0, 0).")

    for ang in angle_list:
        rad = np.deg2rad(ang)
        transform= np.array([[np.cos(rad), -np.sin(rad)],
                             [np.sin(rad), np.cos(rad)

        ]])
        if len(origin_list) == 2:
            rotated_list.append((transform @ coords) + np.array(origin_list).reshape(2,1) )

    fig = go.Figure()
    num_curves = len(rotated_list) + 1
    paint = [mcolors.to_hex(cm.tab10(i % 10)) for i in range(num_curves)]

    fig.add_trace(go.Scatter(x=[], y=[], mode="lines", name="Original", line=dict(color="white")))
    #Add empty traces for each rotated curve
    for j, color in enumerate(paint[1:]):
        fig.add_trace(go.Scatter(x=[], y = [], mode="lines", name=f"Rotated{angle[j]}°", line=dict(color=color)))

    #Animating the frames
    frames = []
    for k in range(0, len(x), 1):
        frame_data = []

        # Original curve up to k
        frame_data.append(go.Scatter(x=x[:k], y=y[:k], mode="lines", line=dict(color="black")))

        for j, rotated in enumerate(rotated_list):
            frame_data.append(go.Scatter(x=rotated[0, :k], y=rotated[1, :k], mode="lines",line=dict(color=paint[j])))
        frames.append(go.Frame(data=frame_data, name=str(k)))

else:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode="lines", name="Original", line=dict(color="white")))
    frames = []
    if x is not None and y is not None:
        for i in range(0, len(x), 1):  # step for speed
            frames.append(go.Frame(
                data=[
                    go.Scatter(x=x[:i], y=y[:i], mode="lines", line=dict(color="red")),
                ],
                name=str(i)
            ))

fig.frames = frames

#Layout

fig.update_layout(
    xaxis=dict(range=[xmin, xmax]),
    yaxis=dict(range=[ymin, ymax],scaleanchor="x"),
    title="Multiple Rotated Curves Animation",
    updatemenus=[{
        "buttons": [
            {"args": [None, {"frame": {"duration": 20, "redraw": True},
                             "fromcurrent": True, "transition": {"duration": 0}}],
             "label": "Play",
             "method": "animate"},
            {"args": [[None], {"frame": {"duration": 0, "redraw": False},
                               "mode": "immediate",
                               "transition": {"duration": 0}}],
             "label": "Pause",
             "method": "animate"}
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }]
)

#Layout with play/pause
# --- Streamlit Display ---
st.plotly_chart(fig, use_container_width=True)

