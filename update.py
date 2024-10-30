import requests
import json

# Fetch the github_rank
response = requests.get(
    "https://github-rank-git-main-mitanicks-projects.vercel.app/?user=ch4og"
)
github_rank = response.json()

response = requests.get(
    "https://wakatime-stats.vercel.app/?user=ch4og&domain=wakapi.dev"
)
wakatime_stats = response.json()
wakatime_langs = list(wakatime_stats.keys())
wakatime_time = list(wakatime_stats.values())

response = requests.get(
    "https://wakatime-stats.vercel.app/?user=ch4og&domain=wakapi.dev&total=true"
)
wakatime_total = response.json()
# Prepare the Markdown content
markdown_content = f"""
## 👋 Hi, I'm [ch4og](https://ch4og.com)

- GNU/Linux enthusiast and cybersecurity student.
- Speaker of English, Russian and Polish languages.
- I use NixOS btw.

<table>
<tr><th>GitHub Stats</th><th>Wakatime Stats</th></tr>
<tr><td>

|**Rank**|`{github_rank['rank']}`|
|---|---|
|Stars|`{github_rank['stars']}`|
|Public Commits|`{github_rank['commits']}`|
|Pull Requests|`{github_rank['prs']}`|
|Issues|`{github_rank['issues']}`|
|Code Reviews|{github_rank['reviews']}|
|Contributed to|`{github_rank['contributed_to']}`

</td><td>

|**Total**|`{wakatime_total['total']}`|
|---|---|
|{wakatime_langs[0]}|`{wakatime_time[0]}`|
|{wakatime_langs[1]}|`{wakatime_time[1]}`|
|{wakatime_langs[2]}|`{wakatime_time[2]}`|
|{wakatime_langs[3]}|`{wakatime_time[3]}`|
|{wakatime_langs[4]}|`{wakatime_time[4]}`|

</td></tr> </table>
"""

# Write to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(markdown_content)
