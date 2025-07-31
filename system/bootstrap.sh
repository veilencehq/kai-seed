#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Bootstrapping Kai’s core environment..."
pkg update -y
pkg install python git -y
pip install --upgrade pip
echo "✅ Bootstrap complete. Kai’s environment is ready."
