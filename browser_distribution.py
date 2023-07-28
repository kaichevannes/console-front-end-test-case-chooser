import random

# Desktop Browsers.
EDGE = "Edge"
EDGE_LATEST = "v115"
EDGE_PRECEDING = "v114"

FIREFOX = "Firefox"
FIREFOX_LATEST = "v115"
FIREFOX_PRECEDING = "v114"

CHROME = "Chrome"
CHROME_LATEST = "v115"
CHROME_PRECEDING = "v114"

SAFARI = "Safari"
SAFARI_LATEST = "v16.5 (Ventura)"
SAFARI_PRECEDING = "v15.6 (Monterey)"


class BrowserDistribution:
    """Represent a browser"""

    def __init__(
        self, browsers, browsers_probability, resolutions, resolutions_probability
    ):
        self.browsers = browsers
        self.browsers_probability = browsers_probability
        self.resolutions = resolutions
        self.resolutions_probability = resolutions_probability

    def get_test_case(self):
        """Get the test case for the browser this class represents

        Returns:
            str: A browser and resolution to test
        """
        test_browser = self.get_random_selection(
            self.browsers, self.browsers_probability
        )
        test_resolution = self.get_random_selection(
            self.resolutions, self.resolutions_probability
        )

        return test_browser, test_resolution

    def get_random_selection(self, list_to_check, probability_distribution):
        """Choose a random option from the given list based on the probability distribution

        Args:
            list_to_check (array(T)): list to select from
            probability_distribution (sequence): probability distribution of the list

        Returns:
            T: the selected option from the list
        """
        return random.choices(list_to_check, weights=probability_distribution, k=1)[0]


class WindowsBrowserDistribution(BrowserDistribution):
    """Represent a Windows browser distribution."""

    WINDOWS_BROWSERS = [
        f"{CHROME} {CHROME_LATEST}/{CHROME_PRECEDING}",
        f"{EDGE} {EDGE_LATEST}/{EDGE_PRECEDING}",
        f"{FIREFOX} {FIREFOX_LATEST}/{FIREFOX_PRECEDING}",
    ]
    WINDOWS_BROWSERS_PROBABILITY = (46.68, 5.28, 4.61)  # Chrome, Edge, Firefox
    WINDOWS_RESOLUTIONS = ["1920x1080", "1536x864", "1440x900", "1024x768"]
    WINDOWS_RESOLUTIONS_PROBABILITY = (22.93, 10.36, 6.8, 2.98)

    def __init__(self):
        super().__init__(
            self.WINDOWS_BROWSERS,
            self.WINDOWS_BROWSERS_PROBABILITY,
            self.WINDOWS_RESOLUTIONS,
            self.WINDOWS_RESOLUTIONS_PROBABILITY,
        )


class MacBrowserDistribution(BrowserDistribution):
    """Represent a Mac browser distribution."""

    MAC_BROWSERS = [
        f"{SAFARI} {SAFARI_LATEST}/{SAFARI_PRECEDING}",
        f"{CHROME} {CHROME_LATEST}/{CHROME_PRECEDING}",
    ]
    MAC_BROWSERS_PROBABILITY = (20.5, 14.42)  # Safari, Chrome
    MAC_RESOLUTIONS = ["1920x1080", "1280x1024", "1024x768"]
    MAC_RESOLUTIONS_PROBABILITY = (22.93, 5.83, 2.98)

    def __init__(self):
        super().__init__(
            self.MAC_BROWSERS,
            self.MAC_BROWSERS_PROBABILITY,
            self.MAC_RESOLUTIONS,
            self.MAC_RESOLUTIONS_PROBABILITY,
        )


class IosMobileBrowserDistribution(BrowserDistribution):
    """Represent an iOS mobile browser distribution."""

    IOS_MOBILE_BROWSERS = [SAFARI, ""]
    IOS_MOBILE_BROWSERS_PROBABILITY = (100, 0)  # Safari
    IOS_MOBILE_RESOLUTIONS = [
        "414x896 (Apple iPhone 11)",
        "390x844 (Apple iPhone 13)",
        "375x812 (Apple iPhone XS)",
        "375x667 (Apple iPhone 6/7/8)",
        "360x780 (Apple iPhone 12 Mini)",
    ]
    IOS_MOBILE_RESOLUTIONS_PROBABILITY = (6.48, 5.33, 4.17, 4.1, 4.21)

    def __init__(self):
        super().__init__(
            self.IOS_MOBILE_BROWSERS,
            self.IOS_MOBILE_BROWSERS_PROBABILITY,
            self.IOS_MOBILE_RESOLUTIONS,
            self.IOS_MOBILE_RESOLUTIONS_PROBABILITY,
        )


class AndroidMobileBrowserDistribution(BrowserDistribution):
    """Represent an Android mobile browser distribution."""

    ANDROID_MOBILE_BROWSERS = [CHROME, ""]
    ANDROID_MOBILE_BROWSERS_PROBABILITY = (100, 0)
    ANDROID_MOBILE_RESOLUTIONS = [
        "412x915 (Samsung Galaxy A51)",
        "393x851 (Google Pixel 5)",
        "360x800 (Samsung Galaxy S21)",
        "360x640 (Samsung S6)",
    ]
    ANDROID_MOBILE_RESOLUTIONS_PROBABILITY = (4.75, 3.46, 8.83, 5.69)

    def __init__(self):
        super().__init__(
            self.ANDROID_MOBILE_BROWSERS,
            self.ANDROID_MOBILE_BROWSERS_PROBABILITY,
            self.ANDROID_MOBILE_RESOLUTIONS,
            self.ANDROID_MOBILE_RESOLUTIONS_PROBABILITY,
        )


class IosTabletBrowserDistribution(BrowserDistribution):
    """Represent an iOS tablet browser distribution."""

    IOS_TABLET_BROWSERS = [SAFARI, ""]
    IOS_TABLET_BROWSERS_PROBABILITY = (100, 0)
    IOS_TABLET_RESOLUTIONS = ["2160x1620 (Apple iPad 9th)", ""]
    IOS_TABLET_RESOLUTIONS_PROBABILITY = (100, 0)

    def __init__(self):
        super().__init__(
            self.IOS_TABLET_BROWSERS,
            self.IOS_TABLET_BROWSERS_PROBABILITY,
            self.IOS_TABLET_RESOLUTIONS,
            self.IOS_TABLET_RESOLUTIONS_PROBABILITY,
        )


class AndroidTabletBrowserDistribution(BrowserDistribution):
    """Represent an Android tablet browser distribution."""

    ANDROID_TABLET_BROWSERS = [CHROME, ""]
    ANDROID_TABLET_BROWSERS_PROBABILITY = (100, 0)
    ANDROID_TABLET_RESOLUTIONS = ["2560x1600 (Samsung Galaxy Tab S8)", ""]
    ANDROID_TABLET_RESOLUTIONS_PROBABILITY = (100, 0)

    def __init__(self):
        super().__init__(
            self.ANDROID_TABLET_BROWSERS,
            self.ANDROID_TABLET_BROWSERS_PROBABILITY,
            self.ANDROID_TABLET_RESOLUTIONS,
            self.ANDROID_TABLET_RESOLUTIONS_PROBABILITY,
        )
