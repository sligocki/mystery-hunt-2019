import random

class Formula:
  def __init__(self, const):
    self.const = const
    self.terms = []

  def add(self, coef, symb):
    self.terms.append((coef, symb))

  def Evaluate(self, values):
    total = self.const
    for coef, symb in self.terms:
      total += coef * values[symb]
    return total


def load_puzzle(f):
  formulas = []
  vars = set()
  for line in f:
    parts = line.split()
    f = Formula(int(parts[0]))
    for i in range(1, len(parts), 2):
      if parts[i] == "+":
        coef = 1
      elif parts[i] == "-":
        coef = -1
      else:
        assert False, parts[i]
      var = parts[i+1]
      f.add(coef, var)
      vars.add(var)
    formulas.append(f)
  return formulas, vars


def try_valuation(formulas, values):
  success = True
  results = []
  for formula in formulas:
    result = formula.Evaluate(values)
    if result < 0:
      success = False
    results.append(result)
  return success, results


def find_random_improvement(results, formulas, constraints):
  bad_indexes = [i for i in range(len(results))
                 if results[i] < 0]
  chosen_index = random.choice(bad_indexes)
  coef, var = random.choice([(coef, var) for (coef, var) in formulas[chosen_index].terms
                             if var not in constraints])
  return coef, var


def greedy_optimizer(formulas, vars, constraints={}):
  """Uses a simple greedy algorithm to try and find a valuation that
  makes all formulas non-negaive."""
  # Start with all 0 valuations
  values = {var: 0 for var in vars}
  for var in constraints:
    values[var] = constraints[var]
  i = 0
  while True:
    success, results = try_valuation(formulas, values)
    #print()
    #print(i)
    #print(values, sum(abs(val) for val in values.values()))
    #print(results, sum(result for result in results if result < 0))
    if success:
      return values
    coef, var = find_random_improvement(results, formulas, constraints)
    values[var] += coef
    i += 1


def find_range(formulas, vars, iters):
  good_vals = {var : [] for var in vars}
  # Run many simulations
  for _ in range(iters):
    vals = greedy_optimizer(formulas, vars)
    for var in vars:
      good_vals[var].append(vals[var])
  # Check ranges
  for var in sorted(vars):
    print(var, min(good_vals[var]), max(good_vals[var]))


import sys
filename = sys.argv[1]
with open(filename) as f:
  formulas, vars = load_puzzle(f)

# A) Find any valuations for variables that makes all formulas non-negativ$
print(greedy_optimizer(formulas, vars))

# B) Run many opimizations and see the ranges you get.
#iters = int(sys.argv[2])
#print(find_range(formulas, vars, iters))

# C) Find valuations with a constraint.
#print(greedy_optimizer(formulas, vars, {"◇" : int(sys.argv[2])}))
