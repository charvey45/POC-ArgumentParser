import argparse

# Configures the argument parser for this program.
def configureparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host",
            help="Your AWS IoT custom endpoint")
    parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
    parser.add_argument("-c", "--cert", action="store", required=True, dest="certificatePath",
            help="Certificate file path")
    parser.add_argument("-k", "--key", action="store", required=True, dest="privateKeyPath",
            help="Private key file path")
    parser.add_argument("-p", "--port", action="store", dest="port", type=int, default=8883,
            help="Port number override")
    parser.add_argument("-n", "--thingName", action="store", required=True, dest="thingName",
            help="Targeted thing name")
    parser.add_argument("-d", "--requestDelay", action="store", dest="requestDelay", type=float, default=1,
            help="Time between requests (in seconds)")
    parser.add_argument("-v", "--enableLogging", action="store_true", dest="enableLogging",
            help="Enable logging for the AWS IoT Device SDK for Python")
    return parser


if __name__ == "__main__":
    parser = configureparser()
    args = parser.parse_args()