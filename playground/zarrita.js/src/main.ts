import * as zarrita from "zarrita";
import { ZipFileStore } from "@zarrita/storage";

const url = new URLSearchParams(window.location.search).get("url")!;

const store = ZipFileStore.fromUrl(url);
const group = await zarrita.open(store, { kind: "group" });
const metadata = JSON.stringify(group.attrs, null, 2);

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <pre><code>${metadata}</code></pre>
`;
