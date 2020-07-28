import  hashlib
##对于字符串进行MD5加密
def get_md5(content):
    md1 = hashlib.md5(content)
    return md1.hexdigest()

