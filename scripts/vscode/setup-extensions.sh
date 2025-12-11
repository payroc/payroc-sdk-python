#!/bin/bash
# Setup VS Code Extensions for Payroc SDK Development (macOS/Linux)
# This script installs the recommended extensions for developing the Payroc Python SDK

echo "Installing VS Code extensions for Payroc SDK development..."

# Check if code command is available
if ! command -v code &> /dev/null; then
    echo "Error: VS Code command 'code' not found in PATH."
    echo "Please ensure VS Code is installed and the 'code' command is available."
    echo "You can add it to PATH by opening VS Code and running 'Shell Command: Install 'code' command in PATH' from the command palette."
    exit 1
fi

# Install Python extension
echo "Installing Python extension..."
code --install-extension ms-python.python --force

# Install Pylance
echo "Installing Pylance..."
code --install-extension ms-python.vscode-pylance --force

echo "✓ Extensions installed successfully!"
echo ""
echo "Next steps:"
echo "1. Reload VS Code (Ctrl+R or Cmd+Shift+P > Reload Window)"
echo "2. Run tests using the Test Explorer in the sidebar or 'pytest' command"
echo ""
echo "For more information, see CONTRIBUTING.md"
