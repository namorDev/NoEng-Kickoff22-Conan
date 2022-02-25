# Usage options
There are several ways you can use this repository:
- Visual Studio Code Remote Container with Docker Desktop
- Visual Studio Code Remote Container in WSL or Linux
- Use Dockerfile itself
- Do not use Docker and install conan / cmake by yourself

## Prerequisites: VS Code Remote Container and Docker Desktop
- Docker Desktop installed
- VS Code installed
- VS Code Remote - Containers extension installed

Now open VS Code and execute command (Ctrl+Shift+P) `Remote-Containers: Open Folder in Container` or click "Reopen in Container" on the popup.

## Prerequisites: Visual Studio Code Remote Container in WSL or Linux
- Docker installed (check that docker deamon is running with `ps -aux | grep docker`
- Add user to docker group `sudo usermod -aG docker $USER` (you might have to restart your system after that)
- VS Code installed
- VS Code Remote-Containers extension installed: `code --install-extension ms-vscode-remote.vscode-remote-extensionpack` 

Now open VS Code and execute command (Ctrl+Shift+P) `Remote-Containers: Open Folder in Container` or click "Reopen in Container" on the popup.

<<<<<<< Updated upstream
# Sources 
=======
# Sources
>>>>>>> Stashed changes
- https://dominikberner.ch/using-devcontainers-with-cpp/
- https://github.com/axel-op/vscode-devcontainer-cpp-conan
- https://github.com/bredej/vscode-conan-remote
- https://github.com/mymichu/workspace-c-cpp-conan

