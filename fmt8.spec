%define _disable_lto 1

%define		major 8
%define		minor 1
%define		libname %mklibname %{name} %{major}
%define		devel %mklibname -d %{name}

Name:		fmt8
Version:	8.1.1
Release:	2
Summary:	Small, safe and fast formatting library
Group:		Development/C++
License:	BSD
URL:		https://fmtlib.org
Source0:	https://github.com/fmtlib/fmt/archive/%{version}/fmt-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja

%description
fmt is an open-source formatting library for C++. It can be used as a safe
alternative to printf or as a fast alternative to IOStreams.

%package -n	%{libname}
Summary:	Old version of the libfmt libraries
Group:		Development/C++

%description -n	%{libname}
This package contains the old version 8 of the library for libfmt

%prep
%autosetup -n fmt-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# No -devel stuff for pure compat packages
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/cmake \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_libdir}/*.so

%files -n	%{libname}
%{_libdir}/libfmt.so.%{major}
%{_libdir}/libfmt.so.%{major}.%{minor}{,.*}
