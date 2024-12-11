import { c } from "vite/dist/node/types.d-aGj9QkWt";

/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      animation: {
        spral: "spral 2s linear infinite",
      },
      keyframes: {
        spral: {
          "0%, 100%": { transform: "rotate(0deg)" },
          "50%": { transform: "rotate(360deg)" },
        },
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};
