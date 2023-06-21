from jira import JIRA
from atlassian import Confluence
import os
os.environ['JIRA_USERNAME'] = 'jadhavabhijeet6411@gmail.com'
os.environ['JIRA_PASSWORD'] = 'ATATT3xFfGF018_CYI9NHU0OOWFf07Pax1hyAtYfKVRbF1aVbUZKj9UC5Jut8YNSeFmpU1GD6FKkB3THnZEsCEywIsA0VzjJshj2Z1ReyuH9rRyZ8WJzTmCRigjOvWUTx2NpCvZGdnZS4toJtfWwSAamuzEJvHOjGOttz80IdIjdJIYbztTKTkE=55A0A156'

# Connect to JIRA
jira = JIRA(server='https://demo-sw.atlassian.net', basic_auth=("jadhavabhijeet6411@gmail.com", "ATATT3xFfGF018_CYI9NHU0OOWFf07Pax1hyAtYfKVRbF1aVbUZKj9UC5Jut8YNSeFmpU1GD6FKkB3THnZEsCEywIsA0VzjJshj2Z1ReyuH9rRyZ8WJzTmCRigjOvWUTx2NpCvZGdnZS4toJtfWwSAamuzEJvHOjGOttz80IdIjdJIYbztTKTkE=55A0A156"))

# Connect to Confluence
confluence = Confluence(url="https://demo-sw.atlassian.net/wiki/home", username="jadhavabhijeet6411@gmail.com", password="ATATT3xFfGF018_CYI9NHU0OOWFf07Pax1hyAtYfKVRbF1aVbUZKj9UC5Jut8YNSeFmpU1GD6FKkB3THnZEsCEywIsA0VzjJshj2Z1ReyuH9rRyZ8WJzTmCRigjOvWUTx2NpCvZGdnZS4toJtfWwSAamuzEJvHOjGOttz80IdIjdJIYbztTKTkE=55A0A156")

# Fetch pull request details from the GitHub environment variables
pr_number = os.getenv('GITHUB_REF').split('/')[-1]
pr_title = os.getenv('GITHUB_HEAD_REF')

# Update the JIRA Confluence page with the pull request details
page_id = '393217'  # Replace with the ID of your Confluence page
page = confluence.get_page_by_id(page_id)
table_content = f"| {pr_number} | {pr_title} |\n"  # Customize the table structure as needed
#new_content = f"{page['body']['storage']['value']}\n{table_content}"
confluence.update_page(page_id, pr_title)
