#!/usr/bin/env python

# Description: Update the label for all issues that are marked as ready to prod with the current release number and close them all.
# Requirements: python-gitlab Python libraries. GitLab API read access, and maintainer access to all configured groups/projects.
# Author: Nelson Ríos
# License: MIT, (c) 2023-present GitLab B.V.

import gitlab

OLD_LABEL_NAME = "✅ READY TO PROD"
NEW_LABEL_NAME = "🏷️ api:1.31.0"
# GITLAB_SERVER = ""
# GITLAB_TOKEN = ''
# PROJECT_ID = ''

gl = gitlab.Gitlab(GITLAB_SERVER, private_token=GITLAB_TOKEN)

# Retrieve the project
project = gl.projects.get(PROJECT_ID)

# Create new label
project.labels.create(
    {
        "name": NEW_LABEL_NAME,
        "color": "#6699cc",
    }
)
print(NEW_LABEL_NAME, "🤖 New label created.")

# Get the list of issues with a specific label
issues = project.issues.list(labels=[OLD_LABEL_NAME], get_all=True)

# Iterate over the filtered issues and operate over them
for issue in issues:
    issue.labels.append(NEW_LABEL_NAME)
    issue.labels.remove(OLD_LABEL_NAME)
    issue.state_event = "close"
    issue.save()
    print(issue.id, issue.title, "👈 Label updated and issue closed.")
