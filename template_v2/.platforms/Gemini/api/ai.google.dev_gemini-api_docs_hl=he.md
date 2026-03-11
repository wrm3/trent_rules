[דילוג לתוכן הראשי](https://ai.google.dev/gemini-api/docs?hl=he#main-content)

[![Gemini API](https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg?hl=he)](https://ai.google.dev/)

`/`

Language

- [English](https://ai.google.dev/gemini-api/docs)
- [Deutsch](https://ai.google.dev/gemini-api/docs?hl=de)
- [Español – América Latina](https://ai.google.dev/gemini-api/docs?hl=es-419)
- [Français](https://ai.google.dev/gemini-api/docs?hl=fr)
- [Indonesia](https://ai.google.dev/gemini-api/docs?hl=id)
- [Italiano](https://ai.google.dev/gemini-api/docs?hl=it)
- [Polski](https://ai.google.dev/gemini-api/docs?hl=pl)
- [Português – Brasil](https://ai.google.dev/gemini-api/docs?hl=pt-br)
- [Shqip](https://ai.google.dev/gemini-api/docs?hl=sq)
- [Tiếng Việt](https://ai.google.dev/gemini-api/docs?hl=vi)
- [Türkçe](https://ai.google.dev/gemini-api/docs?hl=tr)
- [Русский](https://ai.google.dev/gemini-api/docs?hl=ru)
- [עברית](https://ai.google.dev/gemini-api/docs?hl=he)
- [العربيّة](https://ai.google.dev/gemini-api/docs?hl=ar)
- [فارسی](https://ai.google.dev/gemini-api/docs?hl=fa)
- [हिंदी](https://ai.google.dev/gemini-api/docs?hl=hi)
- [বাংলা](https://ai.google.dev/gemini-api/docs?hl=bn)
- [ภาษาไทย](https://ai.google.dev/gemini-api/docs?hl=th)
- [中文 – 简体](https://ai.google.dev/gemini-api/docs?hl=zh-cn)
- [中文 – 繁體](https://ai.google.dev/gemini-api/docs?hl=zh-tw)
- [日本語](https://ai.google.dev/gemini-api/docs?hl=ja)
- [한국어](https://ai.google.dev/gemini-api/docs?hl=ko)

[אחזור מפתח API](https://aistudio.google.com/apikey?hl=he) [ספר המתכונים](https://github.com/google-gemini/cookbook) [קהילה](https://discuss.ai.google.dev/c/gemini-api/?hl=he)

[היכנס](https://ai.google.dev/_d/signin?continue=https%3A%2F%2Fai.google.dev%2Fgemini-api%2Fdocs%3Fhl%3Dhe&prompt=select_account)


השקנו את Gemini 3.1 Flash-Lite Preview. [אפשר לנסות את זה ב-AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.1-flash-lite-preview&hl=he).




- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

# ‏Gemini API

הדרך הכי מהירה מהנחיה לתוצר עם Gemini,‏ Veo,‏ Nano Banana ועוד.

[Python](https://ai.google.dev/gemini-api/docs?hl=he#python)[JavaScript](https://ai.google.dev/gemini-api/docs?hl=he#javascript)[Go](https://ai.google.dev/gemini-api/docs?hl=he#go)[Java](https://ai.google.dev/gemini-api/docs?hl=he#java)[C#‎](https://ai.google.dev/gemini-api/docs?hl=he#c%E2%80%8E)[REST](https://ai.google.dev/gemini-api/docs?hl=he#rest)עוד

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "parts": [\
          {\
            "text": "Explain how AI works in a few words"\
          }\
        ]\
      }\
    ]
  }'
```

[אני רוצה להתחיל לפתח](https://ai.google.dev/gemini-api/docs/quickstart?hl=he)

כדאי לעיין במדריך למתחילים כדי לקבל מפתח API ולבצע את הקריאה הראשונה ל-API תוך כמה דקות.

* * *

## הכירו את המודלים

[הצג הכול](https://ai.google.dev/gemini-api/docs/models?hl=he)

[auto\_awesome\\
Gemini 3.1 Pro\\
חדש\\
\\
המודל הכי חכם שלנו, הכי טוב בעולם בהבנה מולטימודלית, והכול מבוסס על יכולות רציונליות מתקדמות.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=he) [spark\\
‫Gemini 3 Flash\\
חדש\\
\\
ביצועים ברמה של Frontier, שמתחרים במודלים גדולים יותר בעלות נמוכה בהרבה.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=he) [spark\\
Gemini 3.1 Flash-Lite\\
חדש\\
\\
מודל חזק לעבודה עם נפחים גדולים של נתונים, שמתאים לתרחישים שבהם העלות היא שיקול חשוב, עם הביצועים והאיכות של סדרת Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=he) [🍌\\
‫Nano Banana 2 ו-Nano Banana Pro\\
\\
\\
מודלים חדשניים ליצירה ולעריכה של תמונות.](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) [video\_library\\
Veo 3.1\\
\\
\\
המודל המתקדם שלנו ליצירת סרטונים, עם אודיו מובנה.](https://ai.google.dev/gemini-api/docs/video?hl=he) [spark\\
Gemini Robotics\\
\\
\\
מודל ראייה-שפה (VLM) שמביא את יכולות ה-AI של Gemini לרובוטיקה ומאפשר הסקת מסקנות מתקדמת בעולם הפיזי.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=he)

## יכולות

[imagesmode\\
\\
יצירת תמונות באופן טבעי (Nano Banana)\\
\\
\\
יצירה ועריכה של תמונות עם הקשר רחב באמצעות Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=he) [article\\
\\
הקשר רחב\\
\\
\\
להזין מיליוני טוקנים למודלים של Gemini ולקבל תובנות מתמונות, סרטונים ומסמכים לא מובנים.](https://ai.google.dev/gemini-api/docs/long-context?hl=he) [code\\
\\
פלט מובנה\\
\\
\\
להגביל את Gemini לתגובה ב-JSON, שהוא פורמט נתונים מובְנה שמתאים לעיבוד אוטומטי.](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) [functions\\
\\
בקשה להפעלת פונקציה\\
\\
\\
אפשר ליצור תהליכי עבודה מבוססי-סוכנים על ידי חיבור Gemini לממשקי API ולכלים חיצוניים.](https://ai.google.dev/gemini-api/docs/function-calling?hl=he) [videocam\\
\\
יצירת סרטונים באמצעות Veo 3.1\\
\\
\\
אתם יכולים ליצור תוכן וידאו באיכות גבוהה מהנחיות טקסט או תמונה באמצעות המודל המתקדם שלנו.](https://ai.google.dev/gemini-api/docs/video?hl=he) [android\_recorder\\
\\
נציגי תמיכה קוליים עם Live API\\
\\
\\
אפשר ליצור סוכנים ואפליקציות קוליות בזמן אמת באמצעות Live API.](https://ai.google.dev/gemini-api/docs/live?hl=he) [build\\
\\
כלים\\
\\
\\
חיבור של Gemini לעולם באמצעות כלים מובנים כמו חיפוש Google, הקשר של כתובת URL, מפות Google, הרצת קוד ושימוש במחשב.](https://ai.google.dev/gemini-api/docs/tools?hl=he) [stacks\\
\\
הבנת מסמכים\\
\\
\\
אפשר לעבד עד 1,000 דפים של קובצי PDF עם הבנה מלאה של מודלים מולטי-מודאליים או סוגים אחרים של קבצים מבוססי-טקסט.](https://ai.google.dev/gemini-api/docs/document-processing?hl=he) [cognition\_2\\
\\
העמקה\\
\\
\\
כדאי לבדוק איך יכולות החשיבה משפרות את ההנמקה במשימות מורכבות ובסוכנים.](https://ai.google.dev/gemini-api/docs/thinking?hl=he)

[‏Google AI Studio\\
\\
\\
אפשר לבדוק הנחיות, לנהל את מפתחות ה-API, לעקוב אחרי השימוש וליצור אבות טיפוס.](https://aistudio.google.com/?hl=he) [group\\
\\
קהילת המפתחים\\
\\
\\
לשאול שאלות ולמצוא פתרונות ממפתחים אחרים וממהנדסי Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=he) [menu\_book\\
\\
הפניית API\\
\\
\\
מידע מפורט על Gemini API זמין במאמרי העזרה הרשמיים.](https://ai.google.dev/api?hl=he) [sensors\\
\\
סטטוס\\
\\
\\
בדיקת הסטטוס של Gemini API,‏ Google AI Studio ושירותי המודלים שלנו.](https://aistudio.google.com/status?hl=he)

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב [מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-03-03 (שעון UTC).




\[\[\["התוכן קל להבנה","easyToUnderstand","thumb-up"\],\["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"\],\["סיבה אחרת","otherUp","thumb-up"\]\],\[\["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"\],\["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"\],\["התוכן לא עדכני","outOfDate","thumb-down"\],\["בעיה בתרגום","translationIssue","thumb-down"\],\["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"\],\["סיבה אחרת","otherDown","thumb-down"\]\],\["עדכון אחרון: 2026-03-03 (שעון UTC)."\],\[\],\[\]\]