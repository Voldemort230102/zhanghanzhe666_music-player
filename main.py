import webview
print("Music Player 1.0.0")
print("By: KirinXuan和zhz")
print("源码重构")
print("核心技术: Pywebview，CSS3，JavaScript，HTML5，Python3")
print("特点：保持上一代加载速度快的特点，在此基础上更新UI，支持个性化，增加功能（修复一些Bug）")
def main():
    webview.create_window('Music Player', 'index.html')
    webview.start()

if __name__ == '__main__':
    main()