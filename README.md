# Heat-Dispersion-Simulator
Python Application that simulates heat dispersion on a 2D Plane
Utilizes the PyPlot API to create images showcasing the dispersion of heat on a 2D Plane.

Algorithm for calculating the temperature for each cell is adapted from the following formula:
temp[i, j] = 1/4(oldTemp[i-1, j] + oldTemp[i+1, j] + oldTemp[i, j-1] + oldTemp[i, j+1])

This formula calculates the current temperature using the temperature at the cardinal neighbors at the previous state. Calculations end at convergence, where two consecutive iterations result in the same values at each cell.
