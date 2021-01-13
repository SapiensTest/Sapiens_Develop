from selenium import webdriver
import time
import pandas as pd

def func1(var1, var2):
    pass

def func2(var1, var2):
    pass

def func3(var1, var2, var3):
    pass

def func4(var1, var2, var3):
    pass

driver = webdriver.Chrome("D:\Work\Web Scraping\chromedriver_win32 (1)\chromedriver.exe")
df = pd.read_csv(r'D:\Work\Web Scraping\export.csv',encoding = 'cp1252')
df = df.dropna(how='all', axis=1)
df.dropna(subset=['HOUSE_NR', 'STREET_NAME'],inplace = True)
#df['ZIP']=df['ZIP'].fillna(0)
#df['ZIP']=df['ZIP'].astype(int)
df['Com']= df["HOUSE_NR"].astype(str)+" "+df["STREET_NAME"].astype(str)+" "+df['CITY_NAME'].astype(str)+' '+df['PROVINCE_NAME'].astype(str)
df = df.head()
#df = df.iloc[539:1001]
final_list=[]
for row in df['Com']: 
    try:
        Input_Address=row.replace('nan','')
        driver.maximize_window()
        driver.set_page_load_timeout(100)
        driver.get("http://www.domain.com.au/")
        driver.implicitly_wait(5)
        prop = driver.find_element_by_xpath('//*[@id="fe-pa-domain-home-typeahead-input"]')
        prop.send_keys(Input_Address)
        driver.find_element_by_xpath("//div[@data-testid = 'search-bar-desktop']//span[text() ='Search']").click()
        time.sleep(10)
        records = int(driver.find_element_by_xpath('//*[@id="skip-link-content"]/div[1]/div[1]/h1').text.split()[0])
        if records >0:
            Result_add = driver.find_elements_by_tag_name('h2')
            #driver.implicitly_wait(5)
            l=[]
            for i in Result_add:
                l.append(i.text)
            final_list.append(l)
        else:
            final_list.append("No Records")
    except:
        pass
df_new = pd.DataFrame(final_list,columns =['Output'])
df_in = df['Com']
df_final = pd.concat([df_in,df_new],axis=1)
df_final.to_csv(r'D:\Work\Web Scraping\Output.csv')
#Result_add = driver.find_element_by_xpath('//*[@id="skip-link-content"]/div[1]/div[2]/ul/li[2]/div/div[2]/div/a/h2').text
#print(Result_add)
#print(Input_Address)

driver.close()

#D:\Work\Web Scraping\chromedriver_win32\chromedriver.exe
# multiple results 
# 0 properties detect
#//*[@id="skip-link-content"]/div[1]/div[1]/h1
