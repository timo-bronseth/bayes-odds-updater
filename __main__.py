"""
    end goal: be able to have columns of beliefs, evidence, likelihood ratios, and calculate conclusions.
    It should be practically useful for people who want to do complex belief updates, or keep track of
    how their minds change, or outsource their beliefs (i.e. cease relying on intuition).
"""
from numpy import multiply
from textwrap import dedent, fill


def _is_floatifiable(string: str) -> bool:
    """Checks if it's possible to cast a str to float, and returns True if so."""

    try:
        float(string)
        return True
    except ValueError:
        return False


def _cast_odds_as_lists_of_floats(args: list) -> list:
    """
    Takes a list of strings-of-strings (e.g. "'0', '1', '2'") and returns a list of those strings,
    with its items typecasted to floats, typecasted as lists separated by commas (e.g. "[1.0, 2.0, 3.0]").
    Uses nested list comprehension btw!
    """

    args = [[float(sentence.strip()) if _is_floatifiable(sentence) else sentence.strip()
             for sentence in arg.split(':')]
            for arg in args]  # Nested list comprehension!

    return list(args)


def print_bayes_update(prior_beliefs: list,
                       likelihood_ratios: list,
                       belief_names: list,
                       evidence_name: str,
                       posterior_beliefs: list) -> None:
    """Prints the prettified updates to console."""

    # TODO: Finish this
    print(dedent(f"""
                    \t\t priors \t\t likelihood ratios \t\t posteriors
                    {belief_names[0]} \t\t {likelihood_ratios[0]} \t\t {posterior_beliefs[0]}
                    
                 """))


def bayes_update(prior_beliefs: list,
                 likelihood_ratios: list,
                 belief_names: list,
                 evidence_name: str) -> tuple:
    """
    Multiplies vectors of prior beliefs (oods) and likelihood ratios (odds)
    according to Bayes theorem.
    """

    posterior_beliefs = multiply(prior_beliefs, likelihood_ratios)

    return prior_beliefs, likelihood_ratios, belief_names, evidence_name, list(posterior_beliefs)


def bayes_query() -> tuple:
    """Queries the user for their priors and likelihood ratios."""

    evidence_name = \
        input(dedent("""
                        Give a name to the evidence you want to consider
                        (e.g. 'clinical trial' or 'uncle Joey anecdote'):

                        > """))

    belief_names = \
        input(dedent("""
                        List the names of the beliefs you want to update
                        (e.g. 'positive effect, no effect, negative effect'):
                        
                        > """))

    prior_beliefs = \
        input(dedent(f"""
                         List your prior odds for the following hypotheses:
                         (e.g. '1:4:2')
                         {belief_names}:
                        
                         > """))

    likelihood_ratios = \
        input(fill("List your likelihood ratios for the following hypotheses given the evidence:" +
                   f"That is, if [{belief_names[0]}] is true, how much more likely would you be to " +
                   f"observe [{evidence_name}] compared to if other hypotheses were true?:", 80) +
              "(e.g. '4:2:0.5')" +
              f"\n\n{belief_names}:" +
              "\n\n" +
              " > ")

    # Typecast arguments as lists formatted appropriately.
    args = _cast_odds_as_lists_of_floats([prior_beliefs, likelihood_ratios, belief_names])
    prior_beliefs, likelihood_ratios, belief_names = args[0], args[1], args[2]  # sad can't use *args here :c

    return prior_beliefs, likelihood_ratios, belief_names, evidence_name


if __name__ == "__main__":
    # Unpack the return values from bayes_query()
    # as arguments into bayes_update().
    print_bayes_update(*bayes_update(*bayes_query()))
