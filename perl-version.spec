%define upstream_name	 version
%define upstream_version 0.95

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5
Epoch:      1

Summary:	Perl extension for Version Objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

Provides:   perl(version) = %{epoch}:%{version}

%description
Overloaded version objects for all versions of Perl. This module implements
all of the features of version objects which will be part of Perl 5.10.0
except automatic version object creation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/version*
%{perl_vendorarch}/auto/version
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.950.0-3
+ Revision: 765804
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.950.0-2
+ Revision: 764328
- rebuilt for perl-5.14.x

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:0.950.0-1
+ Revision: 759448
- version update 0.95

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.880.0-2
+ Revision: 676529
- rebuild

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.880.0-1
+ Revision: 635559
- update to new version 0.88

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.850.0-1mdv2011.0
+ Revision: 597206
- update to 0.85

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.820.0-3mdv2011.0
+ Revision: 556189
- rebuild for perl 5.12
- rebuild

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.820.0-1mdv2010.1
+ Revision: 536956
- update to 0.82

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.800.0-3mdv2010.1
+ Revision: 515380
- add %%{epoch} in manual provides:

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.800.0-2mdv2010.1
+ Revision: 515351
- adding explicit provides:

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.800.0-1mdv2010.1
+ Revision: 494927
- update to 0.80

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.790.0-1mdv2010.1
+ Revision: 489513
- update to 0.79

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.780.0-1mdv2010.1
+ Revision: 461359
- update to 0.78

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.770.200-1mdv2010.0
+ Revision: 437214
- update to 0.7702

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.770.100-2mdv2010.0
+ Revision: 420987
- rebuild

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.770.100-1mdv2010.0
+ Revision: 418661
- update to 0.7701

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.76-1mdv2010.0
+ Revision: 372415
- update to new version 0.76

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.74-1mdv2008.1
+ Revision: 109457
- set epoch
- new version

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.7400-2mdv2008.1
+ Revision: 109331
- rebuild

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7400-1mdv2008.1
+ Revision: 104605
- update to new version 0.7400

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7300-1mdv2008.1
+ Revision: 97572
- update to new version 0.7300

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.7203-1mdv2008.0
+ Revision: 42912
- New version 0.7203


* Sun Dec 24 2006 Olivier Thauvin <nanardon@mandriva.org> 0.68-1mdv2007.0
+ Revision: 101959
- 0.68

* Tue Aug 29 2006 Scott Karns <scottk@mandriva.org> 0.67.01-1mdv2007.0
+ Revision: 58287
- Version 0.6701

* Fri Aug 18 2006 Scott Karns <scottk@mandriva.org> 0.67-3mdv2007.0
+ Revision: 56546
- Removed unnecessary BuildRequires gcc
- Added BuildRequires perl(ExtUtils::CBuilder)

* Fri Aug 18 2006 Scott Karns <scottk@mandriva.org> 0.67-2mdv2007.0
+ Revision: 56542
- Added BuildRequires gcc

* Mon Aug 14 2006 Scott Karns <scottk@mandriva.org> 0.67-1mdv2007.0
+ Revision: 55805
- Version 0.67
- Patched Build.PL for broken Module::Build-0.2805 (per CPAN
  maintainer of version)
- import perl-version-0.64-1mdv2007.0

* Sat Jun 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.64-1mdv2007.0
- new version
- revert to author's namespace for source URL, standard one doesn't seem to exist

* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2007.0
- New release 0.63
- no use for perl-devel, this one uses Module::Build

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.59-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires

* Tue Apr 04 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.59-1mdk
- 0.59

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.57-1mdk
- 0.57

* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Thu Oct 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.49-1mdk
- 0.49

* Sat Oct 01 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.48-2mdk
- Buildrequires fix

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.48-1mdk
- 0.48

* Thu Aug 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.47-1mdk
- 0.47

* Tue Aug 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.46-1mdk
- 0.46

* Tue Jul 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.44-1mdk
- 0.44
- Convert spec to build using Build.PL

* Sun May 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-2mdk 
- drop patch, the pseudo-shellbang is actually used by perl

* Thu Apr 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdk 
- first mandriva release

