# Optimal indexing in NumPy
Using views so as to reduce memory usage.
Use slices with `[:]` or `slice()`.

# Differential equations 101
Ordinary Differential Equations (ODEs) require initial conditions to determine a unique solution.
Partial Differential Equations (PDEs) require initial conditions and boundary conditions (depending on the problem) to specify a unique solution.

💡 Why?

ODEs describe functions of one variable (typically time), so an initial value pins down the solution.
PDEs involve multiple variables (e.g., time and space), so boundary conditions are needed to handle the spatial components, along with initial conditions for time evolution (if it's time-dependent).