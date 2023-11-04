import bokeh.plotting as bkp
import random

def run():
    
    bkp.output_file('izigraph.html')
    fig=bkp.figure()

    total_vals=random.randint(1,1000)
    x_vals=[random.randint(0,100) for i in range(total_vals)]
    y_vals=[]

    for i in x_vals:
        y_vals.append(((i*i)**(1/random.randint(1,4)))*random.randint(1,100))

    fig.scatter(x_vals, y_vals)
    bkp.show(fig)

if __name__ == "__main__":
    run()

