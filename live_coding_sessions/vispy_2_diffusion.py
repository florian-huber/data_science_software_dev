import numpy as np
from vispy import app, scene
from vispy.app import Timer

# Diffusion function: adds Gaussian noise to particle positions
def diffuse(x, y, step_size=0.1):
    x += np.random.normal(scale=step_size, size=x.shape)
    y += np.random.normal(scale=step_size, size=y.shape)
    return x, y

canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

view.camera = scene.cameras.PanZoomCamera(aspect=1)

n_points = 1000
x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
y = np.random.normal(loc=0.0, scale=10.0, size=n_points)

scatter = scene.visuals.Markers()
scatter.set_data(np.array([x, y]).T, face_color='red', size=5)
view.add(scatter)

def update(event):
    global x, y
    x, y = diffuse(x, y)
    scatter.set_data(np.array([x, y]).T, face_color='red', size=5)

timer = Timer(interval=0.05, connect=update, start=True)

if __name__ == '__main__':
    app.run()