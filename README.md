# work_enpowerment_simulation

## Introduction

このリポジトリは、こちらの[GitHub](https://github.com/Aquamana06/work_enpowerment_simulation)で管理されています。

## 実験環境構築

1. ターミナルを開き、本リポジトリを任意の場所に clone する
   ```sh
   git clone https://github.com/Aquamana06/work_enpowerment_simulation.git
   ```
   <details>
      
      <summary>「Gitは内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチファイルとして認識されていません」とでた場合</summary>
      
      ### 以下のどちらかを実行
      - GitがPCにインストールされていないのでGitをインストール
         - [インストール方法 for Windows](https://qiita.com/T-H9703EnAc/items/4fbe6593d42f9a844b1c)
         - もう一度、手順1からやり直す（git cloneをする）
      - プログラムを直接ダウンロード
         - 以下の画像のように、画面上部の緑色「code」を押し、「Download ZIP」からプログラムをダウンロード
         - この方法の場合は、手順1を修了し、手順2「clone したリポジトリに移動」から再開
        <img width="917" alt="Screenshot 2024-03-21 at 11 00 16" src="https://github.com/Aquamana06/work_enpowerment_simulation/assets/42343541/76e961b2-6dc1-4f15-8fd7-8d4997320938">
         
   </details>


2. clone したリポジトリに移動
   ```sh
   cd work_enpowerment_simulation/
   ```
3. ライブラリをインストール
   ```sh
   pip install -r requirements.txt
   ```
4. 実行  
   API トークンは、実験時に配布します。
   - デモ
     ```sh
     python main.py demo APIトークン
     ```
   - 本番
     ```sh
     python main.py test APIトークン
     ```
   - （例）API トークンが xxxx の場合
     ```sh
     python main.py demo xxxx
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
