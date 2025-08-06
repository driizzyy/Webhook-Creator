# 🚀 Discord Webhook Creator Pro v2.0

<div align="center">

![Discord Webhook Creator Pro](https://img.shields.io/badge/Discord-Webhook%20Creator%20Pro-5865f2?style=for-the-badge&logo=discord&logoColor=white)
![Version](https://img.shields.io/badge/Version-2.0-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey?style=for-the-badge)

**Professional Discord webhook management system with modern GUI interface**

[🌐 **Visit Official Website**](https://driizzyy.github.io/Webhook-Creator-Website/) | [📦 Download Latest Release](https://github.com/driizzyy/Webhook-Creator/releases/latest) | [📚 Documentation](#documentation) | [🐛 Report Bug](https://github.com/driizzyy/Webhook-Creator/issues)

</div>

---

## 🌟 Features Overview

Discord Webhook Creator Pro is a **feature-rich, professional-grade application** designed for seamless Discord webhook management. Built with modern Python technologies and a sleek GUI interface, it offers everything you need for efficient Discord communication automation.

### 🎯 **Core Capabilities**
- **🔗 Multi-Webhook Management** - Create, manage, and switch between multiple webhooks
- **💬 Rich Message Types** - Text messages, rich embeds, and file attachments
- **🎨 Professional Embed Creator** - Customizable titles, colors, and descriptions
- **⚡ Real-time Connection Status** - Live Discord API connectivity monitoring  
- **🌙 Modern Theme System** - Dark and Light theme support
- **💾 Auto-Save Functionality** - Persistent settings and message templates
- **🔐 Secure Token Management** - Encrypted token storage with visibility toggle
- **📱 Cross-Platform Support** - Works on Windows, Linux, and macOS

### 🚀 **Advanced Features**
- **Direct Webhook Creation** - Create webhooks directly from Discord channels
- **Legacy Import System** - Import existing webhooks from files
- **Real-time Updates** - Built-in update checker and GitHub integration
- **Professional UI/UX** - Modern card-based interface design
- **Error Handling** - Comprehensive error management with user-friendly messages
- **Settings Persistence** - All configurations saved between sessions

---

## 🌐 Official Website

**Experience Discord Webhook Creator Pro online!**

🔗 **[https://driizzyy.github.io/Webhook-Creator-Website/](https://driizzyy.github.io/Webhook-Creator-Website/)**

Our official website features:
- 📊 **Real-time GitHub Stats** - Live repository information and download counts
- 🚀 **Interactive Demo** - Try the tool's features directly in your browser
- 📖 **Complete Documentation** - Comprehensive guides and tutorials
- 💡 **Usage Examples** - Step-by-step implementation guides
- 🎨 **Modern Design** - Professional Discord-themed interface
- 📱 **Mobile Responsive** - Perfect viewing on all devices

---

## 📦 Quick Start

### Option 1: Download Pre-built Executable (Recommended)
1. Visit our [Releases Page](https://github.com/driizzyy/Webhook-Creator/releases/latest)
2. Download `Discord_Webhook_Creator_Pro.exe` for Windows
3. Run the executable - no installation required!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/driizzyy/Webhook-Creator.git
cd Webhook-Creator

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Requirements
- **Python 3.7+** (for source installation)
- **Internet connection** for Discord API access
- **Discord account** with appropriate permissions

---

## 🎮 How to Use

### 1. 🔑 **Initial Setup**
1. **Launch the application**
2. **Configure your Discord token** in the Settings tab
3. **Add a Channel ID** where you want to send messages
4. **Test connection** using the refresh button

### 2. 🎯 **Creating Webhooks**
```
🔗 Method 1: Direct Creation
→ Enter your Discord token and target channel ID
→ Click "Create Webhook" button
→ Webhook is automatically created and saved

📁 Method 2: Import Existing
→ Place webhook URL in webhook.txt file
→ Application automatically imports on startup
→ Webhook appears in dropdown selection
```

### 3. 💬 **Sending Messages**

#### **Text Messages**
- Select "📝 Text Message" type
- Enter your content in the message box
- Optionally enable "@everyone" tagging
- Click "🚀 Send Message"

#### **Rich Embeds** (Recommended)
- Select "📋 Rich Embed" type  
- Choose your webhook from dropdown
- Customize embed title and color
- Add your message content
- Send via webhook for professional appearance

#### **File Attachments**
- Select "📎 File Attachment" type
- Message sends with attached configuration files
- Perfect for sharing settings or logs

### 4. ⚙️ **Advanced Configuration**
- **Theme Switching**: Choose between Dark/Light themes
- **Auto-Save**: Enable automatic saving of messages and settings
- **Connection Monitoring**: Real-time Discord API status
- **Update Management**: Built-in update checker and downloader

---

## 🏗️ Architecture & Design

### **Technology Stack**
- **Frontend**: Python Tkinter with custom styling
- **Backend**: Discord API v9 integration
- **Networking**: Requests library for HTTP communications
- **Threading**: Asynchronous operations for UI responsiveness
- **Storage**: JSON-based configuration management

### **Project Structure**
```
Discord-Webhook-Creator-Pro/
├── main.py                 # Core application logic
├── config.json            # Application configuration
├── webhooks.json          # Webhook storage
├── gui_settings.json      # UI preferences
├── requirements.txt       # Python dependencies
├── discord_tool.spec      # PyInstaller build configuration
└── README.md              # This documentation
```

### **Key Components**
- **🖥️ GUI Engine**: Modern tkinter interface with custom themes
- **🔌 API Handler**: Discord API v9 communication layer  
- **💾 Config Manager**: JSON-based settings persistence
- **🎨 Theme System**: Dynamic UI styling and color schemes
- **🔄 Update System**: GitHub API integration for version management

---

## 🎨 Screenshots & Interface

### **Main Interface - Dark Theme**
- Modern card-based layout design
- Professional Discord color scheme
- Intuitive navigation with tabbed interface
- Real-time connection status monitoring

### **Message Creator**
- Multi-type message support (Text/Embed/File)
- Rich embed customization options
- Live preview capabilities
- Webhook selection and management

### **Settings & Configuration**  
- Theme switching (Dark/Light modes)
- Token management with security features
- Auto-save preferences
- Advanced configuration options

---

## 📚 Documentation

### **Discord API Integration**
This tool utilizes Discord's official Webhook API for embed messages, ensuring full compliance with Discord's Terms of Service. Unlike selfbot solutions, webhook integration is officially supported and recommended by Discord for embed messaging.

### **Webhook vs Direct API**
- **Webhooks**: Perfect for rich embeds, custom avatars, and professional appearance
- **Direct API**: Traditional text messages using user tokens
- **File Attachments**: Seamless file sharing through Discord's upload system

### **Security & Best Practices**
- **Token Encryption**: User tokens stored with security measures
- **Rate Limiting**: Built-in protection against API abuse
- **Error Handling**: Comprehensive error management and user feedback
- **Privacy**: No data collection or external reporting

---

## 🔧 Advanced Configuration

### **Custom Embed Colors**
```
Hex Color Examples:
• Discord Purple: #5865F2
• Success Green: #57F287  
• Warning Yellow: #FEE75C
• Error Red: #ED4245
• Custom: Any valid hex code
```

### **Webhook Management**
- **Multi-webhook Support**: Manage unlimited webhooks
- **Auto-detection**: Automatic webhook discovery and validation
- **Backup & Restore**: Export/import webhook configurations
- **Cleanup Tools**: Remove outdated or invalid webhooks

### **Performance Optimization**
- **Asynchronous Operations**: Non-blocking UI during API calls
- **Connection Pooling**: Efficient HTTP connection management  
- **Memory Management**: Optimized resource usage
- **Startup Optimization**: Fast application loading times

---

## 🚀 Building from Source

### **Development Setup**
```bash
# Clone repository
git clone https://github.com/driizzyy/Webhook-Creator.git
cd Webhook-Creator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pyinstaller  # For building executables

# Run in development mode
python main.py
```

### **Building Executable**
```bash
# Using provided spec file (recommended)
pyinstaller discord_tool.spec

# Manual build
pyinstaller --onefile --windowed --name "Discord_Webhook_Creator_Pro" main.py

# Output location
./dist/Discord_Webhook_Creator_Pro.exe
```

### **Build Configuration**
The included `discord_tool.spec` file provides optimized build settings:
- **Single file executable** for easy distribution
- **No console window** for clean user experience  
- **Icon and metadata** inclusion
- **Dependency optimization** for smaller file size

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **Ways to Contribute**
- 🐛 **Bug Reports**: Found an issue? Let us know!
- 💡 **Feature Requests**: Have ideas for improvements?
- 🔧 **Code Contributions**: Submit pull requests
- 📚 **Documentation**: Help improve our guides
- 🌟 **Star the Repository**: Show your support!

### **Development Guidelines**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📋 Changelog

### **Version 2.0 - Professional Edition** 🎉
- ✨ **Complete UI Overhaul** - Modern card-based interface
- 🔗 **Multi-webhook Management** - Create and manage multiple webhooks  
- 🎨 **Theme System** - Dark/Light theme support
- ⚡ **Performance Improvements** - Faster startup and operation
- 🔐 **Enhanced Security** - Improved token management
- 📱 **Cross-platform Support** - Windows, Linux, macOS compatibility
- 🚀 **Auto-updater** - Built-in update system
- 💾 **Settings Persistence** - Save preferences between sessions

### **Version 1.x - Legacy**
- Basic webhook functionality
- Simple text message sending
- Basic GUI interface

---

## 🆘 Support & Help

### **Need Help?**
- 🌐 **Visit**: [Official Website](https://driizzyy.github.io/Webhook-Creator-Website/)
- 📚 **Read**: [Documentation](#documentation)  
- 🐛 **Report**: [GitHub Issues](https://github.com/driizzyy/Webhook-Creator/issues)
- 💬 **Discuss**: [GitHub Discussions](https://github.com/driizzyy/Webhook-Creator/discussions)

### **Common Solutions**
- **Connection Issues**: Verify token and channel permissions
- **Webhook Errors**: Check webhook URL validity and server permissions
- **UI Problems**: Try switching themes or restarting application
- **Performance**: Close unnecessary applications and check internet connection

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **What this means:**
- ✅ **Commercial Use** - Use in commercial projects
- ✅ **Modification** - Modify the source code
- ✅ **Distribution** - Distribute the software  
- ✅ **Private Use** - Use for personal projects
- ❌ **Liability** - No warranty provided
- ❌ **Trademark Use** - Cannot use project trademarks

---

## 👨‍💻 Creator

**Created with ❤️ by [driizzyy](https://github.com/driizzyy)**

### **Connect with the Developer**
- 🔗 **GitHub**: [@driizzyy](https://github.com/driizzyy)
- 🌐 **Website**: [https://driizzyy.github.io/Webhook-Creator-Website/](https://driizzyy.github.io/Webhook-Creator-Website/)
- 📧 **Issues**: [GitHub Issues Page](https://github.com/driizzyy/Webhook-Creator/issues)

---

## 🌟 Show Your Support

If you find Discord Webhook Creator Pro useful, please consider:

- ⭐ **Starring this repository**
- 🍴 **Forking for your own projects**
- 📢 **Sharing with friends and colleagues**
- 🐛 **Reporting bugs and suggesting features**
- 💬 **Joining our community discussions**

---

<div align="center">

**Discord Webhook Creator Pro v2.0**  
*Professional webhook management made simple*

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/driizzyy/Webhook-Creator?style=for-the-badge&logo=github)
![GitHub Downloads](https://img.shields.io/github/downloads/driizzyy/Webhook-Creator/total?style=for-the-badge&logo=github)

**[🌐 Visit Official Website](https://driizzyy.github.io/Webhook-Creator-Website/)**

---

*© 2025 driizzyy. All rights reserved.*

</div>
