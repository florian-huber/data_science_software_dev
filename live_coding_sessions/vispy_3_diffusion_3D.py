import numpy as np
from vispy import app, scene
from vispy.app import Timer

def diffuse_3d(x, y, z, step_size=0.1):
    x += np.random.normal(scale=step_size, size=x.shape)
    y += np.random.normal(scale=step_size, size=y.shape)
    z += np.random.normal(scale=step_size, size=z.shape)
    return x, y, z

canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

# Set up a 3D camera
view.camera = scene.cameras.TurntableCamera(fov=45, distance=50)

n_points = 2000
x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
y = np.random.normal(loc=0.0, scale=10.0, size=n_points)
z = np.random.normal(loc=0.0, scale=10.0, size=n_points)

colors = np.random.rand(n_points, 4)
colors[:, 0] = 1.0  # Make the cubes primarily red
colors[:, 3] = 1.0  # Fully opaque

scatter = scene.visuals.Markers()
scatter.set_data(np.array([x, y, z]).T, face_color=colors, size=5)
view.add(scatter)

def update(event):
    global x, y, z
    x, y, z = diffuse_3d(x, y, z)
    scatter.set_data(np.array([x, y, z]).T, face_color=colors, size=5)

timer = Timer(interval=0.05, connect=update, start=True)

if __name__ == '__main__':
    app.run()