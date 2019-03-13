---
id: github-documentation
title: GitHub (version v2.*.*)
sidebar_label: GitHub
---

## add_email_to_user

Add email address(es).
You can post a single email address or an array of addresses.


<details><summary>Parameters</summary>

#### $body

**Type:** array

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## add_file_to_repo

Create a file.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### path (required)

The file path or directory. Set this to an empty string to get the contents of all files in the repository.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## add_label_for_issue

Add labels to an issue.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** array

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## add_repo_for_team

In order to add a repository to a team, the authenticated user must be an owner of the org that the team is associated with. Also, the repository must be owned by the organization, or a direct fork of a repository owned by the organization.

<details><summary>Parameters</summary>

#### repo (required)

Name of repository.

**Type:** string

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## compare_commits

Compare two commits

<details><summary>Parameters</summary>

#### baseId (required)

**Type:** string

#### headId (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_blob

Create a Blob.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_comment_for_commit

Create a commit comment.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_comment_for_gist

Create a comment

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_comment_for_issue

Create a comment.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_comment_for_pull_request

Create a comment.
  #TODO Alternative input ( http://developer.github.com/v3/pulls/comments/ )
  description: |
    Alternative Input.
    Instead of passing commit_id, path, and position you can reply to an
    existing Pull Request Comment like this:

        body
           Required string
        in_reply_to
           Required number - Comment id to reply to.


<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_deployment

Users with push access can create a deployment for a given ref

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_fork

Create a fork.
Forking a Repository happens asynchronously. Therefore, you may have to wai
a short period before accessing the git objects. If this takes longer than 5
minutes, be sure to contact Support.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_gists

Create a gist.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_git_commit

Create a Commit.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_git_ref

Create a Reference

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_git_tag

Create a Tag Object.
Note that creating a tag object does not create the reference that makes a
tag in Git. If you want to create an annotated tag in Git, you have to do
this call to create the tag object, and then create the refs/tags/[tag]
reference. If you want to create a lightweight tag, you only have to create
the tag reference - this call would be unnecessary.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_git_tree

Create a Tree.
The tree creation API will take nested entries as well. If both a tree and
a nested path modifying that tree are specified, it will overwrite the
contents of that tree with the new path contents and write a new tree out.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_hook_for_repo

Create a hook.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_issue

Create an issue.
Any user with pull access to a repository can create an issue.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_key_for_repo

Create a key.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_key_for_user

Create a public key.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_label_for_repo

Create a label.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** array

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_milestone

Create a milestone.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_pull_request

Create a pull request.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_release

Create a release
Users with push access to the repository can create a release.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_repo_for_user

Create a new repository for the authenticated user. OAuth users must supply
repo scope.


<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_repo_in_org

Create a new repository for the authenticated user. OAuth users must supply
repo scope.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_status_for_deployment

Create a Deployment Status
Users with push access can create deployment statuses for a given deployment:


<details><summary>Parameters</summary>

#### id (required)

The Deployment ID to list the statuses from.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_status_for_ref

Create a Status.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_team_in_org

Create team.
In order to create a team, the authenticated user must be an owner of organization.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## create_test_for_hook

Test a push hook.
This will trigger the hook with the latest push to the current repository
if the hook is subscribed to push events. If the hook is not subscribed
to push events, the server will respond with 204 but no test POST will
be generated.
Note: Previously /repos/:owner/:repo/hooks/:id/tes


<details><summary>Parameters</summary>

#### hookId (required)

Id of hook.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_asset_for_release

Delete a release asset

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_collaborator_for_repo

Remove collaborator.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### user (required)

Login of the user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_comment_for_commit_in_repo

Delete a commit comment

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_comment_for_gist

Delete a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_comment_for_issue

Delete a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_comment_for_pull_request

Delete a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_file_in_repo

Delete a file.
This method deletes a file in a repository.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### path (required)

The file path or directory. Set this to an empty string to get the contents of all files in the repository.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_gist

Delete a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_git_ref

Delete a Reference
Example: Deleting a branch: DELETE /repos/octocat/Hello-World/git/refs/heads/feature-a 
Example: Deleting a tag:        DELETE /repos/octocat/Hello-World/git/refs/tags/v1.0


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_hook_for_repo

Delete a hook.

<details><summary>Parameters</summary>

#### hookId (required)

Id of hook.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_key_for_repo

Delete a key.

<details><summary>Parameters</summary>

#### keyId (required)

Id of key.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_key_for_user

Delete a public key. Removes a public key. Requires that you are authenticated via Basic Auth or via OAuth with at least admin:public_key scope.

<details><summary>Parameters</summary>

#### keyId (required)

Id of key.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_label_for_repo

Delete a label.

<details><summary>Parameters</summary>

#### name (required)

Name of the label.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_labels_for_issue

Remove all labels from an issue.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_member_of_org

Remove a member.
Removing a user from this list will remove them from all teams and they
will no longer have any access to the organization's repositories.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_milestone

Delete a milestone.

<details><summary>Parameters</summary>

#### number (required)

Number of milestone.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_public_member_of_org

Conceal a user's membership.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_release

Users with push access to the repository can delete a release.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_repo

Delete a Repository.
Deleting a repository requires admin access. If OAuth is used, the delete_repo
scope is required.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_subscription_for_repo

Delete a Repository Subscription.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## delete_team

Delete team.
In order to delete a team, the authenticated user must be an owner of the
org that the team is associated with.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_asset_for_release

Edit a release asset
Users with push access to the repository can edit a release asset.


<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_branch_protection_rules

update branch protection rules

<details><summary>Parameters</summary>

#### branch (required)

Name of the branch.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_collaborator_for_repo

Add collaborator.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### user (required)

Login of the user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_comment_for_commit_in_repo

Update a commit comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_comment_for_gist

Edit a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### id (required)

Id of gist.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_comment_for_issue

Edit a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_comment_for_pull_request

Edit a comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_gist

Edit a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_git_ref

Update a Reference

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_hook_for_repo

Edit a hook.

<details><summary>Parameters</summary>

#### hookId (required)

Id of hook.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_issue

Edit an issue.
Issue owners and users with push access can edit an issue.


<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_label_for_repo

Update a label.

<details><summary>Parameters</summary>

#### name (required)

Name of the label.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** array

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_labels_for_issue

Replace all labels for an issue.
Sending an empty array ([]) will remove all Labels from the Issue.


<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** array

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_membership_for_user_on_team

Add team membership.
In order to add a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with.

If the user is already a part of the team's organization (meaning they're on at least one other team in the organization), this endpoint will add the user to the team.

If the user is completely unaffiliated with the team's organization (meaning they're on none of the organization's teams), this endpoint will send an invitation to the user via email. This newly-created membership will be in the 'pending' state until the user accepts the invitation, at which point the membership will transition to the 'active' state and the user will be added as a member of the team.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_milestone

Update a milestone.

<details><summary>Parameters</summary>

#### number (required)

Number of milestone.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_notification_thread_subscription

Set a Thread Subscription.
This lets you subscribe to a thread, or ignore it. Subscribing to a thread
is unnecessary if the user is already subscribed to the repository. Ignoring
a thread will mute all future notifications (until you comment or get @mentioned).


<details><summary>Parameters</summary>

#### id (required)

Id of thread.

**Type:** integer

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_org

Edit an Organization.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_public_member_of_org

Publicize a user's membership.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_pull_request

Update a pull request.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_release

Users with push access to the repository can edit a release

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_repo

Edit repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_subscription_for_repo

Set a Repository Subscription

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_team

Edit team.
In order to edit a team, the authenticated user must be an owner of the org
that the team is associated with.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## edit_user

Update the authenticated user.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## follow_user

Follow a user.
Following a user requires the user to be logged in and authenticated with
basic auth or OAuth with the user:follow scope.


<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## fork_gist

Fork a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_asset_for_release

Get a single release asset

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_blob

Get a Blob.
Since blobs can be any arbitrary binary data, the input and responses for
the blob API takes an encoding parameter that can be either utf-8 or
base64. If your data cannot be losslessly sent as a UTF-8 string, you can
base64 encode it.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_branch_for_repo

Get Branch

<details><summary>Parameters</summary>

#### branch (required)

Name of the branch.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_branch_protection_rules

List branch protection rules for a repo

<details><summary>Parameters</summary>

#### branch (required)

Name of the branch.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_comment

Get a single comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_comment_for_commit_in_repo

Get a single commit comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_comment_for_issue

Get a single comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_comment_for_pull_request

Get a single comment.

<details><summary>Parameters</summary>

#### commentId (required)

Id of comment.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_commit

Get a single commit.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_emojis

Lists all the emojis available to use on GitHub.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_event_for_issue

Get a single event.

<details><summary>Parameters</summary>

#### eventId (required)

Id of the event.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_events

List public events.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_feeds

List Feeds.
GitHub provides several timeline resources in Atom format. The Feeds API
 lists all the feeds available to the authenticating user.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_files_in_repo

Get contents.
This method returns the contents of a file or directory in a repository.
Files and symlinks support a custom media type for getting the raw content.
Directories and submodules do not support custom media types.
Note: This API supports files up to 1 megabyte in size.
Here can be many outcomes. For details see "http://developer.github.com/v3/repos/contents/"


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### path (required)

The file path or directory. Set this to an empty string to get the contents of all files in the repository.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### ref

The String name of the Commit/Branch/Tag. Defaults to 'master'.

**Type:** string

</details>

## get_gist

Get a single gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_git_commit

Get a Commit.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_git_ref

Get a Reference

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_git_tree

Get a Tree.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### recursive

Get a Tree Recursively. (0 or 1)

**Type:** integer

</details>

## get_github_metadata

This gives some information about GitHub.com, the service.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_hook_for_repo

Get single hook.

<details><summary>Parameters</summary>

#### hookId (required)

Id of hook.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_issue

Get a single issue

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_key_for_repo

Get a key

<details><summary>Parameters</summary>

#### keyId (required)

Id of key.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_key_for_user

Get a single public key.

<details><summary>Parameters</summary>

#### keyId (required)

Id of key.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_label_for_repo

Get a single label.

<details><summary>Parameters</summary>

#### name (required)

Name of the label.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_labels_for_issue

List labels on an issue.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_members_of_team

List team members.
In order to list members in a team, the authenticated user must be a member
of the team.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_membership_for_user_on_team

Get team membership.
In order to get a user's membership with a team, the authenticated user must be a member of the team or an owner of the team's organization.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_milestone

Get a single milestone.

<details><summary>Parameters</summary>

#### number (required)

Number of milestone.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_notification_thread

View a single thread.

<details><summary>Parameters</summary>

#### id (required)

Id of thread.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_org

Get an Organization.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_pull_request

Get a single pull request.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_rate_limit

Get your current rate limit status
Note: Accessing this endpoint does not count against your rate limit.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_readme

Get the README.
This method returns the preferred README for a repository.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### ref

The String name of the Commit/Branch/Tag. Defaults to master.

**Type:** string

</details>

## get_release

Get a single release

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_repo

Get repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_subscription_for_repo

Get a Repository Subscription.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_team

Get team.

<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_template

Get a single template.

<details><summary>Parameters</summary>

#### language (required)

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_user

Get a single user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## get_user_authenticated

Get the authenticated user.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_collaborator_for_repo

Check if user is a collaborator

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### user (required)

Login of the user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_gist_starred

Check if a gist is starred.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_member_of_org

Check if a user is, publicly or privately, a member of the organization.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_notification_thread_subscribed

Get a Thread Subscription.

<details><summary>Parameters</summary>

#### id (required)

Id of thread.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_public_member_of_org

Check public membership.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_pull_request_merged

Get if a pull request has been merged.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_repo_managed_by_team

Check if a team manages a repository

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_repo_starred

Check if you are starring a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_repo_watched

Check if you are watching a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_user_assigned_to_repo

Check assignee.
You may also check to see if a particular user is an assignee for a repository.


<details><summary>Parameters</summary>

#### assignee (required)

Login of the assignee.

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## is_user_following_target_user

Check if one user follows another.

<details><summary>Parameters</summary>

#### targetUser (required)

Name of user.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_all_notifications

List your notifications.
List all notifications for the current user, grouped by repository.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### all

True to show notifications marked as read.

**Type:** boolean

#### participating

True to show only notifications in which the user is directly participating
or mentioned.


**Type:** boolean

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

</details>

## list_all_repos

List all public repositories.
This provides a dump of every public repository, in the order that they
were created.
Note: Pagination is powered exclusively by the since parameter. is the
Link header to get the URL for the next page of repositories.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

The integer ID of the last Repository that you've seen.

**Type:** string

</details>

## list_assets_for_release

List assets for a release

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_assignees_for_repo

List assignees.
This call lists all the available assignees (owner + collaborators) to which
issues may be assigned.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_branches_for_repo

Get list of branches

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_collaborators_for_repo

List.
When authenticating as an organization owner of an organization-owned
repository, all organization owners are included in the list of
collaborators. Otherwise, only users with access to the repository are
returned in the collaborators list.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_commit

List comments for a single commitList comments for a single commit.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_commits_in_repo

List commit comments for a repository.
Comments are ordered by ascending ID.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_gist

List comments on a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_issue

List comments on an issue.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_issues_in_repo

List comments in a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

Ignored without 'sort' parameter.

**Type:** string

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated

</details>

## list_comments_for_pull_request

List comments on a pull request.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_comments_for_pull_requests

List comments in a repository.
By default, Review Comments are ordered by ascending ID.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

Ignored without 'sort' parameter.

**Type:** string

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated

</details>

## list_commits

List commits on a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### author

GitHub login, name, or email by which to filter by commit author.

**Type:** string

#### path

Only commits containing this file path will be returned.

**Type:** string

#### sha

Sha or branch to start listing commits from.

**Type:** string

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

#### until

ISO 8601 Date - Only commits before this date will be returned.

**Type:** string

</details>

## list_commits_for_pull_request

List commits on a pull request.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_contributors_to_repo

Get list of contributors.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### anon

Set to 1 or true to include anonymous contributors in results.

**Type:** string

</details>

## list_deployments

Users with pull access can view deployments for a repository

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_emails_for_user

List email addresses for a user.
In the final version of the API, this method will return an array of hashes
with extended information for each email address indicating if the address
has been verified and if it's primary email address for GitHub.
Until API v3 is finalized, use the application/vnd.github.v3 media type to
get other response format.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_for_issue

List events for an issue.

<details><summary>Parameters</summary>

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_for_issues_in_repo

List issue events for a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_for_network

List public events for a network of repositories.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_for_org

List public events for an organization.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_for_repo

Get list of repository events.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_performed_for_user

If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_received_for_user

These are events that you'll only see public events.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_events_received_public_for_user

List public events that a user has received

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_files_for_pull_requests

List pull requests files.

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_followers

List the authenticated user's followers

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_followers_for_user

List a user's followers

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_following

List who the authenticated user is following.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_following_for_user

Check if you are following a user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_forks

List forks.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### sort

**Type:** string

**Potential values:** newes, oldes, watchers

</details>

## list_gists

List the authenticated user's gists or if called anonymously, this will
return all public gists.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.
Only gists updated at or after this time are returned.


**Type:** string

</details>

## list_gists_for_user

List a users gists.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

</details>

## list_gists_public

List all public gists.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.
Only gists updated at or after this time are returned.


**Type:** string

</details>

## list_gists_starred

List the authenticated user's starred gists.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.
Only gists updated at or after this time are returned.


**Type:** string

</details>

## list_git_refs

Get all References

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_git_tags

Get a Tag.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### shaCode (required)

SHA-1 code of the commit.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_hooks_for_repo

Get list of hooks.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_issues

List issues.
List all issues across all the authenticated user's visible repositories.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

**Type:** string

**Potential values:** asc, desc

#### filter

Issues assigned to you / created by you / mentioning you / you're
subscribed to updates for / All issues the authenticated user can see


**Type:** string

**Potential values:** assigned, created, mentioned, subscribed, all

#### labels

String list of comma separated Label names. Example - bug,ui,@high.

**Type:** string

#### since

Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Only issues updated at or after this time are returned.


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated, comments

#### state

**Type:** string

**Potential values:** open, closed

</details>

## list_issues_for_org

List issues.
List all issues for a given organization for the authenticated user.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

**Type:** string

**Potential values:** asc, desc

#### filter

Issues assigned to you / created by you / mentioning you / you're
subscribed to updates for / All issues the authenticated user can see


**Type:** string

**Potential values:** assigned, created, mentioned, subscribed, all

#### labels

String list of comma separated Label names. Example - bug,ui,@high.

**Type:** string

#### since

Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Only issues updated at or after this time are returned.


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated, comments

#### state

**Type:** string

**Potential values:** open, closed

</details>

## list_issues_for_repo

List issues for a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

**Type:** string

**Potential values:** asc, desc

#### filter

Issues assigned to you / created by you / mentioning you / you're
subscribed to updates for / All issues the authenticated user can see


**Type:** string

**Potential values:** assigned, created, mentioned, subscribed, all

#### labels

String list of comma separated Label names. Example - bug,ui,@high.

**Type:** string

#### since

Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Only issues updated at or after this time are returned.


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated, comments

#### state

**Type:** string

**Potential values:** open, closed

</details>

## list_issues_for_user

List issues.
List all issues across owned and member repositories for the authenticated
user.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

**Type:** string

**Potential values:** asc, desc

#### filter

Issues assigned to you / created by you / mentioning you / you're
subscribed to updates for / All issues the authenticated user can see


**Type:** string

**Potential values:** assigned, created, mentioned, subscribed, all

#### labels

String list of comma separated Label names. Example - bug,ui,@high.

**Type:** string

#### since

Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Only issues updated at or after this time are returned.


**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated, comments

#### state

**Type:** string

**Potential values:** open, closed

</details>

## list_keys

List your public keys.
Lists the current user's keys. Management of public keys via the API requires
that you are authenticated through basic auth, or OAuth with the 'user', 'write:public_key' scopes.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_keys_for_repo

Get list of keys.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_keys_for_user

List public keys for a user.
Lists the verified public keys for a user. This is accessible by anyone.


<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_labels_for_milestone

Get labels for every issue in a milestone.

<details><summary>Parameters</summary>

#### number (required)

Number of milestone.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_labels_for_repo

List all labels for this repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_languages

List languages.
List languages for the specified repository. The value on the right of a
language is the number of bytes of code written in that language.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_members_for_org

Members list.
List all users who are members of an organization. A member is a user that belongs to at least 1 team in the organization. If the authenticated user is also an owner of this organization then both concealed and public members will be returned. If the requester is not an owner of the organization the query will be redirected to the public members list.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_milestones

List milestones for a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

Ignored without 'sort' parameter.

**Type:** string

#### sort

**Type:** string

**Potential values:** due_date, completeness

#### state

String to filter by state.

**Type:** string

**Potential values:** open, closed

</details>

## list_notifications_for_repo

List your notifications in a repository
List all notifications for the current user.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### all

True to show notifications marked as read.

**Type:** boolean

#### participating

True to show only notifications in which the user is directly participating
or mentioned.


**Type:** boolean

#### since

The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
Example: "2012-10-09T23:39:01Z".


**Type:** string

</details>

## list_orgs

List public and private organizations for the authenticated user.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_orgs_for_user

List all public organizations for a user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_public_members_of_org

Public members list.
Members of an organization can choose to have their membership publicized
or not.


<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_pull_requests

List pull requests.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### base

Filter pulls by base branch name. Example - gh-pages.

**Type:** string

#### head

Filter pulls by head user and branch name in the format of 'user:ref-name'.
Example: github:new-script-format.


**Type:** string

#### state

String to filter by state.

**Type:** string

**Potential values:** open, closed

</details>

## list_releases

Users with push access to the repository will receive all releases (i.e., published releases and draft releases). Users with pull access will receive published releases only

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_repos

List repositories for the authenticated user. Note that this does not include
repositories owned by organizations which the user can access. You can lis
user organizations and list organization repositories separately.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### type

Will cause a 422 error if used in the same request as visibility or affiliation.

**Type:** string

**Potential values:** all, owner, public, private, member

</details>

## list_repos_for_team

List team repos

<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_repos_for_user

List public repositories for the specified user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### type

**Type:** string

**Potential values:** all, owner, member

</details>

## list_repos_in_org

List repositories for the specified org.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### type

**Type:** string

**Potential values:** all, public, private, forks, sources, member

</details>

## list_stargazers_for_repo

List Stargazers.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_starred_repos_for_user

List repositories being starred by a user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_stars

List repositories being starred by the authenticated user.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### direction

Ignored without 'sort' parameter.

**Type:** string

#### sort

**Type:** string

**Potential values:** created, updated

</details>

## list_statuses_for_deployment

Users with pull access can view deployment statuses for a deployment

<details><summary>Parameters</summary>

#### id (required)

The Deployment ID to list the statuses from.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_statuses_for_ref

List Statuses for a specific Ref.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_subscribers_for_repo

List watchers.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_tags_for_repo

Get list of tags.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

</details>

## list_teams_for_repo

Get list of teams

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_teams_for_user

List all of the teams across all of the organizations to which the authenticated user belongs. This method requires user or repo scope when authenticating via OAuth.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_teams_in_org

List teams.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_templates

Listing available templates.
List all templates available to pass as an option when creating a repository.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_users

Get all users.
This provides a dump of every user, in the order that they signed up for GitHub.
Note: Pagination is powered exclusively by the since parameter. Use the Link
header to get the URL for the next page of users.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### since

The integer ID of the last User that you've seen.

**Type:** integer

</details>

## list_watched_repos

List repositories being watched by a user.

<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_watched_repos_for_user

List repositories being watched by the authenticated user.

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## list_watchers_for_repo

List Stargazers. New implementation.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## mark_notification_as_read

Mark as read.
Marking a notification as "read" removes it from the default view on GitHub.com.


<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## mark_notification_in_repo_as_read

Mark notifications as read in a repository.
Marking all notifications in a repository as "read" removes them from the
default view on GitHub.com.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## mark_notification_thread_as_read

Mark a thread as read

<details><summary>Parameters</summary>

#### id (required)

Id of thread.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## merge_pull_request

Merge a pull request (Merge Button's)

<details><summary>Parameters</summary>

#### number (required)

Id of pull.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## merge_repo

Perform a merge.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## mute_notification_thread_subscription

Delete a Thread Subscription.

<details><summary>Parameters</summary>

#### id (required)

Id of thread.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## post_markdown

Render an arbitrary Markdown document

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## post_markdown_raw

Render a Markdown document in raw mode

<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## remove_email_from_user

Delete email address(es).
You can include a single email address or an array of addresses.


<details><summary>Parameters</summary>

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## remove_label_for_issue

Remove a label from an issue.

<details><summary>Parameters</summary>

#### name (required)

Name of the label.

**Type:** string

#### number (required)

Number of issue.

**Type:** integer

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## remove_membership_for_user_on_team

Remove team membership.
In order to remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. NOTE: This does not delete the user, it just removes their membership from the team.


<details><summary>Parameters</summary>

#### teamId (required)

Id of team.

**Type:** integer

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## remove_repo_from_team

In order to remove a repository from a team, the authenticated user must be an owner of the org that the team is associated with. NOTE: This does not delete the repository, it just removes it from the team.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### teamId (required)

Id of team.

**Type:** integer

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_code_frequency_for_repo

Get the number of additions and deletions per week.
Returns a weekly aggregate of the number of additions and deletions pushed
to a repository.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_commit_activity_for_repo

Get the last year of commit activity data.
Returns the last year of commit activity grouped by week. The days array
is a group of commits per day, starting on Sunday.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_contributors_for_repo

Get contributors list with additions, deletions, and commit counts.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_org_dashboard_for_user

This is the user's organization dashboard. You must be authenticated as the user to view this.

<details><summary>Parameters</summary>

#### org (required)

Name of organisation.

**Type:** string

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_participation_for_repo

Get the weekly commit count for the repo owner and everyone else.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_punch_card_for_repo

Get the number of commits per hour in each day.
Each array contains the day number, hour number, and number of commits
0-6 Sunday - Saturday
0-23 Hour of day
Number of commits

For example, [2, 14, 25] indicates that there were 25 total commits, during
the 2.00pm hour on Tuesdays. All times are based on the time zone of
individual commits.


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## report_status_combined_for_ref

Get the combined Status for a specific Ref
The Combined status endpoint is currently available for developers to preview. During the preview period, the API may change without advance notice. Please see the blog post for full details.
To access this endpoint during the preview period, you must provide a custom media type in the Accept header:
application/vnd.github.she-hulk-preview+json


<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### ref (required)

Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## search_code

Search code.

<details><summary>Parameters</summary>

#### q (required)

The search terms. This can be any combination of the supported code
search parameters:
'Search In' Qualifies which fields are searched. With this qualifier
you can restrict the search to just the file contents, the file path,
or both.
'Languages' Searches code based on the language it's written in.
'Forks' Filters repositories based on the number of forks, and/or
whether code from forked repositories should be included in the results
at all.
'Size' Finds files that match a certain size (in bytes).
'Path' Specifies the path that the resulting file must be at.
'Extension' Matches files with a certain extension.
'Users' or 'Repositories' Limits searches to a specific user or repository.


**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### order

The sort field. if sort param is provided. Can be either asc or desc.

**Type:** string

**Potential values:** desc, asc

#### sort

Can only be 'indexed', which indicates how recently a file has been indexed
by the GitHub search infrastructure. If not provided, results are sorted
by best match.


**Type:** string

**Potential values:** indexed

</details>

## search_issues

Find issues by state and keyword. (This method returns up to 100 results per page.)

<details><summary>Parameters</summary>

#### q (required)

The q search term can also contain any combination of the supported issue search qualifiers:

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### order

The sort field. if sort param is provided. Can be either asc or desc.

**Type:** string

**Potential values:** desc, asc

#### sort

The sort field. Can be comments, created, or updated. Default: results are sorted by best match.

**Type:** string

**Potential values:** updated, created, comments

</details>

## search_repos

Search repositories.

<details><summary>Parameters</summary>

#### q (required)

The search terms. This can be any combination of the supported repository
search parameters:
'Search In' Qualifies which fields are searched. With this qualifier you
can restrict the search to just the repository name, description, readme,
or any combination of these.
'Size' Finds repositories that match a certain size (in kilobytes).
'Forks' Filters repositories based on the number of forks, and/or whether
forked repositories should be included in the results at all.
'Created' and 'Last Updated' Filters repositories based on times of
creation, or when they were last updated.
'Users or Repositories' Limits searches to a specific user or repository.
'Languages' Searches repositories based on the language they are written in.
'Stars' Searches repositories based on the number of stars.


**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### order

The sort field. if sort param is provided. Can be either asc or desc.

**Type:** string

**Potential values:** desc, asc

#### sort

If not provided, results are sorted by best match.

**Type:** string

**Potential values:** stars, forks, updated

</details>

## search_users

Search users.

<details><summary>Parameters</summary>

#### q (required)

The search terms. This can be any combination of the supported user
search parameters:
'Search In' Qualifies which fields are searched. With this qualifier you
can restrict the search to just the username, public email, full name,
location, or any combination of these.
'Repository count' Filters users based on the number of repositories they
have.
'Location' Filter users by the location indicated in their profile.
'Language' Search for users that have repositories that match a certain
language.
'Created' Filter users based on when they joined.
'Followers' Filter users based on the number of followers they have.


**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

#### order

The sort field. if sort param is provided. Can be either asc or desc.

**Type:** string

**Potential values:** desc, asc

#### sort

If not provided, results are sorted by best match.

**Type:** string

**Potential values:** followers, repositories, joined

</details>

## star_gist

Star a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## star_repo

Star a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## transfer_repo

Transfer a repository. This API is currently available for developers to preview. see https://developer.github.com/changes/2017-11-09-repository-transfer-api-preview/

<details><summary>Parameters</summary>

#### owner (required)

The original owner of the repo

**Type:** string

#### repo (required)

The repository name

**Type:** string

#### $body

**Type:** object

#### Accept

Is used to set specified media type.

**Type:** string

</details>

## unfollow_user

Unfollow a user.
Unfollowing a user requires the user to be logged in and authenticated with
basic auth or OAuth with the user:follow scope.


<details><summary>Parameters</summary>

#### username (required)

Name of user.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## unstar_gist

Unstar a gist.

<details><summary>Parameters</summary>

#### id (required)

Id of gist.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## unstar_repo

Unstar a repository

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## unwatch_repo

Stop watching a repository

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

## watch_repo

Watch a repository.

<details><summary>Parameters</summary>

#### owner (required)

Name of repository owner.

**Type:** string

#### repo (required)

Name of repository.

**Type:** string

#### Accept

Is used to set specified media type.

**Type:** string

#### X-GitHub-Media-Type

You can check the current version of media type in responses.

**Type:** string

#### X-GitHub-Request-Id

**Type:** integer

</details>

