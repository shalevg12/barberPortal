# BARBER ARCADE ✂️🎮

הפורטל המרכזי לכל המשחקים של אבי וקוקו במספרה, מותאם למובייל ולעברית (RTL).

**כתובת קבועה:** https://shalevg12.github.io/barberPortal/

**שלט QR להדפסה:** https://shalevg12.github.io/barberPortal/qr.html

## משחקים

- [קרב המספריים — Barber Battle](https://shalevg12.github.io/barber-battle/)
- [מרוץ המספרה — Temple Run Maspera](https://shalevg12.github.io/templeRunMaspera/)
- [פלפי ברבר — Flappy Barber](https://shalevg12.github.io/flappyBarber/)

## הוספת משחק חדש

כל משחק נשאר בריפוזיטורי נפרד. כדי להוסיף משחק לפורטל, מוסיפים אובייקט נוסף למערך שבקובץ [games.js](games.js), עם המאפיינים:

- id — מזהה ייחודי
- name, englishName — שמות להצגה
- description, category, label, symbol — טקסטים וכיתוב בכרטיס
- theme — battle, run או flappy (אפשר להוסיף עיצובים בעתיד)
- url — הכתובת הציבורית של המשחק

אין צורך לעדכן את קוד ה-QR: הוא תמיד מפנה לפורטל ולא למשחק מסוים.

## GitHub Pages

האתר סטטי (HTML, CSS, JavaScript) ולא דורש התקנה, בנייה או שרת.

ב-GitHub: **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**.

לאחר שהפריסה פעילה, ניתן להיכנס לכתובת הקבועה ולהדפיס את השלט מתוך qr.html.

## תמונות וקוד QR

תמונות אבי וקוקו נלקחו ממשחקי המספרה הקיימים. קובץ QR סטטי נשמר ב-assets/portal-qr.png ומקודד לכתובת הקבועה.
