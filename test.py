from textwrap import fill, dedent, wrap, TextWrapper
evidence_name = "clinical trial"
belief_names = ['drug positive effect', 'no effect', 'negative effect']
my_string = TextWrapper(f"""
                         List your likelihood ratios for the following (e.g. if {belief_names[0]}
                         is true, how much more likely would you be to observe {evidence_name} compared to if
                         other hypotheses were true?):
                         {belief_names}:
    
                     > 
                     """, break_long_words=False,replace_whitespace=False)
print(my_string)

# TODO: Look at this https://stackoverflow.com/questions/1166317/python-textwrap-library-how-to-preserve-line-breaks