from docplex.mp.model import Model

mdl = Model(name=f"test")

mdl.x = mdl.integer_var(lb=0, ub=10)
mdl.y = mdl.integer_var(lb=0, ub=10)

mdl.maximize(mdl.x + mdl.y)

mdl.solve(log_output=True)
mdl.print_solution()
