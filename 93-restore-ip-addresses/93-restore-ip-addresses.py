class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def isvalid(ip):
            if len(ip) >=2 and ip[0]=='0':
                return False
            if not (0 <= int(ip) <= 255):
                return False
            
            return True
        def search(index,curr):
            if index>=len(s) and len(curr)==4:
                result.append('.'.join(curr))
                return
            for j in range(index,len(s)):
                ip=s[index:j+1]
                if isvalid(ip):
                    curr.append(ip)
                    search(j+1,curr)
                    curr.pop()
        search(0,[])
        return result