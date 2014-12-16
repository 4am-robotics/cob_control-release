Name:           ros-indigo-cob-hardware-interface
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS cob_hardware_interface package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-brics-actuator
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-brics-actuator
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-sensor-msgs

%description
This package implements the cob_hardware_interface. The interface uses topic
communication rather than direct pointer access to the drivers. I.e. it publishs
the desired velocity to a topic and reads from the /joint_states topic. Thus, it
can be used for both velocity-controlled real hardware as well as velocity-
controlled simulation (i.e. using the JointVelocityControllers)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Dec 16 2014 Felix Messmer <fxm@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Felix Messmer <fxm@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Felix Messmer <fxm@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Felix Messmer <fxm@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

