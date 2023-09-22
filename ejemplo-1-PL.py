# importaciones
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximizar beneficios', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


# VARIABLES
x = solver.IntVar(0, solver.infinity(), 'collares')
y = solver.IntVar(0, solver.infinity(), 'pulseras')


# RESTRICCIONES
solver.Add(x + y <= 50)
solver.Add(2*x + y <= 54) 
solver.Add(x >= 0) 
solver.Add(y >= 0)

# FUNCION a maximizar
solver.Maximize(5*x + 4*y)


# SOLVE the problem
status = solver.Solve()
# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
    print('================= Solución =================')
    #print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
    #print()
    print(f'Beneficio óptimo = {solver.Objective().Value()} euros')
    print('Fabricación:')
    print(f' - Collares = {x.solution_value()}')       
    print(f' - Pulseras = {y.solution_value()}')       

# If no optimal solution has been found, print the status
else:
    print('No se pudo encontrar solución óptima.')
