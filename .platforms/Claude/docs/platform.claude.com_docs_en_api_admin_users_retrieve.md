Users

Retrieve

Copy page

# Get User

GET/v1/organizations/users/{user\_id}

Get User

##### Path ParametersExpand Collapse

user\_id: string

ID of the User.

##### ReturnsExpand Collapse

User = object {id, added\_at, email, 3 more}

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 3 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

"managed"

type: "user"

Object type.

For Users, this is always `"user"`.

Get User

```
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
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