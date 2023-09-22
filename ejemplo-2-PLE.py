from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximizar beneficios', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# VARIABLES
a = solver.IntVar(0, solver.infinity(), 'inversión 1')
b = solver.IntVar(0, solver.infinity(), 'inversión 2')
c = solver.IntVar(0, solver.infinity(), 'inversión 3')
d = solver.IntVar(0, solver.infinity(), 'inversión 4')

# RESTRICCIONES
solver.Add(5000*a + 7000*b + 4000*c + 3000*d <= 14000)  # dinero disponible para invertir
# no podemos invertir más de una vez en el mismo producto
solver.Add(0<= a <= 1)
solver.Add(0<= b <= 1)
solver.Add(0<= c <= 1)
solver.Add(0<= d <= 1)


# FUNCION a maximizar
solver.Maximize(16000*a + 22000*b + 12000*c + 8000*d)

# SOLUCIONADOR
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('================= Solución =================')
    print(f'Beneficio óptimo = {solver.Objective().Value()} euros')
    print('Mejores inversiones:')
    if a.solution_value() == 1:
        print(f' - Invertir en el producto 1')
        # si no, no imprimir nada
    if b.solution_value() == 1:
        print(f' - Invertir en el producto 2')
    if c.solution_value() == 1:
        print(f' - Invertir en el producto 3')
    if d.solution_value() == 1:
        print(f' - Invertir en el producto 4')    

else:
    print('No se pudo encontrar solución óptima.')
