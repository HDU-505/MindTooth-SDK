# Mindtooth-SDK说明

## 文件构成

Mindtooth的SDK是已经打包好的exe文件以及相关的动态链接库dll文件，其主要作用是与硬件设备的通信及数据交换；

- `eegAmpController.exe`可执行文件是主要的SDK文件，其余dll是依赖文件；

- 各bat文件是相应的运行脚本；
- `command_server.py`是用于向设备发送相关指令的脚本（主要包含阻抗检测`calibration`和数据获取指令`acquisition`）[方式是通过websocket连接至该server，并传输对应指令触发SDK切换模式，使用字符串传输即可]
- `config.cfg`是设备的相关配置文件，其中主要包含采样率的设置之类的（这部分也是需要上层可以修改的）

- `lsl.dll`文件是SDK与上层应用的通信协议，该协议是公开协议，相关信息可以查阅资料
- 补充：bsr文件夹内包含完整的mindtooth设备体系的全套应用代码（可作为参考），SDK文件夹是提取出的核心文件（精简版）

## SDK数据格式

### 阻抗数据

- 命令：`calibration`

- 数据格式：[GND,REF,CH01,CH02...CH08,0,timestamp]，其中GND,REF为参考电极，CH01~CH08是数据通道，0为阻抗模式的标志位，timestamp是LSL的同步时间戳；

- eg:

  ![脑电示例](./images/脑电示例.png)
  =======
### 脑电数据

- 命令：`acquisition`

- 数据格式：[CH01,CH02...CH08,1,timestamp]，脑电模式没有REF和GND的数据；脑电模式的标志位是1；其他同上;

- eg:

  ![阻抗示例](./images/阻抗示例.png)
  =======
## SDK使用说明

1. 打开设备电源开关
2. 运行comand_server.py服务器

![comand_server_example](./images/comand_server_example.png)

3. 运行Apps/EegAmpApp/eegAmpController.exe文件，此为SDK核心文件

![sdk_example](./images/sdk_example.png)
=======
4. 等待设备搜索

5. 测试方式：通过连接`ws://127.0.0.1:8888/websocket/w`服务器，发送相关指令，并监听特定LSL流获取数据

6. 后续系统通过LSL与SDK链接

注：对于LSL数据流的信息可以通过find_lsl_stream.py脚本进行查看，如下图所示。

![find_lsl_stream_example](./images/find_lsl_stream_example.png)
=======

**注2：通过观察发现指令也是通过LSL流发送的，所以可以在系统中取出Websocket这一层，直接使用LSL发送指令，但需注意SDK只有在检测到有Command LSL流后才会开始工作；**

# 范式数据接入说明

目前范式的标签信息接入方式采用socket（C/S）方式接入，其中上层需要监控固定端口，范式内的脚本会自动连接到对应的端口并传输相应的标签信息（标签指的是被试人员与范式的交互动作标签，比如答题结果、按键操作信息等）

正式商业版的范式会采用`psychopy`编写（开源软件），其内核采用python脚本；