Summary: NethServer backup data and config files
Name: nethserver-backup-data
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Group: System
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: cifs-utils, nfs-utils, duplicity
Requires: nethserver-backup-config >= 1.2.0
AutoReq: no

%description
NethServer backup of config and data files

%prep
%setup

%build
%{makedocs}
perl createlinks

# relocate perl modules under default perl vendorlib directory:
mkdir -p root%{perl_vendorlib}
mv -v NethServer root%{perl_vendorlib}

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%config /etc/backup-data.d/custom.include
%config /etc/backup-data.d/custom.exclude


%changelog
* Thu Apr 23 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.3-1
- Language packs support - Feature #3115 [NethServer]

* Wed Mar 18 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.2-1
- backup-data fails just after installation - Bug #3004 [NethServer]

* Thu Mar 05 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- backup-data retention policy multiple of 7 - Enhancement #3007 [NethServer]

* Tue Aug 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Backup data: avoid multiple sessions - Enhancement #2828 [NethServer]

* Tue Jul 01 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.11-1.ns6
- Remove modifications for Enhancement #2773

* Mon Jun 30 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.10-1.ns6
- Backup data: restore files from a certain time - Enhancement #2749
- Backup config: minimize creation of new backup - Enhancement #2699

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.9-1.ns6
- Backup data: can't install package if backup is in progress - Bug #2667 [NethServer]
- Backup data: can't restore backup from old chians - Bug #2665 [NethServer]
- Send backup notification to root - Enhancement #2647 [NethServer]
- restore-data-duplicity action fails with whitespaces - Bug #2643 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.8-1.ns6
- NethCamp 2014 - Task #2618 [NethServer]
- Backup: force backup of configuration before starting backup-data - Enhancement #2118 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]
- Dashboard: new widgets - Enhancement #1671 [NethServer]

* Wed Oct 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.7-1.ns6
- Exclude e-smith db directory #2143
- Minor fix on web UI #2040

* Tue Aug 06 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1.ns6
- Do not raise error on empty USBLabel if VFSType is not usb #2022

* Wed Jul 31 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.5-1.ns6
- Check if USBLabel is empty, check if USB disk is mounted on /mnt/backup #2022
- Force exclusions before inclusions
- Attach log on notification

* Fri Jul 12 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1.ns6
- Backup: implement and document full restore #2043

* Tue Jun 25 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
* Add last-backup log extract to notification

* Mon Jun 17 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Avoid duplicate notifications. Refs #2023
- Implement simple retention policy. Refs #2024

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Rebuild for automatic package handling. #1870
- Add mail notification #1572
- Add web user interface
- Various bug fixes

* Mon Mar 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release

* Wed Jan 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.9.0-1
- Fist release

