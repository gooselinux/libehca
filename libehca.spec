Name: libehca
Version: 1.2.1
Release: 6%{?dist}
Summary: IBM InfiniBand HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.g0a82a52.tar.gz
Patch0: libehca-verbs-API.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, autoconf, libtool
ExclusiveArch: ppc ppc64
Obsoletes: %{name}-devel
%description
IBM hardware driver for use with libibverbs user space verbs access
library.

%package static
Summary: Static version of the libehca driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libehca that may be linked directly to an application.

%prep
%setup -q
%patch0 -p1 -b .api

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%doc COPYING

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.2.1-6.el6
- Updates for pkgwrangler issues
- Related: bz543948

* Mon Dec 21 2009 Doug Ledford <dledford@redhat.com> - 1.2.1-5.el5
- Add API patch for new libibverbs API
- buildrequire a few things that the build logs say it wants

* Mon Dec 21 2009 Doug Ledford <dledford@redhat.com> - 1.2.1-4.el5
- Bump tarball to updated OFED tarball
- Build against latest libibverbs
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 1.2.1-3.el5
- Bump buildrequires to a version of libibverbs that has a known good ppc
  memory sync
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 1.2.1-2.el5
- Rebuild against non-XRC libibverbs
- Related: bz506258

* Fri Apr 17 2009 Doug Ledford <dledford@redhat.com> - 1.2.1-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Tue Sep 16 2008 Doug Ledford <dledford@redhat.com> - 1.2-2
- The libibverbs-1.1.2 package includes a ppc specific barrier fix in its
  arch header file, therefore bump and rebuild even though no changes are
  present in this library itself.
- Resolves: bz451455

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.2-1
- Update to OFED 1.3 final bits
- Related: bz428197

* Thu Feb 14 2008 Doug Ledford <dledford@redhat.com> - 1.0-1
- Bump release to sane value
- Obsolete old -devel package
- Related: bz432765

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 1.0-0.1
- Initial import of package
