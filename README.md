# پروژه برنامه‌نویسی سوکت - سیستم چت

## درس: شبکه‌های کامپیوتری

---

## 👨‍💻 توضیحات پروژه
یک سیستم چت چند مرحله‌ای با استفاده از برنامه‌نویسی سوکت در پایتون. 
در این پروژه، یک سیستم ساده ارتباط کلاینت و سرور در 4 فاز به مرور توسعه داده شده و در نهایت به یک سیستم چت با رابط گرافیکی تبدیل شده است.

---

## 🧩 تکنولوژی‌های استفاده شده
- پایتون
- برنامه‌نویسی سوکت (Socket Programming)
- چندنخی (Threading)
- رابط گرافیکی Tkinter

---

## 📌 فازهای پروژه

### 🟢 فاز ۱ - ارتباط ساده کلاینت و سرور
- ایجاد ارتباط ساده بین کلاینت و سرور
- ارسال پیام از کلاینت به سرور
- پاسخ ساده از سمت سرور

📷 سرور run می‌شود و منتظر کلاینت می‌ماند:


<img width="613" height="174" alt="Screenshot 2026-05-16 094551" src="https://github.com/user-attachments/assets/f3ab5ea4-7b93-48af-bfd7-0cec5d60575f" />


📷 کلاینت به سرور وصل می‌شود و به صورت خودکار یک پیام Hello Server برای سرور ارسال می‌کند (پیام کلاینت در سمت سرور قابل مشاهده است، در عکس بعد):


<img width="614" height="153" alt="Screenshot 2026-05-16 094823" src="https://github.com/user-attachments/assets/9bda8b01-264b-430c-a9e0-25cf75b84f50" />


📷 سرور اتصال کلاینت را با نمایش IP آن اعلام کرده و به او جواب Hello Client می‌فرستد (پیام سرور در سمت کلاینت قابل مشاهده است، در عکس قبل):


<img width="624" height="194" alt="Screenshot 2026-05-16 094755" src="https://github.com/user-attachments/assets/8c1cc096-dba9-4d64-8636-e34cec461ca7" />




---

### 🟡 فاز ۲ - پشتیبانی از چند کلاینت
- پشتیبانی از چند کلاینت به صورت همزمان با استفاده از Threading
- هر کلاینت می‌تواند پیام ارسال کند و پاسخ دریافت کند
- امکان خروج با دستور /exit (مازاد برای این فاز)
- ثبت و نمایش IP کلاینت‌ها هنگام اتصال و قطع اتصال

📷 سرور run می‌شود. کلاینت ها می‌توانند همزمان به سرور وصل شوند و هرکدام پیام خود را ارسال کنند، و برای خروج از اتصال می‌توانند از دستور /exit استفاده کرده و سرور خروج آن ها را به درستی و بدون کرش کردن مدیریت می‌کند:

<img width="625" height="247" alt="Screenshot 2026-05-16 105453" src="https://github.com/user-attachments/assets/1949c4a8-de82-4810-a763-2f1ade099794" />

<img width="625" height="214" alt="Screenshot 2026-05-16 105505" src="https://github.com/user-attachments/assets/4cbcb378-82db-4ce1-ace8-8bb970d34fd9" />

<img width="623" height="198" alt="Screenshot 2026-05-16 105518" src="https://github.com/user-attachments/assets/5113e7b2-8a86-4352-9cba-3439d8c78787" />




---

### 🟠 فاز ۳ - سیستم چت گروهی (Broadcast)
- امکان چت بین چند کلاینت به صورت همزمان
- ارسال پیام یک کلاینت به همه کلاینت‌ها
- نمایش پیام‌ها به صورت زنده
- امکان خروج با دستور /exit
- نمایش IP فرستنده هر پیام

📷 تصویر:

<img width="643" height="269" alt="Screenshot 2026-05-16 110836" src="https://github.com/user-attachments/assets/e0c90764-f966-4194-af88-02d44aa4db02" />

<img width="636" height="230" alt="Screenshot 2026-05-16 110912" src="https://github.com/user-attachments/assets/e34028b2-59e3-4f82-9cc4-dace9fe7b4ac" />

<img width="626" height="212" alt="Screenshot 2026-05-16 110923" src="https://github.com/user-attachments/assets/fe1b05e4-40f6-4754-b159-29fd342742e1" />



---

### 🔵 فاز ۴ - رابط گرافیکی (GUI)
- افزودن رابط گرافیکی برای کلاینت
- نمایش زمان ارسال پیام‌ها
- امکان ارسال پیام خصوصی با استفاده از @username
- بهبود تجربه کاربری

📷 تصویر:

<img width="694" height="146" alt="Screenshot 2026-05-16 112410" src="https://github.com/user-attachments/assets/f5115dfd-358f-4ee5-9173-8cdc8f32f3b9" />

<img width="673" height="152" alt="Screenshot 2026-05-16 112421" src="https://github.com/user-attachments/assets/2c3c8385-e1b2-4acd-b815-6176d8a298db" />

<img width="663" height="152" alt="Screenshot 2026-05-16 112432" src="https://github.com/user-attachments/assets/bfcc6d46-441a-4267-b280-d7a23190f9be" />

<img width="762" height="799" alt="Screenshot 2026-05-16 031134" src="https://github.com/user-attachments/assets/c20ef056-3de5-4e21-a56a-a30f8b1a791c" />

<img width="1905" height="803" alt="Screenshot 2026-05-16 030831" src="https://github.com/user-attachments/assets/0883e095-81e5-461a-8d03-f242a6edad8d" />

<img width="1277" height="808" alt="Screenshot 2026-05-16 030857" src="https://github.com/user-attachments/assets/f3f1ca31-828f-4b07-b98f-76963f10a073" />

<img width="678" height="229" alt="Screenshot 2026-05-16 112711" src="https://github.com/user-attachments/assets/4e3deded-34d4-4423-8aa1-ba041c3c0bb2" />






---

## 🚀 نحوه اجرا

### اجرای سرور
```bash
python server.py
