[Skip to main content](https://ai.google.dev/gemini-api/docs/logs-datasets#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs/logs-datasets)
- [Deutsch](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ko)

[Get API key](https://aistudio.google.com/apikey) [Cookbook](https://github.com/google-gemini/cookbook) [Community](https://discuss.ai.google.dev/c/gemini-api/)Sign in

- On this page
- [1\. Enable logging in Google AI Studio](https://ai.google.dev/gemini-api/docs/logs-datasets#1_enable_logging_in_google_ai_studio)
- [2\. View logs in AI Studio](https://ai.google.dev/gemini-api/docs/logs-datasets#2_view_logs_in_ai_studio)
- [3\. Curate and share datasets](https://ai.google.dev/gemini-api/docs/logs-datasets#3_curate_and_share_datasets)
- [Next steps & what to test](https://ai.google.dev/gemini-api/docs/logs-datasets#next_steps_what_to_test)
- [Compatibility](https://ai.google.dev/gemini-api/docs/logs-datasets#compatibility)

Gemini 3.1 Flash-Lite Preview is now available. [Try it in AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview).


- [Home](https://ai.google.dev/)
- [Gemini API](https://ai.google.dev/gemini-api)
- [Docs](https://ai.google.dev/gemini-api/docs)



 Send feedback



# Logs and datasets

- On this page
- [1\. Enable logging in Google AI Studio](https://ai.google.dev/gemini-api/docs/logs-datasets#1_enable_logging_in_google_ai_studio)
- [2\. View logs in AI Studio](https://ai.google.dev/gemini-api/docs/logs-datasets#2_view_logs_in_ai_studio)
- [3\. Curate and share datasets](https://ai.google.dev/gemini-api/docs/logs-datasets#3_curate_and_share_datasets)
- [Next steps & what to test](https://ai.google.dev/gemini-api/docs/logs-datasets#next_steps_what_to_test)
- [Compatibility](https://ai.google.dev/gemini-api/docs/logs-datasets#compatibility)

This guide contains everything you need to get started with enabling logging
for your existing Gemini API applications. In this guide you'll learn how to
view logs from an existing or new application in the Google AI Studio dashboard
to better understand model behavior and how users may be interacting with your
applications. Use logging to observe, debug, and _optionally share usage feedback_
_with Google to help improve Gemini across developer use cases_.[\*](https://ai.google.dev/gemini-api/docs/logs-policy)

All `GenerateContent` and `StreamGenerateContent` API calls are supported,
including those made through [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)
endpoints.

## 1. Enable logging in Google AI Studio

Before you begin, ensure you have a billing-enabled project that you own.

1. Open the logs page in Google [AI Studio](https://aistudio.google.com/logs).
2. Choose your project from the drop-down and press the enable button to enable logging for all requests by default.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png)

You can enable or disable logging for all projects or for specific projects, and
change these preferences at any time through Google AI Studio.

## 2. View logs in AI Studio

1. Go to [AI Studio](https://aistudio.google.com/logs).
2. Select the project you've enabled logging for.
3. You should see your logs appear in the table in reverse chronological order.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Click on an entry for a full page view of the request and response pair. You can
inspect the full prompt, the complete response from Gemini, and the context from
the previous turn. Note that each project has a default storage limit of up to
1,000 logs, and logs not saved in datasets will expire after 55 days. If your
project reaches its storage limit you will be promoted to delete logs.

## 3. Curate and share datasets

- From the logs table, locate the filter bar at the top to select a property to
filter by.
- From your filtered view of logs use the checkboxes to select all or a
few of the logs.
- Click the "Create Dataset" button that appears at the top of the list.
- Give your new dataset a descriptive name and optional description.
- You will see the dataset you just created with the curated set of logs.
- Export your dataset for further analysis as CSV, JSONL files or to Google Sheets.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Datasets can be helpful for a number of different use cases.

- **Curate challenge sets:** Drive future improvements that target areas where you want your AI to improve.
- **Curate sample sets:** For example, a sample from real usage to generate responses from another model, or a collection of edge cases for routine checks before deployment.
- **Evaluation sets:** Sets that are representative of real usage across important capabilities, for comparison across other models or system instruction iterations.

You can help drive progress in AI research, the Gemini API, and Google AI Studio
by choosing to share your datasets as demonstration examples. This allows us to
refine our models in diverse contexts and create AI systems that remain useful
to developers across many fields and applications

## Next steps & what to test

Now that you have logging enabled, here are a few things to try:

- **Prototype with session history:** Leverage [AI Studio Build](https://aistudio.google.com/apps) to vibe code apps and add your API key to enable a history of user logs.
- **Re-run logs with the Gemini Batch API:** Use datasets for response sampling
and evaluation of models or application logic by re-running logs via the
[Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Compatibility

Logging is not currently supported for the following:

- Imagen and Veo models
- Gemini embedding model
- Inputs containing videos, GIFs or PDFs



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-31 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2025-12-31 UTC."\],\[\],\[\]\]