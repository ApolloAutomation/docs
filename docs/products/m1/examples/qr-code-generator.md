---
title: M-1 LED Matrix Setting up your own QR code for Wi-Fi, link to a website, etc.
description: Step by step guide to setting up your own QR code for Wi-Fi, link to a website, etc.
---
# 🔧 QR Code Generator (Wi-Fi, Text, URL)

!!! tip "You can set multiple different custom QR Codes as presets in WLED."

    The WLED firmware on your device will allow you to call these presets in automations or make buttons to control them on your Home Assistant dashboard!

<div style="margin-top: 1em; line-height: 1.8;">
  <label><strong>QR Code Type:</strong><br>
    <select id="qrType" onchange="updateForm()" style="width: 100%; max-width: 300px;">
      <option value="wifi">Wi-Fi</option>
      <option value="text">Text</option>
      <option value="url">URL</option>
      <option value="vcard">vCard (Contact)</option>
    </select>
  </label>
</div>

<!-- Dynamic form inputs -->
<div id="qrForm" style="margin-top: 1em;"></div>

<button onclick="generateQRCode()" style="padding: 0.5em 1em; font-weight: bold;">Generate QR Code</button>
<button id="downloadBtn" onclick="downloadQRCode()" disabled style="padding: 0.5em 1em; font-weight: bold; margin-left: 1em;">Download</button>

<div id="qrcode" style="margin-top: 2em;"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
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
      `;
    } else if (type === "url") {
      form.innerHTML = `
        <label><strong>URL:</strong><br><input type="url" id="url" placeholder="https://example.com" style="width: 100%; max-width: 500px;"></label><br>
      `;
    } else if (type === "vcard") {
      form.innerHTML = `
        <label><strong>Full Name:</strong><br><input type="text" id="fullname" style="width: 100%; max-width: 300px;"></label><br>
        <label><strong>Phone:</strong><br><input type="tel" id="phone" style="width: 100%; max-width: 300px;"></label><br>
        <label><strong>Email:</strong><br><input type="email" id="email" style="width: 100%; max-width: 300px;"></label><br>
        <label><strong>Org (optional):</strong><br><input type="text" id="org" style="width: 100%; max-width: 300px;"></label><br>
      `;
    }
  }

  function generateQRCode() {
    const type = document.getElementById("qrType").value;
    let data = "";

    if (type === "wifi") {
      const ssid = document.getElementById("ssid").value;
      const password = document.getElementById("password").value;
      const encryption = document.getElementById("encryption").value;
      if (!ssid) return alert("SSID is required.");
      data = `WIFI:T:${encryption};S:${ssid};P:${password};;`;
    }

    else if (type === "text") {
      data = document.getElementById("text").value.trim();
      if (!data) return alert("Text is required.");
    }

    else if (type === "url") {
      data = document.getElementById("url").value.trim();
      if (!data.startsWith("http")) return alert("Please enter a valid URL.");
    }

    else if (type === "vcard") {
      const fn = document.getElementById("fullname").value;
      const phone = document.getElementById("phone").value;
      const email = document.getElementById("email").value;
      const org = document.getElementById("org").value;
      if (!fn) return alert("Full name is required.");
      data = `BEGIN:VCARD
VERSION:3.0
FN:${fn}
${org ? "ORG:" + org + "\n" : ""}TEL:${phone}
EMAIL:${email}
END:VCARD`;
    }

    qr = new QRious({
      value: data,
      size: 256,
      background: getComputedStyle(document.body).backgroundColor,
      foreground: getComputedStyle(document.body).color
    });

    const container = document.getElementById("qrcode");
    container.innerHTML = '';
    container.appendChild(qr.image);

    document.getElementById("downloadBtn").disabled = false;
  }

  function downloadQRCode() {
    if (!qr) return;
    const link = document.createElement('a');
    link.download = 'qr-code.png';
    link.href = qr.toDataURL('image/png');
    link.click();
  }

  // Regenerate QR when dark mode changes
  const observer = new MutationObserver(() => {
    if (qr) generateQRCode();
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-md-color-scheme']
  });

  // Initialize default form
  updateForm();
</script>

[Click here to add your QR Code to the M-1 LED Matrix!](https://wiki.apolloautomation.com/products/m1/examples/create-logo-image/){        .md-button .md-button--primary }