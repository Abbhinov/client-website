import { readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, relative, sep } from "node:path";

const root = process.cwd();
const htmlFiles = [];
const cssFiles = [];

function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    const full = `${dir}${sep}${entry.name}`;
    if (entry.isDirectory()) {
      walk(full);
    } else if (entry.name.endsWith(".html")) {
      htmlFiles.push(full);
    } else if (entry.name.endsWith(".css")) {
      cssFiles.push(full);
    }
  }
}

function prefixFor(file) {
  const relDir = relative(root, dirname(file));
  if (!relDir) return "./";
  return `${relDir.split(sep).filter(Boolean).map(() => "..").join("/")}/`;
}

function rootRelativeToFileRelative(value, file) {
  if (!value.startsWith("/") || value.startsWith("//")) return value;
  const match = value.match(/^([^?#]*)([?#].*)?$/);
  const pathname = match?.[1] || value;
  const suffix = match?.[2] || "";
  let target = pathname === "/" ? "index.html" : pathname.replace(/^\//, "");
  if (target.endsWith("/")) target += "index.html";
  return `${prefixFor(file)}${target}${suffix}`;
}

function relativizeHtml(html, file) {
  return html
    .replace(/\b(href|src|content)=(")(\/(?!\/)[^"]*)"/g, (_match, attr, quote, value) => `${attr}=${quote}${rootRelativeToFileRelative(value, file)}${quote}`)
    .replace(/\b(href|src|content)=(')(\/(?!\/)[^']*)'/g, (_match, attr, quote, value) => `${attr}=${quote}${rootRelativeToFileRelative(value, file)}${quote}`);
}

function relativizeCss(css, file) {
  return css.replace(/url\((['"]?)(\/(?!\/)[^)'" ]+)\1\)/g, (_match, quote, value) => `url(${quote}${rootRelativeToFileRelative(value, file)}${quote})`);
}

walk(root);

for (const file of htmlFiles) {
  const before = readFileSync(file, "utf8");
  const after = relativizeHtml(before, file);
  if (after !== before) writeFileSync(file, after, "utf8");
}

for (const file of cssFiles) {
  const before = readFileSync(file, "utf8");
  const after = relativizeCss(before, file);
  if (after !== before) writeFileSync(file, after, "utf8");
}

console.log(`Relativized ${htmlFiles.length} HTML files and checked ${cssFiles.length} CSS files.`);
