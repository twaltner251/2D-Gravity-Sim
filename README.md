## The goal of this project is to create a simple, fun, interactive simulation to observe how N amount of objects with radius R and density D interact with eachother's gravitational pull.

Left click anywhere on the pygame screen to add a ball, and see how they interact!

Video of Stationary Center Mass:
<img src="Stationary_Center_Mass.gif" alt="App Demo GIF" width="600" />

Video of Movable Center Mass:
<img src="Movable_Center_Mass.gif" alt="App Demo GIF" width="600" />

Demo Video:
<img src="Demo_Video.gif" alt="App Demo GIF" width="600" />

Version 2 Optimizations and Updates:
* Switched from Euler integration to Verlet int
* Stored mass in ball class to save computation
* Fixed incorrect mass calculation, previously had m = d/v when in reality it is m = d*v
* Implemented dt variable instead of constant like 0.016s (1/60, 60fps) so we can determine actual time passed as # each loop wont be perfectly same amount of time of 0.016s
* Organized control code into main()
* Added collsion with walls constant "B" representing Bounce factor
* Added optional high density mass, can be configured by user thru terminal. User can configure the density, and whether or not it is stationary. (if it is affected by surrounding ball's gravity or not)

Previous Version README:
My implementation of a simple 2D Gravity Sim first starts with defining my constants that are integral to the environment and behavior of my sim.

My ball class handles the pos as a list, and tracks the x/y velocities, radius, and density of each ball, defined upon initialization. It also includes a update_pos() method that applies the current x/y velociy to our x/y position.

After that we have a distance() helper method that calculates the Euclidean distance given two positions.

The update() method handles the gravity logic.

After that we use a typical pygame setup with a while loop to handle each frame, and creating balls upon MOUSEDOWN events.
