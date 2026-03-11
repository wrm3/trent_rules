Invites

Delete

Copy page

# Delete Invite

DELETE/v1/organizations/invites/{invite\_id}

Delete Invite

##### Path ParametersExpand Collapse

invite\_id: string

ID of the Invite.

##### ReturnsExpand Collapse

id: string

ID of the Invite.

type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

Delete Invite

```
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

##### Returns Examples

Ask Docs
![Chat avatar](https://platform.claude.com/docs/images/book-icon-light.svg)

a.claude.ai

# a.claude.ai is blocked

**a.claude.ai** refused to connect.

ERR\_BLOCKED\_BY\_RESPONSE

**a.claude.ai** refused to connect.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)