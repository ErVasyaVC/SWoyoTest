import argparse


def cli()-> (str, str, str):
    parser = argparse.ArgumentParser(description="Send sms")
    parser.add_argument("-s","--sender", type=str, required=True, help="Sender number")
    parser.add_argument("-r","--receiver", type=str, required=True, help="Recipient number")
    parser.add_argument("-m","--message", type=str, required=True, help="Text SMS")
    args = parser.parse_args()

    return args.sender, args.receiver, args.message