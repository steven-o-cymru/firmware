# Versions

What a package contains, and what each piece is pinned at. Every one of these
is fixed at build time: a release is a fixed set of these versions, not
whatever was current when it was built.

| Component | Pinned at |
|---|---|
| Stock FlashForge base | `1.9.7-1.2.9-20260810`, fetched from [ghzserg/FF](https://github.com/ghzserg/FF) at build time |
| [Klipper](https://github.com/Klipper4FlashForge/klipper/tree/creator5) | [`f51aab7a`](https://github.com/Klipper4FlashForge/klipper/commit/f51aab7a843a3852c808e28d694be8b59bbbc130) on branch `creator5` (reported as `v0.13.0-12-gf51aab7a`), with the `ff_*` toolchanger extras |
| [Mainsail](https://github.com/mainsail-crew/mainsail) | [`v2.19.0`](https://github.com/mainsail-crew/mainsail/releases/tag/v2.19.0) |
| [Fluidd](https://github.com/fluidd-core/fluidd) | [`v1.37.5`](https://github.com/fluidd-core/fluidd/releases/tag/v1.37.5) |
| [Moonraker](https://github.com/Arksine/moonraker) | [`v0.11.0`](https://github.com/Arksine/moonraker/releases/tag/v0.11.0) |
| [HelixScreen](https://github.com/Klipper4FlashForge/helixscreen) | [`v0.99.118-creator5`](https://github.com/Klipper4FlashForge/helixscreen/releases/tag/v0.99.118-creator5) |

How the pieces fit together on the printer — which of them is a service, what
starts what, and what stays stock — is [How it works](how-it-works.md).
