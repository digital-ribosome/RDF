import numpy as np
import matplotlib.pyplot as plt

#Calculation RDF
def calculate_rdf(coordinates, storona, dr, max_radius):
    num_particles = len(coordinates)
    rdf = np.zeros(int(max_radius / dr) + 1)
    normirovka = np.zeros(int(max_radius / dr) + 1)
    rdf_4ast = np.zeros(int(max_radius / dr) + 1)
    num_dist = 0
    min_dist = max_radius
    for i in range(num_particles):
        for j in range(num_particles):
          if (i != j and
              coordinates[i, 0] >= max_radius and
              coordinates[i, 0] <= (storona - max_radius) and
              coordinates[i, 1] >= max_radius  and
              coordinates[i, 1] <= (storona - max_radius)):
              #border conditions check
              distance = np.sqrt((coordinates[i, 0] - coordinates[j, 0]) ** 2 + (coordinates[i, 1] - coordinates[j, 1]) ** 2)
              if min_dist >= distance:
                min_dist = distance
              if distance <= max_radius:
                num_dist += 1
                bin_index = int(distance / dr)
                rdf[bin_index] += 2  # Count both particles

    for i in range(len(normirovka)):
      normirovka[i] = np.pi * (((i + 1) * dr) ** 2) - (((i ) * dr) **2)

    rdf /= np.pi *(np.arange(dr, max_radius + dr, dr)) * dr * (num_particles*num_particles) / ((storona**2))
    return rdf

#Ploting RDF
def plot_rdf(rdf, dr, max_radius):
    r_values = np.arange(dr, max_radius, dr)
    rdf_nolast = np.delete(rdf, -1)
    plt.figure(1)
    plt.plot(r_values, rdf_nolast)
    plt.xlabel('r')
    plt.ylabel('g(r))')

#Ploting map
def dot_map(coordinates):
    x_values = coordinates[:, 0]
    y_values = coordinates[:, 1]
    # Create a scatter plot
    plt.figure(2)
    plt.scatter(x_values, y_values)
    # Customize the plot
    plt.title('2D Image of objects')
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')

# File name and constants
coordinates = np.loadtxt('aunp1', skiprows = 1) #x,y coordinates set
storona = 15e-06	#picture size
dr = storona/400.1	#rdf step
max_radius = storona/4 	#boundary conditions
rdf = calculate_rdf(coordinates, storona, dr, max_radius)

#Ploting
dot_map(coordinates)
plot_rdf(rdf, dr, max_radius)
plt.show()
