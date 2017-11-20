# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 18:16:27 2017

@author: lx
"""

import sys
sys.path.append('..')

from common_packet import send_mail
from localhost_ip import get_my_ip
#获取文件中的IP
f = open('ip','r')
ip1 = f.readline()
f.close()
ip2 = get_my_ip()
if ip1 != ip2 :
    #发送邮件
    mailto_list=["mashuguo@171xue.com"]
    cc_list = ["mashuguo@171xue.com"]
    sub ="new ip is %s"%(ip2)

    send_mail.send_mail(mailto_list,cc_list ,sub, )
    print ("发送邮件")
    #更改文件IP中的内容
    f = open('ip','w')
    f.write(ip2)
    f.close()
    print ('新IP写入文件')
    pass    
else :
    pass 

