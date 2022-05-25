def bayes(prior, likelihood, evidence):
    """
    Bayes Theorem

    :param prior: P(H), probability that the hypothesis is true
    :param likelihood: P(E|H), probability of the evidence is true given the hypothesis is true
    :param evidence: P(E), probability that the evidence is true, is equal to -> P(E|H) * P(H) + P(E|~H) * P(~H) 
    :return: posterior, P(H|E), probability of the hypothesis is true given the evidence is true

    """
    return (prior * likelihood) / evidence

def run():
    prob_cancer = 1/100000  # prior - P(H)
    prob_no_cancer = 1 - prob_cancer # P(~H)
    prob_symtom_cancer = 1 # P(E|H)
    prob_symtom_no_cancer = 10/99999 # P(E|~H)
    prob_symtom = (prob_symtom_cancer * prob_cancer) + (prob_symtom_no_cancer * prob_no_cancer) # P(E)

    prob_cancer_given_symtom = bayes(prob_cancer, prob_symtom_cancer, prob_symtom) # P(H|E)

    print(prob_cancer_given_symtom)

if __name__ == "__main__":
    run()