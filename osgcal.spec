Summary:	Cal3D adapter for OpenSceneGraph
Summary(pl):	Adapter Cal3D dla OpenSceneGraph
Name:		osgcal
Version:	0.1.28
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.gna.org/underware/dists/%{name}-%{version}.tar.gz
# Source0-md5:	8953cf2792ebf186762a879214972843
Patch0:		%{name}-namespace.patch
URL:		http://osgcal.sourceforge.net/
BuildRequires:	OpenSceneGraph-devel
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
udostêpniaj±cym bibliotekê i wtyczki pozwalaj±ce wstawiaæ nowe obiekty
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
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CXXFLAGS="-I../../include -I../include %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_prefix} -name CVS -type d |xargs rm -fr

install -D %{name}.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/%{name}.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/osgCal
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.so
%{_libdir}/lib*.la

#%{_libdir}/lib*.a
