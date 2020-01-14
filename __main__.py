"""
    end goal: be able to have columns of beliefs, evidence, likelihood ratios, and calculate conclusions.
    It should be practically useful for people who want to do complex belief updates, or keep track of
    how their minds change, or outsource their beliefs (i.e. cease relying on intuition).
"""
from numpy import dot
from textwrap import dedent, fill


def print_bayes_update(prior_beliefs: dict, likelihood_ratios: dict, posterior_beliefs: dict) -> None:
    """Prints the prettified updates to console."""
    # TODO: Print priors, lratios an posteriors. Maybe arrows too. Animations?


def bayes_update(prior_beliefs: dict, likelihood_ratios: dict) -> dict:
    """
    Takes prior beliefs and likelihood ratios, both expressed as
    dictionaries of odds ratios (h1:odds1, h2:odds2, ...), and uses
    Bayes theorem to return a dictionary of posterior beliefs.
    """

    # TODO: Extract probabilities from the two dicts using zip somehow?
    posterior_probability_distribution = None
    print(prior_beliefs.values())

    # TODO: Matrix multiply priors and likelihoods.
    # posterior_beliefs = dot(prior_beliefs, likelihood_ratios)

    # TODO: Combine posteriors with dict of hypothesis names again.

    # return posterior_probability_distribution


def bayes_query() -> tuple:
    """Queries the user for their priors and likelihood ratios."""

    evidence_name =\
        input(dedent("""
                        Give a name to the evidence you want to consider
                        (e.g. "clinical trial" or "uncle Joey anecdote"):

                     > 
                     """))

    belief_names =\
        input(dedent("""
                        List the names of the beliefs you want to update
                        (e.g. 'drug has positive effect', 'no effect', 'negative effect'):
                        
                     > 
                     """))

    prior_beliefs =\
        input(dedent(f"""
                         List your prior odds for the following
                         {belief_names}:
                        
                     > 
                     """))

    likelihood_ratios = \
        print(fill(dedent(f"""
                         List your likelihood ratios for the following (e.g. if {belief_names[0]} is true, how much more likely would you be to observe {} compared to if other hypotheses were true?): {belief_names}:
    
                     > 
                     """)))

    # return dict(prior_beliefs), dict(likelihood_ratios)


if __name__ == "__main__":

    # Unpack the return values from bayes_query()
    # as arguments into bayes_update().
    print(bayes_update(*bayes_query()))
