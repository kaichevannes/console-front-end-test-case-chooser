import random
from browser.distribution import (
    WindowsBrowserDistribution,
    MacBrowserDistribution,
    IosMobileBrowserDistribution,
    AndroidMobileBrowserDistribution,
    IosTabletBrowserDistribution,
    AndroidTabletBrowserDistribution,
)
from config import WINDOWS, MAC, MOBILE, TABLET

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


class TestCaseGenerator:
    """Generate a single test case."""

    def __init__(self, desktop_probability, mobile_probability, tablet_probability):
        self.desktop_probability = desktop_probability
        self.mobile_probability = mobile_probability
        self.tablet_probability = tablet_probability

    def generate_test_case(self):
        """Generate a single test case.

        Returns:
            [(os,browser,resolution)]: the test case tuple being returned
        """
        desktop_test_case = self.generate_desktop(self.desktop_probability)
        mobile_test_case = self.generate_mobile(self.mobile_probability)
        tablet_test_case = self.generate_tablet(self.tablet_probability)
        combined_task_list = [desktop_test_case, mobile_test_case, tablet_test_case]
        return list(filter(lambda x: x is not None, combined_task_list))

    def generate_desktop(self, probability):
        """Generate a test case based on the desktop configuration.

        Returns:
            (str,str,str): (os,browser,resolution) to test
        """
        # TODO: Change into class and return a dictionary instead of a tuple
        desktop_os = self.get_desktop_os()

        if desktop_os is None:
            return None

        if not random.random() < probability / 100:
            return None

        if desktop_os == WINDOWS_OS:
            desktop_distribution = WindowsBrowserDistribution()
        elif desktop_os == MAC_OS:
            desktop_distribution = MacBrowserDistribution()

        browser, resolution = desktop_distribution.get_test_case()
        return desktop_os, browser, resolution

    def generate_mobile(self, probability):
        """Generate a test case based on the mobile configuration.

        Returns:
            (str,str,str): (os,browser,resolution) to test
        """
        mobile_os = self.get_mobile_os()

        if mobile_os is None:
            return None

        if not random.random() < probability / 100:
            return None

        if mobile_os == IOS_OS:
            mobile_distribution = IosMobileBrowserDistribution()
        elif mobile_os == ANDROID_OS:
            mobile_distribution = AndroidMobileBrowserDistribution()

        browser, resolution = mobile_distribution.get_test_case()
        return mobile_os, browser, resolution

    def generate_tablet(self, probability):
        """Gemerate a test case based on the tablet configuration.

        Returns:
            (str,str,str): (os,browser,resolution) to test
        """
        tablet_os = self.get_tablet_os()

        if tablet_os is None:
            return tablet_os

        if not random.random() < probability / 100:
            return None

        if tablet_os == IOS_OS:
            tablet_distribution = IosTabletBrowserDistribution()
        elif tablet_os == ANDROID_OS:
            tablet_distribution = AndroidTabletBrowserDistribution()

        browser, resolution = tablet_distribution.get_test_case()
        return tablet_os, browser, resolution

    def get_desktop_os(self):
        """Get the desktop OS to test

        Returns:
            str: the OS to test
        """
        if WINDOWS and MAC:
            return random.choices(DESKTOP_OS, weights=DESKTOP_OS_PROBABILITY, k=1)[0]

        if WINDOWS:
            return WINDOWS_OS

        if MAC:
            return MAC_OS

        return None

    def get_mobile_os(self):
        """Get the mobile OS to test

        Returns:
            str: the OS to test
        """
        if MOBILE:
            return random.choices(MOBILE_OS, weights=MOBILE_OS_PROBABILITY, k=1)[0]

        return None

    def get_tablet_os(self):
        """Get the tablet OS to test

        Returns:
            str: the OS to test
        """
        if TABLET:
            return random.choices(TABLET_OS, TABLET_OS_PROBABILITY, k=1)[0]

        return None
