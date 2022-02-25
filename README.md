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

## Prerequisites: Visual Studio Code Remote Container in WSL or Linux
- Docker installed (check that docker deamon is running with `ps -aux | grep docker`
- Add user to docker group `sudo usermod -aG docker $USER` (you might have to restart your system after that)
- VS Code installed
- VS Code Remote-Containers extension installed: `code --install-extension ms-vscode-remote.vscode-remote-extensionpack` 

## First Steps
1. Open git bash
2. Clone the git repository (fork if you want) `git clone git@github.com:namorDev/NoEng-Kickoff22-Conan.git`
4. Change directory `cd NoEng-Kickoff22-Conan`
5. Open VS Code (`code .`) and execute command (Ctrl+Shift+P) `Remote-Containers: Open Folder in Container` or click "Reopen in Container" on the popup.
6. Wait until container is built
7. Open a terminal inside VS Code and check if conan is properly installed `conan --version`
8. Checkout the remote list `conan remote list`
9. Checkout the recipes in the local cache `conan search`

## Lesson 1
1. Checkout branch Lesson1 `git checkout Lesson1`
2. Install the dependency specified in conanfile.txt by execute command `conan install`
3. Inspect local cache with `conan search` -> We have the recipe but it's not built yet
4. Build it with `conan install --build=missing`
5. Inspect local cache with `code ~/.conan/data`

# Sources 
- https://dominikberner.ch/using-devcontainers-with-cpp/
- https://github.com/axel-op/vscode-devcontainer-cpp-conan
- https://github.com/bredej/vscode-conan-remote
- https://github.com/mymichu/workspace-c-cpp-conan

