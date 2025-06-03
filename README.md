
## 📚 ShapesInc AI Chatbot for Discord — User Manual

---

### 1. What This Bot Does

- **Image Understanding:** Send pictures, and the bot will describe or respond to them.
- **Natural Conversations:** Chat as if you’re talking to a real person.
- **On-Demand Code Generation:** Request code snippets tailored to your prompts.
- **User Recognition:** Maintains separate contexts for each Discord user, so it never confuses one user for another.
- **Secure Authorization:** Requires each user to verify via `/authorize` before chatting—ensuring the bot knows who it’s talking to.

---

### 2. Prerequisites

- **GitHub Account** (to clone the repository).  
- **ShapesInc Account** (to obtain your API key and App ID).  
- **Discord Account** (to create and manage your Discord bot).  
- **Internet-Connected Computer** (to run and test the bot).  
- **Optional Hosting Service** (if you need 24/7 uptime). We’ll demonstrate using [Render](https://render.com/), which has a free tier and doesn’t require a credit card. You can substitute any service that integrates with GitHub.

---

### 3. Step-by-Step Setup

#### 3.1. Clone This Repository

* Open a terminal (Command Prompt, PowerShell, or any shell).
*  Run:
*  
   ```css
   git clone https://github.com/Psyphen36/ShapesInc_For_Discord.git
   cd ShapesInc_For_Discord
   ```

---

#### 3.2. Obtain Your ShapesInc API Key & App ID

* Visit the [ShapesInc Developer section](https://shapes.inc/developer). If you don’t have an account, sign up or log in.
   
* Navigate to **Create New API Key** (or similar).

* Select **APPLICATION** as the key type.
   
* Give the key a name, then click **Generate API Key**.

* Copy both the **API Key** and the **App ID**.


![ShapesInc Dashboard showing API keys](https://github.com/user-attachments/assets/108d9a52-8ef4-42d1-9366-2c347ef856cf)

---

#### 3.3. Create Your Discord Bot & Retrieve the Token

* Go to the [Discord Developer Portal](https://discord.com/developers/applications).

* Click **New Application**, enter a name (e.g., “My ShapesInc Bot”), and click **Create**.

* In the left sidebar, select **Bot** → **Add Bot** → **Yes, do it!**

* Under the **Bot** section, locate **Token** and click **Copy**.

* Save this token for your `.env` file under `DISCORD_TOKEN`.


![Discord Bot Token](https://github.com/user-attachments/assets/31ea3aaf-2ee3-44e0-a8df-d004179f2b3d)

> **Reminder:** In the same **Bot** section, click the three-dot menu (⚙️) to enable the following:
> 
> - **Presence Intent**
>     
> - **Server Members Intent**
>     
> - **Message Content Intent**
>     
> 
> ![Enable Bot Intents](https://github.com/user-attachments/assets/5c3568c8-45ba-4899-a672-e837507fdb69)

---

#### 3.4. Run Locally (Optional)

> **Note:** Running locally is great for testing, but the bot will go offline if your computer shuts down or loses internet.


* **Install Dependencies**

- Ensure you have **Python 3** installed.
  
- In the cloned repo’s root folder, run:
  
 ```css
 pip install --upgrade pip
 pip3 install -r requirements.txt
 ```
   
 - If you see the error:
  
  ```css
   error: externally-managed-environment
  ```
 
   create a virtual environment:
  
 ```ruby
 python3 -m venv ChatBot_env
 ```
  
   Activate it:
  
  - On Linux/macOS:
  
```bash
source ChatBot_env/bin/activate
``` 
   
- On Windows (PowerShell):

```css
ChatBot_env\Scripts\Activate.ps1
```

- After activation, rerun:
   
```css
pip install --upgrade pip
pip3 install -r requirements.txt
```


![Installing Dependencies](https://github.com/user-attachments/assets/f866007e-fb7b-49a0-b262-4112373957d5)

 **Configure Environment Variables**

- In the repo folder, create a file named `.env` (if it doesn’t exist).
   
- Open `.env` in your text editor and add:

```ini
SHAPES_API_KEY="your_shapesinc_api_key_here"
SHAPES_APP_ID="your_shapesinc_app_id_here"
DISCORD_TOKEN="your_discord_bot_token_here"
MODEL="your_shapesinc_model_name_here"
```

- Replace each placeholder in quotes with your actual values.
   
3. **Start the Bot**

```css
python3 main.py
```

- You should see log messages like “Bot is starting…” and “Connected to Discord.”
   
4. **Invite Your Bot to a Server**

- In the Developer Portal, go to **OAuth2 → URL Generator**.

- Under **Scopes**, check **bot**.
   
- Under **Bot Permissions**, select **Send Messages**, **Read Message History**, and **Use Slash Commands** (at minimum).

- Copy the generated invite link and open it in your browser to add the bot to a server you manage.  
![Invite Bot to Server](https://github.com/user-attachments/assets/06ae6fe1-8092-475f-a78f-27fe6622a3c5)


---

#### 3.5. Host on Render (Recommended for 24/7 Uptime)

* Go to [Render.com](https://render.com/) and **Sign Up** (use GitHub for faster setup).

* Click **New** → **Web Service** → **Connect to GitHub** → Select your `ShapesInc_For_Discord` repo.  
![Connect GitHub to Render](https://github.com/user-attachments/assets/177f1bfe-280c-418f-9ee8-d46e288fe280)

*  In the **Create Web Service** dialog:

- **Name** your service (e.g., `shapesinc-discord-bot`).
   
- For **Environment**, select **Python 3** (the default is fine).

- In **Build Command**, enter:
   
```css
pip install --upgrade pip && pip3 install -r requirements.txt
```

- In **Start Command**, enter:
   
```css
python3 main.py
```

> If you renamed `main.py`, replace it with the new filename (e.g., `python3 bot.py`).  
> ![Render Build & Start Commands](https://github.com/user-attachments/assets/cba756b0-270c-4437-98a4-f85093e1ea06)

* **Add Environment Variables** under **Environment** (matching your `.env`):

| Key            | Value                     |
| -------------- | ------------------------- |
| SHAPES_API_KEY | your_shapesinc_api_key    |
| SHAPES_APP_ID  | your_shapesinc_app_id     |
| DISCORD_TOKEN  | your_discord_bot_token    |
| MODEL          | your_shapesinc_model_name |

* Click **Create Web Service**. Render will clone the repo, install dependencies, and deploy your bot.

* Whenever you push updates to GitHub, Render automatically redeploys your bot.  
![Render Deployment Success](https://github.com/user-attachments/assets/322bd923-735e-4553-9884-4308d07cd7e3)  
![Render Auto Redeploy](https://github.com/user-attachments/assets/78f86c8c-a7b9-4313-a827-7f2b8cc0aa10)

---

### 4. How to Use `/authorize`

* In any channel where your bot is present, type:

```ruby
/authorize
```

* The bot will reply with a private link (only visible to you).  
![Authorize Link](https://github.com/user-attachments/assets/3c7ee059-1c26-4a99-89d2-a91cf3bfad63)

* Click the link and copy the **authorization code** displayed.  
![Shapes Authorized Code](https://github.com/user-attachments/assets/47e92ea5-a31c-42b4-b4a2-85bb995748b7)

4. Return to Discord and run:

```ruby
/authorize code:YOUR_CODE_HERE
```

- Replace `YOUR_CODE_HERE` with the code you copied.
   
* If successful, you’ll see:

```text
Successfully Authorised!
```

Now you can chat with the bot or send images.  
![Successfully Authorised](https://github.com/user-attachments/assets/0bf4adc6-784d-4b3e-ab0b-4d1924ed4cce)

---

### 5. Common Troubleshooting

- **Bot Won’t Start or Crashes on Launch**

- Verify your `.env` (or Render environment variables) have no extra spaces and correct quotation marks.
   
- Ensure you ran `pip3 install -r requirements.txt`.

- Check your Discord token—if it was regenerated or revoked, update it in your environment.
   
- **Bot Is Online but Doesn’t Respond**

- Confirm the bot has been invited with the right permissions (e.g., “Send Messages,” “Read Message History,” “Use Slash Commands”).
   
- Make sure slash commands are registered. Sometimes you need to restart the bot or wait a few minutes for Discord to sync.

- **“Invalid Authorization Code” When Using `/authorize`**

- Copy the code exactly—no extra spaces or line breaks.
   
- Ensure you clicked the link from the same Discord account that ran `/authorize`.
   
---

### 6. Special Thanks

Big thanks to **@Rishiraj0100** for the [ShapesInc Library](https://github.com/Rishiraj0100/shapesinc-py), which made building this chatbot so much smoother. Your work and contributions are greatly appreciated!

---

### 7. Congrats—You’re Done!

If you’ve followed all the steps above, your self-hosted ShapesInc AI Chatbot for Discord should be live and ready to go. Enjoy chatting and let the bot amaze you with its image understanding and code-writing capabilities!
