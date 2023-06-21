from jira import JIRA
from atlassian import Confluence

# Connect to JIRA
jira = JIRA(server='https://demo-sw.atlassian.net/jira/', basic_auth=(os.environ['JIRA_USERNAME'], os.environ['JIRA_PASSWORD']))

# Connect to Confluence
confluence = Confluence(url=os.environ['https://demo-sw.atlassian.net/wiki/spaces/~71202026b01f91e1a3436291135759a5455a0e/pages/393217/PR+requests'], username=os.environ['JIRA_USERNAME'], password=os.environ['JIRA_PASSWORD'])

# Fetch pull request details from the GitHub environment variables
pr_number = os.getenv('GITHUB_REF').split('/')[-1]
pr_title = os.getenv('GITHUB_HEAD_REF')

# Update the JIRA Confluence page with the pull request details
page_id = 'AQAG'  # Replace with the ID of your Confluence page
page = confluence.get_page_by_id(page_id)
table_content = f"| {pr_number} | {pr_title} |\n"  # Customize the table structure as needed
new_content = f"{page['body']['storage']['value']}\n{table_content}"
confluence.update_page_content(page_id, new_content)
