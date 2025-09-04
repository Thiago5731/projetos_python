#funções_suporte
import requests
import urllib3

# Desativa avisos de certificado SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def api1(login, password, email):
    """API 1 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "email": email}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api2(login, password, email, threshold):
    """API 2 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "email": email, "threshold": threshold}
    resposta = requests.post(url, data=data, verify=False).text
    print (resposta)
    return resposta

def api3(login, password, email):
    """API 3 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "email": email}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api4(login, password, domain):
    """API 4 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain, "quota": 1}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api5(login, password, email, quota):
    """API 5 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "email": email, "quota": quota}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return 

def api6(login, password, domain):
    """API 6 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain, "status": "disabled"}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api7(login, password, domain, tipo):
    """API 7 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain, "type": tipo}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api8(login, password, domain, host):
    """API 8 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain, "host": host}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta
def api9(login, password, domain):
    """API 9 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api10(login, password, id_revenda):
    """API 10 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "id": id_revenda}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api11(login, password, user_email, start_time, end_time):
    """API 11 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "userEmail": user_email,
            "startTime": start_time, "endTime": end_time}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api111(login, password, user_email, message_ids):
    """API 111 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "userEmail": user_email,
            "messageId": message_ids}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api12(login, password, user_email, start_time, end_time):
    """API 12 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "userEmail": user_email,
            "startTime": start_time, "endTime": end_time}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api13(login, password, user_email, sender_email, start_time, end_time):
    """API 13 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "userEmail": user_email,
            "senderEmail": sender_email, "startTime": start_time, "endTime": end_time}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api14(domain, login, password):
    """API 14 """
    url = "apis.thiagocarvalho.com.br"
    data = {"domain": domain, "login": login, "password": password}
    resposta = requests.post(url, data=data, verify=False).content
    print(resposta)
    return resposta

def api15(domain, login, password, start_time, end_time):
    """API 15 """
    url = "apis.thiagocarvalho.com.br"
    data = {"domain": domain, "login": login, "password": password,
            "startTime": start_time, "endTime": end_time}
    resposta = requests.post(url, data=data, verify=False).content
    print(resposta)
    return resposta

def api16(login, password, domain):
    """API 16 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api17(login, password, domain):
    """API 17 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "domain": domain}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api18(token, domain, group, email):
    """API 18 """
    url = "apis.thiagocarvalho.com.br"
    data = {"token": token, "domain": domain, "group": group, "email": email}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api19(token, level, domain, user, start_time, end_time,
                          active_page, limit, offset, count, receiver_email):
    """API 19 """
    url = "apis.thiagocarvalho.com.br"
    data = {"token": token, "level": level, "domain": domain, "user": user,
            "startTime": start_time, "endTime": end_time, "activePage": active_page,
            "limit": limit, "offset": offset, "count": count, "receiverEmail": receiver_email}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api20(login, password):
    """API 20 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "list": "true"}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api21(login, password, external_domain):
    """API 21 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "externalDomain": external_domain}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta

def api22(login, password, external_domain):
    """API 22 """
    url = "apis.thiagocarvalho.com.br"
    data = {"login": login, "password": password, "externalDomain": external_domain}
    resposta = requests.post(url, data=data, verify=False).text
    print(resposta)
    return resposta
