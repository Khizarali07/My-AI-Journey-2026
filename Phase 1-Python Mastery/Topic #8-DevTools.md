# Topic 1.8: Dev Tools - Virtual Environments & Debugging

As a professional AI Backend Engineer, writing code is only half the battle. You also need to know how to manage your project's environment and how to fix bugs efficiently without littering your code with `print()` statements.

This guide covers two essential tools: **Virtual Environments** and the **VS Code Debugger**.

---

## 1. Virtual Environments (`.venv`)

### Why do we need them?
Python installs packages globally by default. If Project A needs `pandas==1.0` and Project B needs `pandas==2.0`, you have a conflict.
A **Virtual Environment** is a self-contained folder that holds a specific version of Python and the libraries for *just one project*.

### How to Create & Activate

#### Step 1: Create the Environment
Open your terminal in VS Code (Ctrl+`) and run:
```bash
# This creates a hidden folder named ".venv"
python -m venv .venv
```

#### Step 2: Activate the Environment
You must "activate" the environment every time you work on the project.

**Windows (PowerShell):**
```powershell
.venv\Scripts\activate
```
*Note: If you get a permission error, run `Set-ExecutionPolicy Unrestricted -Scope Process` first.*

**Mac / Linux:**
```bash
source .venv/bin/activate
```

**How do I know it worked?**
You will see `(.venv)` appear in green at the start of your terminal command line.

---

## 2. The VS Code Debugger

Stop using `print("var is:", var)`! The debugger lets you pause code execution, inspect variables, and step through logic line-by-line.

### How to use it

#### Step 1: Set a Breakpoint ("The Red Dot")
A breakpoint tells Python: *"Stop right here so I can look around."*

1. Open `Topic #8.1.py`.
2. Move your mouse to the left of the line number (e.g., line 15).
3. Click to create a **Red Dot**.
   - *Keyboard Shortcut:* Click the line and press **F9**.

#### Step 2: Start Debugging
1. Press **F5** (or go to the "Run and Debug" icon in the left sidebar and click "Run").
2. Select "Python File" if prompted.

#### Step 3: Debug Controls
Once the code hits your red dot, it freezes. A toolbar appears at the top:

- **Continue (F5):** Resume running until the next breakpoint.
- **Step Over (F10):** Run the current line and move to the next one (skips going *inside* functions).
- **Step Into (F11):** Go *inside* a function call to see how it works.
- **Step Out (Shift+F11):** Finish the current function and return to where it was called.
- **Restart (Ctrl+Shift+F5):** Start over.
- **Stop (Shift+F5):** Kill the program.

### Inspecting Variables
While the code is paused:
- **Hover** over any variable (e.g., `current_sum`) to see its value.
- Look at the **Variables** pane on the left side of VS Code.

---

## 3. Git Basics (Quick Reference)

Since this is the end of Phase 1, make sure you are saving your progress!

```bash
git init                # Initialize a new repo (do this once)
git add .               # Stage all changes
git commit -m "Message" # Save the snapshot
```
