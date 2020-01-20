from textwrap import fill, dedent, wrap, TextWrapper
# from str import join
import re

evidence_name = "clinical trial"
belief_names = ['positive effect', 'no effect', 'negative effect']
likelihood_ratios = fill("List your likelihood ratios for the following hypotheses given the evidence " +
                 f"(e.g. if [{belief_names[0]}] is true, how much more likely would you be to " +
                 f"observe [{evidence_name}] compared to if other hypotheses were true?):", 80) +\
                 f"\n\n{belief_names}:" +\
                 "\n\n" +\
                 " > "

input(likelihood_ratios)

# Cast all the arguments as lists if they contain more than one item.
prior_beliefs, likelihood_ratios, belief_names, evidence_name = "a, b, c, d, e,f", 'b', 'c', 'd'
args = [prior_beliefs, likelihood_ratios, belief_names, evidence_name]
args = [[sentence.strip() for sentence in arg.split(',')] for arg in
        args]  # List comprehension INSIDE list comprehension
print(args)
prior_beliefs, likelihood_ratios, belief_names, evidence_name = args[0], args[1], args[2], args[3]
# sad can't use *args here :c
