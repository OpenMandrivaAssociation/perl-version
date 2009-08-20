%define upstream_name	 version
%define upstream_version 0.7701

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:	Perl extension for Version Objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JP/JPEACOCK/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/version*
%{perl_vendorarch}/auto/version
%{_mandir}/*/*
