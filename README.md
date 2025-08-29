# System Utility & Admin Dashboard

A comprehensive cross-platform system monitoring solution that collects system health data from multiple machines and provides centralized monitoring through an admin dashboard.

## 🏗️ Architecture Overview

This project consists of two main components:

1. **System Utility (Client)** - Cross-platform Python application that monitors system health
2. **Backend API** - Node.js server with MongoDB storage using MVC architecture

## 🎯 Features

### System Utility (Client)
- ✅ **Cross-platform support** (Windows, macOS, Linux)
- ✅ **System Health Checks**:
  - Disk encryption status
  - OS update status
  - Antivirus presence
  - Inactivity sleep settings validation (≤ 10 minutes)
- ✅ **Background Daemon**:
  - Periodic system checks (every 15-60 minutes)
  - Change-based reporting (only sends updates when system state changes)
  - Minimal resource consumption
  - Secure HTTP communication with backend

### Backend API
- ✅ **RESTful API** built with Node.js
- ✅ **MongoDB Storage** for machine data and check results
- ✅ **MVC Architecture** for clean code organization
- ✅ **Core Endpoints**:
  - Machine registration and data submission
  - Machine listing with filtering (by OS, issues, status)
  - CSV export functionality
- ✅ **Security Features**:
  - Input validation and sanitization
  - Rate limiting
  - Error handling and logging

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** (for system utility)
- **Node.js 16+** and **npm** (for backend)
- **MongoDB 5.0+** (database)
- **Git** (for cloning repository)

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/system-utility-dashboard.git
cd system-utility-dashboard
```

### 2. Backend Setup
```bash
cd backend
npm install
# Edit config.js with your MongoDB connection string
npm run dev
```

The backend will start on `http://localhost:5000`

### 3. System Utility Setup
```bash
cd client
python -m pip install -r requirements.txt
python setup.py install
```

### Running the Utility
```bash
# One-time check
system-utility check

# Start background daemon
system-utility daemon start

# Stop background daemon
system-utility daemon stop

# Check daemon status
system-utility daemon status
```

### Platform-Specific Installation

#### Windows
```bash
# Install as Windows service
pyinstaller --onefile --name "SystemUtilityChecker" --add-data "utility/.env;." .\utility\main.py
```

## 🌐 API Endpoints

### Machine Management
- `POST /api/report` - Register new machine
- `GET /api/report` - List all machines
- `GET /api/report?os_type=Windows` - Get filtered data

### Data Export
- `GET /api/report/csv` - Export all machine data as CSV
- `GET /api/report/csv?os_type=windows` - Export filtered data

### Health Checks
- `GET /api/health` - API health status

## 🧪 System Checks Details

### Disk Encryption
- **Windows**: BitLocker status via WMI
- **macOS**: FileVault status via `fdesetup`
- **Linux**: LUKS encryption detection

### OS Updates
- **Windows**: Windows Update API integration
- **macOS**: Software Update framework
- **Linux**: Package manager integration (apt, yum, dnf)

### Antivirus Detection
- **Windows**: WMI Security Center queries
- **macOS**: XProtect and third-party AV detection
- **Linux**: ClamAV and commercial AV detection

### Sleep Settings
- **Windows**: Power configuration via PowerCfg
- **macOS**: System Preferences power settings
- **Linux**: systemd power management settings

## 🔐 Security Considerations

### Data Storage
- Machine IDs are hashed for privacy
- No personally identifiable information stored

## 🚀 Production Deployment

### Environment Variables
```bash
# Backend
PORT=3000
MONGO_URI=mongodb://username:password@host:port/database

# Utility
API_URL=http://localhost:5000/api/report
```

## 📚 Development Notes

### Backend Development
- Follow MVC pattern established in codebase
- Use middleware for cross-cutting concerns
- Implement proper error handling and logging
- Follow RESTful API conventions

## 🐛 Troubleshooting

### Common Issues

#### System Utility
- **Permission Issues**: Run with administrator/root privileges for system checks
- **Network Connectivity**: Check firewall settings and API endpoint accessibility
- **Service Installation**: Ensure proper permissions for service installation

**Built with** ❤️ **using Python, Node.js, MongoDB, and modern web technologies**
