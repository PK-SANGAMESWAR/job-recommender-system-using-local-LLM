from apify_client import ApifyClient
from dotenv import load_dotenv
import os
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

## Fetch Jobs from LinkedIn
def fetch_linkedin_jobs(search_query,location="india",rows=60):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
    }

    # Run the Actor and wait for it to finish
    run = client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

##Fetch Jobs from Naukri
def fetch_naukri_jobs(search_query,location="india",rows=60):
    # Prepare the Actor input
    run_input = {
        "keyword" : search_query,
        "rows" : rows,
        "freshness" : "all",
        "sortBy" : "relevance",
        "experience" : "all",
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
    }

    # Run the Actor and wait for it to finish
    run = client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    jobs = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs
    