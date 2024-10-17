%define _enable_debug_packages %{nil}
%define debug_package %{nil}

# svn co http://svn.opensync.org/multisync/branches/multisync-gui-0.2X multisync-gui
%define svn	384

Summary:	Graphical front end to OpenSync synchronization system
Name:		multisync-gui
Version:	0.91.1
Release:	0.%{svn}.4
License:	GPLv2+
Group:		Communications
Url:		https://www.opensync.org
Source0:	%{name}-svn%{svn}.tar.bz2
BuildRequires:	imagemagick
BuildRequires:	python
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(opensync-1.0) < 0.30
BuildRequires:	pkgconfig(sqlite3)

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM
data between programs on your computer and other computers, mobile devices,
PDAs or cell phones. It relies on the OpenSync framework to do the actual
synchronisation.

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-0.2X
echo "env.Append(CCFLAGS = '%{optflags}')" >> SConstruct

%build
./configure --prefix=%{_prefix}
%make

%install
%makeinstall_std

# menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Comment=Calendar synchronization program
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
Categories=GTK;TelephonyTools;Utility;
Icon=%{name}
EOF

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{64x64,48x48,32x32,16x16}/apps
install -m 0644 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 48 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

