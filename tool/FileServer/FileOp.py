import json


def get_server_config() -> object:
    """

    :rtype: object
    """
    json_file = open('./server_config.json', 'r', encoding='utf-8')
    j = json.load(json_file)
    tag_server_ip = 'server_ip'
    tag_server_port = 'server_port'
    config = {tag_server_ip: '127.0.0.1', tag_server_port: 12345}
    if tag_server_ip in j.keys():
        config[tag_server_ip] = j[tag_server_ip]
    if tag_server_port in j.keys():
        config[tag_server_port] = j[tag_server_port]
    json_file.close()
    return config
