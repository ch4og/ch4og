import requests
import json

# Fetch the data
response = requests.get(
    "https://github-rank-git-main-mitanicks-projects.vercel.app/?user=ch4og"
)
data = response.json()

# Prepare the Markdown content
markdown_content = f"""
## 👋 Hi, I'm [ch4og](https://ch4og.com)

- GNU/Linux enthusiast and cybersecurity student.
- Speaker of English, Russian and Polish languages.
- I use NixOS btw.


|**GitHub Rank**|`{data['rank']}`|
|---|---|
|Stars|`{data['stars']}`|
|Public Commits|`{data['commits']}`|
|Pull Requests|`{data['prs']}`|
|Issues|`{data['issues']}`|
|Contributed to (2024)|`{data['contributed_to']}`

<img src="/.cache/langs.svg" />

![](https://github-readme-stats.vercel.app/api/wakatime?username=ch4og&theme=dark&hide=unknown&custom_title=Wakapi%20Stats&api_domain=wakapi.dev&layout=compact)
"""

# Write to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(markdown_content)
