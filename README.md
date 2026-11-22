# CSA07 Assignment 3 - Computer Networks (CO3)

Name: Sai Ramanesh
Register number: 1912260298
OS: macOS 15.4.1
Python: 3.14.0
Simulation tool: Cisco Packet Tracer / Wireshark (not used for the submitted programs)

## Programs

| Question | Folder | Program | Screenshot |
|---|---|---|---|
| Q1 - TCP byte stream | `Q1/` | `Q1/Q1_tcp_stream.py` | `screenshots/CO3_Q1_TCP_Byte_Stream.png` |
| Q2 - AIMD fairness | `Q2/` | `Q2/Q2_aimd.py` | `screenshots/CO3_Q2_AIMD_Fairness.png` |
| Q4 - DNS cache with TTL | `Q4/` | `Q4/Q4_dns_cache.py` | `screenshots/CO3_Q4_DNS_Cache.png` |
| Q5 - Erlang B | `Q5/` | `Q5/Q5_erlang_b.py` | `screenshots/CO3_Q5_Erlang_B.png` |

Each folder contains the Python program and the captured `output.txt`.

## How to run

    python3 Q1/Q1_tcp_stream.py
    python3 Q2/Q2_aimd.py
    python3 Q4/Q4_dns_cache.py
    python3 Q5/Q5_erlang_b.py

## Results

- Q1: the server receives all three length-prefixed messages and the client receives `all 3 received`.
- Q2: the AIMD gap falls from 26.0 at round 0 to 0.2 at round 80; the output matches the expected table.
- Q4: TTL 20/60/300/3600 s produces 180/60/12/1 authoritative queries in one hour.
- Q5: offered load 6.0 Erlangs; 13 lines are needed for blocking of 1% or less.

## Notes

The PDF provides Complete-the-Code programs only for Q1, Q2, Q4 and Q5. Q3 (HTTP performance), Q6 (QUIC/TLS 1.3) and Q7 (protocol design) are calculation, Wireshark or written-analysis tasks and have no Python program in the PDF.
