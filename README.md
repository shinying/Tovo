# Tovo Backend

## Set up

```shell
pip install django
pip install django-cors-headers
pip install Pillow
```

## API

### 使用者

#### "/user/his"

獲得使用者歷史紀錄

* method: GET
* args: 
    * "uid" (int)
* return: json
    * "taker" : name (string)
    * "rider" : name (string)
    * "taker_score" (int)
    * "rider_score" (int)
    * "start_time" (datetime)
    * "end_time" (datetime)
    * "duration" : minutes (int)

#### "/user/profile"

獲得使用者個人檔案

* method: GET
* args: 
    * "uid" (int)
* return: array of json with keys below
    * "name" (string)
    * "email" (string)
    * "weight" (int)
    * "score_as_taker" (float)
    * "score_as_rider" (float)
    * "gear" (int)
    * "rose" (int)


#### "/user/all"

獲得自己以外的使用者清單

* method: GET
* args:
    * "uid" (int) - please pass with url
* return: array of json
    * "uid" (int)
    * "name" (string)

#### "/user/create"

註冊新使用者

* method: POST
* args:
    * "email" (string)
    * "name" (string)
    * "password" (string)
    * "gender" : "F" or "M" (char)
* return: none

#### "/user/login"

登入

* method: POST
* args:
    * "name" (string)
    * "password" (string)
* return: json
    * "uid" : user ID (int)
    * "name" (string)

#### "/user/update"

更新個人資料

* method: POST
* args: json
    * "uid" (int)
    * "name" (string)
    * "email" (string)
    * "weight" (int)
    * "image" (string)
* return: none


## 旅程

#### "/trip/"

查看還沒有人接的單

* method: GET
* args: none
* return: json
    * "tid" : trip ID (int)
    * "name" (string)
    * "gender" : "Male" or "Female" (string)
    * "score" (float)
    * "weight" (int)
    * "image" : url of image (string)
    * "slon" : starting longitude (float)
    * "slat" : starting latitude (float)
    * "elon" : ending longitude (float)
    * "elat" : ending latitude (float)
    * "duration" : estimated time of the trip (int)

#### "/trip/go"

新增旅程

* method: POST
* args:
    * "uid" (int)
    * "slon" (float)
    * "slat" (float)
    * "elon" (float)
    * "elat" (float)
* return:
    * "tid" : trip ID (int)

#### "/trip/accept"

接單

* method: POST
* args:
    * "uid" (int)
    * "tid" (int)
* return: none

#### "/trip/start"

旅程開始

* method: POST
* args:
    * "tid" (int)
* return: none

#### "/trip/end"

旅程結束

* method: POST
* args: 
    * "tid" (int)
* return: none

#### "/trip/rate"

評分，自動自動判斷誰評誰

* method: POST
* args: 
    * "tid" : trip ID (int)
    * "uid" : user ID (int)
    * "point" (int)
* return: none

## 獎賞

#### "/buy"

買 title

* method: POST
* args: 
    * "uid" (int)
    * "ttid" : title ID (int)
* return: none

#### "/equip"

裝備 title

* method: POST
* args:
    * "uid" (int)
    * "ttid" (int)
* return none

#### "/give"

轉錢

* method: POST
* args:
    * "uid" : user ID (int)
    * "u2id" : user2 ID (int)
    * "amount" (int)
    * "unit" : "gear" or "rose" (string)
* return: none

#### "/titles"

查看可購買的 titles

* method: GET
* args: none
* return: array of json
    * "ttid" : title ID (int)
    * "name" (string)
    * "price" (iny)
    * "job" : "Taker" or "Rider" (string)

#### "/rank/taker"

* method: GET
* args: none
* return: array of json
    * "name" (string)
    * "title" (string)
    * "gear" (int)
    * "day" (int)

#### "/rank/rider"

* method: GET
* args: none
* return: array of json
    * "name" (string)
    * "title" (string)
    * "rose" (int)
    * "day" (int)
