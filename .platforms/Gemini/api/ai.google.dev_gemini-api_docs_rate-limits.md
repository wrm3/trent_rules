[Skip to main content](https://ai.google.dev/gemini-api/docs/rate-limits#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/rate-limits)
- [Deutsch](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/rate-limits?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/rate-limits?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/rate-limits?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/rate-limits?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/rate-limits?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/rate-limits?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/rate-limits?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/rate-limits?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/rate-limits?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Frate-limits&prompt=select_account)

- On this page
- [How rate limits work](https://ai.google.dev/gemini-api/docs/rate-limits#how-rate-limits-work)
- [Usage tiers](https://ai.google.dev/gemini-api/docs/rate-limits#usage-tiers)
- [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits)
- [Batch API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits#batch-api)
- [How to upgrade to the next tier](https://ai.google.dev/gemini-api/docs/rate-limits#how-to-upgrade-to-the-next-tier)
- [Request a rate limit increase](https://ai.google.dev/gemini-api/docs/rate-limits#request-rate-limit-increase)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Rate limits

- On this page
- [How rate limits work](https://ai.google.dev/gemini-api/docs/rate-limits#how-rate-limits-work)
- [Usage tiers](https://ai.google.dev/gemini-api/docs/rate-limits#usage-tiers)
- [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits)
- [Batch API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits#batch-api)
- [How to upgrade to the next tier](https://ai.google.dev/gemini-api/docs/rate-limits#how-to-upgrade-to-the-next-tier)
- [Request a rate limit increase](https://ai.google.dev/gemini-api/docs/rate-limits#request-rate-limit-increase)

Rate limits regulate the number of requests you can make to the Gemini API
within a given timeframe. These limits help maintain fair usage, protect against
abuse, and help maintain system performance for all users.

[View your active rate limits in AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days)

## How rate limits work

Rate limits are usually measured across three dimensions:

- Requests per minute ( **RPM**)
- Tokens per minute (input) ( **TPM**)
- Requests per day ( **RPD**)

Your usage is evaluated against each limit, and exceeding any of them will
trigger a rate limit error. For example, if your RPM limit is 20, making 21
requests within a minute will result in an error, even if you haven't exceeded
your TPM or other limits.

Rate limits are applied per project, not per API key. Requests per day ( **RPD**)
quotas reset at midnight Pacific time.

Limits vary depending on the specific model being used, and some limits only
apply to specific models. For example, Images per minute, or IPM, is only
calculated for models capable of generating images (Nano Banana), but is
conceptually similar to TPM. Other models might have a token per day limit (TPD).

Rate limits are more restricted for experimental and preview models.

## Usage tiers

Rate limits are tied to the project's usage tier. As your API usage and spending
increase, you'll be automatically upgraded to a higher tier with increased rate
limits.

The qualifications for Tiers 2 and 3 are based on the total cumulative spending
on Google Cloud services (including, but not limited to, the Gemini API) for the
billing account linked to your project.

| Tier | Qualifications |
| --- | --- |
| Free | Users in [eligible countries](https://ai.google.dev/gemini-api/docs/available-regions) |
| Tier 1 | Full paid Billing account [linked to the project](https://ai.google.dev/gemini-api/docs/billing#setup-billing) |
| Tier 2 | Total spend: > $250 and at least 30 days since successful payment |
| Tier 3 | Total spend: > $1,000 and at least 30 days since successful payment |

When you request an upgrade, our automated abuse protection system performs
additional checks. While meeting the stated qualification criteria is generally
sufficient for approval, in rare cases an upgrade request may be denied based on
other factors identified during the review process.

This system helps maintain the security and integrity of the Gemini API platform
for all users.

## Gemini API rate limits

Rate limits depend on a variety of factors (such as your quota tier) and can be
viewed in Google AI Studio. As your tier and account status change over time,
your rate limits will automatically be updated.

[View your active rate limits in AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days)

Specified rate limits are not guaranteed and actual capacity may vary.

## Batch API rate limits

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api) requests are subject to their own rate
limits, separate from the non-batch API calls.

- **Concurrent batch requests:** 100
- **Input file size limit:** 2GB
- **File storage limit:** 20GB
- **Enqueued tokens per model:** The **Batch enqueued tokens** table lists the
maximum number of tokens that can be enqueued for batch processing across
all your active batch jobs for a given model.

[Tier 1](https://ai.google.dev/gemini-api/docs/rate-limits#tier-1)[Tier 2](https://ai.google.dev/gemini-api/docs/rate-limits#tier-2)[Tier 3](https://ai.google.dev/gemini-api/docs/rate-limits#tier-3)More

| Model | Batch enqueued tokens |
| --- | --- |
| Text-out models |
| Gemini 3.1 Pro Preview | 5,000,000 |
| Gemini 3.1 Flash-Lite Preview | 10,000,000 |
| Gemini 3 Flash Preview | 3,000,000 |
| Gemini 2.5 Pro | 5,000,000 |
| Gemini 2.5 Pro TTS | 25,000 |
| Gemini 2.5 Flash | 3,000,000 |
| Gemini 2.5 Flash Preview | 3,000,000 |
| Gemini 2.5 Flash Image Preview | 3,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 10,000,000 |
| Gemini 2.5 Flash-Lite Preview | 10,000,000 |
| Gemini 2.0 Flash | 10,000,000 |
| Gemini 2.0 Flash Image | 3,000,000 |
| Gemini 2.0 Flash-Lite | 10,000,000 |
| Multi-modal generation models |
| Gemini 3.1 Flash Image Preview 🍌 | 1,000,000 |
| Gemini 3 Pro Image Preview 🍌 | 2,000,000 |

| Model | Batch enqueued tokens |
| --- | --- |
| Text-out models |
| Gemini 3.1 Pro Preview | 500,000,000 |
| Gemini 3.1 Flash-Lite Preview | 500,000,000 |
| Gemini 3.1 Flash Preview | 400,000,000 |
| Gemini 2.5 Pro | 500,000,000 |
| Gemini 2.5 Pro TTS | 100,000 |
| Gemini 2.5 Flash | 400,000,000 |
| Gemini 2.5 Flash Preview | 400,000,000 |
| Gemini 2.5 Flash Image Preview | 400,000,000 |
| Gemini 2.5 Flash TTS | 100,000 |
| Gemini 2.5 Flash-Lite | 500,000,000 |
| Gemini 2.5 Flash-Lite Preview | 500,000,000 |
| Gemini 2.0 Flash | 1,000,000,000 |
| Gemini 2.0 Flash Image | 400,000,000 |
| Gemini 2.0 Flash-Lite | 1,000,000,000 |
| Multi-modal generation models |
| Gemini 3.1 Flash Image Preview 🍌 | 250,000,000 |
| Gemini 3 Pro Image Preview 🍌 | 270,000,000 |

| Model | Batch enqueued tokens |
| --- | --- |
| Text-out models |
| Gemini 3.1 Pro Preview | 1,000,000,000 |
| Gemini 3.1 Flash-Lite Preview | 1,000,000,000 |
| Gemini 3.1 Flash Preview | 1,000,000,000 |
| Gemini 2.5 Pro | 1,000,000,000 |
| Gemini 2.5 Pro TTS | 1,000,000 |
| Gemini 2.5 Flash | 1,000,000,000 |
| Gemini 2.5 Flash Preview | 1,000,000,000 |
| Gemini 2.5 Flash Image Preview | 1,000,000,000 |
| Gemini 2.5 Flash TTS | 4,000,000 |
| Gemini 2.5 Flash-Lite | 1,000,000,000 |
| Gemini 2.5 Flash-Lite Preview | 1,000,000,000 |
| Gemini 2.0 Flash | 5,000,000,000 |
| Gemini 2.0 Flash Image | 1,000,000,000 |
| Gemini 2.0 Flash-Lite | 5,000,000,000 |
| Multi-modal generation models |
| Gemini 3.1 Flash Image Preview 🍌 | 750,000,000 |
| Gemini 3 Pro Image Preview 🍌 | 1,000,000,000 |

## How to upgrade to the next tier

To transition from the Free tier to a paid tier, you must first
[set up billing in AI Studio](https://ai.google.dev/gemini-api/docs/billing).

Once your project meets the [specified criteria](https://ai.google.dev/gemini-api/docs/rate-limits#usage-tiers), it will be
automatically upgraded to the next tier. Tier upgrades from the Free to Tier 1
will typically take effect instantly, and subsequent tier upgrades will take
effect within 10 minutes. Navigate to the [Projects page](https://aistudio.google.com/projects) in AI Studio to check your tiers.

## Request a rate limit increase

Each model variation has an associated rate limit (requests per minute, RPM).
For details on those rate limits, see the
[AI Studio Rate Limit](https://aistudio.google.com/rate-limit) page.

[Request paid tier rate limit increase](https://forms.gle/ETzX94k8jf7iSotH9)

We offer no guarantees about increasing your rate limit, but we'll do our best
to review your request.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-03 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-03-03 UTC."\],\[\],\[\]\]