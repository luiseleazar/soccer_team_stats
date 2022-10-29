import unittest
import re

from utils import get_first_link, get_arguments
from generate_report import generate_pdf_with_table
from send_email import send_email_with_file
from team_stats import get_all_stats_df

TEAM_TO_TEST = 'Real Madrid'

class TestUtils(unittest.TestCase):
    
    def test_get_link_returns_a_string(self):
        url = get_first_link(TEAM_TO_TEST)
        message = "Given object is not str"
        self.assertIsInstance(url, str, message)

    def test_link_is_from_footy_website(self):
        url = get_first_link(TEAM_TO_TEST)
        pattern = r"https://footystats.org/clubs/."
        match = re.match(pattern, url)
        self.assertIsNotNone(match)
    
    def test_arguments_is_dict_of_lists(self):
        args = get_arguments("arguments.json")
        self.assertIsInstance(args, dict)
        for item in args.values():
            self.assertIsInstance(item, list)


class TestGenerateReport(unittest.TestCase):

    def test_empty_team_raise_error(self):
        dataframe =[["","","",""],["","","",""]]
        team = ""
        self.assertRaises(ValueError, generate_pdf_with_table, dataframe, team)

    def test_empty_dataframe_raise_error(self):
        dataframe = [[], [], []]
        team = 'Real Madrid'
        self.assertRaises(ValueError, generate_pdf_with_table, dataframe, team)


class TestSendEmail(unittest.TestCase):

    def test_not_list_arguments_raises_error(self):
        receiver = 'luiseleazar4@hotmail.com'
        filename = 'test.pdf'
        self.assertRaises(TypeError, send_email_with_file, receiver, filename)


class TestTeamStats(unittest.TestCase):

    def test_returns_list_of_lists(self):
        website = 'https://footystats.org/clubs/real-madrid-cf-84'
        dataframe = get_all_stats_df(website)

        self.assertIsInstance(dataframe, list)
        for data in dataframe:
            self.assertIsInstance(data, list)

    def test_wrong_website_raises_error(self):
        website = 'https://espn.com'
        self.assertRaises(ValueError, get_all_stats_df, website)


if __name__ == '__main__':
    unittest.main()