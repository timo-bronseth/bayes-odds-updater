from textwrap import fill, dedent, wrap, TextWrapper
# from str import join
import re

evidence_name = "clinical trial"
belief_names = ['positive effect', 'no effect', 'negative effect']
my_string = f"""
                         List your likelihood ratios for the following (e.g. if {belief_names[0]}
                         is true, how much more likely would you be to observe {evidence_name}
                         compared to if other hypotheses were true?):\n
                         {belief_names}:
    
                     > 
                     """

for line in my_string.split('\n'):
    dedent(line)
    print(line)

# print(fill(re.sub(' {2}', '', my_string), break_long_words=False, replace_whitespace=True))


# TODO: Look at this https://stackoverflow.com/questions/1166317/python-textwrap-library-how-to-preserve-line-breaks
