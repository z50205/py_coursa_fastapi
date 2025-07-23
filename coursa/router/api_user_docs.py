from fastapi.responses import HTMLResponse

post_api_users = {
    "summary": "新建用戶API(依照checkbox建立教師)",
    "description": "依照用戶資料儲存至資料庫，密碼以hash儲存、並有role指示是否具教師資格",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "成功建立用戶",
                "content": {
                    "application/json": {
                        "example": {
                            "status": "ok",
                            "detail": "create name success."
                        }
                    }
                }
            },
            409: {
                "description": "用戶名稱重複",
                "content": {
                    "application/json": {
                        "example": {
                            "status": "fail",
                            "detail": "duplicate name name."
                        }
                    }
                }
            },
        }
    },
    "tags": ["User(Controller)"]
}

get_api_teachers = {
    "summary": "取得教師資格列表",
    "description": "依照user資料表之role欄位取得教師列表",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "取得教師資格列表",
                "content": {
                    "application/json": {
                        "example": {
                            "1d9d12c9-d47c-40d2-bf59-2155f2c1c835":{"teacher_name":"二三四"},
                            "6ae59620-ce20-4d94-9cb4-e56e8824ab45":{"teacher_name":"一二三"},
                            "bf971ead-0060-4952-b50b-09323233ce77":{"teacher_name":"四五六"}
                        }
                    }
                }
            },
        }
    },
    "tags": ["User(Controller)"]
}

get_api_teachers_courses = {
    "summary": "取得授課教師及其課程資訊",
    "description": "依照courseuser資料中介表取得授課教師資訊及其課程資訊",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "取得授課教師資訊及其課程資訊",
                "content": {
                    "application/json": {
                        "example": {
                            "6ae59620-ce20-4d94-9cb4-e56e8824ab45":{"teacher_name":"一二三","teacher_email":"123@123.com","courses":[{"name":"234"},{"name":"材料力學"}]},
                            "bf971ead-0060-4952-b50b-09323233ce77":{"teacher_name":"四五六","teacher_email":"456@456.com","courses":[{"name":"結構學"}]}
                        }
                    }
                }
            },
        }
    },
    "tags": ["User(Controller)"]
}

get_api_teachers_courses_by_teachername = {
    "summary": "取得特定授課教師課程資訊",
    "description": "依照courseuser資料中介表取得特定用戶名稱之特定授課教師課程資訊",
    "openapi_extra":{
        "responses": {
            200: {
                "description": "取得特定授課教師課程資訊",
                "content": {
                    "application/json": {
                        "example": {
                            "b393f13b-0ad0-457a-ac23-07f247f3f0bc":{"course_name":"結構學","weekday":"5","start":"1200","end":"1600","description":"Structural engineering is interesting.","location":"和平樓"}
                        }
                    }
                }
            },
        }
    },
    "tags": ["User(Controller)"]
}