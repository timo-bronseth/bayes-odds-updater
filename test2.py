# Cast all the arguments as lists if they contain more than one item.
prior_beliefs, likelihood_ratios, belief_names, evidence_name = "a, b, c, d, e,f", 'b', 'c', 'd'
args = [prior_beliefs, likelihood_ratios, belief_names, evidence_name]
args = [[sentence.strip() for sentence in arg.split(',')] for arg in
        args]  # List comprehension INSIDE list comprehension
print(args)
prior_beliefs, likelihood_ratios, belief_names, evidence_name = args[0], args[1], args[2], args[3]
# sad can't use *args here :c
