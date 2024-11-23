import math

def boolean_model(query, faqs):
    terms = query.lower().split()
    results = []
    for faq in faqs:
        text = f"{faq.question.lower()} {faq.answer.lower()}"
        if all(term in text for term in terms):
            results.append(faq)
    return results

def extended_boolean_model(query, faqs):
    terms = query.lower().split()
    results = []
    for faq in faqs:
        text = f"{faq.question.lower()} {faq.answer.lower()}"
        score = sum(1 for term in terms if term in text)
        if score > 0:
            results.append((faq, score))
    return sorted(results, key=lambda x: x[1], reverse=True)

def vector_space_model(query, faqs):
    query_terms = query.lower().split()
    results = []
    for faq in faqs:
        text_terms = (faq.question.lower() + " " + faq.answer.lower()).split()
        common_terms = set(query_terms) & set(text_terms)
        score = len(common_terms) / math.sqrt(len(query_terms) * len(text_terms))
        results.append((faq, score))
    return sorted(results, key=lambda x: x[1], reverse=True)
