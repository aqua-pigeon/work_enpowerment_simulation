# work_enpowerment_simulation

## Introduction

このリポジトリは、こちらの[GitHub](https://github.com/Aquamana06/work_enpowerment_simulation)で管理されています。

## 実験環境構築

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
