import json
def headers(header_string):
    tmp = {}
    if(header_string.startswith("POST")):
        tmp["POST_FIELDS"] = {}
        for pair in header_string.split("\r\n\r\n")[1].split("&"):
            tmp["POST_FIELDS"][pair.split("=")[0]] = pair.split("=")[1]
    return tmp

def parse(request):
    parsed = {}
    parsed["method"] = request.split()[0]
    parsed["url"] = request.split()[1]
    parsed["data"] = headers(request)
    return parsed

def build_response(response_dict):
    http_version = response_dict["http-version"]
    http_status = response_dict["status"]
    response_str = f"{http_version} {http_status}"

    if(isinstance(response_dict["content"], dict)):
        response_dict["content-type"] = "application/json"
        response_dict["content"] = json.dumps(response_dict["content"])

    for key, value in response_dict.items():
        if(key == "content"):
            response_str += "\r\n\r\n" + value
        else:
            response_str = response_str + "\r\n" + key + ": " + value
    return response_str
