from slc_web import _
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


INDUSTRIES = [
    ("agriculture", _("Agriculture")),
    ("government", _("Government")),
    ("raw_mat", _("Raw materials")),
    ("man_con", _("Manufacturing and construction")),
    ("service", _("Service")),
    ("edu", _("Education")),
    ("inf_ser", _("Information Services")),
    ("ngo", _("NGO")),
]


@provider(IVocabularyFactory)
def industries_vocabulary(context):
    """Vocabulary of industries."""
    terms = []
    for id_, title in INDUSTRIES:
        terms.append(SimpleTerm(id_, id_, title))
    return SimpleVocabulary(terms)