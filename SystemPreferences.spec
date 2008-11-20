Summary:	GNUstep System Preferences
Name:		SystemPreferences
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnustep.org/pub/gnustep/usr-apps/%{name}-%{version}.tar.gz
# Source0-md5:	15dad0ce0d07de79fecdcec26485bdc1
Patch0:		%{name}-initWithArgs.patch
URL:		http://www.gnustep.it/enrico/system-preferences/
BuildRequires:	gnustep-gui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNUstep System Preferences.

%package devel
Summary:	Header files for PreferencesPane framework
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-gui-devel

%description devel
Header files for PreferencesPane framework.

%prep
%setup -q
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

for I in PreferencePanes SystemPreferences Modules; do
	cd $I
	%{__make} -j1 \
		OPTFLAG="%{rpmcflags}" \
		messages=yes
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

for I in PreferencePanes SystemPreferences Modules; do
	cd $I
	%{__make} -j1 install \
		GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
		DESTDIR=$RPM_BUILD_ROOT
		messages=yes
	cd ..
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/SystemPreferences
%{_libdir}/GNUstep/Bundles/ColorSchemes.prefPane/ColorSchemes
%{_libdir}/GNUstep/Bundles/Defaults.prefPane/Defaults
%{_libdir}/GNUstep/Bundles/FileSystem.prefPane/FileSystem
%{_libdir}/GNUstep/Bundles/FontModule.prefPane/FontModule
%{_libdir}/GNUstep/Bundles/ModifierKeys.prefPane/ModifierKeys
%{_libdir}/GNUstep/Bundles/TimeZone.prefPane/TimeZone
%{_libdir}/GNUstep/Bundles/Volumes.prefPane/Volumes
%{_libdir}/GNUstep/Colors/*.colorScheme
%{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/PreferencePanes
%{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/Versions/[0-9]*/PreferencePanes
%{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/Versions/[0-9]*/libPreferencePanes.so
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/Versions/[0-9]*/libPreferencePanes.so.1
%attr(755,root,root) %{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/Versions/[0-9]*/libPreferencePanes.so.1.0.0
%{_libdir}/GNUstep/Frameworks/PreferencePanes.framework/libPreferencePanes.so
%{_libdir}/libPreferencePanes.so
%attr(755,root,root) %{_libdir}/libPreferencePanes.so.1
%attr(755,root,root) %{_libdir}/libPreferencePanes.so.1.0.0

%dir %{_libdir}/GNUstep/Applications/*.app
%dir %{_libdir}/GNUstep/Applications/*.app/Resources
%{_libdir}/GNUstep/Applications/*.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/*.app/Resources/*.plist
%{_libdir}/GNUstep/Applications/*.app/Resources/*.tiff
%{_libdir}/GNUstep/Applications/*.app/Resources/English.lproj
%attr(755,root,root) %{_libdir}/GNUstep/Applications/SystemPreferences.app/SystemPreferences
#%{_libdir}/GNUstep/Applications/*.app/Resources/*.openapp

%dir %{_libdir}/GNUstep/Frameworks/*.framework
%{_libdir}/GNUstep/Frameworks/*.framework/Resources
%dir %{_libdir}/GNUstep/Frameworks/*.framework/Versions
%dir %{_libdir}/GNUstep/Frameworks/*.framework/Versions/[0-9]*
%{_libdir}/GNUstep/Frameworks/*.framework/Versions/[0-9]*/Resources
%{_libdir}/GNUstep/Frameworks/*.framework/Versions/Current

%dir %{_libdir}/GNUstep/Bundles/*.prefPane
%{_libdir}/GNUstep/Bundles/*.prefPane/Resources

%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/Frameworks/*.framework/Headers
%{_libdir}/GNUstep/Frameworks/*.framework/Versions/[0-9]*/Headers
%{_includedir}/*
