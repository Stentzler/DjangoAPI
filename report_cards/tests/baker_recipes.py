from model_bakery.recipe import Recipe
from report_cards.models import ReportCard

report_card_custom = Recipe(
    ReportCard,
    result_q1 = 90,
    result_q2 = 40,
    result_q3 = 50,
    result_q4 = 70,
)