import json
import subprocess
import sys
import os
import requests
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
from datetime import datetime
import webbrowser

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.abspath(filename)

INFO_FILE = "webhook.txt"
class DiscordToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord Webhook Creator Pro v2.0 - by driizzyy")
        self.root.geometry("1200x1000")
        self.root.minsize(800, 600)
        self.config = self.load_config()
        self.token = self.config.get("token", "")
        self.current_theme = self.config.get("theme", "Dark")
        self.setup_theme_colors()
        self.setup_styles()
        self.create_widgets()
        self.load_saved_data()
        self.apply_theme()
    def setup_theme_colors(self):
        self.themes = {
            'Dark': {
                'bg_primary': '#1a1a1a',
                'bg_secondary': '#2d2d2d',
                'bg_tertiary': '#3d3d3d',
                'accent': '#5865f2',
                'accent_hover': '#4752c4',
                'success': '#57f287',
                'warning': '#fee75c',
                'error': '#ed4245',
                'text_primary': '#ffffff',
                'text_secondary': '#b9bbbe',
                'border': '#424242'
            },
            'Light': {
                'bg_primary': '#ffffff',
                'bg_secondary': '#f6f6f6',
                'bg_tertiary': '#e1e1e1',
                'accent': '#5865f2',
                'accent_hover': '#4752c4',
                'success': '#3ba55d',
                'warning': '#faa81a',
                'error': '#ed4245',
                'text_primary': '#2c2f33',
                'text_secondary': '#747f8d',
                'border': '#e3e5e8'
            }
        }
        self.colors = self.themes.get(self.current_theme, self.themes['Dark'])
    def apply_theme(self):
        self.setup_theme_colors()
        self.setup_styles()
        
        # Update root background
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Update text widgets that don't use ttk styles
        if hasattr(self, 'message_text'):
            self.message_text.configure(
                bg=self.colors['bg_tertiary'],
                fg=self.colors['text_primary'],
                insertbackground=self.colors['text_primary'],
                selectbackground=self.colors['accent']
            )
        
        self.root.update_idletasks()
    
    def setup_styles(self):
        """Configure modern styling for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles with current theme colors
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 16, 'bold'), 
                       foreground=self.colors['text_primary'], 
                       background=self.colors['bg_primary'])
        
        style.configure('Header.TLabel', 
                       font=('Segoe UI', 12, 'bold'), 
                       foreground=self.colors['text_primary'], 
                       background=self.colors['bg_primary'])
        
        style.configure('Modern.TFrame', 
                       background=self.colors['bg_primary'])
        
        style.configure('Card.TFrame', 
                       background=self.colors['bg_secondary'], 
                       relief='flat', borderwidth=1)
        
        style.configure('Modern.TButton', 
                       font=('Segoe UI', 10), 
                       padding=(20, 10))
        
        style.configure('Accent.TButton', 
                       font=('Segoe UI', 10, 'bold'), 
                       padding=(20, 10))
        
        # Entry styles
        style.configure('Modern.TEntry',
                       fieldbackground=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       bordercolor=self.colors['border'])
        
        # Label styles
        style.configure('Info.TLabel',
                       foreground=self.colors['text_secondary'],
                       background=self.colors['bg_secondary'])
        
        # Checkbutton styles  
        style.configure('Modern.TCheckbutton',
                       foreground=self.colors['text_primary'],
                       background=self.colors['bg_secondary'])
        
        # Radiobutton styles
        style.configure('Modern.TRadiobutton',
                       foreground=self.colors['text_primary'],
                       background=self.colors['bg_secondary'])
        
        # Combobox styles
        style.configure('Modern.TCombobox',
                       fieldbackground=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'])
        
        # Notebook styles
        style.configure('Modern.TNotebook', 
                       background=self.colors['bg_primary'])
        
        style.configure('Modern.TNotebook.Tab',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_secondary'],
                       padding=[20, 10])
        
        style.map('Modern.TNotebook.Tab',
                 background=[('selected', self.colors['accent'])],
                 foreground=[('selected', 'white')])
        
        self.root.configure(bg=self.colors['bg_primary'])
    
    def load_config(self):
        """Load configuration from config.json"""
        try:
            with open(resource_path("config.json"), "r") as f:
                return json.load(f)
        except Exception as e:
            messagebox.showerror("Configuration Error", f"Failed to load config.json: {e}")
            return {}
    
    def save_config(self):
        """Save configuration to config.json"""
        try:
            with open(resource_path("config.json"), "w") as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save config.json: {e}")
    
    def create_widgets(self):
        """Create the main GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, style='Modern.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="Discord Webhook Creator Pro", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame, style='Modern.TNotebook')
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs
        self.create_message_tab()
        self.create_settings_tab()
        self.create_update_tab()
        self.create_credits_tab()
        self.create_about_tab()
    
    def create_message_tab(self):
        """Create the Discord message sending tab"""
        tab_frame = ttk.Frame(self.notebook, style='Modern.TFrame')
        self.notebook.add(tab_frame, text='📨 Discord Messages')
        
        # Main content frame with scrollbar
        canvas = tk.Canvas(tab_frame, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab_frame, orient='vertical', command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='Modern.TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Connection Status Card
        status_card = ttk.Frame(scrollable_frame, style='Card.TFrame')
        status_card.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(status_card, text="🔗 Connection Status", style='Header.TLabel').pack(anchor='w', padx=15, pady=(15, 5))
        
        status_frame = ttk.Frame(status_card, style='Card.TFrame')
        status_frame.pack(fill='x', padx=15, pady=(0, 15))
        
        self.status_label = ttk.Label(status_frame, text="● Checking connection...", style='Info.TLabel')
        self.status_label.pack(side='left')
        
        refresh_btn = ttk.Button(status_frame, text="Refresh", command=self.check_connection, style='Modern.TButton')
        refresh_btn.pack(side='right')
        
        # Discord Configuration Card
        config_card = ttk.Frame(scrollable_frame, style='Card.TFrame')
        config_card.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(config_card, text="⚙️ Discord Configuration", style='Header.TLabel').pack(anchor='w', padx=15, pady=(15, 5))
        
        # Token input
        token_frame = ttk.Frame(config_card, style='Card.TFrame')
        token_frame.pack(fill='x', padx=15, pady=5)
        
        ttk.Label(token_frame, text="User Token:", style='Info.TLabel').pack(anchor='w')
        
        token_input_frame = ttk.Frame(token_frame, style='Card.TFrame')
        token_input_frame.pack(fill='x', pady=(5, 0))
        
        self.token_entry = ttk.Entry(token_input_frame, show="*", font=('Consolas', 9), style='Modern.TEntry')
        self.token_entry.pack(side='left', fill='x', expand=True)
        
        toggle_token_btn = ttk.Button(token_input_frame, text="👁", width=3, command=self.toggle_token_visibility, style='Modern.TButton')
        toggle_token_btn.pack(side='right', padx=(5, 0))
        
        # Channel ID input
        channel_frame = ttk.Frame(config_card, style='Card.TFrame')
        channel_frame.pack(fill='x', padx=15, pady=5)
        
        ttk.Label(channel_frame, text="Channel ID:", style='Info.TLabel').pack(anchor='w')
        self.channel_entry = ttk.Entry(channel_frame, font=('Consolas', 9), style='Modern.TEntry')
        self.channel_entry.pack(fill='x', pady=(5, 15))
        
        # Message Configuration Card
        msg_card = ttk.Frame(scrollable_frame, style='Card.TFrame')
        msg_card.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(msg_card, text="💬 Message Configuration", style='Header.TLabel').pack(anchor='w', padx=15, pady=(15, 5))
        
        # Message type selection
        type_frame = ttk.Frame(msg_card, style='Card.TFrame')
        type_frame.pack(fill='x', padx=15, pady=5)
        
        ttk.Label(type_frame, text="Message Type:", style='Info.TLabel').pack(anchor='w')
        
        self.message_type = tk.StringVar(value="embed")
        type_options = [("📝 Text Message", "text"), ("📋 Rich Embed", "embed"), ("📎 File Attachment", "file")]
        
        type_select_frame = ttk.Frame(type_frame, style='Card.TFrame')
        type_select_frame.pack(fill='x', pady=(5, 0))
        
        for text, value in type_options:
            ttk.Radiobutton(type_select_frame, text=text, variable=self.message_type, value=value, 
                           command=self.on_message_type_change, style='Modern.TRadiobutton').pack(anchor='w', pady=2)
        
        # Message content
        content_frame = ttk.Frame(msg_card, style='Card.TFrame')
        content_frame.pack(fill='x', padx=15, pady=5)
        
        ttk.Label(content_frame, text="Message Content:", style='Info.TLabel').pack(anchor='w')
        
        self.message_text = scrolledtext.ScrolledText(content_frame, height=4, wrap=tk.WORD, font=('Segoe UI', 10),
                                                     bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'])
        self.message_text.pack(fill='x', pady=(5, 0))
        self.message_text.insert('1.0', "Enter your message here...")
        
        # Additional options
        options_frame = ttk.Frame(msg_card, style='Card.TFrame')
        options_frame.pack(fill='x', padx=15, pady=5)
        
        self.tag_everyone = tk.BooleanVar()
        ttk.Checkbutton(options_frame, text="Tag @everyone", variable=self.tag_everyone, style='Modern.TCheckbutton').pack(anchor='w', pady=2)
        
        # Embed customization (only visible when embed is selected)
        self.embed_frame = ttk.Frame(msg_card, style='Card.TFrame')
        
        # Webhook selection
        webhook_select_frame = ttk.Frame(self.embed_frame, style='Card.TFrame')
        webhook_select_frame.pack(fill='x', pady=2)
        ttk.Label(webhook_select_frame, text="Webhook:", style='Info.TLabel').pack(anchor='w')
        
        webhook_combo_frame = ttk.Frame(webhook_select_frame, style='Card.TFrame')
        webhook_combo_frame.pack(fill='x', pady=(5, 0))
        
        self.webhook_var = tk.StringVar()
        self.webhook_combo = ttk.Combobox(webhook_combo_frame, textvariable=self.webhook_var, 
                                         style='Modern.TCombobox', state="readonly")
        self.webhook_combo.pack(side='left', fill='x', expand=True)
        
        create_webhook_btn = ttk.Button(webhook_combo_frame, text="Create Webhook", 
                                       command=self.create_webhook, style='Modern.TButton')
        create_webhook_btn.pack(side='right', padx=(5, 0))
        
        embed_title_frame = ttk.Frame(self.embed_frame, style='Card.TFrame')
        embed_title_frame.pack(fill='x', pady=2)
        ttk.Label(embed_title_frame, text="Embed Title:", style='Info.TLabel').pack(anchor='w')
        self.embed_title = ttk.Entry(embed_title_frame, style='Modern.TEntry')
        self.embed_title.pack(fill='x')
        self.embed_title.insert(0, "Message from Tool")
        
        embed_color_frame = ttk.Frame(self.embed_frame, style='Card.TFrame')
        embed_color_frame.pack(fill='x', pady=2)
        ttk.Label(embed_color_frame, text="Embed Color (hex):", style='Info.TLabel').pack(anchor='w')
        self.embed_color = ttk.Entry(embed_color_frame, style='Modern.TEntry')
        self.embed_color.pack(fill='x')
        self.embed_color.insert(0, "#7289DA")
        
        # Send button
        send_frame = ttk.Frame(msg_card, style='Card.TFrame')
        send_frame.pack(fill='x', padx=15, pady=(10, 15))
        
        self.send_btn = ttk.Button(send_frame, text="🚀 Send Message", command=self.send_message_async, style='Accent.TButton')
        self.send_btn.pack(side='right')
        
        self.progress = ttk.Progressbar(send_frame, mode='indeterminate')
        
        # Initialize display
        self.on_message_type_change()
        
        # Load available webhooks
        self.load_webhooks()
        
        # Import webhook from webhook.txt if exists and webhooks.json is empty
        self.import_legacy_webhook()
    
    def load_webhooks(self):
        """Load available webhooks from webhooks.json"""
        try:
            with open(resource_path("webhooks.json"), "r") as f:
                webhooks = json.load(f)
            
            webhook_options = []
            for webhook in webhooks:
                name = webhook.get('name', 'Unknown')
                url = webhook.get('url', '')
                webhook_options.append(f"{name} ({url[-10:]}...)")  # Show last 10 chars of URL
            
            self.webhook_combo['values'] = webhook_options
            if webhook_options:
                self.webhook_combo.set(webhook_options[0])
                
        except Exception:
            # If no webhooks file exists, start with empty
            self.webhook_combo['values'] = ["No webhooks available"]
            self.webhook_combo.set("No webhooks available")
    
    def save_webhook(self, name, url, channel_id):
        """Save a webhook to webhooks.json"""
        try:
            # Load existing webhooks
            try:
                with open(resource_path("webhooks.json"), "r") as f:
                    webhooks = json.load(f)
            except:
                webhooks = []
            
            # Check if webhook already exists
            for webhook in webhooks:
                if webhook.get('url') == url:
                    return  # Already saved
            
            # Add new webhook
            webhooks.append({
                "name": name,
                "url": url,
                "channel_id": channel_id,
                "created_at": datetime.now().isoformat()
            })
            
            # Save back to file
            with open(resource_path("webhooks.json"), "w") as f:
                json.dump(webhooks, f, indent=2)
                
            # Reload webhook dropdown
            self.load_webhooks()
            
        except Exception as e:
            pass
    
    def get_selected_webhook_url(self):
        """Get the URL of the currently selected webhook"""
        try:
            with open(resource_path("webhooks.json"), "r") as f:
                webhooks = json.load(f)
            
            selected = self.webhook_combo.get()
            if "No webhooks available" in selected:
                return None
                
            # Extract the webhook identifier from the selection
            for webhook in webhooks:
                name = webhook.get('name', 'Unknown')
                url = webhook.get('url', '')
                if f"{name} ({url[-10:]}...)" == selected:
                    return url
            
            return None
        except:
            return None
    
    def create_webhook(self):
        """Create a new webhook in the specified channel"""
        def create():
            try:
                token = self.token_entry.get() or self.token
                channel_id = self.channel_entry.get()
                
                if not token or not channel_id:
                    self.root.after(0, lambda: messagebox.showerror("Error", "Token and Channel ID are required"))
                    return
                
                # Create webhook using Discord API
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                }
                
                webhook_data = {
                    "name": f"Discord-Tool-{datetime.now().strftime('%m%d-%H%M')}"
                }
                
                url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
                response = requests.post(url, headers=headers, json=webhook_data)
                
                if response.status_code == 200:
                    webhook_info = response.json()
                    webhook_url = f"https://discord.com/api/webhooks/{webhook_info['id']}/{webhook_info['token']}"
                    
                    # Save webhook
                    self.save_webhook(webhook_data['name'], webhook_url, channel_id)
                    
                    self.root.after(0, lambda: messagebox.showinfo("Success", f"✅ Webhook created: {webhook_data['name']}"))
                else:
                    error_msg = f"Failed to create webhook: HTTP {response.status_code}"
                    try:
                        error_data = response.json()
                        error_msg = error_data.get('message', error_msg)
                    except:
                        pass
                    self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
                    
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Error creating webhook: {e}"))
        
        threading.Thread(target=create, daemon=True).start()
    
    def import_legacy_webhook(self):
        """Import webhook from webhook.txt if it exists"""
        try:
            # Check if we already have webhooks
            try:
                with open(resource_path("webhooks.json"), "r") as f:
                    existing = json.load(f)
                if existing:
                    return  # Already have webhooks
            except:
                pass
            
            # Try to read from webhook.txt
            try:
                with open(resource_path("webhook.txt"), "r") as f:
                    webhook_url = f.read().strip()
                
                if webhook_url.startswith("https://discord.com/api/webhooks/"):
                    # Save as imported webhook
                    self.save_webhook("Imported Webhook", webhook_url, "unknown")
                    messagebox.showinfo("Import", "✅ Imported webhook from webhook.txt")
            except:
                pass  # No webhook.txt or couldn't read it
                
        except Exception as e:
            pass
    
    def create_settings_tab(self):
        """Create the settings tab"""
        tab_frame = ttk.Frame(self.notebook, style='Modern.TFrame')
        self.notebook.add(tab_frame, text='⚙️ Settings')
        
        # Settings cards container
        settings_frame = ttk.Frame(tab_frame, style='Modern.TFrame')
        settings_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Discord Settings Card
        discord_card = ttk.Frame(settings_frame, style='Card.TFrame')
        discord_card.pack(fill='x', pady=(0, 20))
        
        ttk.Label(discord_card, text="🔗 Discord Settings", style='Header.TLabel').pack(anchor='w', padx=15, pady=(15, 10))
        
        # Auto-save settings
        auto_frame = ttk.Frame(discord_card, style='Card.TFrame')
        auto_frame.pack(fill='x', padx=15, pady=5)
        
        self.auto_save = tk.BooleanVar(value=True)
        ttk.Checkbutton(auto_frame, text="Auto-save channel IDs and messages", variable=self.auto_save, style='Modern.TCheckbutton').pack(anchor='w')
        
        # Application Settings Card
        app_card = ttk.Frame(settings_frame, style='Card.TFrame')
        app_card.pack(fill='x', pady=(0, 20))
        
        ttk.Label(app_card, text="🎨 Application Settings", style='Header.TLabel').pack(anchor='w', padx=15, pady=(15, 10))
        
        # Theme selection
        theme_frame = ttk.Frame(app_card, style='Card.TFrame')
        theme_frame.pack(fill='x', padx=15, pady=5)
        
        ttk.Label(theme_frame, text="Theme:", style='Info.TLabel').pack(anchor='w')
        
        self.theme_var = tk.StringVar(value=self.current_theme)
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=["Dark", "Light"], 
                                  state="readonly", style='Modern.TCombobox')
        theme_combo.pack(fill='x', pady=(5, 15))
        theme_combo.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        # Save settings button
        save_btn = ttk.Button(app_card, text="💾 Save Settings", command=self.save_settings, style='Accent.TButton')
        save_btn.pack(anchor='e', padx=15, pady=(0, 15))
    
    def create_update_tab(self):
        """Create the update tab"""
        tab_frame = ttk.Frame(self.notebook, style='Modern.TFrame')
        self.notebook.add(tab_frame, text='🔄 Updates')
        
        update_card = ttk.Frame(tab_frame, style='Card.TFrame')
        update_card.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Update header
        ttk.Label(update_card, text="🔄 Update Manager", style='Title.TLabel').pack(pady=(30, 10))
        
        # Current version info
        version_frame = ttk.Frame(update_card, style='Card.TFrame')
        version_frame.pack(fill='x', pady=20)
        
        ttk.Label(version_frame, text="Current Version:", style='Header.TLabel').pack(anchor='w')
        ttk.Label(version_frame, text="Discord Webhook Creator Pro v2.0", style='Info.TLabel').pack(anchor='w', pady=(5, 0))
        
        # Update status
        self.update_status_label = ttk.Label(update_card, text="🔍 Click 'Check for Updates' to check for the latest version", 
                                           style='Info.TLabel')
        self.update_status_label.pack(pady=20)
        
        # Update buttons
        button_frame = ttk.Frame(update_card, style='Card.TFrame')
        button_frame.pack(pady=20)
        
        self.check_update_btn = ttk.Button(button_frame, text="🔍 Check for Updates", 
                                          command=self.check_for_updates, style='Modern.TButton')
        self.check_update_btn.pack(side='left', padx=(0, 10))
        
        self.update_btn = ttk.Button(button_frame, text="⬇️ Download Update", 
                                   command=self.download_update, style='Accent.TButton', state='disabled')
        self.update_btn.pack(side='left', padx=(10, 0))
        
        # GitHub link
        github_frame = ttk.Frame(update_card, style='Card.TFrame')
        github_frame.pack(pady=20)
        
        ttk.Label(github_frame, text="💡 Always get the latest version from GitHub:", style='Info.TLabel').pack()
        ttk.Button(github_frame, text="🔗 View on GitHub", 
                  command=lambda: self.open_url("https://github.com/driizzyy/Webhook-Creator"), 
                  style='Modern.TButton').pack(pady=(10, 0))
    
    def create_credits_tab(self):
        """Create the credits tab"""
        tab_frame = ttk.Frame(self.notebook, style='Modern.TFrame')
        self.notebook.add(tab_frame, text='👤 Credits')
        
        credits_card = ttk.Frame(tab_frame, style='Card.TFrame')
        credits_card.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Credits header
        ttk.Label(credits_card, text="👤 Credits & Information", style='Title.TLabel').pack(pady=(30, 20))
        
        # Developer info
        dev_frame = ttk.Frame(credits_card, style='Card.TFrame')
        dev_frame.pack(fill='x', pady=20)
        
        ttk.Label(dev_frame, text="🧑‍💻 Developed by:", style='Header.TLabel').pack(anchor='w')
        ttk.Label(dev_frame, text="driizzyy", style='Title.TLabel').pack(anchor='w', pady=(5, 10))
        
        # GitHub links
        links_frame = ttk.Frame(credits_card, style='Card.TFrame')
        links_frame.pack(pady=30)
        
        ttk.Label(links_frame, text="🔗 Links:", style='Header.TLabel').pack(pady=(0, 15))
        
        # Repository link
        repo_btn = ttk.Button(links_frame, text="📂 Webhook Creator Repository", 
                             command=lambda: self.open_url("https://github.com/driizzyy/Webhook-Creator"), 
                             style='Accent.TButton')
        repo_btn.pack(pady=5)
        
        # Profile link
        profile_btn = ttk.Button(links_frame, text="👤 driizzyy's GitHub Profile", 
                                command=lambda: self.open_url("https://github.com/driizzyy"), 
                                style='Modern.TButton')
        profile_btn.pack(pady=5)
        
        # Tool info
        info_frame = ttk.Frame(credits_card, style='Card.TFrame')
        info_frame.pack(pady=30)
        
        info_text = """🛠️ Tool Information:
• Advanced Discord webhook management system
• Professional embed creator with webhook integration
• Modern GUI with theme support
• Cross-platform compatibility

💡 This tool respects Discord's Terms of Service by using webhooks 
for embed messages instead of selfbot functionality.

⭐ If you find this tool useful, please consider starring the repository!"""
        
        ttk.Label(info_frame, text=info_text, style='Info.TLabel', justify='left').pack()
    
    def check_for_updates(self):
        """Check for updates from GitHub"""
        def check():
            try:
                self.root.after(0, lambda: self.update_status_label.config(text="🔍 Checking for updates..."))
                self.root.after(0, lambda: self.check_update_btn.config(state='disabled'))
                
                # Check GitHub releases API
                api_url = "https://api.github.com/repos/driizzyy/Webhook-Creator/releases/latest"
                response = requests.get(api_url, timeout=10)
                
                if response.status_code == 200:
                    release_data = response.json()
                    latest_version = release_data.get('tag_name', 'Unknown')
                    current_version = "v2.0"  # Current version
                    
                    if latest_version != current_version:
                        # Update available
                        message = f"🎉 Update available: {latest_version} (Current: {current_version})"
                        self.root.after(0, lambda: self.update_status_label.config(text=message))
                        self.root.after(0, lambda: self.update_btn.config(state='normal'))
                        
                        # Store download URL
                        self.latest_download_url = release_data.get('html_url', 'https://github.com/driizzyy/Webhook-Creator')
                    else:
                        # Up to date
                        message = f"✅ You have the latest version: {current_version}"
                        self.root.after(0, lambda: self.update_status_label.config(text=message))
                        self.root.after(0, lambda: self.update_btn.config(state='disabled'))
                else:
                    # Error checking
                    message = "❌ Unable to check for updates. Check your internet connection."
                    self.root.after(0, lambda: self.update_status_label.config(text=message))
                    
            except Exception as e:
                error_msg = f"❌ Error checking for updates: {str(e)}"
                self.root.after(0, lambda: self.update_status_label.config(text=error_msg))
            finally:
                self.root.after(0, lambda: self.check_update_btn.config(state='normal'))
        
        threading.Thread(target=check, daemon=True).start()
    
    def download_update(self):
        """Open the download page for the update"""
        if hasattr(self, 'latest_download_url'):
            self.open_url(self.latest_download_url)
            messagebox.showinfo("Update", "Opening the GitHub release page in your browser.\nDownload the latest version and replace your current files.")
        else:
            self.open_url("https://github.com/driizzyy/Webhook-Creator/releases/latest")
    
    def create_about_tab(self):
        """Create the about tab"""
        tab_frame = ttk.Frame(self.notebook, style='Modern.TFrame')
        self.notebook.add(tab_frame, text='ℹ️ About')
        
        about_card = ttk.Frame(tab_frame, style='Card.TFrame')
        about_card.pack(fill='both', expand=True, padx=20, pady=20)
        
        # App info
        ttk.Label(about_card, text="Discord Webhook Creator Pro", style='Title.TLabel').pack(pady=(30, 10))
        ttk.Label(about_card, text="Version 2.0 - Professional Edition", 
                 style='Info.TLabel').pack(pady=(0, 5))
        ttk.Label(about_card, text="Created by driizzyy", 
                 style='Header.TLabel').pack(pady=(5, 20))
        
        # Features list
        features_text = """🚀 Features:
• Professional Discord webhook management system
• Rich embed creator with webhook integration
• File attachment support with webhook compatibility
• Multi-webhook management and selection
• Auto-save functionality for workflow efficiency
• Modern GUI interface with theme switching
• Cross-platform compatibility (Windows/Linux)

⚡ Advanced Capabilities:  
• Multiple message types (Text, Embed, File)
• Real-time Discord connection status checking
• Webhook creation directly from Discord channels
• Professional embed customization (title, color, description)
• Automatic webhook import from legacy files
• Settings persistence across sessions

🔒 Discord ToS Compliant:
This tool uses Discord webhooks for embed messages, which is fully 
compliant with Discord's Terms of Service. No selfbot functionality 
is used for sending embeds."""
        
        features_label = ttk.Label(about_card, text=features_text, 
                                  style='Info.TLabel', justify='left')
        features_label.pack(pady=(0, 20))
        
        # Links
        links_frame = ttk.Frame(about_card, style='Card.TFrame')
        links_frame.pack(pady=20)
        
        ttk.Button(links_frame, text="📚 Discord Developer Docs", 
                  command=lambda: self.open_url("https://discord.com/developers/docs"), 
                  style='Modern.TButton').pack(side='left', padx=5)
        
        ttk.Button(links_frame, text="🔗 GitHub Repository", 
                  command=lambda: self.open_url("https://github.com/driizzyy/Webhook-Creator"), 
                  style='Modern.TButton').pack(side='left', padx=5)
    
    # Event handlers and functionality methods
    def on_theme_change(self, event=None):
        """Handle theme change"""
        new_theme = self.theme_var.get()
        if new_theme != self.current_theme:
            self.current_theme = new_theme
            self.config["theme"] = new_theme
            self.apply_theme()
            messagebox.showinfo("Theme Changed", f"Theme changed to {new_theme}")
    
    def toggle_token_visibility(self):
        """Toggle token visibility"""
        current_show = self.token_entry.cget('show')
        if current_show == '*':
            self.token_entry.config(show='')
        else:
            self.token_entry.config(show='*')
    
    def on_message_type_change(self):
        """Handle message type change"""
        msg_type = self.message_type.get()
        
        if msg_type == "embed":
            self.embed_frame.pack(fill='x', padx=15, pady=(5, 0))
        else:
            self.embed_frame.pack_forget()
    
    def check_connection(self):
        """Check Discord connection status"""
        def check():
            try:
                token = self.token_entry.get() or self.token
                if not token:
                    self.root.after(0, lambda: self.status_label.config(text="● No token configured", foreground=self.colors['error']))
                    return
                
                headers = {"Authorization": token}
                response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=5)
                
                if response.status_code == 200:
                    user_data = response.json()
                    username = user_data.get('username', 'Unknown')
                    self.root.after(0, lambda: self.status_label.config(text=f"● Connected as {username}", foreground=self.colors['success']))
                else:
                    self.root.after(0, lambda: self.status_label.config(text="● Authentication failed", foreground=self.colors['error']))
            except Exception as e:
                self.root.after(0, lambda: self.status_label.config(text="● Connection failed", foreground=self.colors['error']))
        
        threading.Thread(target=check, daemon=True).start()
    
    def send_message_async(self):
        """Send message in background thread"""
        def send():
            self.root.after(0, lambda: self.send_btn.config(state='disabled'))
            self.root.after(0, lambda: self.progress.pack(side='left', padx=(0, 10), fill='x', expand=True))
            self.root.after(0, lambda: self.progress.start())
            
            try:
                success = self.send_discord_message()
                if success:
                    self.root.after(0, lambda: messagebox.showinfo("Success", "✅ Message sent successfully!"))
                    if self.auto_save.get():
                        self.root.after(0, self.save_form_data)
            except Exception as e:
                error_msg = str(e) if str(e) else f"Unknown error: {type(e).__name__}"
                self.root.after(0, lambda: messagebox.showerror("Error", f"❌ Failed to send message:\n{error_msg}"))
            finally:
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.progress.pack_forget())
                self.root.after(0, lambda: self.send_btn.config(state='normal'))
        
        threading.Thread(target=send, daemon=True).start()
    
    def send_discord_message(self):
        """Send message to Discord"""
        token = self.token_entry.get() or self.token
        channel_id = self.channel_entry.get()
        message_content = self.message_text.get('1.0', 'end-1c')
        message_type = self.message_type.get()
        tag_everyone = self.tag_everyone.get()
        
        if not token or not channel_id:
            raise ValueError("Token and Channel ID are required")
        
        mention = "@everyone\n" if tag_everyone else ""
        
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        payload = None
        files = None
        
        if message_type == "embed":
            # Get selected webhook URL
            webhook_url = self.get_selected_webhook_url()
            if not webhook_url:
                raise ValueError("No webhook selected. Please create a webhook first.")
            
            # Safety checks for embed widgets
            try:
                embed_title = self.embed_title.get() if hasattr(self, 'embed_title') else "Message from Tool"
                embed_color_str = self.embed_color.get() if hasattr(self, 'embed_color') else "#7289DA"
                embed_color = self.hex_to_int(embed_color_str)
            except Exception as widget_error:
                embed_title = "Message from Tool"
                embed_color = 7506394
            
            # Prepare embed payload for webhook
            payload = {
                "embeds": [{
                    "title": embed_title,
                    "description": message_content if message_content.strip() else "No message content",
                    "color": embed_color,
                    "timestamp": datetime.now().isoformat()
                }]
            }
            
            # Add @everyone mention if requested (webhooks can do this)
            if tag_everyone:
                payload["content"] = "@everyone"
            
            # Debug print
            
            # Send via webhook (different URL and headers)
            webhook_headers = {"Content-Type": "application/json"}
            response = requests.post(webhook_url, headers=webhook_headers, json=payload)
            
            if response.status_code not in (200, 201, 204):
                try:
                    error_data = response.json()
                    error_msg = error_data.get('message', 'Unknown webhook error')
                    raise Exception(f"Webhook Error {response.status_code}: {error_msg}")
                except:
                    raise Exception(f"Webhook HTTP {response.status_code}: {response.text}")
            
            return True
        elif message_type == "file":
            payload = {"content": f"{mention}{message_content}" if f"{mention}{message_content}".strip() else "File attachment"}
            try:
                with open(resource_path(INFO_FILE), "rb") as f:
                    files = {"file": (INFO_FILE, f)}
            except Exception as e:
                raise Exception(f"Could not attach info file: {e}")
        else:
            content = f"{mention}{message_content}" if f"{mention}{message_content}".strip() else "Empty message"
            payload = {"content": content}
        
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        
        if files:
            response = requests.post(url, headers=headers, data=payload, files=files)
        else:
            response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code not in (200, 201):
            # Parse error details if available
            try:
                error_data = response.json()
                error_msg = error_data.get('message', 'Unknown error')
                raise Exception(f"Discord API Error {response.status_code}: {error_msg}")
            except:
                raise Exception(f"HTTP {response.status_code}: {response.text}")
        
        return True
    
    def hex_to_int(self, hex_color):
        """Convert hex color to integer"""
        try:
            if hex_color.startswith('#'):
                hex_color = hex_color[1:]
            return int(hex_color, 16)
        except:
            return 7506394
    
    def save_form_data(self):
        """Save form data for next session"""
        try:
            data = {
                "last_channel_id": self.channel_entry.get(),
                "last_message": self.message_text.get('1.0', 'end-1c'),
                "last_message_type": self.message_type.get(),
                "last_tag_everyone": self.tag_everyone.get(),
                "embed_title": self.embed_title.get() if hasattr(self, 'embed_title') else "",
                "embed_color": self.embed_color.get() if hasattr(self, 'embed_color') else "",
                "selected_webhook": self.webhook_var.get() if hasattr(self, 'webhook_var') else ""
            }
            
            with open(resource_path("gui_settings.json"), "w") as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass  # Silently fail if can't save
    
    def load_saved_data(self):
        """Load saved form data"""
        try:
            with open(resource_path("gui_settings.json"), "r") as f:
                data = json.load(f)
            
            if data.get("last_channel_id"):
                self.channel_entry.insert(0, data["last_channel_id"])
            
            if data.get("last_message"):
                self.message_text.delete('1.0', tk.END)
                self.message_text.insert('1.0', data["last_message"])
            
            if data.get("last_message_type"):
                self.message_type.set(data["last_message_type"])
                self.on_message_type_change()
            
            if data.get("last_tag_everyone") is not None:
                self.tag_everyone.set(data["last_tag_everyone"])
            
            if data.get("embed_title") and hasattr(self, 'embed_title'):
                self.embed_title.delete(0, tk.END)
                self.embed_title.insert(0, data["embed_title"])
            
            if data.get("embed_color") and hasattr(self, 'embed_color'):
                self.embed_color.delete(0, tk.END)
                self.embed_color.insert(0, data["embed_color"])
            
            if data.get("selected_webhook") and hasattr(self, 'webhook_var'):
                self.webhook_var.set(data["selected_webhook"])
                
            # Load token
            if self.token:
                self.token_entry.insert(0, self.token)
                
        except Exception:
            pass  # Silently fail if can't load
    
    def save_settings(self):
        """Save application settings"""
        try:
            # Update token in config if changed
            new_token = self.token_entry.get()
            if new_token != self.token:
                self.config["token"] = new_token
                self.token = new_token
            
            # Save theme
            self.config["theme"] = self.current_theme
            
            # Save auto-save preference
            self.config["auto_save"] = self.auto_save.get()
            
            self.save_config()
            messagebox.showinfo("Success", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")
    
    def open_url(self, url):
        """Open URL in default browser"""
        webbrowser.open(url)

def main():
    """Main application entry point"""
    root = tk.Tk()
    app = DiscordToolGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Check connection on startup
    root.after(1000, app.check_connection)
    
    root.mainloop()

if __name__ == "__main__":
    main()