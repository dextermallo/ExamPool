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
print(<var>, file = sys.stderr)

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


