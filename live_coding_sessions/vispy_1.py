import numpy as np
from vispy import app, scene

# Create a canvas with an interactive view
canvas = scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

# Use a camera suitable for a 2D scene
view.camera = scene.cameras.PanZoomCamera(aspect=1)

# Generate some random 2D points
n_points = 1000
x = np.random.normal(loc=0.0, scale=1.0, size=n_points)
y = np.random.normal(loc=0.0, scale=1.0, size=n_points)

# Create a scatter visual
scatter = scene.visuals.Markers()
scatter.set_data(np.array([x, y]).T, face_color='red', size=5)
view.add(scatter)

if __name__ == '__main__':
    app.run()