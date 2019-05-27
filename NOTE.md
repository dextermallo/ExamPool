# updated 2019/4/28/13:25 by Dexter.

# NOTED
1. 導向路徑
href = "accounts/logout/"  > /root/accounts/logout/
href = "/accounts/logout/" > /現在所在的位子/accounts/logout/

2. POST
post 是丟 input name = "", 不是看id

3. Error when all things right.
畫面正常，POST也有跑但是都沒出去，先檢查port (27017 & 8000)，
可能有共用port的情形，全部關閉再重開mongo & django

4. debug in terminal
import sys
print([var], file = sys.stderr)

5. {% include <html path> %}
路徑是以templates為root, 以絕對路徑access較佳

6. django-widget-tweaks: 'render_field' tag requires a form field followed by a list of attributes and values in the form attr="value": class
{% render_field field class ="form-control is-valid" %}
                           ^ ^both case sensitivite.(no space)

7. Migrate Error
先檢查database & 重新 migrate，有可能是database裡面的表格形式不是對的

8. add json to mongo via cmd.
mongoimport --db dbName --collection collectionName --file fileName.json
 ＊注意匯入的檔案名稱是appname_collectionName，如catalog_department

9. 在 ImageField問題上，因為無法抓到 database的實際 url，且生成的也不是.jpg，
最佳解是利用 django 原生的方式處理 (MEDIA_ROOT + url)

# COMMAND
1. installation
brew install mongodb 
pip3 install django  
pip3 install djongo  
pip3 install django-widget-tweaks  

2. usage
cd env  
source bin/activate  

3. call cmd
python3 manage.py shell  

4. run
python3 manage.py runserver  

5. migrate (syncdb)  
python3 manage.py migrate  

6. quit   
deactivate  

7. startup(on Mac)
cd env  
source bin/activate  
alias e="python3 manage.py"  
alias c="clear"  
e migrate  
c  

8. kill port(on Mac)
lsof -i:[port-number]
kill -9 [pid]

9. drop database
mongo [dbname] --eval "db.dropDatabase()"

10. delete migrations (in root path)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# IDEA
1. 刷題
2. npm
3. jinja custom filter https://docs.djangoproject.com/en/dev/howto/custom-template-tags/

# TODO
02. 完成 user profile頁面.
03. 處理註冊名重複問題
04. 修正註冊後不會自動登入
05. 首頁內容
06. 各頁面美化
10. 檔案名修正(info, login, etc.)
11. 修改 catalog 檔案夾名
12. static 多餘資料去除
16. 新增 comment 於個人頁面顯示
   
# LOG
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
## 2019/5/02
   1. 加入.sh 自動初始化  
## 2019/5/12
   1. 頁面美化
## 2019/5/17
   1. 整合美化註冊、登入頁面
   2. 優化使用者資訊頁面
   3. 修正部分static url
   4. 優化.sh
   5. 整合Note.md, TODO.md.
   6. 刪除 static 不必要的檔案.
## 2019/5/19
   1. 修正 logo 大小錯誤
   2. 新增 contribution 列表頁面、查詢功能、model
   3. 新增django-mathfilters(0.4.0)，可在html中對數值進行運算
   4. 新增 fontawesome(5.8.2).
   5. 部分 UI 優化
## 2019/5/20
   1. 頁面小圖標
   2. 抽離耦合css
   3. 修正部分頁面名稱
   4. 修正 profile favorite 查詢功能
## 2019/5/26
   1. 擴展 user model
   2. user 管理介面功能
   3. 修改register.html (耦合)
   4. ImageField 上傳使用者圖片

