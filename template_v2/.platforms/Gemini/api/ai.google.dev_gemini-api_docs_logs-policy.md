[Skip to main content](https://ai.google.dev/gemini-api/docs/logs-policy#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/logs-policy)
- [Deutsch](https://ai.google.dev/gemini-api/docs/logs-policy?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/logs-policy?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/logs-policy?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/logs-policy?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/logs-policy?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/logs-policy?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/logs-policy?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/logs-policy?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/logs-policy?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/logs-policy?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/logs-policy?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/logs-policy?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/logs-policy?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/logs-policy?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/logs-policy?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/logs-policy?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%2Flogs-policy&prompt=select_account)

- On this page
- [1\. Data that can be shared](https://ai.google.dev/gemini-api/docs/logs-policy#1_data_that_can_be_shared)
- [2\. How we use your data](https://ai.google.dev/gemini-api/docs/logs-policy#2_how_we_use_your_data)
- [3\. Data permissions](https://ai.google.dev/gemini-api/docs/logs-policy#3_data_permissions)
- [4\. Data sharing and feedback](https://ai.google.dev/gemini-api/docs/logs-policy#4_data_sharing_and_feedback)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)

Was this helpful?



 Send feedback



# Data Logging and Sharing

- On this page
- [1\. Data that can be shared](https://ai.google.dev/gemini-api/docs/logs-policy#1_data_that_can_be_shared)
- [2\. How we use your data](https://ai.google.dev/gemini-api/docs/logs-policy#2_how_we_use_your_data)
- [3\. Data permissions](https://ai.google.dev/gemini-api/docs/logs-policy#3_data_permissions)
- [4\. Data sharing and feedback](https://ai.google.dev/gemini-api/docs/logs-policy#4_data_sharing_and_feedback)

This page outlines the storage and management of
[Gemini API logs](https://ai.google.dev/gemini-api/docs/logs-datasets), which are developer-owned
API data from supported Gemini API calls for projects with billing enabled. Logs
encompass the entire process from a user's request to the model's response.

## 1. Data that can be shared

As a project owner you have the choice to opt-in to logging of Gemini API calls,
for your own use or for feedback and sharing with Google to help us continually
improve our models.

With logging enabled, you can help us build AI systems that continue to be
valuable for developers across various fields and use cases by choosing to
contribute the following data for product improvements and model training:

- **Datasets:** Use the Logs and Datasets interface of Google AI Studio to
choose logs (requests, responses, metadata etc.) of interest from
supported Gemini API calls; contributed through inclusion in datasets, with the
option to opt-out during dataset creation.
- **Feedback:** When reviewing logs, you can provide feedback; including thumbs
up/down ratings and any written comments you provide.

When you share a dataset with Google, your logs in that dataset, including
requests and responses, will be processed in accordance with our
[Terms](https://developers.google.com/terms) for
" [Unpaid Services](https://ai.google.dev/gemini-api/terms#data-use-unpaid),"
meaning the dataset may be used to develop and improve Google
products, services, and machine learning technologies, including improving and
training our models. **Do not include personal, sensitive, or confidential**
**information.**

## 2. How we use your data

Logs will expire after 55 days by default. They will become unavailable
after this period. Datasets can be created to retain logs of interest or value
beyond this period for downstream use cases and optional contribution to model
improvements. Logs stored in datasets do not have set expiry dates, however each
project has a default storage limit of up to 1,000 logs.

By default, because logging is only available for billing-enabled projects,
prompts and responses within logs are not used for product improvement or
development, in accordance with our [Terms](https://developers.google.com/terms)
on data use.

If you choose to share datasets of your logs with Google, those datasets will be
used as real-world demonstration data to better understand the diversity of
domains and contexts AI systems and applications are used in. This data may be
used to improve model quality, and inform the training and evaluation of future
models and services. This data is processed in accordance with our data use
terms for [Unpaid Services](https://ai.google.dev/gemini-api/terms#data-use-unpaid).
Accordingly, human reviewers may read, annotate, and process the API inputs and
outputs you share. Before data is used for model improvement, Google takes steps
to protect user privacy as part of this process. This includes disconnecting
this data from your Google Account, API key, and Cloud project before reviewers
see or annotate it.

## 3. Data permissions

By opting-in to contributing API data, you confirm that you have the necessary
permissions for Google to process and use the data as described in this
documentation. **Please do not contribute logs containing sensitive,**
**confidential, or proprietary information obtained through the paid service**.
The license you grant to Google under the " [Submission of Content](https://developers.google.com/terms#b_submission_of_content)"
section in the API Terms also extends, to the extent required under applicable
law for our use, to any content (e.g., prompts, including associated system
instructions, cached content, and files such as images, videos, or documents)
you submit to the Services and to any generated responses.

## 4. Data sharing and feedback

You can help us advance the frontier of AI research, the Gemini API and Google
AI Studio by opting in to share your data as examples, enabling us to
continually improve our models across various contexts and build AI systems that
continue to be valuable to developers across various fields and use cases.

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2025-12-18 UTC."\],\[\],\[\]\]