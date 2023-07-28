import random
from browser_distribution import (
    WindowsBrowserDistribution,
    MacBrowserDistribution,
    IosMobileBrowserDistribution,
    AndroidMobileBrowserDistribution,
    IosTabletBrowserDistribution,
    AndroidTabletBrowserDistribution,
)

WINDOWS_OS = "Windows 10"
MAC_OS = "Mac"
IOS_OS = "iOS"
ANDROID_OS = "Android"

# Browser/Resolution use distributions
# Desktop
DESKTOP_OS = [WINDOWS_OS, MAC_OS]
DESKTOP_OS_PROBABILITY = (68.15, 21.38)

# Mobile
MOBILE_OS = [IOS_OS, ANDROID_OS]
MOBILE_OS_PROBABILITY = (50.78, 48.73)

# Tablet
TABLET_OS = [IOS_OS, ANDROID_OS]
TABLET_OS_PROBABILITY = (59.03, 40.83)

# Test distribution
DESKTOP_PROBABILITY = 100
MOBILE_PROBABILITY = 15
TABLET_PROBABILITY = 5

class TestCaseChooser:
    """Choose the test case for each task of a given spec section."""

    def __init__(self, windows=True, mac=True, mobile=True, tablet=True):
        self.windows = windows
        self.mac = mac
        self.mobile = mobile
        self.tablet = tablet

        self.spec_section = None
        self.mobile_application = not (self.windows and self.mac)
        self.task_index = -1
        self.current_task = None

    def set_spec_section(self, spec_section):
        """Set the section to generate test cases for."""
        self.spec_section = spec_section
        self.task_index = -1

    def next_test_case(self):
        """Get the next test case to manually test.
        Generally, always check for desktop, sometimes for mobile, rarely for tablet.
        If it a mobile application then always for mobile, rarely for tablet.

        Returns:
            [(browser,resolution)]: An array of browser resolution pairs
        """
        if self.spec_section is None:
            raise LookupError(
                "Spec section is None, set the spec section before trying to generate a test case."
            )

        test_case = []
        self.task_index += 1

        if self.task_index >= len(self.spec_section.tasks):
            return test_case

        self.current_task = self.spec_section.tasks[self.task_index]

        # TODO: Turn into class.
        if not self.mobile_application:
            if not random.random() < DESKTOP_PROBABILITY / 100:
                return test_case

            desktop_os = self.get_desktop_os()
            if desktop_os == WINDOWS_OS:
                desktop_distribution = WindowsBrowserDistribution()
            elif desktop_os == MAC_OS:
                desktop_distribution = MacBrowserDistribution()

            desktop_test_case = desktop_distribution.get_test_case()
            test_case.append(desktop_test_case)

            if not random.random() < MOBILE_PROBABILITY / 100:
                return test_case

        mobile_os = self.get_mobile_os()
        if not mobile_os is None:
            if mobile_os == IOS_OS:
                mobile_distribution = IosMobileBrowserDistribution()
            elif mobile_os == ANDROID_OS:
                mobile_distribution = AndroidMobileBrowserDistribution()

            mobile_test_case = mobile_distribution.get_test_case()
            test_case.append(mobile_test_case)

        if not random.random() < TABLET_PROBABILITY / 100:
            return test_case

        tablet_os = self.get_tablet_os()
        if not tablet_os is None:
            if tablet_os == IOS_OS:
                tablet_distribution = IosTabletBrowserDistribution()
            elif tablet_os == ANDROID_OS:
                tablet_distribution = AndroidTabletBrowserDistribution()

            tablet_test_case = tablet_distribution.get_test_case()
            test_case.append(tablet_test_case)

        return test_case

    def get_desktop_os(self):
        """Get the desktop OS to test

        Returns:
            str: the OS to test
        """
        if self.windows and self.mac:
            return random.choices(DESKTOP_OS, weights=DESKTOP_OS_PROBABILITY, k=1)[0]

        if self.windows:
            return WINDOWS_OS

        if self.mac:
            return MAC_OS

        return None

    def get_mobile_os(self):
        """Get the mobile OS to test

        Returns:
            str: the OS to test
        """
        if self.mobile:
            return random.choices(MOBILE_OS, weights=MOBILE_OS_PROBABILITY, k=1)[0]

        return None

    def get_tablet_os(self):
        """Get the tablet OS to test

        Returns:
            str: the OS to test
        """
        if self.tablet:
            return random.choices(TABLET_OS, TABLET_OS_PROBABILITY, k=1)[0]

        return None
