from model_bakery.recipe import Recipe
from report_cards.models import ReportCard

report_card_custom = Recipe(
    ReportCard,
    N1 = 90,
    N2 = 40,
    N3 = 50,
    N4 = 70
)