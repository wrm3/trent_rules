[Skip to content](https://opencode.ai/docs/windows-wsl/#_top)

# Windows (WSL)

Run OpenCode on Windows using WSL for the best experience.

While OpenCode can run directly on Windows, we recommend using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) for the best experience. WSL provides a Linux environment that works seamlessly with OpenCode’s features.

* * *

## [Setup](https://opencode.ai/docs/windows-wsl/\#setup)

1. **Install WSL**

If you haven’t already, [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) using the official Microsoft guide.

2. **Install OpenCode in WSL**

Once WSL is set up, open your WSL terminal and install OpenCode using one of the [installation methods](https://opencode.ai/docs/).



```
curl -fsSL https://opencode.ai/install | bash
```

3. **Use OpenCode from WSL**

Navigate to your project directory (access Windows files via `/mnt/c/`, `/mnt/d/`, etc.) and run OpenCode.



```
cd /mnt/c/Users/YourName/project

opencode
```


* * *

## [Desktop App + WSL Server](https://opencode.ai/docs/windows-wsl/\#desktop-app--wsl-server)

If you prefer using the OpenCode Desktop app but want to run the server in WSL:

1. **Start the server in WSL** with `--hostname 0.0.0.0` to allow external connections:



```
opencode serve --hostname 0.0.0.0 --port 4096
```

2. **Connect the Desktop app** to `http://localhost:4096`


```
OPENCODE_SERVER_PASSWORD=your-password opencode serve --hostname 0.0.0.0
```

* * *

## [Web Client + WSL](https://opencode.ai/docs/windows-wsl/\#web-client--wsl)

For the best web experience on Windows:

1. **Run `opencode web` in the WSL terminal** rather than PowerShell:



```
opencode web --hostname 0.0.0.0
```

2. **Access from your Windows browser** at `http://localhost:<port>` (OpenCode prints the URL)


Running `opencode web` from WSL ensures proper file system access and terminal integration while still being accessible from your Windows browser.

* * *

## [Accessing Windows Files](https://opencode.ai/docs/windows-wsl/\#accessing-windows-files)

WSL can access all your Windows files through the `/mnt/` directory:

- `C:` drive → `/mnt/c/`
- `D:` drive → `/mnt/d/`
- And so on…

Example:

```
cd /mnt/c/Users/YourName/Documents/project

opencode
```

* * *

## [Tips](https://opencode.ai/docs/windows-wsl/\#tips)

- Keep OpenCode running in WSL for projects stored on Windows drives - file access is seamless
- Use VS Code’s [WSL extension](https://code.visualstudio.com/docs/remote/wsl) alongside OpenCode for an integrated development workflow
- Your OpenCode config and sessions are stored within the WSL environment at `~/.local/share/opencode/`