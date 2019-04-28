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
