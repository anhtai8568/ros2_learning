# ROS 2 & Autonomous Robot – Lộ trình học 12 tuần

Repo ghi lại quá trình học ROS 2 và xây dựng robot tự hành, từ Terminal Linux đến một robot omni 4 bánh tự định vị, lập bản đồ và đi tới đích trong mô phỏng.

**Môi trường:** Ubuntu 24.04 · ROS 2 Jazzy · Gazebo Harmonic · Python 3.12

**Cấu trúc:** 12 tuần, mỗi tuần 6 ngày học. Mỗi ngày khoảng 2 giờ, tổng khoảng 10–12 giờ mỗi tuần.

---

## Tiến độ

| Tuần | Chủ đề | Trạng thái |
|:---:|---|---|
| 1 | Làm quen Ubuntu 24.04 & Terminal | ✅ Đã hoàn thành |
| 2 | Tiến trình, quyền, gói phần mềm, Bash và Git | 🔄 Đang học |
| 3 | Python cho ROS 2 và toán cơ bản | ⏳ Chưa học |
| 4 | ROS 2 Jazzy: Node, Topic, Workspace | ⏳ Chưa học |
| 5 | Service, Action, Parameter, Launch | ⏳ Chưa học |
| 6 | TF2, Bag, Debug và Kiểm tra giữa kỳ 1 | ⏳ Chưa học |
| 7 | Gazebo Harmonic và URDF/Xacro | ⏳ Chưa học |
| 8 | Robot omni 4 bánh: động học và cảm biến | ⏳ Chưa học |
| 9 | SLAM: tạo bản đồ | ⏳ Chưa học |
| 10 | Định vị AMCL và Nav2 | ⏳ Chưa học |
| 11 | Tránh vật cản, tinh chỉnh Nav2 và Kiểm tra giữa kỳ 2 | ⏳ Chưa học |
| 12 | Đa bản đồ (multi-map) và dự án cuối | ⏳ Chưa học |

### Đầu ra từng tuần

| Tuần | Đầu ra |
|:---:|---|
| 1 | Cây thư mục `ros2_ws/src`; file `ghi_chu.txt`; báo cáo tuần 1 |
| 2 | Script `setup.sh` tự tạo workspace; alias; repo Git có commit đầu tiên |
| 3 | Chương trình `RobotState`; hàm tính quãng đường và góc quay |
| 4 | Package ROS 2 đầu tiên có talker/listener |
| 5 | Package có service, action, parameter và launch file chạy 3 node |
| 6 | Node phát TF; bag đã ghi và phát lại; điểm kiểm tra giữa kỳ 1 |
| 7 | Package `robot_description`; robot hiện trong RViz2 và Gazebo |
| 8 | Robot omni chạy bằng teleop, có odom và LiDAR |
| 9 | Bản đồ phòng (`.yaml` và `.pgm`) |
| 10 | Robot tới được goal đầu tiên |
| 11 | Bảng so sánh 3 bộ tham số; điểm kiểm tra giữa kỳ 2 |
| 12 | Demo, số liệu và báo cáo cuối khóa |

---

## Chi tiết theo tuần

### Tuần 1: Làm quen Ubuntu 24.04 & Terminal ✅

**Mục tiêu:** Đi lại, tạo, xem, xóa file bằng terminal; hiểu shell, PATH, quyền cơ bản.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Terminal, shell, đường dẫn | `pwd`, `ls`, `ls -la`, `cd`, `cd -`; đi qua `/`, `/home`, `/etc`, `/opt` | Đường dẫn tuyệt đối khác tương đối ở điểm nào? |
| 2 | Shell tìm lệnh: PATH và biến môi trường | `which ls`, `echo $PATH`, `echo $HOME`; thử biến có và không có `export` | Vì sao biến mất khi đóng terminal? |
| 3 | Quyền truy cập file | Tạo file, xem quyền, `chmod 750`, `chmod +x` | `-rw-r--r--` có chạy được `./setup.sh` không? `chmod 750` cho ra quyền gì? |
| 4 | Tra cứu và thao tác file | `man ls`, `cp a.txt c.txt`, `mv b.txt d.txt`, `rm a.txt` | Sau ba lệnh trên còn những file nào? |
| 5 | Xem file và chuyển hướng | `mkdir -p ros2_ws/src`, `echo >` và `>>`, `cat`, `head`, `tail` | `mkdir` có và không có `-p` khác nhau thế nào? |
| 6 | Ôn tập, kiểm tra, báo cáo | Kiểm tra 20 phút (đã bỏ qua theo yêu cầu) | Sản phẩm: báo cáo tuần 1 (.docx) |

### Tuần 2: Tiến trình, quyền, gói phần mềm, Bash và Git 🔄

**Mục tiêu:** Quản lý tiến trình và gói, viết script bash đơn giản, dùng Git cơ bản.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Tiến trình (process) | `sleep 300 &`, `pgrep`, `kill`, `top`; `Ctrl+C` và `kill -9` | `Ctrl+C` khác `kill` ở điểm nào? |
| 2 | User, sudo, quyền sở hữu và apt | `sudo apt update`, `apt list --upgradable`; cài và gỡ `tree`; `chown` | `apt update` và `apt upgrade` khác nhau thế nào? |
| 3 | PATH, `.bashrc`, alias | Thêm `~/bin` vào PATH; tạo `alias ll='ls -la'` | Vì sao phải giữ `$PATH` ở cuối khi thêm đường dẫn? |
| 4 | Pipe, grep và công cụ lọc chữ | `ps aux \| grep sleep`, `ls /etc \| grep conf \| wc -l` | Đoán kết quả: `echo -e "b\na\nb" \| sort \| uniq` |
| 5 | Bash script: biến, if, for | Script in 5 dòng bằng `for`; script nhận tên thư mục qua `$1` | Script thiếu quyền `x` thì chạy thế nào? |
| 6 | Git cơ bản, `setup.sh`, ôn tập | Viết `setup.sh` tạo `~/ros2_ws/src`; `git init`, `commit` đầu tiên; kiểm tra 10–15 phút | Sản phẩm: `setup.sh`, repo Git, báo cáo tuần 2 |

### Tuần 3: Python cho ROS 2 và toán cơ bản ⏳

**Mục tiêu:** Viết được Python đủ dùng cho node ROS 2: hàm, class, callback; nắm góc, sin/cos, phép quay.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Python và môi trường | Tạo `venv`; tính chu vi bánh xe từ bán kính | Kiểu của `3`, `3.0` và `"3"` là gì? |
| 2 | List, dict, vòng lặp, if | Lưu 4 vận tốc bánh vào list, tính trung bình; dict tên bánh → vận tốc | Đoán kết quả của một đoạn `for` lồng `if` |
| 3 | Hàm và module | Viết `distance(v, t)` và `deg_to_rad`; tách hàm sang file riêng và `import` | Hàm không có `return` trả về gì? |
| 4 | Class và OOP | Class `RobotState` lưu `x`, `y`, `theta`; phương thức `move(dx, dy)` | `self` là gì? Vì sao mọi phương thức đều có nó? |
| 5 | Callback, lambda và toán cho robot | Hàm gọi callback sau mỗi bước vòng lặp; quay vector `(1, 0)` góc 90° bằng sin/cos | Quay `(1, 0)` góc 90° ra điểm nào? |
| 6 | Đọc hiểu C++, ôn tập, báo cáo | Hoàn thiện `RobotState`; quiz 10 câu | Sản phẩm: chương trình Python chạy đúng, báo cáo tuần 3 |

### Tuần 4: ROS 2 Jazzy: Node, Topic, Workspace ⏳

**Mục tiêu:** Cài ROS 2 Jazzy, hiểu ROS graph, viết publisher và subscriber bằng Python.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Cài ROS 2 Jazzy và chạy demo | Cài bằng apt; `source /opt/ros/jazzy/setup.bash`; chạy `talker` và `listener` | Vì sao terminal mới không thấy lệnh `ros2` nếu chưa source? |
| 2 | Node và ROS graph | `ros2 node/topic list/info/echo/hz`; `rqt_graph` | Ai publish, ai subscribe trong sơ đồ `rqt_graph`? |
| 3 | Message và interface | `ros2 interface show`; `ros2 topic pub` gửi thử; xem `geometry_msgs/msg/Twist` | `Twist` gồm những trường nào? |
| 4 | Workspace và package | Tạo `~/ros2_ws`, package `my_first_pkg` (`ament_python`); `colcon build` | `build`, `install`, `log` chứa gì? Có nên commit lên Git không? |
| 5 | Viết publisher bằng Python | Node talker publish chuỗi mỗi 0.5 giây; đo bằng `ros2 topic hz` | Timer 0.5 giây ra tần số bao nhiêu Hz? |
| 6 | Subscriber, ôn tập, báo cáo | Node listener in chuỗi nhận được; chạy hai node cùng lúc | Sản phẩm: package talker/listener, báo cáo tuần 4 |

### Tuần 5: Service, Action, Parameter, Launch ⏳

**Mục tiêu:** Biết khi nào dùng topic, service hay action; dùng parameter và launch file.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Service: khái niệm và dòng lệnh | Gọi service `add_two_ints` của demo; `ros2 service call` | Khi nào dùng service thay vì topic? |
| 2 | Service bằng Python | Viết server cộng hai số và client gọi nó (`call_async`) | Điều gì xảy ra nếu gọi service khi server chưa chạy? |
| 3 | Parameter | Node có tham số tốc độ, đổi bằng `ros2 param set`; nạp từ file YAML | Parameter khác biến môi trường ở điểm nào? |
| 4 | Action | Chạy demo Fibonacci action; viết action đếm đến N có phản hồi tiến độ | Vì sao đi tới điểm đến nên là action chứ không phải service? |
| 5 | Launch file | `LaunchDescription`, `Node`; truyền parameter và remap; launch 3 node | Launch file giúp ích gì so với mở 3 terminal? |
| 6 | Mini project, ôn tập, báo cáo | Hệ thống 3 node: cảm biến giả, xử lý, hiển thị; viết README cho package | Sản phẩm: package có launch và README, báo cáo tuần 5 |

### Tuần 6: TF2, Bag, Debug và Kiểm tra giữa kỳ 1 ⏳

**Mục tiêu:** Hiểu hệ tọa độ (frame) và công cụ debug, vì Nav2 dựa hoàn toàn vào TF.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | TF2: hệ tọa độ | Demo `turtle`; `view_frames` xem cây TF | Frame nào là cha của `base_link` trong robot di động? |
| 2 | Broadcaster TF | `static_transform_publisher`; phát TF từ `odom` tới `base_link` cho robot ảo | Static khác dynamic transform thế nào? |
| 3 | RViz2 và listener TF | Hiển thị robot ảo trong RViz2; `tf2_echo`; `tf2_ros` Buffer và Listener | Nếu Fixed Frame chọn sai thì có hiện tượng gì? |
| 4 | `ros2 bag` | `bag record`, `info`, `play`; phát lại và xem trong RViz2 | Phát lại bag có cần node publisher gốc không? |
| 5 | Công cụ debug | Mức log DEBUG/INFO/WARN/ERROR; `ros2 doctor`; cố tình gây 3 lỗi rồi sửa | Node publish nhưng subscriber không nhận: kiểm tra những gì? |
| 6 | Kiểm tra giữa kỳ 1 | Bài kiểm tra 90 phút: lý thuyết và viết code | Sản phẩm: bài kiểm tra, báo cáo tuần 6 |

### Tuần 7: Gazebo Harmonic và URDF/Xacro ⏳

**Mục tiêu:** Mô tả robot bằng URDF/Xacro và đưa robot vào world Gazebo Harmonic.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Kiến trúc Gazebo Harmonic | Chạy world mẫu; `gz topic -l` | Gazebo và ROS 2 là hai chương trình riêng, vậy nối chúng bằng gì? |
| 2 | World SDF cơ bản | Viết world có sàn, 4 tường, 2 vật cản; chạy bằng `gz sim` | Link và joint trong SDF khác trong URDF ở đâu? |
| 3 | URDF cơ bản | Dựng thân robot hình hộp (`link`, `joint`, `visual`, `collision`) | `visual` và `collision` khác nhau thế nào? |
| 4 | Inertial và Xacro | Macro tạo một bánh, gọi 4 lần, `xacro` thành URDF | Vì sao nên dùng macro cho bốn bánh? |
| 5 | Đưa robot vào Gazebo | `ros_gz_sim create`; `ros_gz_bridge` nối topic; bridge topic `clock` | `use_sim_time = true` để làm gì? |
| 6 | Launch tổng hợp, ôn tập, báo cáo | Một lệnh launch chạy Gazebo + robot + RViz2 | Sản phẩm: package `robot_description`, báo cáo tuần 7 |

### Tuần 8: Robot omni 4 bánh: động học và cảm biến ⏳

**Mục tiêu:** Hiểu vì sao omni di chuyển ngang được và điều khiển robot trong Gazebo bằng `cmd_vel`.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Bánh omni và kiểu bố trí | Vẽ sơ đồ bố trí bánh (kiểu X và `+`) và chiều quay | Robot omni đi ngang bằng cách nào? |
| 2 | Động học ngược | Viết hàm Python đổi `(vx, vy, ω)` thành 4 vận tốc bánh; kiểm tra tiến, ngang, xoay tại chỗ | Khi chỉ có `vy`, các bánh quay thế nào? |
| 3 | Điều khiển omni trong Gazebo | Đưa vận tốc vào Gazebo qua `cmd_vel` và bridge; `ros2 topic pub`; chỉnh khối lượng, ma sát | `Twist.linear.y` có ý nghĩa với robot omni không? |
| 4 | Teleop và odometry | `teleop_twist_keyboard`; vẽ quỹ đạo odom; so sánh với lệnh đã gửi | Vì sao odometry bị trôi theo thời gian? |
| 5 | LiDAR trong Gazebo | Thêm LiDAR vào robot; bridge `/scan` (`LaserScan`); xem trong RViz2 | `LaserScan` có những trường nào? |
| 6 | Kiểm chứng, ôn tập, báo cáo | Robot đi hình vuông, đo sai số điểm cuối | Sản phẩm: video hoặc ảnh, bảng kiểm tra, báo cáo tuần 8 |

### Tuần 9: SLAM: tạo bản đồ ⏳

**Mục tiêu:** Dựng bản đồ bằng LiDAR trong Gazebo và lưu lại để dùng sau.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Nguyên lý SLAM | Xem một bản đồ mẫu trong RViz2 | Ba giá trị của một ô occupancy grid là gì? |
| 2 | Cài đặt `slam_toolbox` | Chạy `slam_toolbox` (online async); kiểm tra TF trước khi chạy | Vì sao SLAM không chạy nếu thiếu TF odom? |
| 3 | Dựng bản đồ | Lái robot quét hết world phòng, đi chậm và đi vòng lại | Vì sao quay nhanh làm bản đồ xấu? |
| 4 | Lưu và nạp bản đồ | `map_saver_cli`; mở lại bằng `map_server` | Độ phân giải 0.05 nghĩa là gì? |
| 5 | Chất lượng bản đồ | Chỉnh tham số, dựng lại bản đồ và so sánh | Nêu hai nguyên nhân bản đồ bị lệch |
| 6 | Hoàn thiện, ôn tập, báo cáo | Bản đồ phòng hoàn chỉnh | Sản phẩm: `.yaml` và `.pgm`, báo cáo tuần 9 |

### Tuần 10: Định vị AMCL và Nav2 ⏳

**Mục tiêu:** Robot định vị trên bản đồ có sẵn và tự đi tới điểm đến.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Định vị và AMCL | Chạy `map_server` và AMCL; đặt initial pose trong RViz2 | Frame `map` và `odom` khác nhau thế nào? |
| 2 | AMCL với robot omni | Lái robot, quan sát đám hạt hội tụ | Vì sao chọn mô hình Omni thay vì DiffDrive? |
| 3 | Kiến trúc Nav2 | Vẽ sơ đồ Nav2 bằng lời: planner, controller, costmap, behavior tree | Planner và controller khác nhau thế nào? |
| 4 | Cấu hình Nav2 cho robot omni | Sửa `nav2_params.yaml`: controller holonomic, kích thước robot | Footprint của robot dùng để làm gì? |
| 5 | Chạy Nav2, gửi goal | Gửi goal trong RViz2; đọc log khi robot không đi | Nếu robot đứng im, kiểm tra những gì đầu tiên? |
| 6 | Goal bằng code, ôn tập, báo cáo | Python gửi goal bằng action `NavigateToPose` | Sản phẩm: robot tới goal, báo cáo tuần 10 |

### Tuần 11: Tránh vật cản, tinh chỉnh Nav2 và Kiểm tra giữa kỳ 2 ⏳

**Mục tiêu:** Hiểu costmap, tinh chỉnh tham số và đo hiệu quả điều hướng bằng số liệu.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Costmap và các lớp | Xem global và local costmap trong RViz2; obstacle layer, inflation layer | Inflation layer giúp gì cho an toàn? |
| 2 | Vật cản trong mô phỏng | Đặt vật cản trong Gazebo, quan sát đường đi | Vì sao local costmap cập nhật nhanh hơn global? |
| 3 | Tham số planner và controller | Thay đổi từng tham số (tốc độ, gia tốc, dung sai goal), ghi lại hiện tượng | Tăng tốc độ tối đa có thể gây hậu quả gì? |
| 4 | Chỉ số đánh giá | Viết script ghi thời gian, quãng đường, số va chạm, tỉ lệ thành công | Vì sao cần chạy nhiều lần? |
| 5 | Thí nghiệm 3 bộ tham số | Chạy mỗi bộ ít nhất 5 lần, lập bảng | Bộ nào tốt nhất và vì sao? |
| 6 | Kiểm tra giữa kỳ 2 | Bài kiểm tra 90 phút: thực hành và lý thuyết | Sản phẩm: bài kiểm tra, báo cáo tuần 11 |

### Tuần 12: Đa bản đồ (multi-map) và dự án cuối ⏳

**Mục tiêu:** Robot đi A → B → C qua nhiều zone, mỗi zone một bản đồ, và đánh giá việc chuyển bản đồ.

| Ngày | Chủ đề | Thực hành | Câu hỏi cuối ngày / sản phẩm |
|:---:|---|---|---|
| 1 | Khái niệm đa bản đồ | Vẽ sơ đồ 3 zone và điểm chuyển giữa các zone | Khi đổi map, robot cần biết điều gì để định vị lại? |
| 2 | Dựng thế giới 3 zone | Xây world 3 zone có hành lang nối trong Gazebo | Điểm chuyển giữa hai zone nên đặt ở đâu? |
| 3 | Dựng bản đồ từng zone | Chạy SLAM cho từng zone, lưu 3 bản đồ | Vùng chồng lấn giữa hai map giúp gì? |
| 4 | Cơ chế chuyển bản đồ | Viết node quản lý map, gọi dịch vụ nạp map, đặt lại initial pose | Điều gì xảy ra nếu quên đặt lại initial pose? |
| 5 | Mission A → B → C | Chạy 5 lần, ghi thời gian chuyển map, sai số, tỉ lệ thành công | Chỉ số nào cho biết chuyển map tốt? |
| 6 | Báo cáo cuối khóa và vấn đáp | Viết báo cáo, quay demo | Sản phẩm: báo cáo cuối khóa (.docx), vấn đáp |

---

## Ghi chú

- Nội dung từng ngày có thể điều chỉnh theo tốc độ học; sẽ đánh giá lại sau mỗi tuần.
- Tên gói, topic và tham số cụ thể của Nav2 và `ros_gz` sẽ được kiểm tra lại theo phiên bản Jazzy / Harmonic trước khi học từng tuần.
- Node.js và web học ROS 2 không nằm trong 12 tuần này; có thể làm sau tuần 12.
- Phần cứng thật (Raspberry Pi 5, ESP32, LiDAR) chỉ đưa vào khi đã có thiết bị.

---

## Cấu trúc repo

```
ros2_learning/
├── README.md                  # Lộ trình này
├── notes/                     # Lộ trình chi tiết (.docx)
├── week_03_python/            # Bài tập Python tuần 3
├── week_04_ros2_core/         # ROS 2 core
├── week_05_services_actions/  # Service, action
├── week_06_tf_debug/          # TF2, bag, debug
├── week_07_urdf_gazebo/       # URDF, Gazebo
├── week_08_omni_robot/        # Robot omni
├── week_09_slam/              # SLAM
├── week_10_navigation/        # Nav2
├── week_11_obstacle_avoidance/# Tránh vật cản
└── week_12_multi_map/         # Đa bản đồ, dự án cuối
```
