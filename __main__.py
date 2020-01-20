"""
    end goal: be able to have columns of beliefs, evidence, likelihood ratios, and calculate conclusions.
    It should be practically useful for people who want to do complex belief updates, or keep track of
    how their minds change, or outsource their beliefs (i.e. cease relying on intuition).
"""
from numpy import multiply
from textwrap import dedent, fill

# TODO: Import exception handler and deal with input exceptions.


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

    args = [[float(item.strip()) if _is_floatifiable(item) else item.strip()
             for item in arg.split(':')]
            for arg in args]  # Nested list comprehension!

    return list(args)


def print_bayes_update(prior_odds: list,
                       likelihood_ratios: list,
                       hypotheses: list,
                       evidence_name: str,
                       posterior_odds: list,
                       tab_size: int = 20) -> None:
    """Prints the prettified updates to console."""

    print("\tprior odds\tlikelihood ratios\tposterior odds\tposterior probabilities".expandtabs(tab_size))

    for index, hypothesis in enumerate(hypotheses):
        print((fill(
              f"{hypothesis}", width=tab_size) + "\t").expandtabs(tab_size) +
              f"{prior_odds[index]} \t".expandtabs(tab_size) +
              f"{likelihood_ratios[index]} \t".expandtabs(tab_size) +
              f"{posterior_odds[index]} \t".expandtabs(tab_size) +
              f"{round(100 * posterior_odds[index] / sum(posterior_odds), 1)} %".expandtabs(tab_size))


def bayes_update(prior_odds: list,
                 likelihood_ratios: list,
                 hypotheses: list,
                 evidence_name: str) -> tuple:
    """
    Multiplies vectors of prior_odds (oods) and likelihood ratios (odds)
    according to Bayes theorem.
    """

    posterior_odds = multiply(prior_odds, likelihood_ratios)

    return prior_odds, likelihood_ratios, hypotheses, evidence_name, list(posterior_odds)


def bayes_query() -> tuple:
    """Queries the user for their prior_odds and likelihood ratios."""

    evidence_name = \
        input(dedent("""
                        Give a name to the evidence you want to consider
                        (e.g. 'clinical trial' or 'uncle Joey anecdote'):

                        > """))

    hypotheses = \
        input(dedent("""
                        List the names of the hypotheses you want to update
                        (e.g. 'positive effect:no effect:negative effect'):
                        
                        > """))

    prior_odds = \
        input(dedent(f"""
                         List your prior odds for the following hypotheses:
                         (e.g. '1:4:2')

                         {hypotheses}:
                        
                         > """))

    likelihood_ratios = \
        input(fill("List your likelihood ratios for the following hypotheses given the evidence:" +
                   f"That is, if [{hypotheses[0]}] is true, how much more likely would you be to " +
                   f"observe [{evidence_name}] compared to if other hypotheses were true?:", 80) +
              "(e.g. '4:2:0.5')" +
              f"\n\n{hypotheses}:" +
              "\n\n" +
              " > ")

    # Typecast arguments as lists formatted appropriately.
    args = _cast_odds_as_lists_of_floats([prior_odds, likelihood_ratios, hypotheses])
    prior_odds, likelihood_ratios, hypotheses = args[0], args[1], args[2]  # sad can't use *args here :c

    return prior_odds, likelihood_ratios, hypotheses, evidence_name


if __name__ == "__main__":
    # Unpack the return values from bayes_query()
    # as arguments into bayes_update().
    print_bayes_update(*bayes_update(*bayes_query()))

    # Quick
    # args = [prior_odds := "1:4:2",
    #         likelihood_ratios := "4:1:0.5",
    #         hypotheses := "positive effect:no effect:negative effect",
    #         evidence_name := "clinical trial"]
    # args = _cast_odds_as_lists_of_floats(args)
    # print_bayes_update(*bayes_update(*args))
