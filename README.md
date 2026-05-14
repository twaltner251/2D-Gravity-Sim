The goal of this project is to create a simple, fun, interactive simulation to observe how N amount of objects with radius R and density D interact with eachother's gravitational pull.
Left click anywhere on the pygame screen to add a ball, and see how they interact!

My implementation of a simple 2D Gravity Sim first starts with defining my constants that are integral to the environment and behavior of my sim.

My ball class handles the pos as a list, and tracks the x/y velocities, radius, and density of each ball, defined upon initialization.
It also includes a update_pos() method that applies the current x/y velociy to our x/y position.

After that we have a distance() helper method that calculates the Euclidean distance given two positions.

The update() method handles the gravity logic.

After that we use a typical pygame setup with a while loop to handle each frame, and creating balls upon MOUSEDOWN events.
