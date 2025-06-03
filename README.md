```markdown
![Short description of this image](path/to/your-image.png)
```

---

## 📚 ShapesInc AI Chatbot for Discord — User Manual

### 1. What My Own Bot Does

* **Reads images:** You can send pictures, and the bot understands them.
* **Chats like a real human:** Text conversations feel natural.
* **Writes code on request:** Ask it to generate code snippets.(vary depending upon what prompts you gave to your own bot)
* **Recognizes each Discord user:** It won’t confuse everyone for “you.”
* **Secure “/authorize” system:** Each person must verify themselves before chatting so it won't get confuse by whom it talking to.

---

### 2. Prerequisites

1. **A GitHub account** (to clone the repo).
2. **A ShapesInc account** (for your API key and App ID).
3. **A Discord account** (to create your own Discord Bot).
4. **Basic computer with internet access.**
5. (Optional) A hosting service (if you don’t want to run it on your local machine). We’ll show a step by step of how to use a free service called [Render](https://render.com/) below(no credit card required!), but you can pick any service that reads from GitHub.

---

### 3. Step-by-Step Setup

#### 3.1. Clone This Repository

1. Open a terminal (Command Prompt, PowerShell, or any shell).
2. Run:

   ```bash
   git clone https://github.com/Psyphen36/ShapesInc_For_Discord.git
   cd ShapesInc_For_Discord
   ```
---

#### 3.2. Get Your ShapesInc API Key & App ID

1. Go to [ShapesInc Developer section]([https://shapes.inc/developer)) if you haven't signup or log in then do that first.
2. Navigate to **Create New API Key** (or similar).
3. Select 3rd option **APPLICATION**
4. name the **key** then press **Generate API Key** 

   ![ShapesInc Dashboard showing API keys](https://github.com/user-attachments/assets/108d9a52-8ef4-42d1-9366-2c347ef856cf)

---

#### 3.3. Update the Bot’s Configuration

1. Go to [Render](https://render.com/)

2. Create Your account

3. Give your workspace a name and select free plan then press create new account
![Give your workspace name and selecte free plan](https://github.com/user-attachments/assets/8d1cccc2-1895-404d-80ad-9b74fecfc80d)

4. Select the service you want i choose web service(2nd one)
![image](https://github.com/user-attachments/assets/30fc2400-ced2-4a53-bc8f-20a4be631264)

5. Connect your github account(you can also host your private github repos)
![image](https://github.com/user-attachments/assets/177f1bfe-280c-418f-9ee8-d46e288fe280)

6.Go to configuration
![configure](https://github.com/user-attachments/assets/6edf5b52-df19-4a27-a5b2-bc361de1728b)

7.select the repo you wanna use then press save. Now close the window and get back to render
![image](https://github.com/user-attachments/assets/372d3601-1918-4ee0-9929-d327eafbe0bf)

8. Now you can able to see the repo, by clicking the repo name you will be redirect to deployment configuration do the steps as below.
     1. name your project
  
     2. use this on Build Command
  
     ```bash
     pip install --upgrade pip && pip3 install -r requirements.txt
     ```
     
     3. use this on Start Command(if you by any chance renamed your main.py file to anything else for example something.py then use `python3 something.py`)
     ```bash
     python3 main.py 
     ```
     
![image](https://github.com/user-attachments/assets/cba756b0-270c-4437-98a4-f85093e1ea06)

9. Configure your environment variable
![image](https://github.com/user-attachments/assets/322bd923-735e-4553-9884-4308d07cd7e3)

   **put your actual values**.

   * **SHAPES\_API\_KEY:** Paste the API Key from ShapesInc.
   * **SHAPES\_APP\_ID:** Paste the App ID from ShapesInc.
   * **DISCORD\_TOKEN:** You’ll get this in the next section.
   * **MODEL:** This should match your bot’s “model name” on ShapesInc (e.g. if you named your bot “otahun,” then `MODEL="otahun"`).

---

#### 3.4. Create Your Discord Bot & Get Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, give it a name (e.g. “My ShapesInc Bot”), and click **Create**.
3. In the left menu, select **Bot** → **Add Bot** → **Yes, do it!**
4. Under the Bot section, find **Token** and click **Copy**.
5. Paste that token into your `.env` file as `DISCORD_TOKEN`.

  ![image](https://github.com/user-attachments/assets/31ea3aaf-2ee3-44e0-a8df-d004179f2b3d)

Note: click these three buttons that are present in the same Bot section
![image](https://github.com/user-attachments/assets/5c3568c8-45ba-4899-a672-e837507fdb69)

---

#### 3.5. Install Dependencies

1. Make sure you have **Python 3** installed.
2. In your terminal, run (inside the cloned folder):

   ```bash
   pip install --upgrade pip
   pip3 install -r requirements.txt
   ```

   This will download all the Python packages the bot needs.

   ![Terminal installing requirements](images/install-reqs.png)
   *(Insert a screenshot of the terminal running `pip3 install -r requirements.txt`.)*

---

#### 3.6. Run Locally (Optional)

> **Note:** Running on your local computer is fine for testing, but it will stop working if you close your machine or lose internet.

1. In your terminal (still inside the repo folder), run:

   ```bash
   python3 main.py
   ```

2. You should see messages like “Bot is starting…” and “Connected to Discord.”

3. Invite your bot to a Discord server (use the OAuth2 URL Generator in the Developer Portal, check the “bot” scope, give it permissions, and copy the generated invite link).

   ![Bot running locally](images/bot-running.png)
   *(Screenshot of terminal showing bot is online.)*

---

#### 3.7. Host on Render (Recommended for 24/7 Uptime)

1. Go to [Render.com](https://render.com/) and **sign up** (you can use GitHub to log in).

2. Click **New** → **Web Service** → **Connect to GitHub** → select your `ShapesInc_For_Discord` repo.

3. Under **Environment**, add these variables exactly as in your `.env` file:

   | Key              | Value                          |
   | ---------------- | ------------------------------ |
   | SHAPES\_API\_KEY | (your\_shapesinc\_api\_key)    |
   | SHAPES\_APP\_ID  | (your\_shapesinc\_app\_id)     |
   | DISCORD\_TOKEN   | (your\_discord\_bot\_token)    |
   | MODEL            | (your\_shapesinc\_model\_name) |

4. In the **Build Command** field, enter:

   ```
   pip install --upgrade pip && pip3 install -r requirements.txt
   ```

5. In the **Start Command** field, enter:

   ```
   python3 main.py
   ```

6. Click **Create Web Service**. Render will read your repo, install dependencies, and run your bot automatically.

7. Whenever you push code to GitHub, Render will re-deploy it for you.

   ![Render environment variables setup](images/render-env.png)
   *(Add a screenshot of Render’s environment variable form.)*

---

### 4. How to Use `/authorize`

1. In any Discord channel where your bot is invited, type:

   ```
   /authorize
   ```
2. The bot will reply with a private link (only you can see it).
3. Click the link, copy the **authorization code** you see.
4. Back in Discord, type (replace `CODE123` with the one you got):

   ```
   /authorize code:CODE123
   ```
5. If successful, the bot will say “You are now verified!” and you can start chatting or sending images.

   ![Authorize flow in Discord](images/authorize-flow.png)
   *(Insert a screenshot of the bot replying with the link, and then the user sending `/authorize code:...`.)*

---

### 5. Common Troubleshooting

* **Bot doesn’t start / crash on launch:**

  * Double-check that your `.env` (or Render environment variables) are correct—no extra spaces or missing quotes.
  * Ensure you ran `pip3 install -r requirements.txt`.
  * Check the Discord token: if it’s revoked, regenerate it in the Developer Portal.
* **Bot is online but doesn’t respond to commands:**

  * Make sure your bot is invited to the server with the correct permissions (e.g. “Send Messages,” “Read Message History,” “Use Slash Commands”).
  * Check that you registered the slash commands (sometimes you need to run a separate script or wait a few minutes for Discord to update).
* **“Invalid authorization code” when using `/authorize`:**

  * Copy the code exactly (no extra spaces).
  * Make sure you clicked the link from the same Discord user—only that user sees the code.

---

### 6. Adding Your Own Images

Whenever you want to show what something looks like (for example, how to set up a Discord application or how your terminal should look), add images into a folder called `images/` (or whatever you like). Then, in the README:

```markdown
![Description of what this screenshot shows](images/your-image-file.png)
```

* Keep image filenames short and descriptive (e.g., `clone-repo.png`, `discord-token.png`).
* Make sure to commit and push the `images/` folder alongside your README.

---

### 7. Congrats—You’re Done!

If you followed these steps, your **self-hosted** ShapesInc AI Chatbot for Discord should be up and running.

* Anyone in your server can now chat, send images, and get code suggestions.
* Each user must run `/authorize` once to verify.
* You can always come back to this README if you need reminders or want to add more screenshots.

Happy hosting!
