import subprocess

from utils import get_arguments, get_first_link, logger
from team_stats import get_all_stats_df, get_desired_stats_dataframe
from generate_report import generate_pdf_with_table, get_string_table
from send_email import send_email_with_file

logger.info("Beginning Team Stats")

arguments = get_arguments("arguments.json")
SENDER = arguments["sender"]
TEAM_LIST = arguments["teams"]
RECEIVER_LIST = arguments["receivers"]

def main():
    table_list = []
    filename_list = []
    for team in TEAM_LIST:
        logger.info(f"{team} stats will be sent")
        website = get_first_link(team)
        all_stats_df = get_all_stats_df(website)
        desired_df = get_desired_stats_dataframe(all_stats_df, "stats.json")
        table = get_string_table(desired_df, team)
        table_list.append(table)

        pdf_file = generate_pdf_with_table(desired_df, team)
        filename_list.append(pdf_file)
        logger.info(f"{pdf_file} generated")

    send_email_with_file(SENDER, RECEIVER_LIST, filename_list)
    logger.info(f"Email sent to {RECEIVER_LIST}")

    subprocess.run(['rm', '*.pdf'])
    logger.info("All PDF files removed from current dir")


if __name__ == '__main__':
    main()