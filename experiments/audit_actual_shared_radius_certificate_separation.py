"""Verify both directions of the strict fixed marked-source certificate separation."""
from pathlib import Path
import argparse
import json
from audit_actual_shared_radius_anchor_obstruction import verify as verify_anchor
from audit_actual_sector_cover import verify as verify_cover


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name(
        'audit_actual_shared_radius_certificate_separation_results.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    anchor_data = json.loads((root / 'actual_shared_radius_anchor_obstruction_certificate.json').read_text())
    cover_data = json.loads((root / 'actual_sector_cover_certificate.json').read_text())
    for key in ('k', 'word', 'mark', 'ports', 'protected', 'ordinary'):
        assert anchor_data[key] == cover_data[key], key
    anchor = verify_anchor(anchor_data)
    cover = verify_cover(cover_data)
    result = {
        'status': 'PASS',
        'scope': 'The SAME original marked 17-port source fails the unrefined anchored criterion by >0.025 and passes a complete forty-branch actual-sector cover by >0.04. Universal genuine-sector coverage remains open.',
        'original_source_identity': 'PASS',
        'anchor_obstruction': anchor,
        'actual_sector_cover': cover,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('anchor_obstruction', 'actual_sector_cover')}, indent=2))


if __name__ == '__main__':
    main()
