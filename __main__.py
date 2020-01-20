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


def bayes_update(prior_beliefs: list,
                 likelihood_ratios: list,
                 belief_names: list,
                 evidence_name: str) -> list:
    """
    Takes prior beliefs and likelihood ratios, both expressed as
    dictionaries of odds ratios (h1:odds1, h2:odds2, ...), and uses
    Bayes theorem to return a dictionary of posterior beliefs.
    """

    # Cast all the arguments as lists if they contain more than one item.
    prior_beliefs, likelihood_ratios, belief_names, evidence_name = "a, b, c, d, e,f", 'b', 'c', 'd'
    args = [prior_beliefs, likelihood_ratios, belief_names, evidence_name]
    args = [[sentence.strip() for sentence in arg.split(',')] for arg in args]  # List comprehension INSIDE list comprehension
    print(args)
    prior_beliefs, likelihood_ratios, belief_names, evidence_name = args[0], args[1], args[2], args[3]
    # sad can't use *args here :c

    # TODO: Extract probabilities from the two dicts using zip somehow?
    posterior_probability_distribution = None
    print(prior_beliefs)
    print(type(prior_beliefs))

    # TODO: Matrix multiply priors and likelihoods.
    # posterior_beliefs = dot(prior_beliefs, likelihood_ratios)

    # TODO: Combine posteriors with dict of hypothesis names again.

    # return posterior_probability_distribution


def bayes_query() -> tuple:
    """Queries the user for their priors and likelihood ratios."""

    evidence_name = \
        input(dedent("""
                        Give a name to the evidence you want to consider
                        (e.g. "clinical trial" or "uncle Joey anecdote"):

                        > """))

    belief_names = \
        input(dedent("""
                        List the names of the beliefs you want to update
                        (e.g. "positive effect, no effect, negative effect"):
                        
                        > """))

    prior_beliefs = \
        input(dedent(f"""
                         List your prior odds for the following
                         {belief_names}:
                        
                         > """))

    likelihood_ratios = \
        input(fill("List your likelihood ratios for the following hypotheses given the evidence " +
                   f"(e.g. if [{belief_names[0]}] is true, how much more likely would you be to " +
                   f"observe [{evidence_name}] compared to if other hypotheses were true?):", 80) +
              f"\n\n{belief_names}:" +
              "\n\n" +
              " > ")

    # Cast all the arguments as lists if they contain more than one item.
    # args = [tuple(arg) for arg in [prior_beliefs, likelihood_ratios, belief_names, evidence_name]
    #         if len(list(arg)) > 1]

    return prior_beliefs, likelihood_ratios, belief_names, evidence_name


if __name__ == "__main__":
    # Unpack the return values from bayes_query()
    # as arguments into bayes_update().
    print(bayes_update(*bayes_query()))
