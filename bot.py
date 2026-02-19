import fluxer
from colorama import Fore, Style, init
import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime


init(autoreset=True)

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = fluxer.Intents.default()
intents.message_content = True

client = fluxer.Bot(intents=intents, command_prefix='n!')

def log(msg: str, level: str = "info"):
    time = datetime.now().strftime("%H:%M:%S")
    levels = {
        "info": Fore.CYAN + "[INFO]",
        "success": Fore.GREEN + "[SUCCESS]",
        "warn": Fore.YELLOW + "[WARN]",
        "error": Fore.RED + "[ERROR]",
        "critical": Fore.MAGENTA + "[CRITICAL]",
    }
    tag = levels.get(level, Fore.WHITE + "[LOG]")
    print(f"{Fore.BLACK}[{time}]{Style.RESET_ALL} {tag} {Fore.WHITE}{msg}{Style.RESET_ALL}")

@client.event
async def on_ready():
    log(f"System online as {client.user} ({client.user.id})", "success")
    log(f"Connected to {len(client.guilds)} guilds.", "info")


async def load_cogs():
    loaded = []
    failed = []

    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            name = filename[:-3]
            try:
                await client.load_extension(f"cogs.{name}")
                loaded.append(filename)
            except Exception as e:
                failed.append((filename, str(e)))

    if loaded:
        log("Loaded cogs:", "success")
        for file in loaded:
            print(Fore.GREEN + f"   → {file}")
    if failed:
        log("Failed to load cogs:", "error")
        for file, error in failed:
            print(Fore.RED + f"   → {file}: {error}")

async def main():
    try:
        await load_cogs()
    except Exception as e:
        log(f"Critical error loading cogs: {e}", "critical")

    try:
        log("Starting Nari client...", "info")
        await client.start(TOKEN)
    except KeyboardInterrupt:
        log("Manual shutdown requested (Ctrl+C)", "warn")
        await client.close()
    except Exception as e:
        log(f"Failed to start bot: {e}", "critical")

if __name__ == "__main__":
    asyncio.run(main())