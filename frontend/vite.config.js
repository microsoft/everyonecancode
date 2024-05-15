import { defineConfig } from "vite";
// import vue from "@vitejs/plugin-vue";

import { createVuePlugin as vue } from "vite-plugin-vue2";

const path = require("path");
const codespaceName = process.env['CODESPACE_NAME'];
const codespaceDomain = process.env['GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN'];
const hmrPort = 5173;

const hmrRemoteHost = codespaceName ? `${codespaceName}-${hmrPort}.${codespaceDomain}` : 'localhost';
const hmrRemotePort = codespaceName ? 443 : hmrPort;
const hmrRemoteProtocol = codespaceName ? 'wss' : 'ws';


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
    extensions: [".mjs", ".js", ".ts", ".jsx", ".tsx", ".json", ".vue"],
  },
  server: {
    hmr: {
        protocol: hmrRemoteProtocol,
        host: hmrRemoteHost,
        port: hmrPort,
        clientPort: hmrRemotePort
    }
  },
});
