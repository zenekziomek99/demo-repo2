import requests
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# Store API response in a variable.
response_dict = r.json()
u print("Total repositories:", response_dict['total_count'])
# Explore information about the repositories.
v repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
# Examine the first repository.
w repo_dict = repo_dicts[0]
x print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)