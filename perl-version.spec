%define modname	version
%define modver 0.9909

Summary:	Perl extension for Version Objects
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
Provides:	perl(version) = %{epoch}:%{version}

%description
Overloaded version objects for all versions of Perl. This module implements
all of the features of version objects which will be part of Perl 5.10.0
except automatic version object creation.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*
