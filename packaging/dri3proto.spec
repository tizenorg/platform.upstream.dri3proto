%bcond_with x

Name:     dri3proto
Summary:  X.Org X11 Protocol dri3proto
Version:  1.0
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.bz2
Source1001: 	dri3proto.manifest

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

%if !%{with x}
ExclusiveArch:
%endif

%description
%{summary}

%prep
%setup -q
cp %{SOURCE1001} .

%build

%autogen --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
%make_install

%remove_docs

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
