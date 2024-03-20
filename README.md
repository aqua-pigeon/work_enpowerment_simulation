# work_enpowerment_simulation

## Introduction

このリポジトリは、こちらの[GitHub](https://github.com/Aquamana06/work_enpowerment_simulation)で管理されています。

## 実験環境構築

1. 本リポジトリを任意の場所に clone する
   ```sh
   git clone https://github.com/Aquamana06/work_enpowerment_simulation.git
   ```
2. clone したリポジトリに移動
   ```sh
   cd work_enpowerment_simulation/
   ```
3. ライブラリをインストール
   ```sh
   pip install -r requirements.txt
   ```
4. ファイルを作成
   utils フォルダの中に**get_api_token.py**という名前のファイルを作成  
   ファイルの中身は以下をコピペ
   ```python
   def get_slack_api_token():
     return ""  # ここにトークンを入れる
   ```
5. API トークンを設定
   - utils/get_api_token.py の""に API トークンをペースト
   - API トークンは実験者から直接配布される
   ```python
    return ""  # ここにトークンを入れる
   ```
6. 実行  
   デモ
   ```sh
   python main.py demo
   ```
   本番
   ```sh
   python main.py test
   ```

## Git 操作メモ

- 最新のリモートリポジトリの状態をローカルリポジトリに反映する
  ```git
      git pull
  ```
- conflict が起きたとき
  ```git
    git stash
    git pull
    git stash pop
  ```
- ローカルリポジトリの変更をリモートリポジトリに反映する
  ```git
      git add .
      git commit -m "コミットメッセージ"
      git push
  ```
- main ブランチから今のブランチにマージする
  ```git
      git merge main
  ```
- ブランチを切り替える
  ```git
      git checkout ブランチ名
  ```
- ブランチを作成する
  ```git
      git checkout -b ブランチ名
  ```

## ライブラリのインストール

- 使用ライブラリ一覧
  - requirements.txt に記載
  - pip でインストールする
- インストール
  ```sh
      pip install -r requirements.txt
  ```

## log ファイルのクリア

```ps1
  Get-ChildItem -Path "log\" -Filter "*.json" | ForEach-Object {
    # ファイルが.jsonであれば削除する
    Remove-Item $_.FullName
    Write-Output "Removed: $($_.FullName)"
}
```
