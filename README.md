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

## Lessons
- As starting point for this hands-on you can checkout the Lesson0 branch: `git checkout Lesson0`
- Or checkout tag for Lesson1: `git checkout tags/Lesson1` (you will be in detached HEAD -> do also `git reset --hard`)
- To get on a stable revision for each exercise, you can always checkout a specific tag
- To get back to main branch you can always use `git checkout main`
- Check the `Commands.md` file for the commands used in each lesson


# Sources 
- https://dominikberner.ch/using-devcontainers-with-cpp/
- https://github.com/axel-op/vscode-devcontainer-cpp-conan
- https://github.com/bredej/vscode-conan-remote
- https://github.com/mymichu/workspace-c-cpp-conan
