from modules.shared import opts
do_debug_print = getattr(opts, "civitai_debug_prints", False)
def init():
    global download_queue, last_version, cancel_status, recent_model, last_url, \
           json_data, json_info, main_folder, previous_inputs, download_fail, \
           sortNewest, isDownloading, old_download, scan_files, from_update_tab, \
           url_list, print, subfolder_json

    import warnings, os, json
    from urllib3.exceptions import InsecureRequestWarning
    warnings.simplefilter('ignore', InsecureRequestWarning)

    config_folder = os.path.normpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "config"
    ))
    os.makedirs(config_folder, exist_ok=True)

    subfolder_json = os.path.join(config_folder, "civitai_subfolders.json")
    if not os.path.exists(subfolder_json):
        with open(subfolder_json, 'w', encoding='utf-8') as json_file:
            json.dump({}, json_file)

    cancel_status = None
    recent_model = None
    json_data = None
    json_info = None
    main_folder = None
    previous_inputs = None
    last_version = None
    url_list = {}
    download_queue = []

    from_update_tab = False
    scan_files = False
    download_fail = False
    sortNewest = False
    isDownloading = False
    old_download = False
    old_download = False

_print = print
def print(print_message):
    _print(f'\033[96mCivitAI Browser+\033[0m: {print_message}')
    
def debug_print(print_message):
    if do_debug_print:
        _print(f'\033[96m[DEBUG] CivitAI Browser+\033[0m: {print_message}')
