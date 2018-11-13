from bs4 import BeautifulSoup
import requests

headers ={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Mobile Safari/537.36',
    'Cookie': 'TART=%1%enc%3AdM3RTHYCg6xI5Z0TXt0tQqDKaCwOTpkYmkkV9xbfnyJMGqMGomQBNW1KdDPLDnUe1ih3jKiMJWY%3D; TAUnique=%1%enc%3AEm4bmPTyg9%2FopmMr%2Ffl0OOVSWF5pokLoKMyBsw7gK0YBS27FZ6YVQQ%3D%3D; TASSK=enc%3AAHMn5V13ipPpojyFTL7%2F2v070iNtrIyprXn0BqrxBGvt7mF888a4zJcfg3dDdkps11WV30uhVS09TRJhGunCs61YBJgrfX%2FV6hXa8vX%2FpYSLtTJvTdKu1CVQxJOkEPdGgw%3D%3D; TAPD=tripadvisor.cn; _ga=GA1.2.1680043165.1532148506; _gid=GA1.2.328661753.1532148506; _smt_uid=5b52bb1b.a7c77e7; CommercePopunder=SuppressAll*1532148523376; ki_r=; TAAuth3=3%3Ae992d639fa1bc613ff5c3b9c5b1c6281%3AAFH8cShoBbKFDgW%2BEMU8uLlEzXaBI1TkifaierbG2pM5Bw0HlCa8enwhPf6Dej7g%2F1KnTet%2Fn%2BV226EEkND1zHwVduG5pFB5p9OmiD6h6XHPRKKm3m3Em6CL%2Bqf%2BxkCLfuRTHppLxXv1olmCXEt39br1KX4h4I0TVVo0%2F2JaBJKMvE%2Ffb9%2BNNhtVQalUQi16yw%3D%3D; ServerPool=X; TAReturnTo=%1%%2FAttractions-g60763-Activities-oa1140-New_York_City_New_York.html; ki_t=1532161367802%3B1532161367802%3B1532170114690%3B1%3B38; interstitialCounter=2; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; MobileLastViewedList=%1%%2FAttractions-g60763-Activities-oa1170-New_York_City_New_York.html; roybatty=TNI1625!ABFQ69nHF%2BZOHE75amLu0CS%2FDZcPRR3%2F3rpttIT%2F%2F%2FOQ02BVUxdn1jlwNaxxIyYrMDT6Qc7Xo8y9ZDKy%2BVxC2hIahEbPSXPpDkgl%2FFU9ARp5ujGhjyefxd%2F87EVRIiKtgDccET5SYpd8RXoNau6f6i3W%2FiedFThPHoNuqwX%2B5tO%2B%2C1; _gat_UA-79743238-4=1; TASession=%1%V2ID.1CC649B78B016902446BA7225FC84EBB*SQ.41*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*LS.DemandLoadAjax*GR.22*TCPAR.3*TBR.28*EXEX.79*ABTR.77*PHTB.51*FS.53*CPU.35*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.01A7FE36C783D030A3546E9691F7AA5C*FA.1*DF.0*FLO.60763*TRA.true*LD.60763; TATravelInfo=V2*AY.2018*AM.7*AD.29*DY.2018*DM.7*DD.30*A.2*MG.-1*HP.2*FL.3*DSM.1532171713299; TAUD=LA-1532148502527-1*RDD-1-2018_07_21*HC-19954*HDD-11851822-2018_07_29.2018_07_30*LD-23210753-2018.7.29.2018.7.30*LG-23210754-.0.F.'
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html'.format(str(i)) for i in range(0, 1171, 30)]#1170

def get_attractions(url,data=None):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, "lxml")

    titles = soup.select('div.title.titleLLR > div')
    imgs = soup.select('img[width="54"]')
    cates = soup.select('div.attraction_types > span')
    #print(imgs)
    if data == None:
        for title, img, cate in zip(titles, imgs, cates):
            data = {
                'title': title.get_text().replace('\n', ''),
                'img': img.get('src'),
                'cate': cate.get_text()
            }
            print(data)
    #print(data)

if __name__ == "__main__":
    #get_attractions(url)
   # aa = 0
   # for single_url in urls:
   #     time.sleep(1)
   #     aa = aa + 30
   #     get_attractions(single_url)
   #     print(aa)