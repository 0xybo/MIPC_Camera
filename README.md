<div align="center">
    <img src="https://github.com/0xybo/homeassistant-mipc-camera/blob/main/brands/icon.png" height="100">
</div>
<div align="center">
    <h1>MIPC Camera</h1>
</div>

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
<!--
[![Last Release](https://img.shields.io/github/v/release/0xybo/homeassistant-mipc-camera?style=for-the-badge)](https://github.com/0xybo/homeassistant-mipc-camera/releases)
-->
<!-- 
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
-->

<h1>⚠️ Not maintained</h1>

Home Assistant custom component for viewing cameras connected to a MIPC account.

Site : http://www.mipcm.com/download/

App : https://www.mipcm.com/

Description available on the website : _MIPC is a mobile real-time video surveillance software used with Cloud IP Camera. Through this client, you can view your home, shops, offices and other places at any time in real-time video and video history, also receive immediate alert to the place of abnormal information alarm, and take safety precautions at the first time._

**Currently, the integration can only load video streams from cameras added to the MIPC account.**

# Installation

## HACS

**Requirements :**
- [HACS](https://hacs.xyz/) installed

**Shortcut :**
1. Open [https://my.home-assistant.io/redirect/hacs_repository/?owner=0xybo&repository=homeassistant-mipc-camera&category=integration](https://my.home-assistant.io/redirect/hacs_repository/?owner=0xybo&repository=homeassistant-mipc-camera&category=integration) and follow the instructions until you see the repository README on Home Assistant.

    [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=0xybo&repository=homeassistant-mipc-camera&category=integration)

2. Go to installation step 7.

<!-- Installation :
1. Go to HACS "Instegrations >" section
3. In the lower right, click "+ Explore & Download repositories"
4. Search for "mipc" and add it
5. Restart Home Assistant -->

**Installation :**
1. Go to HACS `Integrations` section.
2. In the top right-hand corner, open the menu and click on `Custom repositories`.
3. Enter `https://github.com/0xybo/homeassistant-mipc-camera` in repositoy field.
4. Select `integration` as category.
5. Then click on `Add`.
6. In `Integrations` section click on `MIPC Camera` card.
7. At bottom right, click `Download` and then `Download` in the popup window.
8. Restart Home Assistant.

## Manual

1. Using the tool of choice open the directory for your [HA configuration](https://www.home-assistant.io/docs/configuration/) (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory there, you need to create it.
3. In the `custom_components` directory create a new folder called `mipc_camera`.
4. Download **all** the files from the `custom_components/mipc_camera/` directory in this repository.
5. Place the files you downloaded in the new directory you created.
6. Restart Home Assistant.

# Configuration

**Shortcut :**
1. Open [https://my.home-assistant.io/redirect/config_flow_start/?domain=mipc_camera](https://my.home-assistant.io/redirect/config_flow_start/?domain=mipc_camera) and follow the instructions until the configuration pop-up window appears on Home Assistant.

    [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=mipc_camera)
2. Go to configuration step 5.

**Configuration :**

1. In the Home Assistant UI go to `Configuration`.
2. Click `Integrations`.
3. Click `+ Add Integration`.
4. Search for `mipc`.
5. Complete the form with your [MIPC account](https://www.mipcm.com/) information.
6. The integration will then connect to your account and import all cameras under the identifier `camera.mipc_camera_{{id}}` where `{{id}}` is the camera's internal identifier. 
