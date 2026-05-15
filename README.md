Video of Stationary Center Mass: https://github.com/user-attachments/assets/4e852bcf-9886-4dcf-b397-aef5f6212c0f

Video of Movable Center Mass: https://github.com/user-attachments/assets/f085d930-54df-4a8a-aa9a-400a3815ae28


Version 2 Optimizations and Updates:
[o] Switched from Euler integration to Verlet int 

[o] Stored mass in ball class to save computation 

[o] Fixed incorrect mass calculation, previously had m = d/v when in reality it is m = d*v 

[o] Implemented dt variable instead of constant like 0.016s (1/60, 60fps) so we can determine 
    actual time passed as # each loop wont be perfectly same amount of time of 0.016s 
    
[o] Organized control code into main()

[o] Added collsion with walls constant "B" representing Bounce factor

[o] Added optional high density mass, can be configured by user thru terminal. User can 
    configure the density, and whether or not it is stationary. (if it is affected by 
    surrounding ball's gravity or not)

Previous Version README:

Demo Video: https://github.com/user-attachments/assets/b38f8a42-2b2a-40e1-86ba-6be766dfd7b6

The goal of this project is to create a simple, fun, interactive simulation to observe how N amount of objects with radius R and density D interact with eachother's gravitational pull.
Left click anywhere on the pygame screen to add a ball, and see how they interact!

My implementation of a simple 2D Gravity Sim first starts with defining my constants that are integral to the environment and behavior of my sim.

My ball class handles the pos as a list, and tracks the x/y velocities, radius, and density of each ball, defined upon initialization. 
It also includes a update_pos() method that applies the current x/y velociy to our x/y position.

After that we have a distance() helper method that calculates the Euclidean distance given two positions.

The update() method handles the gravity logic.

After that we use a typical pygame setup with a while loop to handle each frame, and creating balls upon MOUSEDOWN events.
