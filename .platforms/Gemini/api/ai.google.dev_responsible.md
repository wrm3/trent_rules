[Skip to main content](https://ai.google.dev/responsible#main-content)

[![Google AI for Developers](https://www.gstatic.com/devrel-devsite/prod/v75e3d64006adca2b8b590c38f10bf440310b485b03499ed9671198292b2883b7/googledevai/images/lockup-new.svg)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/responsible)
- [Deutsch](https://ai.google.dev/responsible?hl=de)
- [Español – América Latina](https://ai.google.dev/responsible?hl=es-419)
- [Français](https://ai.google.dev/responsible?hl=fr)
- [Indonesia](https://ai.google.dev/responsible?hl=id)
- [Italiano](https://ai.google.dev/responsible?hl=it)
- [Polski](https://ai.google.dev/responsible?hl=pl)
- [Português – Brasil](https://ai.google.dev/responsible?hl=pt-br)
- [Shqip](https://ai.google.dev/responsible?hl=sq)
- [Tiếng Việt](https://ai.google.dev/responsible?hl=vi)
- [Türkçe](https://ai.google.dev/responsible?hl=tr)
- [Русский](https://ai.google.dev/responsible?hl=ru)
- [עברית](https://ai.google.dev/responsible?hl=he)
- [العربيّة](https://ai.google.dev/responsible?hl=ar)
- [فارسی](https://ai.google.dev/responsible?hl=fa)
- [हिंदी](https://ai.google.dev/responsible?hl=hi)
- [বাংলা](https://ai.google.dev/responsible?hl=bn)
- [ภาษาไทย](https://ai.google.dev/responsible?hl=th)
- [中文 – 简体](https://ai.google.dev/responsible?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/responsible?hl=zh-tw)
- [日本語](https://ai.google.dev/responsible?hl=ja)
- [한국어](https://ai.google.dev/responsible?hl=ko)

[Sign in](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fresponsible&prompt=select_account)

- [Responsible Generative AI Toolkit](https://ai.google.dev/responsible)

- [Home](https://ai.google.dev/)
- [Responsible Generative AI Toolkit](https://ai.google.dev/responsible)



 Send feedback



# Responsible Generative AI Toolkit

Tools and guidance to design, build and evaluate open AI models responsibly.

[![Align your model icon](https://ai.google.dev/static/images/responsible/responsible-approach.svg)\\
\\
Responsible application design\\
\\
Define rules for model behaviour, create a safe and accountable application, and maintain transparent communication with users.](https://ai.google.dev/responsible#design) [![Align your model icon](https://ai.google.dev/static/images/responsible/align-your-model.svg)\\
\\
Safety alignment\\
\\
Discover prompt-debugging techniques and guidance for fine-tuning and RLHF to align AI models with safety policies.](https://ai.google.dev/responsible#align) [![Evaluate icon](https://ai.google.dev/static/images/responsible/evaluate.svg)\\
\\
Model evaluation\\
\\
Find guidance and data to conduct a robust model evaluation for safety, fairness, and factuality with the LLM Comparator.](https://ai.google.dev/responsible#evaluate) [![Framework flexible](https://ai.google.dev/static/images/responsible/protect-with-safeguard.svg)\\
\\
Safeguards\\
\\
Deploy safety classifiers, using off-the-shelf solutions or build your own with step-by-step tutorials.](https://ai.google.dev/responsible#protect)

Get started

Define system-level policies

Determine what type of content your application should and should not generate.

- [Define policies](https://ai.google.dev/responsible/docs/design#define-policies)
- [See examples](https://ai.google.dev/responsible/docs/design#hypothetical-policies)

Design for safety

Define your overall approach to implement risk mitigation techniques, considering technical and business tradeoffs.

- [Learn more](https://ai.google.dev/responsible/docs/design#design-safety)

Be transparent

Communicate your approach with artifacts like model cards.

- [See Templates](https://ai.google.dev/responsible/docs/design#transparency-artifacts)

Secure AI systems

Consider AI-specific security risks and remediation methods highlighted in the Secure AI Framework (SAIF).

- [Google's Secure AI Framework](https://safety.google/cybersecurity-advancements/saif/)
- [Documentation](https://ai.google.dev/responsible/docs/design#secure-ai)

Get started

Craft safer, more robust prompts

Use the power of LLMs to help craft safer prompt templates with the Model Alignment library.

- [Try now](https://colab.research.google.com/github/pair-code/model-alignment/blob/main/notebooks/Gemma_for_Model_Alignment.ipynb)
- [Model Alignment](https://ai.google.dev/responsible/docs/alignment/model-alignment)

Tune models for safety

Control model behavior by tuning your model to align with your safety and content policies.

- [Learn about Tuning](https://ai.google.dev/responsible/docs/alignment#tuning)
- [Learn about Tuning SFT](https://ai.google.dev/responsible/docs/alignment#tuning-sft)
- [Learn about Tuning RLHF](https://ai.google.dev/responsible/docs/alignment#tuning-rlhf)

Investigate model prompts

Build safe and helpful prompts through iterative improvement with the Learning Interpretability Tool (LIT).

Model prompts video

- [Try now](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemma/docs/lit_gemma.ipynb)
- [Learning Interpretability Tool](https://ai.google.dev/responsible/docs/alignment/lit)

Get started

LLM Comparator

Conduct side-by-side evaluations with LLM Comparator to qualitatively assess differences in responses between models, different prompts for the same model, or even different tunings of a model

LLM Comparator video

- [Try demo](https://pair-code.github.io/llm-comparator/)
- [Learn about LLM Comparator](https://ai.google.dev/responsible/docs/evaluation#llm-comparator)

Model evaluation guidelines

Learn about red teaming best practices and evaluate your model against academic benchmarks to assess harms around safety, fairness, and factuality.

- [Learn more](https://ai.google.dev/responsible/docs/evaluation)
- [See benchmarks](https://ai.google.dev/responsible/docs/evaluation#benchmarks)
- [See red teaming best practices](https://ai.google.dev/responsible/docs/evaluation#red-teaming)

Get started

SynthID Text

A tool for watermarking and detecting text generated by your model.

- [SynthID text watermarking](https://ai.google.dev/responsible/docs/safeguards/synthid)

ShieldGemma

A series of content safety classifiers, built on Gemma 2, available in three sizes: 2B, 9B, 27B.

- [ShieldGemma content safety classifiers](https://ai.google.dev/responsible/docs/safeguards/shieldgemma)

Agile classifiers

Create safety classifiers for your specific policies using parameter efficient tuning (PET) with relatively little training data

- [Create safety classifiers](https://ai.google.dev/responsible/docs/safeguards/agile-classifiers)

Checks AI Safety

Ensure AI safety compliance against your content policies with APIs and monitoring dashboards.

- [Checks AI Safety](https://checks.google.com/ai-safety/?utm_source=GenAITK&utm_medium=Link&utm_campaign=AI_Toolkit)

Text moderation service

Detect a list of safety attributes, including various potentially harmful categories and topics that may be considered sensitive with this Google Cloud Natural Language API available for free below a certain usage limit.

- [Cloud Natural Language API](https://cloud.google.com/natural-language/docs/moderating-text#:~:text=Text%20moderation%20analyzes%20a%20document,document%2C%20call%20the%20moderateText%20method.&text=Content%20that%20is%20rude%2C%20disrespectful%2C%20or%20unreasonable)
- [Cloud Natural Language pricing](https://cloud.google.com/natural-language/pricing)

Perspective API

Identify "toxic" comments with this free Google Jigsaw API to mitigate online toxicity and ensure healthy dialogue.

- [Perspective API](https://perspectiveapi.com/)


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\[\],\[\],\[\]\]