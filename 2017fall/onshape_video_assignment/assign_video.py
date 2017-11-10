# 從 urllib 模組中導入 urlopen
from urllib.request import urlopen
# 從 bs4 模組中導入 BeautirulSoup
from bs4 import BeautifulSoup
# 從 random 模組導入 shuffle
from random import shuffle

# 將要取出影片連結的網站 url,  放入數列中, 取名為 sources
sources = ['https://www.onshape.com/videos/topic/tech-tips', 'https://www.onshape.com/videos/topic/intro-to-cad', 'https://www.onshape.com/videos/topic/tutorials', 'https://www.onshape.com/videos/topic/essential-training', 'https://www.onshape.com/videos/topic/drawings']

#tech-tips (60)
#intro-to-cad (26)
#tutorials (14)
#essential-training (6)
#drawings (5)

# 按照網頁中的影片數計算, 共有 111 部影片, 但分類中可能重複
#print(60+26+14+6+5)

# 設 links 變數與空數列對應
links = []
# 利用 for 迴圈一一取出各網頁的 html 後, 進行解讀
# 只取出有 videos 與 https 連結的資料, 但避開 all 與 topic 類別連結
for url in sources:
    file = urlopen(url)
    # 因為 urlopen 出來的資料為二位元檔案, 若要讀出列印
    # 必須要先 decode() 為字串
    #print(file.read().decode())
    # 使用 html 解讀各連結的網頁內容
    soup = BeautifulSoup(file, 'html.parser')
    # 利用 Beautifulsoup 物件中的 find_all 方法尋找 anchor
    for link in soup.find_all('a', href=True):
        # 從各 anchor 資料篩選所需的影片連結
        if ('videos' or 'https') in link['href']:
            if 'all' not in link['href']:
                if 'topic' not in link['href']:
                    links.append(link['href'])
                    
# 為避免列出重複資料, 將數列轉為集合後, 再轉回數列
video_list = list(set(links))
shuffle(video_list)
r_video_list = list(reversed(video_list))
# 逐一列出所取得的影片連結
#for i in range(len(video_list)):
    #print(i+1, video_list[i])
#讀取兩班學員學號名單
with open('2a_student_list.txt') as f:
    a_stud_list = f.read().splitlines()
f.closed
#print(a_stud_list )
# 每人取兩個影片, 一個從最前面取, 一個反向取連結

print("甲班 Onshape 影片分配名單:")
print()
for i in range(len(a_stud_list)):
    print("  *  "+str(a_stud_list[i]))
    print("  *  ["+str(video_list[i])+"]")
    print("  *  ["+str(r_video_list[i])+"]")

with open('2b_student_list.txt') as f:
    b_stud_list = f.read().splitlines()
f.closed

print()
print("乙班 Onshape 影片分配名單:")
print()
for i in range(len(b_stud_list)):
    print("  *  "+str(b_stud_list[i]))
    print("  *  ["+str(video_list[i])+"]")
    print("  *  ["+str(r_video_list[i])+"]")
#print(b_stud_list )