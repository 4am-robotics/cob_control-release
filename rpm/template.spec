Name:           ros-melodic-cob-twist-controller
Version:        0.7.7
Release:        1%{?dist}
Summary:        ROS cob_twist_controller package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python2-devel
Requires:       boost-python3-devel
Requires:       eigen3-devel
Requires:       ros-melodic-cmake-modules
Requires:       ros-melodic-cob-control-msgs
Requires:       ros-melodic-cob-frame-tracker
Requires:       ros-melodic-cob-srvs
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-kdl-conversions
Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-orocos-kdl
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rviz
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf-conversions
Requires:       ros-melodic-topic-tools
Requires:       ros-melodic-trajectory-msgs
Requires:       ros-melodic-urdf
Requires:       ros-melodic-visualization-msgs
Requires:       ros-melodic-xacro
BuildRequires:  boost-devel
BuildRequires:  boost-python2-devel
BuildRequires:  boost-python3-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-cob-control-msgs
BuildRequires:  ros-melodic-cob-srvs
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-kdl-conversions
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-orocos-kdl
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf-conversions
BuildRequires:  ros-melodic-trajectory-msgs
BuildRequires:  ros-melodic-urdf
BuildRequires:  ros-melodic-visualization-msgs

%description
The main purpose of the cob_twist_controller is to convert target twists into
joint velocities. Therefore it makes use of several implemented inverse
kinematics approaches at the first order differential level. The inverse
differential kinematics solver considers kinematic chain extensions, singularity
robustness, redundancy resolution and priority-based methods. To avoid hardware
destruction there is a limiter interface active as well. Via parameter server
users can dynamically configure the solving strategy.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Aug 06 2019 Felix Messmer <felixmessmer@gmail.com> - 0.7.7-1
- Autogenerated by Bloom

