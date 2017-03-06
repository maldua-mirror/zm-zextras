#
# spec file for zimbra.rpm
#
Summary: Zimbra Chat
Name: @@_PKG_NAME_@@
Version: @@ENV_PKG_VERSION@@
Release: @@ENV_PKG_RELEASE@@
License: ZPL and other
Group: Applications/Messaging
URL: http://www.zimbra.com
Vendor: Zimbra, Inc.
Packager: Zimbra Packaging Services <build@zimbra.com>
AutoReqProv: no
Requires: zimbra-core

%description
zimbra chat extensions

%define __spec_install_pre /bin/true

%define __spec_install_post /usr/lib/rpm/brp-compress /usr/lib/rpm/brp-strip-comment-note %{nil}

%prep

%build

%install

%pre

%post

%preun

%postun

%files
/opt
