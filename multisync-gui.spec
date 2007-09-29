%define name 	multisync-gui
%define version 0.91.0
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Tool to synchronize PIM data on many devices
URL:		http://www.opensync.org
License:	GPL
Group:		Communications
Source:		%{name}-%{version}.tar.bz2
Patch:	    multisync-gui-0.91.0-icon-path.patch
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  libxml2-devel
BuildRequires:	libopensync-devel
BuildRequires:  libopensync-plugin-evolution2-devel
BuildRequires:	libgnomeui2-devel libglade2.0-devel
BuildRequires:	sqlite3-devel
BuildRequires:  python
BuildRequires:  desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM
data between programs on your computer and other computers, mobile devices,
PDAs or cell phones. It relies on the OpenSync framework to do the actual
synchronisation.

%prep
%setup -q
%patch0 -p0
echo "env.Append(CCFLAGS = '$RPM_OPT_FLAGS')" >> SConstruct

%build
./configure --prefix=%{_prefix} -v
%make

%install
rm -fr %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=multisync-gui
Comment=Calendar synchronization program
Exec=multisync-gui
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
Icon=multisync-gui
EOF

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*
  
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/multisync-gui
%{_datadir}/multisync-gui
%{_datadir}/pixmaps/multisync-gui
%{_datadir}/applications/multisync-gui.desktop
