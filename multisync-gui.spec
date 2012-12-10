# svn co http://svn.opensync.org/multisync/branches/multisync-gui-0.2X multisync-gui
%define svn	384
%if %svn
%define release		%mkrel 0.%svn.2
%define distname	%name-svn%svn.tar.lzma
%define dirname		%name-0.2X
%else
%define release		%mkrel 4
%define distname	%name-%version.tar.bz2
%define dirname		%name-%version
%endif

Name: 		multisync-gui
Version: 	0.91.1
Release: 	%{release}
Summary: 	Graphical front end to OpenSync synchronization system
URL:		http://www.opensync.org
License:	GPLv2+
Group:		Communications
Source0:	%{distname}
BuildRequires:	libxml2-devel
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	sqlite3-devel
BuildRequires:	python
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM
data between programs on your computer and other computers, mobile devices,
PDAs or cell phones. It relies on the OpenSync framework to do the actual
synchronisation.

%prep
%setup -q -n %{dirname}
echo "env.Append(CCFLAGS = '$RPM_OPT_FLAGS')" >> SConstruct

%build
./configure --prefix=%{_prefix}
%make

%install
rm -fr %{buildroot}
%makeinstall_std

# menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Comment=Calendar synchronization program
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
Categories=GTK;TelephonyTools;Utility;
Icon=%{name}
EOF

# delete the upstream one as it sucks
rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{64x64,48x48,32x32,16x16}/apps
install -m 0644 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 48 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 misc/multisync.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.91.1-0.384.2mdv2011.0
+ Revision: 620420
- the mass rebuild of 2010.0 packages

* Fri Aug 07 2009 Emmanuel Andry <eandry@mandriva.org> 0.91.1-0.384.1mdv2010.0
+ Revision: 411221
- New svn snapshot

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.91.1-0.308.2mdv2009.1
+ Revision: 350230
- 2009.1 rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.91.1-0.308.1mdv2009.0
+ Revision: 253359
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.91.1-0.308.1mdv2008.1
+ Revision: 187624
- fix icon name in icon install commands
- fd.o icons
- new license policy
- clean spec
- bump to current SVN snapshot of OpenSync 0.2 branch

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - package renaming
    - rename the package to multisync-gui
      drop private version of msynctool
      drop useless patches
      drop useless icons
      use herein document for menu entry rather than external sources

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.91.0-1mdv2008.0
+ Revision: 80380
- Change group
- Add BR
- Add libglade
- Add Python
- Add dos2unix
- New release 0.91.0
- Import multisync

