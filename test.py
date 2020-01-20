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
