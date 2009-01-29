#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	Virtual-Async-inMemory
Summary:	perl(Filesys::Virtual::Async::inMemory)
#Summary(pl.UTF-8):	
Name:		perl-Filesys-Virtual-Async-inMemory
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaccc90cdd17eda43212e31215d7cfbd
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Filesys-Virtual-Async-inMemory/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Filesys-Virtual-Async
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Test-Simple >= 0.86
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you run the Filesys::Virtual::Async API entirely in memory. Nothing special here, really :)

This module makes extensive use of the functions in File::Spec to be portable, so it might trip you up if
you are developing on a linux box and trying to play with '/foo' on a win32 box :)

This constructor accepts either a hashref or a hash, valid options are:



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Filesys/Virtual/Async/*.pm
#%%{perl_vendorlib}/Filesys/Virtual/Async/inMemory
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
