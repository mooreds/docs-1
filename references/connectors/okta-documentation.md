---
id: okta-documentation
title: Okta (version v1.*.*)
sidebar_label: Okta
layout: docs.mustache
---

## activate_application

Activates an inactive application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

</details>

## activate_factor

The sms,call and token:software:totp factor types require activation to complete the enrollment process.

<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### $body

**Type:** object

</details>

## activate_factor_by_user

The `sms` and `token:software:totp` [factor types](#factor-type) require activation to complete the enrollment process.

<details><summary>Parameters</summary>

#### factorId (required)

**Type:** string

#### userId (required)

**Type:** string

#### $body

**Type:** object

</details>

## activate_policy



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

</details>

## activate_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### ruleId (required)

**Type:** string

</details>

## activate_rule

Activates a specific group rule by id from your organization

<details><summary>Parameters</summary>

#### ruleId (required)

**Type:** string

</details>

## activate_user

Activates a user. This operation can only be performed on users with a `STAGED` status. Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation. The user will have a status of `ACTIVE` when the activation process is complete.

<details><summary>Parameters</summary>

#### sendEmail (required)

Sends an activation email to the user if true

**Type:** boolean

#### userId (required)

**Type:** string

</details>

## add_factor

Enrolls a user with a supported [factor](#list-factors-to-enroll)

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

Factor

**Type:** object

#### activate

**Type:** boolean

#### templateId

id of SMS template (only for SMS factor)

**Type:** string

#### tokenLifetimeSeconds

**Type:** integer

#### updatePhone

**Type:** boolean

</details>

## add_group_target_to_role

Success

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### roleId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## add_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### $body

**Type:** object

#### activate

**Type:** boolean

</details>

## add_role_to_user

Assigns a role to a user.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

</details>

## add_user_to_group

Adds a [user](users.html#user-model) to a group with `OKTA_GROUP` type.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## answer_recovery_question

Answers the user's recovery question to ensure only the end user redeemed the recovery token for recovery transaction with a RECOVERY status.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## assign_user_to_application

Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### $body

**Type:** object

</details>

## authentication

Every authentication transaction starts with primary authentication which validates a user's primary password credential. Password Policy, MFA Policy, and Sign-On Policy are evaluated during primary authentication to determine if the user's password is expired, a factor should be enrolled, or additional verification is required. The transaction state of the response depends on the user's status, group memberships and assigned policies.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## cancel_transaction

Cancels the current transaction and revokes the state token.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## change_password

This operation changes a user's password by providing the existing password and the new password for authentication transactions with either the PASSWORD_EXPIRED or PASSWORD_WARN state. A user must change their expired password for an authentication transaction with PASSWORD_EXPIRED status to successfully complete the transaction. A user may opt-out of changing their password (skip) when the transaction has a PASSWORD_WARN status.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## change_password_by_user

Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid [password credential](#password-object)

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

#### strict

**Type:** boolean

</details>

## change_recovery_question

Changes a user's recovery question &amp; answer credential by validating the user's current password. This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid [password credential](#password-object)

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

</details>

## clone_application_key

Clones a X.509 certificate for an application key credential from a source application to target application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### keyId (required)

**Type:** string

#### targetAid (required)

Unique key of the target Application

**Type:** string

</details>

## create_application

Adds a new application to your Okta organization.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### activate

Executes activation lifecycle operation when creating the app

**Type:** boolean

</details>

## create_application_group_assignment

Assigns a group to an application

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### groupId (required)

**Type:** string

#### $body

**Type:** object

</details>

## create_group

Adds a new group with `OKTA_GROUP` type to your organization.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_policy



<details><summary>Parameters</summary>

#### $body

**Type:** object

#### activate

**Type:** boolean

</details>

## create_rule

Creates a group rule to dynamically add users to the specified group if they match the condition

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_session

Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_user

Creates a new user in your Okta organization with or without credentials.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### activate

Executes activation lifecycle operation when creating the user

**Type:** boolean

#### nextLogin

With activate=true, set nextLogin to "changePassword" to have the password be EXPIRED, so user must change it the next time they log in.

**Type:** string

#### provider

Indicates whether to create a user with a specified authentication provider

**Type:** boolean

</details>

## deactivate_application

Deactivates an active application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

</details>

## deactivate_or_delete_user

Deletes a user permanently. This operation can only be performed on users that have a `DEPROVISIONED` status. **This action cannot be recovered!**

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### sendEmail

**Type:** boolean

</details>

## deactivate_policy



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

</details>

## deactivate_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### ruleId (required)

**Type:** string

</details>

## deactivate_rule

Deactivates a specific group rule by id from your organization

<details><summary>Parameters</summary>

#### ruleId (required)

**Type:** string

</details>

## deactivate_user

Deactivates a user. This operation can only be performed on users that do not have a `DEPROVISIONED` status. Deactivation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `DEPROVISIONED` during deactivation to indicate that the user hasn't completed the asynchronous operation. The user will have a status of `DEPROVISIONED` when the deactivation process is complete.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### sendEmail

**Type:** boolean

</details>

## delete_application

Removes an inactive application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

</details>

## delete_application_group_assignment

Removes a group assignment from an application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### groupId (required)

**Type:** string

</details>

## delete_application_user

Removes an assignment for a user from an application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### userId (required)

**Type:** string

#### sendEmail

**Type:** boolean

</details>

## delete_factor

Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor.

<details><summary>Parameters</summary>

#### factorId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## delete_group

Removes a group with `OKTA_GROUP` type from your organization.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

</details>

## delete_policy



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

</details>

## delete_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### ruleId (required)

**Type:** string

</details>

## delete_rule

Removes a specific group rule by id from your organization

<details><summary>Parameters</summary>

#### ruleId (required)

**Type:** string

#### removeUsers

**Type:** boolean

</details>

## end_all_user_sessions

Removes all active identity provider sessions. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### oauthTokens

Revoke issued OpenID Connect and OAuth refresh and access tokens

**Type:** boolean

</details>

## end_session



<details><summary>Parameters</summary>

#### sessionId (required)

**Type:** string

</details>

## enroll_factor

Enrolls a user with a factor assigned by their MFA Policy.Enroll Okta Security Question Factor Enroll Okta SMS Factor Enroll Okta Call Factor Enroll Okta Verify TOTP Factor Enroll Okta Verify Push Factor Enroll Google Authenticator Factor Enroll RSA SecurID Factor Enroll Symantec VIP Factor Enroll YubiKey Factor Enroll Duo Factor Enroll U2F FactorThis operation is only available for users that have not previously enrolled a factor and have transitioned to the MFA_ENROLL state.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## expire_password

This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### tempPassword

Sets the user's password to a temporary password, if true

**Type:** boolean

</details>

## forgot_password

Starts a new password recovery transaction for a given user and issues a recovery token that can be used to reset a user's password. Self-service password reset (forgot password) must be permitted via the user's assigned password policy to use this operation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## forgot_password_by_user

Generates a one-time token (OTT) that can be used to reset a user's password. The user will be required to validate their security question's answer when visiting the reset link. This operation can only be performed on users with a valid [recovery question credential](#recovery-question-object) and have an `ACTIVE` status.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

#### sendEmail

**Type:** boolean

</details>

## get_application

Fetches an application from your Okta organization by `id`.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_application_group_assignment

Fetches an application group assignment

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### groupId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_application_key

Gets a specific [application key credential](#application-key-credential-model) by `kid`

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### keyId (required)

**Type:** string

</details>

## get_application_user

Fetches a specific user assignment for application by `id`.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### userId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_factor

Fetches a factor for the specified user

<details><summary>Parameters</summary>

#### factorId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## get_group

Lists all group rules for your organization.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_logs

The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

<details><summary>Parameters</summary>

#### after

**Type:** string

#### filter

**Type:** string

#### limit

**Type:** integer

#### q

**Type:** string

#### since

**Type:** string

#### sortOrder

**Type:** string

#### until

**Type:** string

</details>

## get_policy



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### ruleId (required)

**Type:** string

</details>

## get_rule

Fetches a specific group rule by id from your organization

<details><summary>Parameters</summary>

#### ruleId (required)

**Type:** string

#### expand

**Type:** string

</details>

## get_session

Get details about a session.

<details><summary>Parameters</summary>

#### sessionId (required)

**Type:** string

</details>

## get_transaction_state

Every authentication transaction starts with primary authentication which validates a user's primary password credential. Password Policy, MFA Policy, and Sign-On Policy are evaluated during primary authentication to determine if the user's password is expired, a factor should be enrolled, or additional verification is required. The transaction state of the response depends on the user's status, group memberships and assigned policies.

*This operation has no parameters*

## get_user

Fetches a user from your Okta organization.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## list_app_links

Fetches appLinks for all direct or indirect (via group membership) assigned applications.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### showAll

**Type:** boolean

</details>

## list_application_group_assignments

Enumerates group assignments for an application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### after

Specifies the pagination cursor for the next page of assignments

**Type:** string

#### expand

**Type:** string

#### limit

Specifies the number of results for a page

**Type:** integer

#### q

**Type:** string

</details>

## list_application_keys

Enumerates key credentials for an application

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

</details>

## list_application_users

Enumerates all assigned [application users](#application-user-model) for an application.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### after

specifies the pagination cursor for the next page of assignments

**Type:** string

#### expand

**Type:** string

#### filter

**Type:** string

#### limit

specifies the number of results for a page

**Type:** integer

#### q

**Type:** string

#### query_scope

**Type:** string

</details>

## list_applications

Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query.

<details><summary>Parameters</summary>

#### after

Specifies the pagination cursor for the next page of apps

**Type:** string

#### expand

Traverses users link relationship and optionally embeds Application User resource

**Type:** string

#### filter

Filters apps by status, user.id, group.id or credentials.signing.kid expression

**Type:** string

#### includeNonDeleted

**Type:** boolean

#### limit

Specifies the number of results for a page

**Type:** integer

#### q

**Type:** string

</details>

## list_assigned_roles

Lists all roles assigned to a user.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### expand

**Type:** string

</details>

## list_factors

Enumerates all the enrolled factors for the specified user

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## list_group_targets_for_role

Success

<details><summary>Parameters</summary>

#### roleId (required)

**Type:** string

#### userId (required)

**Type:** string

#### after

**Type:** string

#### limit

**Type:** integer

</details>

## list_group_users

Enumerates all [users](/docs/api/resources/users.html#user-model) that are a member of a group.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### after

Specifies the pagination cursor for the next page of users

**Type:** string

#### limit

Specifies the number of user results in a page

**Type:** integer

#### managedBy

**Type:** string

</details>

## list_groups

Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query.

<details><summary>Parameters</summary>

#### after

Specifies the pagination cursor for the next page of groups

**Type:** string

#### expand

**Type:** string

#### filter

Filter expression for groups

**Type:** string

#### limit

Specifies the number of group results in a page

**Type:** integer

#### q

Searches the name property of groups for matching value

**Type:** string

</details>

## list_policies



<details><summary>Parameters</summary>

#### type (required)

**Type:** string

#### after

**Type:** string

#### expand

**Type:** string

#### limit

**Type:** integer

#### status

**Type:** string

</details>

## list_policy_rules



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

</details>

## list_rules

Lists all group rules for your organization.

<details><summary>Parameters</summary>

#### after

Specifies the pagination cursor for the next page of rules

**Type:** string

#### expand

**Type:** string

#### limit

Specifies the number of rule results in a page

**Type:** integer

</details>

## list_supported_factors

Enumerates all the [supported factors](#supported-factors-for-providers) that can be enrolled for the specified user

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## list_supported_security_questions

Enumerates all available security questions for a user's `question` factor

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## list_user_groups

Fetches the groups of which the user is a member.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### after

**Type:** string

#### limit

**Type:** integer

</details>

## list_users

Lists users in your organization with pagination in most cases. A subset of users can be returned that match a supported filter expression or search criteria.

<details><summary>Parameters</summary>

#### after

Specifies the pagination cursor for the next page of users

**Type:** string

#### expand

**Type:** string

#### filter

Filters users with a supported expression for a subset of properties

**Type:** string

#### format

**Type:** string

#### limit

Specifies the number of results returned

**Type:** integer

#### q

Finds a user that matches firstName, lastName, and email properties

**Type:** string

#### search

Searches for users with a supported filtering expression for most properties

**Type:** string

</details>

## previous_transaction_state

Moves the current transaction state back to the previous state. For example, when changing state from the start of primary authentication to MFA_ENROLL &gt; ENROLL_ACTIVATE &gt; OTP, the user's phone might stop working. Since the user can't see the QR code, the transaction must return to MFA_ENROLL.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## primary_authentication

Every authentication transaction starts with primary authentication which validates a user's primary password credential. Password Policy, MFA Policy, and Sign-On Policy are evaluated during primary authentication to determine if the user's password is expired, a factor should be enrolled, or additional verification is required. The transaction state of the response depends on the user's status, group memberships and assigned policies.

*This operation has no parameters*

## refresh_session



<details><summary>Parameters</summary>

#### sessionId (required)

**Type:** string

</details>

## remove_group_target_from_role

Success

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### roleId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## remove_group_user

Removes a [user](users.html#user-model) from a group with `OKTA_GROUP` type.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## remove_role_from_user

Unassigns a role from a user.

<details><summary>Parameters</summary>

#### roleId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## resend_call_recovery_challenge

Resends a Voice Call with OTP (passCode) to the user's phone

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## resend_sms_recovery_challenge

Resends a SMS OTP (passCode) to the user's mobile phone

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## reset_all_factors

This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## reset_password

Resets a user's password to complete a recovery transaction with a PASSWORD_RESET state.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## reset_password_by_user

Generates a one-time token (OTT) that can be used to reset a user's password. The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### provider

**Type:** string

#### sendEmail

**Type:** boolean

</details>

## skip_transaction_state

Send a skip link to skip the current transaction state and advance to the next state.If the response returns a skip link, then you can advance to the next state without completing the current state (such as changing the password).
For example, after being warned that a password will soon expire, the user can skip the change password prompt
by clicking a skip link.Another example: a user has enrolled in multiple factors. After enrolling in one the user receives a skip link
to skip the other factors.This operation is only available for MFA_ENROLL or PASSWORD_WARN states when published as a link.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## suspend_user

Suspends a user. This operation can only be performed on users with an `ACTIVE` status. The user will have a status of `SUSPENDED` when the process is complete.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## unlock_account

Starts a new unlock recovery transaction for a given user and issues a recovery token that can be used to unlock a user's account.Unlock Account with Email Factor Unlock Account with SMS Factor Unlock Account with Trusted ApplicationSelf-service unlock must be permitted via the user's assigned password policy to use this operation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## unlock_user

Unlocks a user with a `LOCKED_OUT` status and returns them to `ACTIVE` status. Users will be able to login with their current password.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## unsuspend_user

Unsuspends a user and returns them to the `ACTIVE` state. This operation can only be performed on users that have a `SUSPENDED` status.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## update_application

Updates an application in your organization.

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_application_user

Updates a user's profile for an application

<details><summary>Parameters</summary>

#### appId (required)

**Type:** string

#### userId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_group

Updates the profile for a group with `OKTA_GROUP` type from your organization.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_policy



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_policy_rule



<details><summary>Parameters</summary>

#### policyId (required)

**Type:** string

#### ruleId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_rule

Success

<details><summary>Parameters</summary>

#### ruleId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_user

Update a user's profile and/or credentials using strict-update semantics.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

#### strict

**Type:** boolean

</details>

## verify_call_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_call_recovery_factor

Verifies a Voice Call OTP (passCode) sent to the user's device for primary authentication for a recovery transaction with RECOVERY_CHALLENGE status.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## verify_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### $body

**Type:** object

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_factor_by_user

Verifies an OTP for a `token` or `token:hardware` factor

<details><summary>Parameters</summary>

#### factorId (required)

**Type:** string

#### userId (required)

**Type:** string

#### $body

**Type:** object

#### User-Agent

**Type:** string

#### X-Forwarded-For

**Type:** string

#### templateId

**Type:** string

#### tokenLifetimeSeconds

**Type:** integer

</details>

## verify_push_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_recovery_token

Validates a recovery token that was distributed to the end user to continue the recovery transaction.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## verify_security_question_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_sms_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_sms_recovery_factor

Verifies a SMS OTP (passCode) sent to the user's mobile phone for primary authentication for a recovery transaction with RECOVERY_CHALLENGE status.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## verify_totp_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

## verify_u2f_factor



<details><summary>Parameters</summary>

#### factorId (required)

Factor ID

**Type:** string

#### rememberDevice (required)

user's decision to remember device

**Type:** boolean

#### autoPush

user's decision to send push to device automatically

**Type:** boolean

</details>

