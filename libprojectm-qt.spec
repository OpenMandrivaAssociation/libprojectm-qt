%define oname projectM-qt

%define devellibname %mklibname -d projectm-qt
%define libname %mklibname projectm-qt


%rename		projectm-qt
Name:		libprojectm-qt
Version:	2.1.0
Release:	1
Summary:	The Qt frontend to the projectM visualization plugin
Group:		System/Libraries
License:	GPLv2+
URL:		http://projectm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/projectm/%{version}/%{oname}-%{version}-Source.tar.gz
BuildRequires:	cmake qt4-devel pkgconfig(libprojectM) = %{version}
Patch0:		libsuffix.patch

%description
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.


%package -n %libname
Summary: %summary
Group:  System/Libraries

%description -n %libname
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.


%package -n	%{devellibname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release} libprojectm-devel qt-devel
Provides:	projectm-qt-devel

%description -n	%{devellibname}
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}-Source
%patch0 -p1

%build
%cmake
%make


%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.*
%{_datadir}/pixmaps/prjm16-transparent.svg

%files -n %{devellibname}
%doc ReadMe
%{_includedir}/lib%{oname}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
