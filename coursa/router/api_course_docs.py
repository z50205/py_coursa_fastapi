get_api_courses = {
    "summary": "取得所有課程資訊",
    "description": "依照courseuser資料中介表取得所有課程資訊及相關的授課教師資訊",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "取得所有課程資訊及授課教師資訊",
                "content": {
                    "application/json": {
                        "example":{"5272ca93-048f-4f85-b2a9-ce67b48a7ab4":{"course_name":"234","weekday":"2","start":"1231","end":"1232","description":"123","location":"123","teachers":[{"name":"一二三","email":"123@123.com"}]},
                                   "b393f13b-0ad0-457a-ac23-07f247f3f0bc":{"course_name":"結構學","weekday":"5","start":"1200","end":"1600","description":"Structural engineering is interesting.","location":"和平樓","teachers":[{"name":"四五六","email":"456@456.com"}]},
                                   "1d8f6c2e-7fec-4648-9816-d715b2f56ffe":{"course_name":"材料力學","weekday":"5","start":"1000","end":"1200","description":"材料力學學力學基礎","location":"大同樓","teachers":[{"name":"一二三","email":"123@123.com"}]}}
                    }
                }
            },
        }
    },
    "tags": ["Course(Controller)"]
}
get_api_courses_by_courseid = {
    "summary": "取得特定Courseid之課程資訊",
    "description": "依照courseuser資料中介表取得所有課程資訊及相關的授課教師資訊",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "取得特定課程資訊及授課教師資訊",
                "content": {
                    "application/json": {
                        "example":{"b393f13b-0ad0-457a-ac23-07f247f3f0bc":{"course_name":"結構學","weekday":"5","start":"1200","end":"1600","description":"Structural engineering is interesting.","location":"和平樓","teachers":[{"name":"四五六","id":"bf971ead-0060-4952-b50b-09323233ce77"}]}}
                    }
                }
            },
        }
    },
    "tags": ["Course(Controller)"]
}
post_api_courses = {
    "summary": "新增課程資訊",
    "description": "依照Form資料建立課程資料、授課資料",
    "openapi_extra":{
        "responses": {
            201:{
          "description": "成功建立課程",
          "content": {
            "application/json":{
                "example":{
                    "status":"ok","detail":"create course success."}
                    }
                }
            },
             403:{
          "description": "授課教師沒有授課權限",
          "content": {
            "application/json":{
                "example":{
                    "status":"fail","detail":"authorization failed."}
                    }
                }
            },
             409:{
          "description": "課程名稱重複",
          "content": {
            "application/json":{
                "example":{
                    "status":"fail","detail":"duplicate course name."}
                    }
                }
            },
        }
    },
    "tags": ["Course(Controller)"]
}
patch_api_courses = {
    "summary": "更新課程資訊",
    "description": "依照courseid及Form資料更新課程資料、授課資料",
    "openapi_extra":{
        "responses": {
            201:{
          "description": "成功更新課程",
          "content": {
            "application/json":{
                "example":{
                    "status":"ok","detail":"update course success."}
                    }
                }
            },
             403:{
          "description": "新授課教師沒有授課權限",
          "content": {
            "application/json":{
                "example":{
                    "status":"fail","detail":"authorization failed."}
                    }
                }
            },
             409:{
          "description": "新課程名稱重複",
          "content": {
            "application/json":{
                "example":{
                    "status":"fail","detail":"duplicate course name."}
                    }
                }
            },
        }
    },
    "tags": ["Course(Controller)"]
}
delete_api_courses = {
    "summary": "刪除課程資訊",
    "description": "依照courseid刪除相關課程資料",
    "openapi_extra":{
        "responses": {
            201:{
          "description": "成功刪除課程",
          "content": {
            "application/json":{
                "example":{
                    "status":"ok","detail":"delete course success."}
                    }
                }
            },
        }
    },
    "tags": ["Course(Controller)"]
}