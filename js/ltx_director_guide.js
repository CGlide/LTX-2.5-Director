import { app } from "../../scripts/app.js";

// LTX Director Guide is a pure pass-through processor node.
// All configuration (images, insert frames, strengths) comes from
// the guide_data output of Prompt Relay Encode (Timeline).
app.registerExtension({
    name: "Comfy.LTXDirectorGuideCS",
    async nodeCreated(node) {
        if (node.comfyClass !== "LTXDirectorGuideCS") return;

        // Hide retake_mode widget on LiteGraph as it is dynamically auto-detected from the timeline data.
        const w = node.widgets?.find(x => x.name === "retake_mode");
        if (w) {
            w.hidden = true;
            if (!w.options) w.options = {};
            w.options.hidden = true;
            if (!window.LiteGraph || !window.LiteGraph.vueNodesMode) {
                w.computeSize = () => [0, -4];
                w.draw = () => { };
            }
            if (w.element) w.element.style.display = "none";
        }
    },
});