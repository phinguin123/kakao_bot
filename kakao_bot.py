# import win32gui, win32con, win32api, schedule, time

# def send_talk():
#     win32api.SendMessage(chat,win32con.WM_SETTEXT, 0, cText) # 채팅창 입력
#     win32api.PostMessage(chat, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) 
#     win32api.PostMessage(chat, win32con.WM_KEYUP, win32con.VK_RETURN, 0) # 엔터키

# kakao = win32gui.FindWindow(None,"Jisoo Kim")
# chat = win32gui.FindWindowEx(kakao, None , "RICHEDIT50W" , None)  # 채팅창안 메세지 입력창 

# cText = "[알림bot]"


# schedule.every().day.at("04:10").do(send_talk)
# schedule.every(2).hours.do(send_talk)
# schedule.every(30).seconds.do(send_talk)

# # 학원
# schedule.every().day.at("19:50").do(send_talk)
# schedule.every().day.at("20:55").do(send_talk)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

import time, win32con, win32api, win32gui, schedule, time

# # 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = 'Jisoo Kim'


# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
    # hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    #win32api.PostMessage(hwndEdit, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) 
    #win32api.PostMessage(hwndEdit, win32con.WM_KEYUP, win32con.VK_RETURN, 0) # 엔터키
    SendReturn(hwndEdit)


# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# # 채팅방 열기
def open_chatroom(chatroom_name):
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "KakaoTalk")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    #win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    #win32api.PostMessage(hwndkakao_edit3, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) 
    win32api.PostMessage(hwndkakao_edit3, win32con.WM_KEYUP, win32con.VK_RETURN, 0) # 엔터키
    time.sleep(1)   # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)


def main():
    open_chatroom(kakao_opentalk_name)  # 채팅방 열기

    text = "[알림봇]"
    kakao_sendtext(kakao_opentalk_name, text)    # 메시지 전송


if __name__ == '__main__':
    schedule.every(10).seconds.do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

    