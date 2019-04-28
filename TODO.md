# updated 2019/4/28/13:25 by Dexter.

# question
1. in info.html difference between 
 | <link rel="stylesheet" type="text/css" href="../../static/bootstrap-4.3.1/css/bootstrap.min.css"> Error 404
 | <link rel="stylesheet" type="text/css" href="/../../static/bootstrap-4.3.1/css/bootstrap.min.css"> OK

# Todo.

 ## model
   1. contribution model
   2. extend user model
   3. favorite model
 ## view
   1. 修正註冊後不會自動登入
   2. 註冊時需檢查用戶名是否重複
 ## controller
  ### 註冊頁面
    1. 頁面美化
    2. 處理註冊名重複問題
    3. 加上nav-bar
  ### 登入頁面
    1. 頁面美化
  ### 用戶資料(帳號管理)
    1. 頁面美化
    2. 功能：user 對自己可管理
    3. 功能：user 對別人可瀏覽
  ### 其他(script)
    1. nav-bar 美化
    2. infonotfound 美化、更名
    3. error 跳轉上一頁的btn
 ## others
   1. 部分檔案名修正(info, login, etc.)
   2. 報告修正
   3. 修改 catalog 檔案夾名
   4. static 多於資料去除
   5. logo 修正
    

# Log

 ## 2019/3/12
    1. CRUD function
    2. mongodb 測試
 ## 2019/3/25
    1. add gitignore
    2. 更名部分資料夾
 ## 2019/4/24
    1. 部署至虛擬環境
    2. 資料連接改為使用djongo API
    3. user model 改採 native model.
 ## 2019/4/26
    1. 完成 login, register 功能
 ## 2019/4/27
    1. 完成 accounts/info/ 個別化登入
    2. UI 微調
    3. templates 覆用
 ## 2019/4/28 
    1. 更改為用forms.py 進行管理
    2. 用 widget-tweaks 解耦 view 和 controller 的關係
    3. 修正 urls.py 路徑
    

