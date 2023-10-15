import open3d as o3d
import numpy as np
import os

number_of_points = 10000
a = 0
b = 0
c = 0


def arrange_objects(n, object_size, spacing):

 
    object_clouds = []


    for i in range(n):
        global a, b, c
        a = a + 0.0001
        b = b + 0.0001
        c = c + 0.0001


        object_mesh = o3d.geometry.TriangleMesh.create_box(width=object_size, height=object_size, depth=object_size)


        rotation = (a, b, c) 
        object_mesh.rotate(o3d.geometry.get_rotation_matrix_from_xyz(rotation), center=(0,0,0))

        #Zufällige Positionen im Raum
        position = np.random.rand(3) * spacing * n - (spacing * (n-1) / 2)
        object_mesh.translate(position)


        object_cloud = object_mesh.sample_points_uniformly(number_of_points)

        #Zufällige Farbe
        object_color = np.random.rand(3)
        object_cloud.paint_uniform_color(object_color)

        #Zu Visualisierungsliste hinzufügen
        object_clouds.append(object_cloud)

    #aus object_clouds ein objekt mit allen Punkteansammlungen machen
    arranged_objects = o3d.geometry.PointCloud()
    for object_cloud in object_clouds:
        arranged_objects += object_cloud
    return arranged_objects


arranged_point_cloud = arrange_objects(n=500, object_size=10, spacing=0.8)




# Visualize the arranged point cloud
o3d.visualization.draw_geometries([arranged_point_cloud])
os.system('htop')