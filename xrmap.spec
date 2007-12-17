%define name xrmap
%define version 2.33
%define release %mkrel 2

Summary: A tool to manipulate and create images of Earth
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Geosciences
Source: ftp://ftp.ac-grenoble.fr/ge/geosciences/xrmap/%{name}-%{version}.tar.bz2
URL: http://freshmeat.net/projects/sunclock/

Buildrequires:	X11-devel imake
BuildRequires:	bzip2-devel
BuildRequires:  png-devel
BuildRequires:  jpeg-devel


%description
The Xrmap package is derived from the rmap package by Reza Naima
   (http://www.reza.net/rmap/ )
It provides a user-friendly X client for manipulating the CIA
World data bank II global vector information and for generating images 
of the Earth. The images can be very accurately zoomed in, up to a 
factor of 100 or more.
Xrmap does have many more features than the original command line program
'rmap', especially it implements Rectangular, Mercator and Miller 
projections in addition to the Spherical projection, as well as reverse 
search of coordinates.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
perl -pi -e "s,/usr/X11R6/lib ,%{_libdir} ," earthview/Makefile

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

# %install
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}
make install.man DESTDIR=$RPM_BUILD_ROOT%{_prefix}

if [ -f $RPM_BUILD_ROOT/usr%_libdir/X11/doc/html/xrmap.1.html ]; then
mkdir -p $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/
mv $RPM_BUILD_ROOT%{_prefix}%_libdir/X11/doc/html/xrmap.1.html $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/doc/html/xrmap.1.html
rm -rf $RPM_BUILD_ROOT%{_prefix}/usr/
fi

mkdir -p $RPM_BUILD_ROOT%_datadir/icons
install xrmap.xpm -m 644 $RPM_BUILD_ROOT%_datadir/icons/xrmap.xpm
install editkit/emx $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/{anthems,examples,extra}
#install anthems/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/anthems
#install examples/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/examples
#install extra/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/extra

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/factbook/{extra,text}
#install factbook/extra/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/factbook/extra
#install factbook/text/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/factbook/text

#mkdir -p $RPM_BUILD_ROOT%_datadir/rmap/flags/{big,small}
#install flags/big/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/flags/big
#install flags/small/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/flags/small

#mkdir -p $RPM_BUILD_ROOT/usr/share/rmap/hymns
#install hymns/* -m 644 $RPM_BUILD_ROOT/usr/share/rmap/hymns

mkdir -p $RPM_BUILD_ROOT/usr/share/rmap/tools/{anthems,cbd2else,factbook,jpd2else,locutils,rez2else,upgrade}
install tools/anthems/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/anthems
install tools/cbd2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/cbd2else
install tools/factbook/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/factbook
install tools/jpd2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/jpd2else
install tools/locutils/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/locutils
install tools/rez2else/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/rez2else
install tools/upgrade/* -m 644 $RPM_BUILD_ROOT%_datadir/rmap/tools/upgrade

mkdir -p %buildroot%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Categories=Education;Science;Geology;        
Name=Xrmap        
Comment=Manipulate and create images of Earth        
Exec=%{name}        
Icon=toys_section
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc CHANGES INSTALL midi_cfg/* tools/README.tools LICENSE MAPEDIT README TODO VECTORMAP
%{_datadir}/icons/xrmap.xpm
%{_datadir}/rmap
%{_datadir}/editkit
%{_prefix}/X11R6/bin/earthview
%{_prefix}/X11R6/bin/emx
%{_prefix}/X11R6/bin/xrmap
%{_prefix}/X11R6/man/man1/xrmap.1*
%{_prefix}/X11R6/man/man1/emx.1*
%{_datadir}/applications/mandriva-*.desktop

