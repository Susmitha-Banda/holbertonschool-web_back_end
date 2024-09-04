import globals from "globals";
import pluginJs from "@eslint/js";

export default [
  {
    files: ["**/*.{js,mjs,cjs}"], // Removed jsx since React isn't involved
    languageOptions: {
      globals: {
        ...globals.browser, // Includes browser globals
        ...globals.node,    // Includes Node.js globals
      },
      ecmaVersion: 2021,
      sourceType: "module",
    },
  },
  pluginJs.configs.recommended,
];
