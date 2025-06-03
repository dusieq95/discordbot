## 📚 ShapesInc AI Chatbot for Discord — User Manual

### 1. What This Bot Does

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

#### 3.5. Run Locally (Optional)

> **Note:** Running on your local computer is fine for testing, but it will stop working if you close your machine or lose internet.

   #### 3.6. Install Dependencies
   
   1. Make sure you have **Python 3** installed.
   2. In your terminal, run (inside the cloned folder):
   
      ```bash
      pip install --upgrade pip
      pip3 install -r requirements.txt
      ```
   
      This will download all the Python packages the bot needs.
   
      if you getting this error:
      ![error: externally-managed-environment](https://github.com/user-attachments/assets/de7885e9-c287-407a-ad58-7f32b4a0b83f)
   
      then use:
      ```bash
      python3 -m venv ChatBot_env
      ```
   
      You can name `ChatBot_env` to anything you want
   
      then enable your environment by using:
      
      ```bash
      source ChatBot/bin/activate
      ```
   
      ![Installing Dependencies](https://github.com/user-attachments/assets/f866007e-fb7b-49a0-b262-4112373957d5)

1. In your terminal (still inside the repo folder), create a file named .env (if it doesn’t exist).
   
   Open .env in a text editor, and paste in:

   ```ini
   SHAPES_API_KEY="your_shapesinc_api_key_here"
   SHAPES_APP_ID="your_shapesinc_app_id_here"
   DISCORD_TOKEN="your_discord_bot_token_here"
   MODEL="your_shapesinc_model_name_here"
   ```

   Replace each placeholder in quotes with your actual values.
   
    **SHAPES_API_KEY**: Paste the API Key from ShapesInc.

    **SHAPES_APP_ID**: Paste the App ID from ShapesInc.

    **DISCORD_TOKEN**: You’ll get this in the next section.

    **MODEL**: This should match your bot’s “model name” on ShapesInc (e.g. if you named your bot “otahun,” then MODEL="otahun").

2. Save that and run:

   ```bash
   python3 main.py
   ```

3. You should see messages like “Bot is starting…” and “Connected to Discord.”

4. Invite your bot to a Discord server (use the OAuth2 URL Generator in the Developer Portal, check the “bot” scope, give it permissions, and copy the generated invite link).

   ![image](https://github.com/user-attachments/assets/06ae6fe1-8092-475f-a78f-27fe6622a3c5)

---

#### 3.7. Host on Render (Recommended for 24/7 Uptime)

1. Go to [Render.com](https://render.com/) and **sign up** (you can use GitHub to log in).

2. Click **New** → **Web Service** → **Connect to GitHub** → select your `ShapesInc_For_Discord` repo.

![Give your workspace name and select free plan](https://github.com/user-attachments/assets/8d1cccc2-1895-404d-80ad-9b74fecfc80d)

![Select the service you want i choose web service(2nd one)](https://github.com/user-attachments/assets/30fc2400-ced2-4a53-bc8f-20a4be631264)

![Connect your github account(you can also host your private github repos)](https://github.com/user-attachments/assets/177f1bfe-280c-418f-9ee8-d46e288fe280)

![Go to configuration](https://github.com/user-attachments/assets/6edf5b52-df19-4a27-a5b2-bc361de1728b)

![select the repo you wanna use then press save. Now close the window and get back to render](https://github.com/user-attachments/assets/372d3601-1918-4ee0-9929-d327eafbe0bf)

8. Now you can able to see the repo, by clicking the repo name you will be redirect to deployment configuration do the steps as below.
   1. name your project
  
   2. In the **Build Command** field, enter:
      
   ```bash
   pip install --upgrade pip && pip3 install -r requirements.txt
   ```
      
   3. In the **Start Command** field(if you by any chance renamed your main.py file to anything else for example something.py then use `python3 something.py`), enter:
      
   ```bash
   python3 main.py
   ```
     
![image](https://github.com/user-attachments/assets/cba756b0-270c-4437-98a4-f85093e1ea06)

9. Configure your environment variable

 Under **Environment**, add these variables exactly as in your `.env` file:

   | Key              | Value                          |
   | ---------------- | ------------------------------ |
   | SHAPES\_API\_KEY | (your\_shapesinc\_api\_key)    |
   | SHAPES\_APP\_ID  | (your\_shapesinc\_app\_id)     |
   | DISCORD\_TOKEN   | (your\_discord\_bot\_token)    |
   | MODEL            | (your\_shapesinc\_model\_name) |


6. Click **Create Web Service**. Render will read your repo, install dependencies, and run your bot automatically.

![image](https://github.com/user-attachments/assets/322bd923-735e-4553-9884-4308d07cd7e3)

7. Whenever you push code to GitHub, Render will re-deploy it for you.

![image](https://github.com/user-attachments/assets/78f86c8c-a7b9-4313-a827-7f2b8cc0aa10)
   
---

### 4. How to Use `/authorize`

1. In any Discord channel where your bot is invited, type:

   ```ini
   /authorize
   ```
2. The bot will reply with a private link (only you can see it).

   ![image](https://github.com/user-attachments/assets/3c7ee059-1c26-4a99-89d2-a91cf3bfad63)

4. Click the link, copy the **authorization code** you see.

   ![Shapes Authorized code](https://github.com/user-attachments/assets/47e92ea5-a31c-42b4-b4a2-85bb995748b7)


6. Back in Discord, type (replace `KJXM9ZUM` with the one you got):

   ```ini
   /authorize code:KJXM9ZUM
   ```
   
7. If successful, the bot will say “Successfully Autholrised!” and you can start chatting or sending images.

   ![Successfully authorised](https://github.com/user-attachments/assets/0bf4adc6-784d-4b3e-ab0b-4d1924ed4cce)

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

## 7. Special Thanks!
Big thanks to **@Rishiraj0100**, whose [ShapesInc Library](https://github.com/Rishiraj0100/shapesinc-py) made building this chatbot so much smoother. Your work and contributions to this repo are truly appreciated!

---

### 7. Congrats—You’re Done!

If you followed these steps, your **self-hosted** ShapesInc AI Chatbot for Discord should be up and running!.
