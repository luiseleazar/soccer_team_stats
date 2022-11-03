# Team Stats

I started this personal "project" in order to practice/test my knowledge in Selenium, Web Scraping, and Python in general.

The program sends an email to the receivers you want with some PDF files containg the stats of the soccer teams you want. These stats may be interesting for betting on sports.

I use the [Footy Stats website](https://footystats.org/) to get the stats.

## How It Works

1. Clone the repo
2. Install requirements
3. In the [arguments.json](arguments.json) file:
    - In he sender field put the sender address
    - In the receivers field put (in a list) the receiver addresses
    - And, in the teams field, put (in a list) the teams you want to know their stats.

4. In the [stats.json](stats.json) file, change from _Enabled_ to _Disabled_ or from _Disabled_ to _Enabled_ to only get the stats you want.
5. Create and Enviroment Variable called 'PY_PW' with your email password.
6. Run [run.py](run.py)

_Note: run.py has 2 arguments that can be passed in CLI: when send=1, it sends email to the receivers, when display=1, a string tables is shown on CLI._

_Note: There's a function on [utils.py](utils.py) that generates a stats.json with all the stats disabled_

## To Improve

- I'd like that there were only 1 PDF file with all the stats from each team in different pages.
- I'd like to have more tests to have a better program.
- arguments.json should be called in another way.
- What happen if I don't pass sender or receivers in the send_email function? Need a unit test for that, and need to add error handling
- Make the program to run in Linux