%define oname rexical

Summary:    Rexical is a lexical scanner generator
Name:       rubygem-%{oname}
Version:    1.0.5
Release:	3
Group:      Development/Ruby
License:    LGPLv2
URL:        http://github.com/tenderlove/rexical/tree/master
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(hoe) >= 2.3.1
BuildRequires: rubygems
BuildArch:  noarch
Provides: rubygem(%{oname}) = %{version}

%description
Rexical is a lexical scanner generator.
It is written in Ruby itself, and generates Ruby program.
It is designed for use with Racc.


%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

sed -i 's!#!.*!#!/usr/bin/env ruby' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/rex*

%files
%{_bindir}/rex
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/sample/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.ja
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/DOCUMENTATION.en.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/DOCUMENTATION.ja.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.5-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Jan 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5-1
+ Revision: 769360
- version update 1.0.5

* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 609238
- %gem_build macros are broken at the moment, using classic method from
  gem2rpm to build the package for the moment.

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - imported package rubygem-rexical


* Mon Nov 01 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.4-1
- Initial package
