%define		snap 20040629
Summary:	Cal3D adapter for OpenSceneGraph
Summary(pl):	Adapter Cal3D dla OpenSceneGraph
Name:		osgcal
Version:	0.1.4
Release:	1.%{snap}.1
License:	LGPL
Group:		Libraries
# from cvs.gna.org/cvs/underware
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	d940588c9c74ab2812174cf5569c4967
# Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://osgcal.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
osgCal is an adapter of cal3d for use inside OpenSceneGraph, providing
a library and a nodekit that allow inserting new nodes in OSG with
animated characters.

%description -l pl
osgCal jest adapterem cal3d do wykorzystania wewn±trz OpenSceneGraph,
udostêpniaj±cym bibliotekê i wtyczki pozwal±ce wstawiaæ nowe obiekty
do OSG w animowanych postaciach.

%package devel
Summary:	Header files for osgcal library
Summary(pl):	Pliki nag³ówkowe biblioteki osgcal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for osgcal library.

%description devel -l pl
Pliki nag³ówkowe biblioteki osgcal.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CXXFLAGS="-I../../include -I../include %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

find $RPM_BUILD_ROOT%{_prefix} -name CVS -type d |xargs rm -fr

install -D %{name}.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/%{name}.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog *.txt
%attr(755,root,root) %{_libdir}/lib*.so
#%attr(755,root,root) %{_libdir}/osgPlugins/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/usage.txt
%{_includedir}/osgCal
%{_pkgconfigdir}/*.pc
