# 🚨 Anti-Snooze Text Challenge Alarm

A lightweight Python-based automated desktop alarm system built to defeat heavy sleep inertia. The alarm forces the Windows system volume to 100% and loops a custom audio track indefinitely until the user successfully types a pre-configured verification phrase into the terminal.

## 🛠️ The Problem & Logic Flow

Standard mobile and desktop alarms fail because hitting "Snooze" requires zero cognitive effort. This project breaks sleep inertia by forcing the brain to activate:
1. **Un-bypassable Volume:** The script continually overrides hardware muting and volume down actions, locking system master volume to maximum capacity.
2. **Cognitive Challenge:** The alarm loop will not terminate until a precise text string is manually typed into the terminal console.

```text
       [System Clock Check]
                 │
                 ▼
     (Does Time == ALARM_TIME?) 
        ├── No  ──► Sleep 5 seconds & Loop
        └── Yes ──► [Force Master Volume to 100%]
                          │
                          ▼
                  [Start Audio Loop]
                          │
                          ▼
                 [Prompt User Input]
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
(Input == SECRET_KEY)             (Input != SECRET_KEY)
        │                                   │
        ▼ Yes                               ▼ No
[Stop Music & Terminate]            [Maintain Max Volume]
                                            │
                                            ▼
                                    [Loop Input Prompt]