%global realversion 1.5.2
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>
%global realname rubygem-rack

%global gemname rack

%global gemdir /usr/lib64/ruby/gems/1.8
%global geminstdir %{gemdir}/gems/%{gemname}-%{realversion}
%global gemspecdir %{gemdir}/specifications/
%global gemcachedir %{gemdir}/cache/

%global rubyabi 1.8

Summary: a modular Ruby webserver interface
Name: EXTRlitprack_CXP9031044
Version: %{rpmversion}
Release: 1
Group: Development/Languages
License: MIT
URL: http://rack.github.com/
Source0: %{gemname}-%{realversion}.tar.gz
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{realversion}
Provides: rubygem-%{gemname} = %{realversion}
Packager:  %{packager}

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.github.com/. repackaged by Ericsson from GitHUB source code.


%prep
%setup -q -c -T
mkdir -p .%{gemdir}

%build

%install
%{__install} -d -m0755 %{buildroot}%{geminstdir}
%{__install} -d -m0755 %{buildroot}/usr/bin
%{__install} -d -m0755 %{buildroot}%{gemspecdir}
%{__install} -d -m0755 %{buildroot}%{gemcachedir}
cp -a  %{_builddir}%{gemname}-%{realversion}/* %{buildroot}%{geminstdir}
cp -a  %{_builddir}rackup %{buildroot}/usr/bin/rackup 
cp -a  %{_builddir}%{gemname}-%{realversion}/rack.gemspec %{buildroot}%{gemspecdir}/rack-%{realversion}.gemspec
cp -a  %{_builddir}rack-%{realversion}.gem %{buildroot}%{gemcachedir}rack-%{realversion}.gem

%files
%defattr(-,root,root,-)
%{geminstdir}
%{gemspecdir}
%{gemcachedir}
/usr/bin/rackup
