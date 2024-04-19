https://www.reddit.com/r/linux4noobs/comments/12mittk/any_way_i_can_use_a_browser_without_a_desktop/
 


我不想安装完整的ubuntu 桌面系统, 只使用最简单的方法打开firefox浏览器


sudo apt update
sudo apt install xinit xorg openbox firefox -y

轻量级的窗口管理器，比如Openbox
Xorg是Ubuntu默认的图形界面支持系统
xinit 是一个用于启动X Window System的程序。它是一个简单的脚本，用于初始化X服务器并运行一个或多个X客户端程序。xinit 通常被更高级的脚本（如 startx）或显示管理器（如gdm, lightdm, sddm等）所使用，这些脚本和程序为用户提供了一个完整的图形会话







vim ~/.xinitrc
exec openbox-session &
exec firefox


startx






==========================================================================================================================================================================================================================


curl -i http://localhost:8000/gethostIp


firefox 打开http页面





firefox http://127.0.0.1:8000/


