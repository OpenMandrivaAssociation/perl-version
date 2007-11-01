%define module	version
%define name	perl-%{module}
%define	modprefix version

%define	realversion 0.7203
%define version	0.7400
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for Version Objects
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/%{module}-%{realversion}.tar.gz
BuildRequires:	perl-devel
#BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Overloaded version objects for all versions of Perl. This module implements
all of the features of version objects which will be part of Perl 5.10.0
except automatic version object creation.

%prep
%setup -q -n %{module}-%{realversion}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/%{modprefix}*
%{perl_vendorarch}/auto/%{modprefix}
%{_mandir}/*/*



