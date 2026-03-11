API Reference

Models

Copy page

cURL

# Models

##### [List Models](https://platform.claude.com/docs/en/api/models/list)

GET/v1/models

##### [Get a Model](https://platform.claude.com/docs/en/api/models/retrieve)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

ModelInfo = object {id, created\_at, display\_name, type}

id: string

Unique model identifier.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

Ask Docs
![Chat avatar](https://platform.claude.com/docs/images/book-icon-light.svg)

a.claude.ai

# a.claude.ai is blocked

**a.claude.ai** refused to connect.

ERR\_BLOCKED\_BY\_RESPONSE

**a.claude.ai** refused to connect.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)