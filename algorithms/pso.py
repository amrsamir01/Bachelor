import random
import timeit
import numpy as np

#follow the bird which is nearest to the food


'''Fitness function
We assume the problem can be expressed by the following equation: f(x1,x2)=(x1+2*-x2+3)^2 + (2*x1+x2-8)^2
The objective is to find the minimum fitness function'''
def fitness_function(x1,x2):
    return (x1+2*-x2+3)**2 + (2*x1+x2-8)**2

'''The velocity adjustment is influenced by 3 factors: 
- the previous velocity (Inertia component)
- the individual particle best position (Cognitive component) 
- the swarm best positions (Social component)'''
def update_velocity(particle, velocity, pbest, gbest, min=0.5, max=1.0, c=0.1):
  # Initialise new velocity array
  num_particle = len(particle)
  new_velocity = np.array([0.0 for i in range(num_particle)])
  # Randomly generate r1, r2 and inertia weight from normal distribution
  r1 = random.uniform(0,max) #r1 and r2 denote hyper parameters and they cause some random perturbations. 
  r2 = random.uniform(0,max)
  w = random.uniform(min,max) #The coefficient w is called inertia weight which is a force to keep the particle moving in the same direction as the previous generation
  c1 = c #c1 and c2 are constant acceleration values where
  c2 = c
  # Calculate new velocity
  for i in range(num_particle):
    new_velocity[i] = w*velocity[i] + c1*r1*(pbest[i]-particle[i])+c2*r2*(gbest[i]-particle[i])
  return new_velocity

def update_position(particle, velocity):
  # Move particles by adding velocity
  return particle + velocity

def pso(population, position_min, position_max, generation):
  # Initialisation
  # Population
  dimension = 2
  particles = [[random.uniform(position_min, position_max) for j in range(dimension)] for i in range(population)]
  # Particle's best position
  pbest_position = particles
  # Fitness
  pbest_fitness = [fitness_function(p[0],p[1]) for p in particles]
  # Index of the best particle
  gbest_index = np.argmin(pbest_fitness)
  # Global best particle position
  gbest_position = pbest_position[gbest_index]
  # Velocity (starting from 0 speed)
  velocity = [[0.0 for j in range(dimension)] for i in range(population)]
  
  # Loop for the number of generation
  for t in range(generation):
    # Stop if the average fitness value reached a predefined success criterion
    if np.average(pbest_fitness) <= 0.001:
      break
    else:
      for n in range(population):
        # Update the velocity of each particle
        velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
        # Move the particles to new position
        particles[n] = update_position(particles[n], velocity[n])
    # Calculate the fitness value
    pbest_fitness = [fitness_function(p[0],p[1]) for p in particles]
    # Find the index of the best particle
    gbest_index = np.argmin(pbest_fitness)
    # Update the position of the best particle
    gbest_position = pbest_position[gbest_index]

  # Print the results
  print('Global Best Position: ', gbest_position)
  print('Best Fitness Value: ', min(pbest_fitness))
  print('Average Particle Best Fitness Value: ', np.average(pbest_fitness))
  print('Number of Generation: ', t)

starttime = timeit.default_timer()
print("The start time is :",starttime)
pso(100, -100.0, 100.0, 400)
print("The end time is :",timeit.default_timer())
print("The time difference is :", timeit.default_timer() - starttime)


