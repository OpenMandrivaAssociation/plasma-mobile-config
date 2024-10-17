Name:		plasma-mobile-config
Summary:	Default configuration for plasma-mobile
Version:	0.4
Release:	2
License:	GPLv2.0
Group:		Graphical desktop/KDE
Url:		https://plasma-active.org/
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.xz
Patch0:		susebranch.patch
Patch1:		0001-on-opensuse-KDE4-dotfolder-is-called-.kde4.patch
Patch2:		0002-use-kwin-instead-of-kwinactive.patch
Patch3:		0003-remove-welcome-applet.patch
BuildRequires:	task-kde4-devel

%description
Contains default configuration files
for KDE applications to work well with plasma-mobile.

%prep
%setup -q
%autopatch -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%doc COPYING
%_kde_configdir/*
%_sysconfdir/skel/.kde4
%_sysconfdir/skel/.config
%_sysconfdir/profile.d/*.sh
