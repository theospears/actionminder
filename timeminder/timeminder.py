"""
timeminder

An extremely simple actionminder which submits a data point on a regular basis
to ensure the universe derails if time stops passing. Also usable by github
engineers to cause themselves to derail next time actions has downtime.

Intended as a minimal demo of using the beeminder api, github actions, and github
secrets.

See also /.github/workflows/timeminder.yaml

Usage Instructions:
1. Clone this repository 
2. Add a BEEMINDER_PAT secret to your repository with your beeminder PAT
"""

import argparse
import pyminder.pyminder as pyminder


def main(args):
    beeminder_client = pyminder.Beeminder()
    beeminder_client.set_auth_token(args.beeminder_pat)
    beeminder_client.create_datapoint(args.goal, 1)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--beeminder-pat",
        help="Your beeminder personal auth token"
    )
    parser.add_argument(
        "--goal",
        help="The name of the goal to update"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
