from Cocoa import (
    NSApplication, NSPanel, NSBackingStoreBuffered, NSColor,
    NSWindowStyleMaskBorderless, NSMakeRect, NSObject, NSApp,
    NSView, CALayer
)
from Cocoa import NSTextField

import AppKit
import sys

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        print("✅ Stealth overlay launching...")

        rect = NSMakeRect(600, 400, 400, 200)  # You can change this size/position

        self.window = NSPanel.alloc().initWithContentRect_styleMask_backing_defer_(
            rect,
            NSWindowStyleMaskBorderless,
            NSBackingStoreBuffered,
            False
        )

        self.window.setLevel_(AppKit.NSScreenSaverWindowLevel)
        self.window.setOpaque_(False)
        self.window.setAlphaValue_(1.0)
        self.window.setHasShadow_(False)
        self.window.setIgnoresMouseEvents_(False)
        self.window.setMovableByWindowBackground_(True)

        # Disable window sharing (for screen capture APIs)
        if hasattr(self.window, "setSharingType_"):
            self.window.setSharingType_(AppKit.NSWindowSharingNone)

        # Collection behavior
        self.window.setCollectionBehavior_(
            AppKit.NSWindowCollectionBehaviorCanJoinAllSpaces |
            AppKit.NSWindowCollectionBehaviorTransient |
            AppKit.NSWindowCollectionBehaviorIgnoresCycle |
            AppKit.NSWindowCollectionBehaviorFullScreenAuxiliary
        )

        # Set background layer using CALayer (like Metal does)
        content_view = self.window.contentView()
        layer = CALayer.layer()
        layer.setBackgroundColor_(NSColor.systemGreenColor().colorWithAlphaComponent_(0.1).CGColor())
        layer.setCornerRadius_(12.0)  # Optional: rounded corners
        content_view.setWantsLayer_(True)
        content_view.setLayer_(layer)
        label = NSTextField.alloc().initWithFrame_(NSMakeRect(20, 150, 360, 40))
        label.setStringValue_("I am working can you Cannot see me ")
        label.setBezeled_(False)
        label.setDrawsBackground_(False)
        label.setEditable_(False)
        label.setSelectable_(False)
        label.setTextColor_(NSColor.whiteColor())
        label.setFont_(AppKit.NSFont.systemFontOfSize_(18))
        label.setAlignment_(AppKit.NSTextAlignmentCenter)

        content_view.addSubview_(label)

        # Show it
        self.window.orderFrontRegardless()
        AppKit.NSApp.activateIgnoringOtherApps_(True)

        print("✅ Overlay now floating (check screen share)")

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)

    import signal
    def quit_overlay(signalNumber, frame):
        print("🔴 Quit signal received. Exiting...")
        sys.exit(0)

    signal.signal(signal.SIGINT, quit_overlay)
    signal.signal(signal.SIGTERM, quit_overlay)

    AppKit.NSApp.activateIgnoringOtherApps_(True)
    app.run()
