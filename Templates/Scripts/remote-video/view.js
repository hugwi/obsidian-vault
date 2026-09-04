// Compatibility shim — not the renderer.
//
// This view was renamed to `remote-media` because it renders stills as well as
// video; calling it "remote-video" from an image-only raw note was misleading.
// Notes clipped before the rename still call `Templates/Scripts/remote-video`,
// so this forwards them to the real view instead of failing with
// "Dataview: custom view not found".
//
// Safe to delete this folder once nothing references it:
//   grep -rl 'Scripts/remote-video' --include='*.md' .

await dv.view("Templates/Scripts/remote-media");
