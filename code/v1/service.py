# import psutil

# def find_between_r( s, first, last ):
#     try:
#         start = s.rindex( first ) + len( first )
#         end = s.rindex( last, start )
#         return s[start:end]
#     except ValueError:
#         return ""

# if __name__ == "__main__":
#     s = psutil.phymem_usage()
#     s = str(s)
#     s = find_between_r(s,"percent=","used").strip().replace(",","")
#     s = float(s)
#     print s
#     if s > 95.0:
#         print 'Critical'
#     else:
#         print 'Cool'

import psutil 

s = psutilself.