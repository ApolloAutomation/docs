---
title: M-1 LED Matrix Setting up your own QR code for Wi-Fi, link to a website, etc.
description: Step by step guide to setting up your own QR code for Wi-Fi, link to a website, etc.
---
# 🔧 QR Code Generator (Wi-Fi, Text, URL)

!!! tip "You can set multiple different custom QR Codes as presets in WLED."

    The WLED firmware on your device will allow you to call these presets in automations or make buttons to control them on your Home Assistant dashboard!

<div><p><label><strong>QR Code Type:</strong><br />
    <select id="qrType" onchange="updateForm()" style="width: 100%; max-width: 300px;">
      <option value="wifi">Wi-Fi</option>
      <option value="text">Text</option>
      <option value="url">URL</option>
      <option value="vcard">vCard (Contact)</option>
    </select>
  </label></p><p></p></div>

<div></div>

&nbsp;

<button onclick="generateQRCode()" style="padding: 0.5em 1em; font-weight: bold;">Generate QR Code</button>

<button id="downloadBtn" onclick="downloadQRCode()" disabled="" style="padding: 0.5em 1em; font-weight: bold; margin-left: 1em;">Download</button>

&nbsp;

<div></div>

&nbsp;

&nbsp;

<script>
  let qr;

  function updateForm() {
    const type = document.getElementById("qrType").value;
    const form = document.getElementById("qrForm");
    form.innerHTML = '';

    if (type === "wifi") {
      form.innerHTML = `
        <label><strong>SSID:</strong><br><input type="text" id="ssid" style="width: 100%; max-width: 300px;"></label><br>
        <label><strong>Password:</strong><br><input type="text" id="password" style="width: 100%; max-width: 300px;"></label><br>
        <label><strong>Encryption:</strong><br>
          <select id="encryption" style="width: 100%; max-width: 300px;">
            <option value="WPA">WPA/WPA2</option>
            <option value="WEP">WEP</option>
            <option value="">None</option>
          </select>
        </label><br>
      `;
    } else if (type === "text") {
      form.innerHTML = `
        <label><strong>Text to encode:</strong><br><textarea id="text" style="width: 100%; max-width: 500px;" rows="4"></textarea></label><br>
<p><code>;     } else if (type === &quot;url&quot;) {       form.innerHTML = </code>
<label><strong>URL:</strong><br><input type="url" id="url" placeholder="https://example.com" style="width: 100%; max-width: 500px;"></label><br>
<code>;     } else if (type === &quot;vcard&quot;) {       form.innerHTML = </code>
<label><strong>Full Name:</strong><br><input type="text" id="fullname" style="width: 100%; max-width: 300px;"></label><br>
<label><strong>Phone:</strong><br><input type="tel" id="phone" style="width: 100%; max-width: 300px;"></label><br>
<label><strong>Email:</strong><br><input type="email" id="email" style="width: 100%; max-width: 300px;"></label><br>
<label><strong>Org (optional):</strong><br><input type="text" id="org" style="width: 100%; max-width: 300px;"></label><br>
`;
}
}</p>
<p>function generateQRCode() {
const type = document.getElementById(&quot;qrType&quot;).value;
let data = &quot;&quot;;</p>
<p>if (type === &quot;wifi&quot;) {
const ssid = document.getElementById(&quot;ssid&quot;).value;
const password = document.getElementById(&quot;password&quot;).value;
const encryption = document.getElementById(&quot;encryption&quot;).value;
if (!ssid) return alert(&quot;SSID is required.&quot;);
data = <code>WIFI:T:${encryption};S:${ssid};P:${password};;</code>;
}</p>
<p>else if (type === &quot;text&quot;) {
data = document.getElementById(&quot;text&quot;).value.trim();
if (!data) return alert(&quot;Text is required.&quot;);
}</p>
<p>else if (type === &quot;url&quot;) {
data = document.getElementById(&quot;url&quot;).value.trim();
if (!data.startsWith(&quot;http&quot;)) return alert(&quot;Please enter a valid URL.&quot;);
}</p>
<p>else if (type === &quot;vcard&quot;) {
const fn = document.getElementById(&quot;fullname&quot;).value;
const phone = document.getElementById(&quot;phone&quot;).value;
const email = document.getElementById(&quot;email&quot;).value;
const org = document.getElementById(&quot;org&quot;).value;
if (!fn) return alert(&quot;Full name is required.&quot;);
data = <code>BEGIN:VCARD VERSION:3.0 FN:${fn} ${org ? &quot;ORG:&quot; + org + &quot;\n&quot; : &quot;&quot;}TEL:${phone} EMAIL:${email} END:VCARD</code>;
}</p>
<p>qr = new QRious({
value: data,
size: 256,
background: getComputedStyle(document.body).backgroundColor,
foreground: getComputedStyle(document.body).color
});</p>
<p>const container = document.getElementById(&quot;qrcode&quot;);
container.innerHTML = '';
container.appendChild(qr.image);</p>
<p>document.getElementById(&quot;downloadBtn&quot;).disabled = false;
}</p>
<p>function downloadQRCode() {
if (!qr) return;
const link = document.createElement('a');
link.download = 'qr-code.png';
link.href = qr.toDataURL('image/png');
link.click();
}</p>
<p>// Regenerate QR when dark mode changes
const observer = new MutationObserver(() =&gt; {
if (qr) generateQRCode();
});</p>
<p>observer.observe(document.documentElement, {
attributes: true,
attributeFilter: ['data-md-color-scheme']
});</p>
<p>// Initialize default form
updateForm();
</script>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

[Click here to add your QR Code to the M-1 LED Matrix!](https://wiki.apolloautomation.com/products/m1/examples/create-logo-image/){        .md-button .md-button--primary }