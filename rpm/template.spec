Name:           ros-indigo-cob-base-velocity-smoother
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_base_velocity_smoother package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_base_velocity_smoother
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
The 'cob_base_velocity_smoother' reads velocity messages and publishes messages
of the same type for &quot;smoothed&quot; velocity to avoid shaking behavior.

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
* Mon Aug 31 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

* Mon Jun 22 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-5
- Autogenerated by Bloom

* Sun Jun 21 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-4
- Autogenerated by Bloom

* Sat Jun 20 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-3
- Autogenerated by Bloom

* Sat Jun 20 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-2
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-1
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Mirus <frm@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Thu Dec 18 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Thu Dec 18 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Dec 16 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Florian Mirus <frm@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Mirus <frm@ipa.fhg.de> - 0.5.4-2
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Mirus <frm@ipa.fhg.de> - 0.5.4-1
- Autogenerated by Bloom

* Tue Aug 26 2014 Florian Mirus <frm@ipa.fhg.de> - 0.5.4-0
- Autogenerated by Bloom

