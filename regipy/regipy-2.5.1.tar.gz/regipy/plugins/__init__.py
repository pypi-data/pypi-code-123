from .amcache.amcache import AmCachePlugin
from .ntuser.persistence import NTUserPersistencePlugin
from .ntuser.user_assist import UserAssistPlugin
from .ntuser.word_wheel_query import WordWheelQueryPlugin
from .ntuser.typed_urls import TypedUrlsPlugin
from .ntuser.installed_programs_ntuser import InstalledSoftwareNTUserPlugin
from .ntuser.tsclient import TSClientPlugin
from .ntuser.classes_installer import ClassesInstallerPlugin
from .ntuser.winrar import WinRARPlugin
from .ntuser.network_drives import NetworkDrivesPlugin
from .ntuser.winscp_saved_sessions import WinSCPSavedSessionsPlugin
from .system.bam import BAMPlugin
from .system.routes import RoutesPlugin
from .system.services import ServicesPlugin
from .system.computer_name import ComputerNamePlugin
from .system.shimcache import ShimCachePlugin
from .system.safeboot_configuration import SafeBootConfigurationPlugin
from .system.usbstor import USBSTORPlugin
from .system.wdigest import WDIGESTPlugin
from .software.tracing import RASTracingPlugin
from .software.classes_installer import SoftwareClassesInstallerPlugin
from .software.installed_programs import InstalledSoftwarePlugin
from .software.image_file_execution_options import ImageFileExecutionOptions
from .software.persistence import SoftwarePersistencePlugin
from .software.uac import UACStatusPlugin
from .software.last_logon import LastLogonPlugin
from .software.profilelist import ProfileListPlugin
from .software.printdemon import PrintDemonPlugin
from .system.timezone_data import TimezoneDataPlugin
from .system.active_controlset import ActiveControlSetPlugin
from .system.bootkey import BootKeyPlugin
from .system.host_domain_name import HostDomainNamePlugin
from .security.domain_sid import DomainSidPlugin
from .sam.local_sid import LocalSidPlugin
from .bcd.boot_entry_list import BootEntryListPlugin
from .ntuser.shellbags_ntuser import ShellBagNtuserPlugin
