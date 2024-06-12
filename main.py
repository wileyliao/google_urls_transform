def convert_google_drive_url(view_url):
    """將 Google Drive 預覽 URL 轉換為下載 URL"""
    if '/file/d/' in view_url and '/view' in view_url:
        # 提取文件 ID
        file_id = view_url.split('/file/d/')[1].split('/view')[0]
        # 構建下載 URL
        download_url = f"https://drive.google.com/uc?id={file_id}"
        return download_url
    else:
        return "Invalid Google Drive view URL"

def batch_convert_google_drive_urls(view_urls):
    """批量轉換 Google Drive 預覽 URL 為下載 URL"""
    return [convert_google_drive_url(url) for url in view_urls]

# 測試用的 URL 列表
view_urls = [
    "https://drive.google.com/file/d/1-bYAfVkocqz4H4X9TmZhPAIFz2xjow6_/view?usp=sharing",
    "https://drive.google.com/file/d/1-g_7gdwo2A3Do5lheVhKSUE-3c0LX0RZ/view?usp=sharing",
    "https://drive.google.com/file/d/1-h-idnLHjo4jhuNxbMT2bTxZZ-tG6Ej4/view?usp=sharing"
]

# 批量轉換
download_urls = batch_convert_google_drive_urls(view_urls)
for view, download in zip(view_urls, download_urls):
    print(f"View URL: {view}\nDownload URL: {download}\n")