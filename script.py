# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#turn up the Temperature
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
# comment 2
f100_in_celsius = f_to_c(100)

print(f100_in_celsius)
# Comment 3
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5)) + 32
  return f_temp
#comment 4
c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)

#use the force
# comment 5
def get_force(mass, acceleration):
  return mass * acceleration
#comment 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

#comment 7
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#comment 8 
def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print(bomb_energy)

#comment 9
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#comment 10 
def get_work(mass, acceleration, distance):
  force = mass * acceleration
  return force * distance
# comment 11
train_work = get_work(train_mass, train_acceleration, train_distance)
#comment 12
print(train_work)

#comment 13
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
