from typing import List

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tabulate import tabulate

def generate_pdf_with_table(dataframe: List[list], team: str):
    """Generate a pdf file including a table with dataframe data"""
    if team == "":
        raise ValueError("Team name must be passed")
    styles = getSampleStyleSheet()
    team_report_name = team.replace(" ", "_") if " " in team else team
    filename = f'{team_report_name}_report.pdf'
    report = SimpleDocTemplate(filename)

    report_title = Paragraph(f"{team.title()} Stats", styles["h1"])
    table_style= [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data=dataframe, style=table_style, hAlign="LEFT")
    report.build([report_title, report_table])

    return filename


def get_string_table(dataframe: List[list], team: str):
    """Returns a tabulated string table with stats passed,
    it also contains a title"""
    table = (tabulate(dataframe[1:], headers=dataframe[0], tablefmt="github"))
    table_title = "\t\t\t" +  team.upper() + " STATS\n\n"

    return table_title + table
