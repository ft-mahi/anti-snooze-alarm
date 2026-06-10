# 🚨 Anti-Snooze Text Challenge Alarm

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A Python-powered desktop alarm system designed to combat heavy sleep inertia and eliminate mindless snoozing. 

Unlike traditional alarms that can be dismissed with a single muscle-memory tap, this project forces you to engage cognitively before the alarm can be silenced. The system overrides your volume settings, continuously loops an alarm sound, and demands a predefined verification phrase to be typed perfectly before letting you go back to sleep (which, by then, you won't want to do!).

---

## ✨ Features

*   **🔊 Automatic Volume Boost:** Instantly raises the Windows master volume when triggered, ensuring the alarm cannot be ignored.
*   **🔁 Continuous Alarm Loop:** Plays a custom audio file indefinitely until the challenge is successfully completed.
*   **🧠 Cognitive Wake-Up Challenge:** Requires typing a specific verification phrase to prevent unconscious alarm dismissal.
*   **⏰ Scheduled Background Trigger:** Runs silently in the background and activates precisely at the configured time.
*   **🔒 Verification-Based Dismissal:** Incorrect text input is rejected, and the alarm continues blaring until the exact phrase is entered.

---

## 💡 Why This Exists

Most alarms fail because dismissing them requires almost zero mental effort. We silence them while half-asleep and immediately fall back into bed. 

This project introduces a small but highly effective cognitive barrier. It forces your brain to "boot up" to solve the challenge, breaking sleep inertia and significantly reducing the likelihood of oversleeping.

---

## 📌 How It Works

1. The application continuously checks the system clock in the background.
2. Once the alarm time hits, the system volume is automatically boosted.
3. The alarm audio starts looping.
4. The terminal prompts you to enter the verification phrase.
5. Entering the **wrong phrase** keeps the alarm active and prompts you again.
6. Entering the **correct phrase** stops the audio and exits the program successfully.

### 🏗️ System Flow

```text
      [System Clock Check]
                │
                ▼
   (Current Time == Alarm Time?)
        ├── No ──► Wait & Continue Monitoring
        │
        ▼ Yes
 [Increase System Volume]
                │
                ▼
      [Start Alarm Loop]
                │
                ▼
     [Request Verification]
                │
      ┌─────────┴─────────┐
      ▼                   ▼
  Correct Input      Wrong Input
      │                   │
      ▼                   ▼
 [Stop Alarm]      [Keep Alarm Active]
      │                   │
      └───────────┬───────┘
                  ▼
          [Ask Again]
