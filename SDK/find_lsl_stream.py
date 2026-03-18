from pylsl import resolve_streams
import time


def discover_lsl_streams(timeout=5.0):
    print(f"[INFO] Resolving LSL streams (timeout={timeout}s)...")
    streams = resolve_streams()

    if not streams:
        print("[WARN] No LSL streams found.")
        return

    print(f"[INFO] Found {len(streams)} LSL stream(s).\n")

    for idx, info in enumerate(streams, start=1):
        print(f"========== Stream {idx} ==========")
        print(f"Name            : {info.name()}")
        print(f"Type            : {info.type()}")
        print(f"Channels        : {info.channel_count()}")
        print(f"Sample Rate     : {info.nominal_srate()}")
        print(f"Channel Format  : {info.channel_format()}")
        print(f"Source ID       : {info.source_id()}")

        try:
            print(f"Hostname        : {info.hostname()}")
        except Exception:
            print("Hostname        : <unknown>")

        print("----------------------------------")
        # 如需完整 XML，取消下面注释
        # print(info.as_xml())
        print()


if __name__ == "__main__":
    discover_lsl_streams(timeout=5.0)

    # 防止程序瞬间退出（Windows 下有用）
    time.sleep(0.1)
