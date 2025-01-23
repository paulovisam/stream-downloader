import os
import re
import json
from collections import defaultdict
from tqdm import tqdm
from pyrogram import Client
import asyncio
import utils
import pyrogram
from halo import Halo
import argparse

pyrogram.utils.MIN_CHANNEL_ID = -1002999999999

session_name = "user_session"
SUPPORTED_MIME_TYPES = ["application/zip", "application/vnd.rar"]

app = Client(session_name)

TASKS_DIR = "tasks"
if not os.path.exists(TASKS_DIR):
    os.mkdir(TASKS_DIR)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Script para baixar arquivos e vídeos de um canal do Telegram."
    )
    parser.add_argument(
        "--channel-id",
        type=int,
        help="ID do canal Telegram (formato: -100xxxxxxxxxx)",
    )
    return parser.parse_args()

async def carregar_dialogos(app):
    print("Carregando diálogos (canais e grupos) do Telegram...")
    spinner = Halo(
        text="Carregando os chats que você participa...", spinner="dots"
    )
    spinner.start()
    try:
        async for dialogo in app.get_dialogs():
            pass
    except Exception as e:
        print(f"Erro ao carregar os diálogos: {e}")
    finally:
        spinner.stop()

async def get_channel():
    id_canal = input("Digite o ID do canal: ")
    return int(id_canal)

def save_progress(channel_id, last_processed_msg_id):
    file_path = os.path.join(TASKS_DIR, f"{channel_id}.json")
    with open(file_path, "w") as f:
        json.dump({"last_processed_msg_id": last_processed_msg_id}, f)

def load_progress(channel_id):
    file_path = os.path.join(TASKS_DIR, f"{channel_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            return data.get("last_processed_msg_id")
    return None

def get_cleaned_file_path(file_name, module_dir):
    file_name = (
        file_name.replace("\\", "_")
        .replace("/", "_")
        .replace("\n", "")
        .strip()
    )
    # file_name = re.sub(r"#[A-Z]\d+\s*", "", file_name)
    file_name = re.sub(r"#\w+\s*", "", file_name)
    return os.path.join(module_dir, file_name)

def get_cleaned_module_name(module_name):
    return re.sub(r"#\w(\d+)", r"\1", module_name).strip()

def parse_summary(summary_message):
    modules = defaultdict(list)
    current_module = None

    for line in summary_message.split("\n"):
        if line.startswith("="):  # Cabeçalho do módulo
            current_module = line.strip("= ").strip()
        elif line.startswith("#"):  # Hashtags
            if current_module:
                hashtags = re.findall(r"#\w\d+", line)
                modules[current_module].extend(hashtags)
    return modules

async def get_all_messages(channel_id, last_processed_msg_id=None):
    """
    Obtém todas as mensagens do canal, começando da última mensagem processada (se especificado).
    """
    all_messages = []
    async for message in app.get_chat_history(channel_id):
        if (
            last_processed_msg_id is not None
            and message.id <= last_processed_msg_id
        ):
            break
        all_messages.append(message)
    all_messages.reverse()
    print(f"Retrieved {len(all_messages)} messages.")
    return all_messages

async def download_videos(
    modules, channel_id, base_dir, last_processed_msg_id=None
):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    messages = await get_all_messages(channel_id, last_processed_msg_id)
    print(f"Found {len(messages)} messages to process.")

    for message in messages:
        if hasattr(message, "video") and message.video:
            hashtags = (
                re.findall(r"#\w\d+", message.caption)
                if message.caption
                else []
            )
            print(f"Message {message.id} hashtags: {hashtags}")

            target_module = None
            for module, module_tags in modules.items():
                if any(tag in module_tags for tag in hashtags):
                    target_module = module
                    break

            if target_module:
                module_dir = os.path.join(
                    base_dir, get_cleaned_module_name(target_module)
                )
                if not os.path.exists(module_dir):
                    os.mkdir(module_dir)

                file_name = (
                    message.caption.strip()
                    if message.caption
                    else f"video_{message.video.file_id}.mp4"
                )
                file_name = get_cleaned_file_path(file_name, module_dir)

                utils.clear()
                with tqdm(
                    total=message.video.file_size,
                    desc=f"Downloading {os.path.basename(file_name)}",
                    leave=False,
                ) as bar:
                    try:
                        await app.download_media(
                            message.video,
                            file_name=file_name,
                            progress=lambda c, t: bar.update(c - bar.n),
                        )
                        print(f"Downloaded: {file_name}")
                    except Exception as e:
                        print(f"Failed to download video: {e}")

        save_progress(channel_id, message.id)

async def download_files(channel_id, base_dir, last_processed_msg_id=None):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)

    messages = await get_all_messages(channel_id, last_processed_msg_id)
    print(f"Found {len(messages)} messages to process.")

    for message in messages:

        if hasattr(message, "document") and message.document:
            mime_type = message.document.mime_type
            file_name = message.document.file_name

            if mime_type in SUPPORTED_MIME_TYPES:
                print(f"Found supported file: {file_name} (MIME: {mime_type})")
                file_path = os.path.join(base_dir, file_name)

                with tqdm(
                    total=message.document.file_size,
                    desc=f"Downloading {file_name}",
                    leave=False,
                ) as bar:
                    try:
                        await app.download_media(
                            message.document,
                            file_name=file_path,
                            progress=lambda current, total: bar.update(
                                current - bar.n
                            ),
                        )
                        print(f"Downloaded: {file_name}")
                    except Exception as e:
                        print(
                            f"Failed to download file: {file_name}. Error: {e}"
                        )

        save_progress(channel_id, message.id)

async def main():

    args = parse_args()

    utils.clear()
    utils.show_banner()
    await utils.authenticate()
    await app.start()
    await carregar_dialogos(app)

    if args.channel_id:
        channel_id = args.channel_id
    else:
        channel_id = int(input("Digite o ID do canal: "))

    chat = await app.get_chat(channel_id)
    pinned_message = chat.pinned_message

    if not pinned_message or not pinned_message.text:
        print("Pinned summary message not found!")
        await app.stop()
        return

    channel_name = chat.title.replace(".", "").replace(
        "/", "_"
    )  # Sanitiza o nome do canal
    base_dir = os.path.join("Downloads", channel_name)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    modules = parse_summary(pinned_message.text)

    last_processed_msg_id = load_progress(channel_id)

    if last_processed_msg_id is not None:
        print(f"Resuming from message ID: {last_processed_msg_id + 1}")
    else:
        print("No progress found. Starting from the latest message.")

    await download_videos(modules, channel_id, base_dir, last_processed_msg_id)

    await download_files(channel_id, base_dir, last_processed_msg_id)

    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
