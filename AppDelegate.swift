// import Cocoa
// import Metal
// import QuartzCore

// class AppDelegate: NSObject, NSApplicationDelegate {

//     var window: NSWindow!
//     var metalLayer: CAMetalLayer!
//     var device: MTLDevice!
//     var commandQueue: MTLCommandQueue!

//     func applicationDidFinishLaunching(_ aNotification: Notification) {
//         device = MTLCreateSystemDefaultDevice()
//         commandQueue = device.makeCommandQueue()

//         let screenRect = NSScreen.main!.frame
//         window = NSWindow(contentRect: screenRect,
//                           styleMask: .borderless,
//                           backing: .buffered,
//                           defer: false)
//         window.isOpaque = false
//         window.backgroundColor = .clear
//         window.level = .screenSaver
//         window.ignoresMouseEvents = true
//         window.collectionBehavior = [.canJoinAllSpaces, .fullScreenAuxiliary]
//         window.makeKeyAndOrderFront(nil)

//         metalLayer = CAMetalLayer()
//         metalLayer.device = device
//         metalLayer.pixelFormat = .bgra8Unorm
//         metalLayer.framebufferOnly = true
//         metalLayer.frame = screenRect
//         metalLayer.contentsScale = NSScreen.main!.backingScaleFactor
//         metalLayer.isOpaque = false
//         metalLayer.backgroundColor = NSColor.systemTeal.withAlphaComponent(0.4).cgColor

//         window.contentView?.wantsLayer = true
//         window.contentView?.layer = metalLayer

//         draw()
//     }

//     func draw() {
//         guard let drawable = metalLayer?.nextDrawable() else { return }

//         let commandBuffer = commandQueue.makeCommandBuffer()
//         let passDescriptor = MTLRenderPassDescriptor()
//         passDescriptor.colorAttachments[0].texture = drawable.texture
//         passDescriptor.colorAttachments[0].loadAction = .clear
//         passDescriptor.colorAttachments[0].clearColor = MTLClearColor(red: 0.0, green: 1.0, blue: 0.0, alpha: 0.4)

//         if let encoder = commandBuffer?.makeRenderCommandEncoder(descriptor: passDescriptor) {
//             encoder.endEncoding()
//         }

//         commandBuffer?.present(drawable)
//         commandBuffer?.commit()
//     }
// }
